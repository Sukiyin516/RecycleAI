# RecycleAI：百炼主开发版本

保留原绿色页面、上传预览、六个演示、双语、测验、积分、环保树和 localStorage。

## 两个独立版本

| 分支 | 用途 | 默认模型 | 密钥变量 |
|---|---|---|---|
| main | 后续持续开发：阿里云百炼 | qwen3.5-flash | DASHSCOPE_API_KEY |
| gemini-version | 原 Gemini 开发备份 | gemini-3.5-flash-lite | GEMINI_API_KEY |

各分支有自己的中文 README、.env.example、依赖和启动脚本。此次仅创建本地分支和未提交修改，不代表已上传 GitHub。分支切换不会切换私人 .env，必须安装对应依赖并重启服务。

## Windows 启动与密钥

需要 Python 3.10+（含 Python launcher）、浏览器及可访问百炼的网络。

1. 双击 start.bat，自动创建 .venv、安装 requirements.txt，并在没有 .env 时复制 .env.example。
2. 用记事本编辑本文件夹 .env，自行填写：

```dotenv
DASHSCOPE_API_KEY=your_dashscope_api_key_here
DASHSCOPE_MODEL=qwen3.5-flash
DASHSCOPE_BASE_URL=https://{WorkspaceId}.cn-beijing.maas.aliyuncs.com/compatible-mode/v1
```

Key 换成自己的百炼 Key；URL 中 {WorkspaceId} 换成自己的业务空间 ID，推荐直接复制百炼控制台的 OpenAI 兼容服务地址。Key、地域、业务空间及模型权限必须匹配。北京示例不能直接套用其他地域，不要使用 Coding Plan 专属接口代替视觉理解接口。不需要 OpenAI 账户或 OpenAI Key。

原有 .env 保留不覆盖，可在其中追加 DASHSCOPE_* 变量。系统环境变量优先。不要把真实配置发到 GitHub。

3. 重启 start.bat，打开 http://127.0.0.1:5000，保持窗口打开。Ctrl+C 停止服务。不要同时启动两个版本占用 5000 端口。

已有环境可在 PowerShell 中运行：

```powershell
cd D:\eduhk_AIET\INIT6065\project\RecycleAI
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

## 识别流程与限制

浏览器通过 POST /api/classify 发送 imageDataUrl；Python 检查并在内存中转码，移除附加元数据，经 HTTPS 发给百炼。使用 HTTPX 调用官方 Chat Completions 兼容接口，关闭思考并要求 JSON；Pydantic 严格验证返回字段和类型。

Qwen 只识别物品、可见条件及匹配标识；类别和投放建议由 rules.json 已核实白名单提供。模糊、混合垃圾、材质不明或未覆盖时返回“暂时无法确定”，不生成知识题。失败、超时、额度不足、空响应、截断、安全拦截或无效 JSON 都返回错误，不用演示结果伪装成功。模型仍可能看错，须核对照片和物品名称。

图片仅支持单帧 JPG/PNG/WEBP，最大 8 MB、2000 万像素。供应商可能有额外限制，拒绝时显示错误。应用不保存上传照片或记录密钥；百炼的数据处理适用账户条款。localStorage 保存积分、题号和语言。密钥仅在后端使用。

五道已核实题最多 50 分；铅蓄电池演示标记待核实、无测验，不将所有废电池统一分类。原有 Lv.2（30分）、Lv.3（60分）逻辑保留，自然达到 Lv.3 需后续添加有官方来源的题目。规则来源及核对日期见 rules.json 和页脚，英文是项目翻译。

原有 Tailwind、字体、图标和彩纸动画依赖外部 CDN；仅监听本机，是课程 Demo，没有公网账户系统。

## 文件与测试

app.py：后端、图片校验及调用；rules.json：白名单；.env.example：无真实密钥模板；.gitignore：排除私人配置；test_app.py：离线及模拟 HTTP 测试；test_browser.py：可选 Edge 回归；TEST_RESULTS.md：测试范围；DEVELOPMENT_LOG.md：迁移原因。

```powershell
.\.venv\Scripts\python.exe -m unittest test_app -v
# 可选：需 Edge；先关闭自己的 5000 端口服务
.\.venv\Scripts\python.exe -m pip install playwright
.\.venv\Scripts\python.exe test_browser.py
```

**尚未使用真实百炼 API Key 验证照片识别。** 配置真实 Key/URL 后，自行验证实际物品名称、分类、中英文及测验开关。演示和模拟成功不能证明真实 API 已连接。

缺密钥时填写 DASHSCOPE_API_KEY；配置错误时核对 DASHSCOPE_BASE_URL；401/403 检查地域和权限；429 检查额度；超时检查网络；模型不可用时检查账户是否支持 qwen3.5-flash。不自动换模型或返回假结果。

## 在 GitHub Desktop 保存两个分支

1. 原目录 RecycleAI 当前为 main。检查 Changes，不含 .env 或真实凭据，Summary 建议 `Migrate main to Bailian Qwen`；Commit to main，再 Push origin。
2. File → Add local repository，选择旁边的 RecycleAI-gemini-version。它是同仓库独立工作目录，当前为 gemini-version。检查仅 README 和忽略规则更新，Summary 建议 `Document Gemini backup version`；Commit to gemini-version，再 Publish branch（首次）或 Push origin。
3. 若 Desktop 不支持该工作目录，在用户确认后，可自行运行以下命令完成 Gemini 文档提交与上传；助手不会代为执行：

```powershell
git -C ..\RecycleAI-gemini-version add README.md .gitignore
git -C ..\RecycleAI-gemini-version commit -m "Document Gemini backup version"
git push -u origin gemini-version
```

不要强制切换、丢弃修改或把百炼修改带入 Gemini 分支。GitHub 网页确认两个分支分别有 README 和 .env.example；不需要合并 Gemini 到 main。

官方参考：[图像理解](https://help.aliyun.com/zh/model-studio/vision)、[Chat 接口](https://help.aliyun.com/en/model-studio/qwen-api-via-openai-chat-completions)、[获取 Key](https://help.aliyun.com/zh/model-studio/get-api-key)。2026-10-31 查阅，模型、接入点、地域、额度及收费以账户控制台为准。
