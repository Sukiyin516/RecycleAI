# RecycleAI 开发记录

## 2026-10-31：保留 Gemini，主线迁移百炼

- 开始时 main 干净，本地 main 与记录的 origin/main 均为 8016f95，另有 727501e。本次未 fetch，不代表实时远程查询。
- 修改接入代码前，创建 gemini-version，指向 8016f95，原始提交和 Gemini 代码完整保留。
- Gemini 分支在 ../RecycleAI-gemini-version 独立目录补齐中文 README，保留原 SDK、默认 gemini-3.5-flash-lite 和 .env.example，不改原始实现。
- 按项目所有者要求，main 以后以百炼 qwen3.5-flash 作为持续开发主线；保留 Gemini 方便其他人选择和学习。初次记录未包含完整选型原因，后续补记见下方 Design Iteration；不据此声称百炼更快、更准确或更便宜，也不声称 Gemini 在所有地区不可用。
- 百炼使用 HTTPX 访问官方 Chat Completions 兼容接口，图片只在内存处理；关闭思考、要求 JSON、严格结构检查，分类仍由已核实规则决定。
- 页面结构、题目、积分、树、双语和存储逻辑保留，只更新服务提供商文字和隐私提示。
- 不覆盖原私人 .env；main 使用 DASHSCOPE_* 配置，Gemini 使用 GEMINI_*。真实凭据禁止纳入 Git。
- 不自动 Commit 或 Push。两个工作目录中的未提交修改由用户在 GitHub Desktop 检查并提交、推送/发布。

本次测试状态见 TEST_RESULTS.md；模拟通过不能当作真实 API 识别成功。

<a id="design-iteration"></a>

## Design Iteration：从 Gemini 到百炼的技术选型调整

补记日期：2026-10-31。依据项目成员在[本次原始Prompt](development_records/prompts/2026-10-31_03_design_iteration.md)中补充的背景，以及同日查阅的官方资料。下述原因属于本次回顾补记；学校账号访问失败的实际发生日期和报错截图待补，不将它们编造成早期已记录的测试。

| 选型过程 | 依据与状态 |
|---|---|
| 最初选择 Gemini，因为它支持图像理解，适合分析垃圾照片、识别物品 | 选型动机来自用户本次说明；图像理解能力已由[Google官方图像理解文档](https://ai.google.dev/gemini-api/docs/image-understanding)核实。模型具备该能力，不等于本项目已用真实Key验证垃圾识别准确率。 |
| 后续遇到学校 Google 账号无法访问 Google AI Studio | 项目成员反馈的实际访问经历；Codex本次没有登录该账号或独立复现。具体原因未查明，不推定所有学校账号都被封禁，也不将账号问题等同于地区限制。待提供遮挡个人资料后的错误截图。 |
| RecycleAI 目标用户位于中国深圳；中国内地不在 Gemini API 官方支持地区名单内 | 目标用户位置由用户明确；[官方地区名单](https://ai.google.dev/gemini-api/docs/available-regions)于2026-10-31核对，未列中国内地。[Gemini附加条款的Use Restrictions](https://ai.google.dev/gemini-api/terms)限制服务访问及向用户提供API应用的地区。因此本项目需考虑地区可用性及服务条款适配，不只考虑模型图像能力；此结论不推广到其他Google产品。 |
| 为提高在中国内地的实际可用性，选择百炼 qwen3.5-flash 作为后续主线 | 这是针对目标使用场景的设计决策和预期目标，不是已经完成的可用性或性能实验结论。真实Key调用、深圳网络环境测试、账号/地域/模型权限、配额及真实用户使用仍需验证。 |
| 保留 Gemini 备份，在 main 持续开发百炼 | 已核实Git状态：main的迁移提交d92f46d；gemini-version保留原实现，文档提交9aa5aea。两版本的代码存在不代表它们都已通过真实供应商API测试。 |

**验证边界：** 已核实官方能力/地区/条款资料和本地Git分支；账号访问问题为项目成员报告。现有离线模拟和本地浏览器测试不能证明真实百炼可用性、用户满意度、学习效果或优于Gemini的准确率。真实用户测试尚未进行。

PPT英文表述集中保存在 [PPT_MATERIALS.md 的 Design Iteration](development_records/PPT_MATERIALS.md#design-iteration-gemini-to-alibaba-cloud-bailian)，其他日志引用本节，避免反复复制完整理由。
