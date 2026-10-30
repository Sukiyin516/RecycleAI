# 截图索引与待补证据

这些是实际浏览器截图，不是AI生成图。旧图从原目录原样复制，不删除或覆盖原图。日期按原测试文档/对应聊天执行日期归档，文件修改时间不作为历史日期证据。[来源及SHA256清单](../evidence/SCREENSHOT_MANIFEST.json)。

| 图片 | 状态及可支持的结论 | 来源/版本 |
|---|---|---|
| [2026-10-29_gemini_home_archived.png](2026-10-29_gemini_home_archived.png) | 主页外观，不证明AI调用 | test-results/home.png；Gemini基线 |
| [2026-10-29_gemini_demo_archived.png](2026-10-29_gemini_demo_archived.png) | 本地演示、50分和Lv.2 | test-results/result.png；非真实识别 |
| [2026-10-29_gemini_mobile_archived.png](2026-10-29_gemini_mobile_archived.png) | 手机布局 | test-results/mobile.png |
| [2026-10-31_bailian_home_archived.png](2026-10-31_bailian_home_archived.png) | 百炼文字的主页 | .tmp/bailian-browser-results/home.png；迁移时未提交的百炼工作区；当前实现已在d92f46d |
| [2026-10-31_bailian_demo_archived.png](2026-10-31_bailian_demo_archived.png) | 本地演示和50分树 | .tmp/bailian-browser-results/result.png；非真实识别 |
| [2026-10-31_bailian_mobile_archived.png](2026-10-31_bailian_mobile_archived.png) | 百炼阶段手机布局 | .tmp/bailian-browser-results/mobile.png |
| [2026-10-31_current_home.png](2026-10-31_current_home.png) | 本轮真实网页，独立浏览器0分 | 本轮Edge捕获；未修改网站功能；随后观察到被纳入d92f46d |
| [2026-10-31_local_demo_banana.png](2026-10-31_local_demo_banana.png) | 本地香蕉皮演示 | 本轮Edge捕获；未调用AI；随后纳入d92f46d |
| [2026-10-31_missing_bailian_key.png](2026-10-31_missing_bailian_key.png) | 上传合成PNG后本地503、缺Key明确提示 | 本轮Edge捕获；没有发送给百炼；随后纳入d92f46d |

所有图均不证明真实Gemini或百炼识别成功，不用于计算识别准确率。PPT上要保留演示/本地测试标识。

## 需要用户手动补充

以下文件尚不存在，所以不建立假链接。截图前关闭.env、密钥控制台、账户个人资料；遮挡Key、Cookie、密码等敏感信息后再保存。

| 要截的页面与状态 | 推荐文件名 | 说明 |
|---|---|---|
| Codex对话：10月31日“先保存Gemini、再迁移百炼”的完整用户Prompt | `2026-10-31_codex_prompt_migration.png` | 能读到要求和真实顺序即可，不必拍整屏隐私 |
| Codex对话：本次“每日记录与PPT素材”用户要求 | `2026-10-31_codex_prompt_records.png` | 原始文字已有存档；对话截图仍待补 |
| GitHub Desktop：main的Changes及当前分支 | `2026-10-31_github_main_changes.png` | 确认不含.env，不把未提交内容标为已提交 |
| GitHub Desktop：gemini-version的History/Changes | `2026-10-31_github_gemini_branch.png` | 能看到分支名；不能泄露凭据 |
| 首次真实API测试：上传照片及真实结果页 | `YYYY-MM-DD_bailian_real_api_result.png` | 必须真实执行成功后，使用当日日期；同时记录模型、返回结果及限制，不包含Key |
| 历史HTML修复前、旧错误现场 | 使用实际历史日期加`_before_fix`或`_error` | 原图和日期均待补；不能今天重演冒充历史 |

如果提交或拍摄发生在以后，文件名用实际发生日期，日志注明它补充的是哪个历史阶段。没有权限获得的截图不能伪造。

## 技术选型背景补充（2026-10-31）

学校Google账号访问AI Studio失败由项目成员报告，本次未获取真实报错截图或复现根因。请在真实问题出现时手动截图，使用实际日期的 `YYYY-MM-DD_school_google_access_error.png`，遮挡邮箱、姓名、账号标识及凭据，并补充发生日期。不要从地区名单推断学校管理员禁用了所有账号，也不要生成假报错页面。[Design Iteration记录](../../DEVELOPMENT_LOG.md#design-iteration)。

## 2026-10-31任务D：北京配置回归

- [2026-10-31_beijing_home.png](2026-10-31_beijing_home.png)：真实Edge回归截图；本地演示/布局，不是百炼识别成功。
- [2026-10-31_beijing_demo.png](2026-10-31_beijing_demo.png)：真实Edge回归截图；本地演示/布局，不是百炼识别成功。
- [2026-10-31_beijing_mobile.png](2026-10-31_beijing_mobile.png)：真实Edge回归截图；本地演示/布局，不是百炼识别成功。

来源与SHA256见[北京配置清单](../evidence/2026-10-31_beijing_api_configuration.json)。需用户手动补本轮Prompt及北京额度开关页；推荐实际日期加 `_codex_prompt_beijing.png`、`_beijing_free_quota.png`，不截Key页并遮挡隐私。

## 2026-10-31任务E：首次真实API返回

[真实百炼照片请求结果](2026-10-31_real_bailian_cup_result.png)：供应商与Flask均200，模型返回“塑料杯”；杯子材质未人工确认，类别按本地规则保持“暂时无法确定”，无测验。此图是真实API连通证据，不是分类准确率证据。截图不含原照片预览、Key或账户页面。SHA256及单次请求usage见[真实请求记录](../evidence/2026-10-31_real_bailian_cup_test.json)。

需用户手动核对并保存北京模型免费额度变化截图，使用实际日期加 `_real_test_quota.png`，遮挡账号隐私，不截Key页面。

## 规则扩充及课堂Demo简化

- [原真实前测1238 Token](2026-10-31_real_bailian_cup_result.png)：不确定，原件不改。
- [严格规则真实后测1717 Token](2026-10-31_real_bailian_cup_after_rules.png)：仍不确定，真实API仅新增1次。
- [扩充规则的可回收杯模拟展示](2026-10-31_expanded_cup_mock.png)：模拟响应，不是真实识别。
- [通过答题长到Lv.3](2026-10-31_expanded_quizzes_tree.png)：浏览器测试，识别响应为模拟。
- [简化杯子分类本地重放](2026-10-31_simple_cup_local_replay.png)：重用已保存明确名称，显示可回收物/AI分类建议；不是新真实API调用。

可用于PPT，但需保留上述真实/模拟/重放图注。Prompt对话和GitHub Changes仍可由用户手动截图，先遮挡敏感信息。

## 四张图片真实演示（任务H）

4张分类页和4张答题后页面：[完整截图索引](../evidence/2026-10-31_four_live_picture_summary.md)。均来自本次真实API和实际答题，未使用模拟响应；截图可直接用于PPT。

## 环保树三个成长形态

实际答题累积到60分，截图包含0分小树苗、30分成长树、60分绿色大树，以及+10奖励：[查看全部四张截图](../evidence/2026-10-31_tree_growth_summary.md)。无直接修改积分，无新增AI调用。
