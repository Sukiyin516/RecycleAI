# RecycleAI 项目开发规范

本文件适用于 RecycleAI 项目根目录及其所有子目录，后续开发任务应持续遵循。

## 每次修改后的交付流程

1. 每次完成代码修改、功能开发、Bug 修复或项目文件更新后，都要提醒用户将最新版本保存到 GitHub。
2. 每次任务结束时，用简单中文总结本次修改了什么，以及测试是否通过。
3. 如实说明测试范围：未运行的测试要明确写明；模拟测试不能描述为真实 API 测试；没有使用真实 Gemini API Key 进行验证时，不得声称真实 AI 识别已测试成功。
4. 根据本次实际修改，建议一个简短、清楚的英文 Commit Summary，例如 `Fix Gemini API connection`。
5. 在最终回复的最后，明确给出以下提醒，保留标题和两个操作：

   **📌 GitHub 版本保存提醒：**
   请打开 GitHub Desktop，检查 Changes，然后执行：
   - Commit to main（保存本地版本）
   - Push origin（上传到 GitHub）

## Git 操作与敏感信息

- 未经用户明确确认，不得自动执行 Commit 或 Push，也不得通过 GitHub Desktop 或其他工具代为执行。
- 不得将 `.env`、真实 API Key、密码或其他敏感信息提交到 GitHub。
- 使用 `.gitignore` 排除本地密钥文件；`.env.example` 只能包含占位符，不能包含真实凭据。
- 不得把密钥写入 HTML、前端 JavaScript 或浏览器 localStorage，也不得在回复、日志或测试截图中展示真实凭据。
- 用户确认 Commit 或 Push 后，仍须检查待提交内容，确保没有敏感信息。

## 版本与后续开发

- main 为阿里云百炼 qwen3.5-flash 主开发分支，后端配置使用 DASHSCOPE_API_KEY、DASHSCOPE_MODEL、DASHSCOPE_BASE_URL。
- gemini-version 保留迁移前 Gemini 实现，不将百炼修改带入该备份分支。两个版本分别维护中文 README 和无真实凭据的 .env.example。
- 不得把模拟 API 测试说成真实百炼或 Gemini 识别测试成功。
- 修改 API 提供商时更新 DEVELOPMENT_LOG.md，记录真实迁移原因，不虚构准确率或性能结论。
- 需要同步两个分支时，分别提醒用户 Commit to main / Commit to gemini-version，再 Push origin（未发布分支使用 Publish branch）。不得自行 Commit 或 Push。

## 每日开发记录与 PPT 素材（长期执行）

- 每次完成开发、修复或项目文档任务后，交付前自动更新 `development_records/daily/YYYY-MM-DD.md`，使用用户客户端 Asia/Shanghai 日期。已有同日文件必须保留，按实际先后顺序追加任务A/B/C，不另建同日重复日志，不覆盖之前的失败记录。
- 日志固定六栏：1.今日开发目标（Objectives）；2.AI Prompt记录（Prompts）；3.开发过程（Development Process）；4.问题与修改（Problems & Iterations）；5.测试结果（Testing）；6.开发证据（Evidence）。每轮任务的事实按顺序追加到相应栏目。参考 `development_records/DAILY_TEMPLATE.md`。
- 重要用户Prompt在 `development_records/prompts/` 按日期和轮次保存原文，日志按顺序相对引用，不擅自改写。缺失标“原始 Prompt 待补充”，不得补造用户要求、对话或AI内部推理。敏感值以 `[已脱敏]` 替换并注明，不保存含真实凭据的原始副本。
- 每完成重要功能或修复，同步更新 `development_records/PPT_MATERIALS.md` 的相关七主题，并引用日志、真实截图或实际代码版本。事实、旧记录记载、当前实测和未来计划必须区分；没有用户测试就不写评价或学习效果结论。
- 将真实截图保存在 `development_records/screenshots/`，命名包含日期和状态，重名加序号，不覆盖旧证据。使用日志到截图的Markdown相对路径，更新截图索引和来源信息。不能生成假截图或把演示/模拟结果当真实AI识别；缺失历史截图不得今天重演后冒充当时现场。
- 有浏览器能力时保存与本任务相关的真实页面/报错状态；无法捕获时，向用户明确说明需手动截图的页面、状态及推荐文件名。Codex对话、GitHub Desktop和课堂反馈等缺失证据列入待补清单。截图/Prompt如可能带Key、密码、Cookie或隐私，提醒先遮挡，禁止落盘或提交含敏感内容的材料。
- 只记实际执行的测试，区分通过、失败后修复、尚未测试，以及离线模拟、本地浏览器联调、真实供应商API、真实用户研究。文档修改不必重复运行所有功能测试，但要说明没运行。不能用提交时间推断开发时间，不能为未提交修改编造Commit Hash。
- 优先引用已有PROMPTS/CHANGELOG/TEST_LOG或DEVELOPMENT_LOG/TEST_RESULTS，避免多份重复全文；不得未经允许删除已有开发记录或用户未提交的修改。
- 用户说“今天收工，整理开发记录”时，检查当天六栏、原始Prompt顺序、截图链接和敏感信息、测试状态、PPT素材及Git状态；补齐可核实记录，给出简短总结、待补证据和建议英文Commit Summary，不自动开发新功能或发起收费API测试。
- 每次结束继续使用上述GitHub版本保存提醒：要求用户在GitHub Desktop检查Changes、Commit和Push；未经明确确认不自动Commit或Push。提交后才能核实并补记真实Hash。这是任务内记录规范，不创建后台定时自动化。

## INT6065 课程 Demo 原则（优先遵循）

- RecycleAI 是大学小组课堂 Demo，不是商业项目。目标是简单、稳定、可现场演示的 AI 垃圾分类与环保学习工具。
- 优先保证现有核心流程可用：上传照片→识别物品→对应深圳四类垃圾桶→投放提示→知识问答→积分→环保树。
- 规则只需覆盖少量常见生活垃圾，有深圳官方指引支持、基本准确即可，不为追求覆盖率或商业级可靠性增加复杂架构。
- 常见物品按可识别的主要类型直接给出类别，例如普通塑料饮料瓶对应可回收物。清空、清洁、干燥及组件分开等常规行为主要放入投放提示和知识题，不要求用户先证明处理完毕、展示内部或拍清所有材质标识后才分类。
- 不因常见饮料杯带有相关杯盖、吸管就一律视为无法识别的混合垃圾。材质确实不明、特殊风险或真正不同垃圾混杂时仍保留“暂时无法确定”；不能强行给出错误答案，也不能将所有塑料制品一律视为可回收物。明显受污染且已有不同官方处理依据的物品仍按对应规则处理。
- 不增加智能追问、复杂数据库、用户注册、排行榜等功能，不重新制作网页。保留绿色外观、中英双语、知识题、积分和树成长机制。
- 每次修改尽量小范围完成；测试选择几个代表性物品和相关受影响功能，已有必要回归可继续使用，但不新增大规模或复杂测试体系。
- 继续保留必要的原始Prompt、开发日志、真实截图、失败与修复记录及PPT素材；不得为“演示成功”修改历史不确定结果。
- 修改完成后用简单中文说明内容和实际测试状态，建议英文Commit Summary，并提醒用户通过GitHub Desktop检查Changes、Commit及Push。未经确认不自动提交或推送，不上传.env、真实Key或隐私。
