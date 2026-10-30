"""离线测试：不会发送图片给百炼，也不消耗 API 额度。"""
import base64
import io
import json
import os
import unittest
import httpx
from unittest.mock import patch, MagicMock

from PIL import Image
from app import app, Observation, RULES


def sample_image():
    output = io.BytesIO()
    Image.new('RGB', (8, 8), 'green').save(output, 'PNG')
    return 'data:image/png;base64,' + base64.b64encode(output.getvalue()).decode()


class BackendTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.env = patch.dict(os.environ, {'DASHSCOPE_API_KEY': '',
            'DASHSCOPE_BASE_URL': 'https://test-workspace.cn-beijing.maas.aliyuncs.com/compatible-mode/v1',
            'DASHSCOPE_MODEL': 'qwen3.5-flash'})
        self.env.start()
        self.addCleanup(self.env.stop)

    def post(self, value=None):
        return self.client.post('/api/classify', json={'imageDataUrl': value or sample_image()})

    def test_home_and_no_secret_static_route(self):
        with self.client.get('/') as response:
            self.assertEqual(response.status_code, 200)
        for path in ('/.env', '/app.py', '/rules.json', '/.git/config'):
            self.assertEqual(self.client.get(path).status_code, 404)

    def test_missing_key(self):
        response = self.post()
        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.json['error']['code'], 'API_KEY_MISSING')
        self.assertNotIn('category', response.json)

    def test_bad_images(self):
        for image in ('not image', 'data:image/png;base64,YWJj',
                      sample_image().replace('image/png', 'image/jpeg'),
                      'data:image/svg+xml;base64,YWJj'):
            self.assertEqual(self.post(image).status_code, 400)
        self.assertEqual(self.post('data:image/png;base64,' + 'A' * (12 * 1024 * 1024)).status_code, 413)

    def test_bad_requests(self):
        self.assertEqual(self.client.post('/api/classify', data='x').status_code, 415)
        self.assertEqual(self.client.post('/api/classify', json=[]).status_code, 400)
        self.assertEqual(self.client.post('/api/classify', data='{', content_type='application/json').status_code, 400)
        self.assertEqual(self.client.post('/api/classify', json={}, headers={'Origin':'https://example.com'}).status_code, 403)

    @patch('app.recognize')
    def test_failures_never_return_results(self, recognize):
        os.environ['DASHSCOPE_API_KEY'] = 'test-only'
        for exc in (TimeoutError(), ValueError('invalid JSON'), RuntimeError('secret-data')):
            recognize.side_effect = exc
            response = self.post()
            self.assertEqual(response.status_code, 502)
            self.assertNotIn('category', response.json)
            self.assertNotIn('secret-data', response.get_data(as_text=True))

    @patch('app.recognize')
    def test_verified_rules_and_uncertain(self, recognize):
        os.environ['DASHSCOPE_API_KEY'] = 'test-only'
        for key, rule in RULES.items():
            recognize.return_value = Observation(itemName='测试物品', enItemName='Test item', ruleKey=key,
                                                 certain=True, singleItem=True, conditionsMet=True)
            result = self.post().json
            self.assertEqual(result['category'], rule['category'])
            self.assertEqual(result['matchedKey'], rule['matchedKey'])
        for kwargs in ({'ruleKey':'unknown'}, {'certain':False}, {'singleItem':False}, {'conditionsMet':False}):
            fields = dict(itemName='不明物品',enItemName='Unknown item',ruleKey='bottle',certain=True,singleItem=True,conditionsMet=True)
            fields.update(kwargs)
            recognize.return_value = Observation(**fields)
            result = self.post().json
            self.assertEqual(result['category'], '暂时无法确定')
            self.assertIsNone(result['matchedKey'])

    @patch('app.httpx.Client')
    def test_api_boundary_and_schema_validation(self, client_class):
        os.environ['DASHSCOPE_API_KEY'] = 'test-only'
        client = client_class.return_value.__enter__.return_value
        content = json.dumps(dict(itemName='香蕉皮', enItemName='Banana peel',
            ruleKey='banana',certain=True,singleItem=True,conditionsMet=True))
        def response(text, finish='stop'):
            return MagicMock(json=MagicMock(return_value={'choices':[{
                'finish_reason':finish, 'message':{'content':text}}]}))
        client.post.return_value = response(content)
        self.assertEqual(self.post().json['category'], '厨余垃圾')
        sent = client.post.call_args.kwargs
        self.assertEqual(sent['json']['model'], 'qwen3.5-flash')
        self.assertFalse(sent['json']['enable_thinking'])
        self.assertTrue(sent['json']['messages'][0]['content'][0]['image_url']['url'].startswith('data:image/jpeg;base64,'))
        self.assertEqual(sent['headers']['Authorization'], 'Bearer test-only')
        for text in ('', '{}', 'not JSON', None):
            client.post.return_value = response(text)
            self.assertEqual(self.post().status_code, 502)
        client.post.return_value = response(content, 'length')
        self.assertEqual(self.post().status_code, 502)
        client.post.return_value = response(content, 'content_filter')
        self.assertEqual(self.post().status_code, 502)

    @patch('app.httpx.Client')
    def test_provider_errors_and_config(self, client_class):
        os.environ['DASHSCOPE_API_KEY'] = 'test-only'
        client = client_class.return_value.__enter__.return_value
        for code, expected in ((401,502),(403,502),(429,503),(500,502)):
            req = httpx.Request('POST', 'https://example.com')
            client.post.side_effect = httpx.HTTPStatusError('private-provider-message',request=req,
                response=httpx.Response(code,request=req))
            result = self.post()
            self.assertEqual(result.status_code, expected)
            self.assertNotIn('category', result.json)
            self.assertNotIn('private-provider-message', result.get_data(as_text=True))
        client.post.side_effect = httpx.ReadTimeout('private-message')
        self.assertEqual(self.post().status_code, 502)
        client.post.reset_mock()
        for url in ('', 'https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1',
                    'http://dashscope.aliyuncs.com/compatible-mode/v1', 'https://example.com/compatible-mode/v1'):
            os.environ['DASHSCOPE_BASE_URL'] = url
            self.assertEqual(self.post().json['error']['code'], 'PROVIDER_CONFIG_ERROR')
        client.post.assert_not_called()


if __name__ == '__main__':
    unittest.main(verbosity=2)
