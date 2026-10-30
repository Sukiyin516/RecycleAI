# 截图索引与待补证据

这些是实际浏览器截图，不是AI生成图。旧图从原目录原样复制，不删除或覆盖原图。日期按原测试文档/对应聊天执行日期归档，文件修改时间不作为历史日期证据。[来源及SHA256清单](../evidence/SCREENSHOT_MANIFEST.json)。

| 图片 | 状态及可支持的结论 | 来源/版本 |
|---|---|---|
| [2026-10-29_gemini_home_archived.png](2026-10-29_gemini_home_archived.png) | 主页外观，不证明AI调用 | test-results/home.png；Gemini基线 |
| [2026-10-29_gemini_demo_archived.png](2026-10-29_gemini_demo_archived.png) | 本地演示、50分和Lv.2 | test-results/result.png；非真实识别 |
| [2026-10-29_gemini_mobile_archived.png](2026-10-29_gemini_mobile_archived.png) | 手机布局 | test-results/mobile.png |
| [2026-10-31_bailian_home_archived.png](2026-10-31_bailian_home_archived.png) | 百炼文字的主页 | .tmp/bailian-browser-results/home.png；未提交百炼工作区 |
| [2026-10-31_bailian_demo_archived.png](2026-10-31_bailian_demo_archived.png) | 本地演示和50分树 | .tmp/bailian-browser-results/result.png；非真实识别 |
| [2026-10-31_bailian_mobile_archived.png](2026-10-31_bailian_mobile_archived.png) | 百炼阶段手机布局 | .tmp/bailian-browser-results/mobile.png |
| [2026-10-31_current_home.png](2026-10-31_current_home.png) | 本轮真实网页，独立浏览器0分 | 本轮Edge捕获；未修改网站功能 |
| [2026-10-31_local_demo_banana.png](2026-10-31_local_demo_banana.png) | 本地香蕉皮演示 | 本轮Edge捕获；未调用AI |
| [2026-10-31_missing_bailian_key.png](2026-10-31_missing_bailian_key.png) | 上传合成PNG后本地503、缺Key明确提示 | 本轮Edge捕获；没有发送给百炼 |

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
