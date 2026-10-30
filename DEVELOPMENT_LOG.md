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

## 2026-10-31 任务D：依据官方文档落实北京接口与免费Demo配置

- 用户提供apireadme.txt，明确北京Base URL为https://dashscope.aliyuncs.com/compatible-mode/v1；作为接入参考，不执行文档中systemd、sudo或打印密钥的示例指令。官方密钥页同日核实一致。
- main已有百炼实现，本轮修正旧模板中的业务空间占位符，并在后端限制北京域名及qwen3.5-flash，保留Flask、/api/classify和本地深圳规则库。Gemini备份不修改。
- 大图长边最多1280、JPEG质量85、校正方向；关闭思考，短JSON输出上限512 Token，不生成规则解释和题目，不自动重试/切换模型或地域。不能据此保证固定Token用量或免费扣量。
- 用户报告剩余免费额度并开启“免费额度用完即停”；未登录账户核实，未调用真实API。私人.env不覆盖，需要用户本地填写北京Key并确认后再继续真实照片测试。
- 本轮10项离线测试及浏览器回归通过，详细证据见[任务D日志](development_records/daily/2026-10-31.md)与[本轮配置证据](development_records/evidence/2026-10-31_beijing_api_configuration.json)。

## 2026-10-31 任务E：用户确认后完成首次真实请求

- 用户确认本地Key并提供饮料杯照片。本地Key误填在旧Gemini变量名，补充正确百炼变量及北京/模型配置；私人.env未纳入Git，旧字段保留，不展示Key。应用源代码未改。
- 只发送1次真实qwen3.5-flash请求；供应商/Flask均200。模型输出“塑料杯 / plastic cup”，材质未独立确认。没有匹配本地规则，因此网页显示不确定、隐藏测验；真实识别结果没有强行改成演示成功。
- 总1238 Token来自供应商usage，不代表免费扣量已核实。截图、原文授权和脱敏结果见[任务E日志](development_records/daily/2026-10-31.md)。早期真实API未测说明仍保留为历史状态。

## 2026-10-31 任务F/G：扩规则后按课堂需要简化

先保存原始杯子“不确定”证据，再新增10条深圳官方来源规则及双语题。后测经批准只真实调用1次，仍不确定（1717 Token），不改历史结果。用户随后明确不要过度分析杯盖、吸管、内部和污染：已将普通塑料杯/瓶按明确名称直接匹配、清洁放指引与题目，标题为AI分类建议；原则写入AGENTS。13项后端和三个代表性本地浏览器场景通过，简化后无新增真实调用。见[迭代记录](development_records/iterations/2026-10-31_expanding_rules.md)。

## 2026-10-31 任务H：四图课堂演示

依用户授权实际测试4张单图，补充充电电池规则后，四类建议和4道题均完成；截图8张、40分/Lv.2，真实4次共7512 Token。没有重做网页。见[四案例记录](development_records/evidence/2026-10-31_four_live_picture_summary.md)。
