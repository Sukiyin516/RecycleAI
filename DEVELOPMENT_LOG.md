# RecycleAI 开发记录

## 2026-10-31：保留 Gemini，主线迁移百炼

- 开始时 main 干净，本地 main 与记录的 origin/main 均为 8016f95，另有 727501e。本次未 fetch，不代表实时远程查询。
- 修改接入代码前，创建 gemini-version，指向 8016f95，原始提交和 Gemini 代码完整保留。
- Gemini 分支在 ../RecycleAI-gemini-version 独立目录补齐中文 README，保留原 SDK、默认 gemini-3.5-flash-lite 和 .env.example，不改原始实现。
- 按项目所有者要求，main 以后以百炼 qwen3.5-flash 作为持续开发主线；保留 Gemini 方便其他人选择和学习。没有证据证明百炼更快、更准确或更便宜，也没有证明 Gemini 不可用。
- 百炼使用 HTTPX 访问官方 Chat Completions 兼容接口，图片只在内存处理；关闭思考、要求 JSON、严格结构检查，分类仍由已核实规则决定。
- 页面结构、题目、积分、树、双语和存储逻辑保留，只更新服务提供商文字和隐私提示。
- 不覆盖原私人 .env；main 使用 DASHSCOPE_* 配置，Gemini 使用 GEMINI_*。真实凭据禁止纳入 Git。
- 不自动 Commit 或 Push。两个工作目录中的未提交修改由用户在 GitHub Desktop 检查并提交、推送/发布。

本次测试状态见 TEST_RESULTS.md；模拟通过不能当作真实 API 识别成功。
