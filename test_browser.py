"""可选浏览器回归测试：先 pip install playwright（并安装 Edge）。不调用真实 AI。"""
import io
import json
import os
import threading
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright, expect
from werkzeug.serving import make_server
from app import app, RULES


def run():
    os.environ['DASHSCOPE_API_KEY'] = ''
    server = make_server('127.0.0.1', 5000, app, threaded=True)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    output = Path('.tmp/bailian-browser-results')
    output.mkdir(parents=True, exist_ok=True)
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(channel='msedge', headless=True)
            page = browser.new_page(viewport={'width':1280,'height':960})
            errors = []
            page.on('pageerror', lambda error: errors.append(str(error)))
            page.goto('http://127.0.0.1:5000', wait_until='domcontentloaded')
            expect(page.locator('#user-points')).to_have_text('0')
            page.screenshot(path=str(output/'home.png'), full_page=True)
            print('PASS: HTML opens via Flask')
            expected = {'bottle':'可回收物','can':'可回收物','box':'可回收物','banana':'厨余垃圾','battery':'暂时无法确定','tissue':'其他垃圾'}
            for key, category in expected.items():
                page.locator('#preset-'+key).click()
                page.locator('#btn-start-ai').click()
                expect(page.locator('#sec-result')).to_be_visible()
                expect(page.locator('#res-category-name')).to_have_text(category)
                page.locator('#btn-lang-toggle').click()
                assert page.locator('#res-item-name').inner_text().isascii()
                page.locator('#btn-lang-toggle').click()
                if key == 'battery':
                    expect(page.locator('#quiz-banner-wrap')).to_be_hidden()
                else:
                    page.locator('#txt-btn-open-quiz').click()
                    page.evaluate('toggleLanguage()')
                    assert page.locator('#quiz-options-container').inner_text().isascii()
                    page.evaluate('toggleLanguage()')
                    if key == 'bottle':
                        page.locator('#quiz-options-container button').nth(1).click()
                        expect(page.locator('#user-points')).to_have_text('0')
                    correct = 1 if key == 'banana' else 0
                    page.locator('#quiz-options-container button').nth(correct).click()
                    page.locator('#txt-btn-close-quiz').click()
                page.evaluate('resetForNextItem()')
            expect(page.locator('#user-points')).to_have_text('50')
            expect(page.locator('#tree-stage-badge')).to_contain_text('Lv.2')
            page.reload(wait_until='domcontentloaded')
            expect(page.locator('#user-points')).to_have_text('50')
            page.locator('#preset-bottle').click()
            page.locator('#btn-start-ai').click()
            expect(page.locator('#sec-result')).to_be_visible()
            page.locator('#txt-btn-open-quiz').click()
            page.locator('#quiz-options-container button').first.click()
            expect(page.locator('#user-points')).to_have_text('50')
            page.locator('#txt-btn-close-quiz').click()
            page.screenshot(path=str(output/'result.png'), full_page=True)
            page.evaluate('resetForNextItem()')
            print('PASS: six demos, translations, wrong/correct answers, no duplicate points, tree Lv.2, storage')
            image = io.BytesIO()
            Image.new('RGB', (8,8), 'green').save(image,'PNG')
            def upload():
                page.locator('#file-input').set_input_files({'name':'test.png','mimeType':'image/png','buffer':image.getvalue()})
                expect(page.locator('#image-preview')).to_be_visible()
                page.locator('#btn-start-ai').click()
            upload()
            expect(page.get_by_text('尚未配置百炼 API Key（DASHSCOPE_API_KEY），请在后端 .env 中填写后重启。', exact=True)).to_be_visible()
            expect(page.locator('#sec-result')).to_be_hidden()
            print('PASS: real browser upload reaches backend; missing key displays explicit error')
            page.route('**/api/classify', lambda route: route.fulfill(status=502,json={'error':{'message':'测试：Bailian 请求失败','enMessage':'Test: Bailian request failed'}}))
            upload()
            expect(page.get_by_text('测试：Bailian 请求失败',exact=True)).to_be_visible()
            expect(page.locator('#sec-result')).to_be_hidden()
            page.unroute('**/api/classify')
            payload = dict(itemName='测试香蕉皮',enItemName='Test banana peel',matchedKey='banana',ruleVerified=True,
                **{k:RULES['banana'][k] for k in ('category','reason','enReason','disposalGuide','enDisposalGuide')})
            page.route('**/api/classify', lambda route: route.fulfill(json=payload))
            upload()
            expect(page.locator('#res-item-name')).to_have_text('测试香蕉皮')
            expect(page.locator('#quiz-banner-wrap')).to_be_visible()
            page.locator('#btn-lang-toggle').click()
            expect(page.locator('#res-item-name')).to_have_text('Test banana peel')
            page.evaluate('resetForNextItem()')
            payload.update(category='暂时无法确定',matchedKey=None,ruleVerified=False)
            upload()
            expect(page.locator('#res-category-name')).to_have_text('Uncertain')
            expect(page.locator('#quiz-banner-wrap')).to_be_hidden()
            print('PASS: simulated API failure/success/uncertain rendering; no real Bailian call')
            page.reload(wait_until='domcontentloaded')
            expect(page.locator('html')).to_have_attribute('lang', 'en')
            page.set_viewport_size({'width':390,'height':844})
            page.screenshot(path=str(output/'mobile.png'), full_page=True)
            assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
            # 检查保留的最高树阶段；这是合成的存储状态，不代表实际答题得到 60 分。
            page.evaluate("localStorage.setItem('recycle_ai_points','60')")
            page.reload(wait_until='domcontentloaded')
            expect(page.locator('#tree-stage-badge')).to_contain_text('Lv.3')
            page.evaluate('resetDemoPoints()')
            expect(page.locator('#user-points')).to_have_text('0')
            expect(page.locator('#tree-stage-badge')).to_contain_text('Lv.1')
            standalone = browser.new_page()
            standalone.goto(Path('RecycleAI_修复版_第一阶段.html').resolve().as_uri(),wait_until='domcontentloaded')
            standalone.locator('#preset-banana').click()
            standalone.locator('#btn-start-ai').click()
            expect(standalone.locator('#res-category-name')).to_have_text('厨余垃圾')
            print('PASS: saved language, mobile layout, synthetic Lv.3 state, reset, standalone HTML demo')
            assert not errors, errors
            browser.close()
    finally:
        server.shutdown()


if __name__ == '__main__':
    run()
