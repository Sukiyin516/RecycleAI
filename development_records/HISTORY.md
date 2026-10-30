# 历史阶段与证据索引

整理日期：2026-10-31。只依据当前可见聊天、现存文件、Git 和旧记录；不把推测当事实。

| 阶段 | 可以确认的事实 | 日期/版本及证据 | 待补充 |
|---|---|---|---|
| 初始网页原型（用户称“初始 Gemini 网页版本”） | 上级目录存在 recycleai_app.html、recycleai_app_A.html | 本次目录检查确认存在；未发现该阶段独立 Git 提交。它们不在当前仓库内，不能作为 GitHub 内有效链接 | 实际创建日期、原始 Prompt、是否曾真实接入 Gemini、当时测试及截图均待补充 |
| HTML 第一阶段修复 | 上级目录存在 RecycleAI_修复版_第一阶段.html；10月29日用户要求表明上传预览、六演示、测验、积分、树、双语和 localStorage 已存在 | [10月29日需求原文](prompts/2026-10-29_01_gemini_backend.md)；727501e 包含后来已接入后端的同名 HTML，不能当作独立修复前快照 | 最初修复日期、修复前后逐项差异、当时原始 Prompt 和截图待补充；不能仅根据文件名判断修复内容 |
| Gemini Flask 接入 | 后端、规则、启动脚本和离线/浏览器测试已存在；未验证真实 Google API | [10月29日日志](daily/2026-10-29.md)、[旧测试记录](../TEST_RESULTS.md)；首次 Git 快照 727501e 提交于10月30日 | 真实密钥识别、真实用户反馈待补充 |
| Git 保存及规范 | 727501e Initial commit；8016f95 Create AGENTS.md | Git 记录时间分别为 2026-10-30 19:35:57+08:00、19:55:11+08:00；[10月30日日志](daily/2026-10-30.md) | GitHub Desktop 操作截图待补充；未 fetch，不断言远端当前状态 |
| Gemini 备份与百炼主线 | 修改前基于8016f95创建gemini-version；main改为qwen3.5-flash；两个独立工作目录 | [开发记录](../DEVELOPMENT_LOG.md)、[10月31日日志](daily/2026-10-31.md)；本轮开始时两分支均8016f95；工作期间观察到main=d92f46d、gemini-version=9aa5aea | 提交Hash已核实；真实百炼识别待补充。跟踪引用已更新但未fetch，不保证实时远端状态 |
| 日志与 PPT 素材机制 | 建立每日六栏、原文 Prompt、截图索引及七主题素材 | [10月31日日志任务B](daily/2026-10-31.md)、[PPT索引](PPT_MATERIALS.md)；首版记录已在2c9b7cf，三张新图在d92f46d；最终校验/更正仍待保存 | 最终更正提交Hash待补 |

原文 Prompt 在 prompts/ 中保存一次；日志及素材用链接引用。未找到既有 PROMPTS.md、CHANGELOG.md、TEST_LOG.md；保留现有 DEVELOPMENT_LOG.md 和 TEST_RESULTS.md。
