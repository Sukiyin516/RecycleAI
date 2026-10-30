请为 RecycleAI 项目建立一套长期使用的**每日开发记录与 PPT 素材整理机制**。

项目用于香港教育大学 INT6065 Artificial Intelligence in Education 小组作业。老师希望我们保留 AI 开发过程中的 Prompt、截图、修改记录与测试证据，用于小组展示和反思。

我的目标是：今后每次使用 Codex 修改项目，都能自动整理开发过程。最终制作 PPT 时，可以直接使用这些记录。

## 一、建立每日开发日志

请在项目的 `development_records/daily/` 文件夹中，按照日期建立 Markdown 文件，例如：

`2026-10-31.md`

每份日志使用以下固定格式：

**1. 今日开发目标（Objectives）**

- 今天想实现什么功能？
- 为什么需要修改？

**2. AI Prompt 记录（Prompts）**

- 记录我实际提交的重要 Prompt。
- 保留原始内容，不要擅自改写。
- 如有多轮修改，按照真实顺序记录。
- 无法获取原始 Prompt 时，标记“原始 Prompt 待补充”。

**3. 开发过程（Development Process）**

- 修改了哪些文件？
- 新增了哪些功能？
- 使用了哪些技术？
- 用简单中文解释如何实现。

**4. 问题与修改（Problems & Iterations）**

- 遇到了什么问题？
- 我向 AI 提出了什么修改要求？
- Codex 如何修复？
- 修改前后有什么区别？

**5. 测试结果（Testing）**

- 记录实际执行的测试。
- 明确区分通过、失败、尚未测试。
- 不得编造测试成功结果。

**6. 开发证据（Evidence）**

- 相关截图及文件路径。
- Git Commit Hash（如已提交）。
- 值得用于 PPT 的开发成果。

## 二、截图保存机制

请使用：

`development_records/screenshots/`

保存网页截图、Prompt 截图、报错和修复前后对比。

文件名称包含日期和内容，例如：

- 2026-10-31_before_api.png
- 2026-10-31_codex_prompt.png
- 2026-10-31_api_success.png

如果你可以实际操作浏览器，请保存真实截图。

如果无法截图，请明确告诉我需要手动截取哪个页面、哪个状态，以及推荐文件名。

不要生成虚假的测试截图。

在每日开发日志中添加对应截图的 Markdown 相对路径链接，方便在 GitHub 中直接查看。

## 三、整理 PPT 素材

请建立：

`development_records/PPT_MATERIALS.md`

每完成一个重要功能或修复时，更新该文件。

按照以下展示主题整理：

1. Problem Identification：为什么要开发 RecycleAI。
2. AI Concepts & System Design：使用了什么 AI 技术，系统如何工作。
3. Prototype Development：原型如何逐步开发。
4. Technical Feasibility：实现方式、运行条件和测试结果。
5. Problems & Iterations：遇到的问题以及如何利用 AI 修改。
6. Evaluation & Feedback：实际用户测试、反馈及改进。
7. Limitations & Reflection：技术限制、伦理问题与反思。

每项只记录已经确认的事实或明确标注的计划，并注明对应的日志、截图或代码版本。

请用简洁中文整理，方便以后制作英文 Presentation。

## 四、让规则长期生效

请检查已有的 `AGENTS.md`。

保留之前的开发规范，在其中补充：

- 每次完成开发任务后，自动更新当天的开发日志。
- 同一天的多次修改合并到同一份日志，按照实际顺序追加。
- 更新对应的 PPT 素材汇总。
- 提醒用户保存需要手动截图的证据。
- 提醒用户通过 GitHub Desktop 执行 Commit 和 Push。
- 提供建议的英文 Commit Summary。
- 未经确认，不得自动 Commit 或 Push。

如果我说“今天收工，整理开发记录”，请检查当天的日志是否完整，并生成简短的当日总结。

## 五、整理已有历史记录

请先检查现有的 Git 历史、开发文档和项目文件。

尽量整理已经能够确认的阶段：

- 初始 Gemini 网页版本
- HTML 功能修复
- Gemini Flask 后端接入
- 从 Gemini 迁移至阿里云百炼的决策及后续开发

只记录有证据支持的开发日期、操作和结果。

无法从现有资料确定的 Prompt、截图或测试结果，请标记“待补充”，不要自行编造。

如果已有 PROMPTS.md、CHANGELOG.md 或 TEST_LOG.md，请尽量沿用并建立引用，避免重复记录同一内容。

## 六、安全要求

- 不得记录、显示或上传真实 API Key。
- 不得将 .env、密码、隐私信息提交到 GitHub。
- 截图和 Prompt 中如有敏感信息，需提醒我遮挡。
- 未经允许不要删除已有开发记录。
- 不要修改现有网站功能，本次任务只建立记录机制和整理可以核实的历史信息。

完成后请告诉我创建了哪些文件、整理了哪些历史记录，以及以后每次开发我需要如何使用这套机制。
