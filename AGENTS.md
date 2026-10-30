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
