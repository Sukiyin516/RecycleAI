# RecycleAI：Gemini 原始开发版本

分支 gemini-version 保存迁移前 Gemini 接入，供备份、学习及自行配置运行。后续主线为 main 的百炼 qwen3.5-flash，无需合并本分支到 main。

## 模型和 Windows 启动

默认模型 gemini-3.5-flash-lite，通过 Google 官方 google-genai Python SDK 调用。可在 .env 修改为自己项目可用、支持图像和结构化输出的模型。网络、地域、费用、配额及权限以 Google 账户为准。

安装 Python 3.10+（包含 Python launcher），双击本目录 start.bat。自动创建 .venv、安装 requirements.txt，并从 .env.example 生成 .env。用记事本编辑 .env：

```dotenv
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-3.5-flash-lite
```

将 Key 占位符换成自己从 [Google AI Studio](https://aistudio.google.com/apikey) 获取的密钥，保存并重启。不要填百炼 Key。系统环境变量优先于 .env。

浏览器打开 http://127.0.0.1:5000，保持窗口打开；Ctrl+C 停止。六个本地演示无需密钥；真实识别必须经后端网址使用，不能只双击 HTML。

也可在本目录 PowerShell 执行：

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

独立工作目录需单独安装依赖。本次未复制任何私人 .env 到 Gemini 工作目录。两个版本不能同时占用 5000 端口。切换分支不会自动切换私人配置。

## 功能及限制

原绿色界面、预览、六个演示、中文/English、题目、积分、环保树及 localStorage 保留。Gemini 识别物品和可见条件，后端用 rules.json 白名单分类。模糊、未覆盖或无法确认时返回“暂时无法确定”；未核实规则无测验；API 失败不能伪装成演示结果。模型仍可能看错，应核对照片。

五道核实题最多 50 分；铅蓄电池案例待核实、无测验，不将所有电池统一分类。保留 30/60 分升级阈值，自然到 60 分需日后增加有来源的题目。

只支持单帧 JPG/PNG/WEBP，最大 8 MB、2000 万像素；内存中校验、转码及移除元数据后发给 Google，不长期保存照片。供应商数据处理适用账户条款。密钥只能在后端，不得放入 HTML、localStorage、日志或 Git；.env.example 只有占位符。

原有样式、字体、图标和彩纸动画有外部 CDN 依赖。服务只监听本机，是课程 Demo，未提供公网商业架构。

## 测试与保存

TEST_RESULTS.md 是 2026-10-29 的模拟和浏览器记录，没有使用真实 Gemini Key 完成照片识别。本次只补齐文档和忽略规则，不修改原 API 实现，也未验证真实 Google 请求。

```powershell
.\.venv\Scripts\python.exe -m unittest test_app -v
```

请配置自己的真实 Key 后验证照片识别、网络、模型权限和配额；演示及模拟成功不能证明真实 API 可用。

本分支基于迁移前 8016f95。此中文文档需用户在 GitHub Desktop 的 Gemini 目录检查后 Commit to gemini-version，再 Publish branch / Push origin。建议 Summary：`Document Gemini backup version`。main 修改另行提交，助手不自动 Commit 或 Push，不提交真实凭据。

参考：[图像理解](https://ai.google.dev/gemini-api/docs/image-understanding)、[结构化输出](https://ai.google.dev/gemini-api/docs/structured-output)。
