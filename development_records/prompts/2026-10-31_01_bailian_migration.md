我希望 RecycleAI 在 GitHub 上同时保留两个版本：

1. Gemini API 版本：作为原始开发版本备份，供其他人自行配置 Gemini API Key 后运行。
2. 阿里云百炼版本：使用 qwen3.5-flash，作为后续持续开发的主要版本，供其他人自行配置百炼 API Key 后运行。

请先检查当前 Git 状态和提交历史。

在修改 Gemini 代码之前，请帮助我将原有 Gemini 接入版本保存在独立的 `gemini-version` 分支中。

之后在 `main` 分支上继续替换为阿里云百炼 API。

要求：

- 不要删除或覆盖已有的 Gemini 版本。
- 保留原有网页界面及功能。
- 两个版本分别提供中文 README 和 `.env.example`。
- 说明各自使用的模型、API Key 配置、运行步骤和限制。
- 不得上传真实 API Key 或 `.env` 文件。
- 不要把未经真实 API 验证的功能标记为测试成功。
- 更新项目开发记录，说明为什么从 Gemini 改为百炼。
- 未经我确认，不要自动 Commit 或 Push。

请先告诉我当前 Git 状态、计划如何保存 Gemini 分支，以及是否存在未提交的修改，再进行操作。

完成后提醒我通过 GitHub Desktop 保存并同步两个分支。
