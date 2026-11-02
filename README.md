# RecycleAI：百炼主开发版本

保留原绿色页面、上传预览、六个演示、双语、测验、积分、环保树和 localStorage。

## 两个独立版本

| 分支 | 用途 | 默认模型 | 密钥变量 |
|---|---|---|---|
| main | 后续持续开发：阿里云百炼 | qwen3.5-flash | DASHSCOPE_API_KEY |
| gemini-version | 原 Gemini 开发备份 | gemini-3.5-flash-lite | GEMINI_API_KEY |

各分支有自己的中文 README、.env.example、依赖和启动脚本。已有迁移版本为main提交d92f46d、Gemini文档为9aa5aea；本轮北京配置调整需另行提交。分支切换不会切换私人 .env，必须安装对应依赖并重启服务。

## Windows 启动与密钥

需要 Python 3.10+（含 Python launcher）、浏览器及可访问百炼的网络。

1. 双击 start.bat，自动创建 .venv、安装 requirements.txt，并在没有 .env 时复制 .env.example。
2. 用记事本编辑本文件夹 .env，自行填写：

```dotenv
DASHSCOPE_API_KEY=your_dashscope_api_key_here
DASHSCOPE_MODEL=qwen3.5-flash
DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
```

Key 换成自己在华北2（北京）创建的百炼 Key；上面的 Base URL 可直接使用，不需要业务空间占位符。依据你提供的 `apireadme.txt` 和[官方密钥文档](https://help.aliyun.com/zh/model-studio/get-api-key)。本课程版本只允许此北京接口或控制台给出的具体北京业务空间域名（`https://实际空间ID.cn-beijing.maas.aliyuncs.com/compatible-mode/v1`），并固定模型为 `qwen3.5-flash`；其他地域、其他模型、空配置或未替换占位符会明确报错，不自动跨区或切模型。不要使用国际站或 Coding Plan 专属接口。不需要 OpenAI 账户或 OpenAI Key。

你已报告该模型有免费额度并开启“免费额度用完即停”；请确认额度、开关和Key属于同一个北京账户/地域/业务空间及模型。本项目不能查询或保证免费额度、免费扣量顺序和账单状态；这些由百炼服务端和账户设置决定。本次未登录控制台核实。不要仅凭本地模拟测试认定免费额度已经成功扣减。

原有 .env 保留不覆盖。请将其中已有的三项 DASHSCOPE_* 更新为上述配置，避免同名变量重复；不要只在旧占位符下面重复追加。系统环境变量优先，如果修改.env后仍提示配置不对，请检查是否有旧系统变量，再重启。不要把真实Key发到聊天、HTML、截图或GitHub。

3. 重启 start.bat，打开 http://127.0.0.1:5000，保持窗口打开。Ctrl+C 停止服务。不要同时启动两个版本占用 5000 端口。

已有环境可在 PowerShell 中运行：

```powershell
cd D:\eduhk_AIET\INIT6065\project\RecycleAI
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

## 同一 Wi-Fi 手机访问（2026-11-02）

启动方式不变：双击 `start.bat`（它运行 `.venv\Scripts\python.exe app.py`）。如果旧窗口还在运行，先按 Ctrl+C 停止，再重新启动；保持窗口打开。后端现在监听 `0.0.0.0:5000`，关闭调试；电脑仍可打开 http://127.0.0.1:5000。手机不能使用自己的 127.0.0.1，也不要把 0.0.0.0 当作访问网址。[Flask 官方说明](https://flask.palletsprojects.com/en/stable/quickstart/#externally-visible-server)。

1. 电脑与手机连接同一 Wi-Fi。
2. 本次电脑 WLAN IPv4 为 `172.17.25.99`，手机浏览器输入 **http://172.17.25.99:5000**（HTTP，含端口）。换 Wi-Fi 或重新联网后地址可能变化，用电脑 PowerShell 的 `ipconfig` 查 WLAN 的 IPv4，再替换网址。
3. 先在电脑浏览器打开这个局域网网址，再在手机打开。手机访问/上传/答题仍需实际验证；电脑自行访问成功不能证明手机已连通。手机积分、语言和树保存在手机自己的浏览器，不同步电脑数据。

若手机打不开，先检查网址、同一 Wi-Fi 和服务器窗口。需要放行防火墙时，请手动操作，不关闭防火墙：

1. 按 Win+R，输入 `wf.msc`，打开“高级安全 Windows Defender 防火墙”。
2. 选择“入站规则”→“新建规则”→“端口”→“TCP”→“特定本地端口”填 `5000`。
3. 选择“允许连接”；在你信任且确实标为“专用”的 Wi-Fi 上，只勾选“专用”，名称填 `RecycleAI TCP 5000`。
4. 建好后打开规则“属性”→“作用域”→“远程 IP 地址”→“下列 IP 地址”→“添加”→“预定义的计算机集：本地子网”。
5. 再试手机网址。使用结束可禁用该规则，并按 Ctrl+C 停止服务器。

学校/公共 Wi-Fi 若被标为“公用”或“域”，上述专用规则不会生效；不要为此随意将公共网络改为专用，可改用自己的可信热点，或向学校 IT 确认权限。访客/校园 Wi-Fi 也可能禁止设备之间互访，即使 Wi-Fi 名称相同仍无法连接。防火墙仅提供操作说明，本次没有修改系统规则。[微软配置步骤](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/configure)、[本地子网范围建议](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/rules)。

这是可信局域网内的临时课程演示，不做路由器端口转发或公网部署；同网段访问者可使用电脑后端的 API 额度，演示完停止服务器。密钥仍只在后端 `.env`，不向手机返回。

## 识别流程与限制

浏览器通过 POST /api/classify 发送 imageDataUrl；Python 检查并在内存中转码，移除附加元数据，经 HTTPS 发给百炼。使用 HTTPX 调用官方 Chat Completions 兼容接口，关闭思考并要求 JSON；Pydantic 严格验证返回字段和类型。

Qwen 只识别物品、可见条件及匹配标识；类别和投放建议由 rules.json 已核实白名单提供。模糊、混合垃圾、材质不明或未覆盖时返回“暂时无法确定”，不生成知识题。失败、超时、额度不足、空响应、截断、安全拦截或无效 JSON 都返回错误，不用演示结果伪装成功。模型仍可能看错，须核对照片和物品名称。

图片仅支持单帧 JPG/PNG/WEBP，最大 8 MB、2000 万像素；后端校正照片方向，将长边缩至最多1280像素并以JPEG质量85转码，移除元数据后只发一张图。小字材质标识可能因此不够清晰，请靠近重拍；不能确认时应返回不确定。供应商可能有额外限制，拒绝时显示错误。应用不保存上传照片或记录密钥；百炼的数据处理适用账户条款。localStorage 保存积分、题号和语言。密钥仅在后端使用。

## 免费额度下的请求控制

- 一张图片、一个短Prompt，不发送聊天历史或整个规则库；只发送物品匹配条件，不让AI生成分类原因和知识题。
- `enable_thinking=false`，使用非思考JSON Object模式；Prompt含JSON关键词，返回后继续严格校验结构。
- 输出上限512 Token，缩短物品名称；中文原因、英文原因和投放建议直接从本地规则返回，不占模型输出。超过上限而截断时显示错误，不当作成功。
- 每次真实识别仅发送一次请求，无自动重试、模型回退或跨区回退；六个本地演示不调用AI。
- 这些措施控制请求规模，不承诺固定输入Token数或零费用。模型按实际图像/文本计量；先用少量清晰单件照片测试，并在百炼北京控制台核对额度变化。

现有17条规则各有一道后台知识题（包含原5题，题ID保留）；六个本地演示仍是原5道可得分题及一个待核实铅蓄电池案例。新规则识别后也能进入测验，因此可以正常答题达到Lv.3；每题仅奖励一次10分，原30/60分树成长机制不变。规则依据与未确认候选见[规则核查](development_records/RULE_REVIEW.md)，英文为项目翻译。

课程Demo采用简单建议：明确识别为普通塑料杯或塑料饮料瓶，直接匹配已核实的可回收物规则，不再要求展示封盖/吸管/内部或先证明清洁。清空、清洁等放投放提示和题目。真正不明类型或无规则时仍不确定、无题无积分。结果标题为“AI分类建议 / AI Sorting Suggestion”，不保证每次识别都正确。

原有 Tailwind、字体、图标和彩纸动画依赖外部 CDN；允许可信局域网访问，是课程 Demo，没有公网账户系统。

## 文件与测试

app.py：后端、图片校验及调用；rules.json：白名单；.env.example：无真实密钥模板；.gitignore：排除私人配置；test_app.py：离线及模拟 HTTP 测试；test_browser.py：可选 Edge 回归；TEST_RESULTS.md：测试范围；DEVELOPMENT_LOG.md：迁移原因。

```powershell
.\.venv\Scripts\python.exe -m unittest test_app -v
# 可选：需 Edge；先关闭自己的 5000 端口服务
.\.venv\Scripts\python.exe -m pip install playwright
.\.venv\Scripts\python.exe test_browser.py
```

**2026-10-31已完成1次真实百炼请求（用户提供的饮料杯照片）。** 北京qwen3.5-flash与本地接口均返回HTTP 200，模型返回“塑料杯 / plastic cup”；材质尚未独立核实，本地规则没有匹配项，页面正确保持“暂时无法确定”，不提供测验。中文和英文结果切换已检查。供应商报告输入1195、输出43、总1238 Token。详见[真实测试证据](development_records/evidence/2026-10-31_real_bailian_cup_test.json)和[结果截图](development_records/screenshots/2026-10-31_real_bailian_cup_result.png)。

这证明此环境的一次真实连通及未知规则处理，不证明杯子材质判断正确、一般识别准确率、深圳实地可用性或免费额度实际扣量。需要在北京控制台核对免费额度变化；模型输出Token不是账单证明。Gemini仍未完成真实调用验证。后续测试需另提供照片，勿重复发送Key。

本次发现Key填在旧GEMINI_API_KEY字段，已仅在私人.env补上正确DASHSCOPE_API_KEY及北京/模型配置，保留旧字段，未显示Key。今后百炼Key要填DASHSCOPE_API_KEY。

缺密钥时填写 DASHSCOPE_API_KEY；配置错误时核对北京DASHSCOPE_BASE_URL及模型名；401/403 检查地域、权限和免费额度设置；429 检查额度；超时检查网络；模型不可用时检查账户是否支持 qwen3.5-flash。不自动换模型或返回假结果。

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

### 最新简化验证（2026-10-31）

规则扩充后，经用户确认的1次真实后测仍返回不确定，总1717 Token，原1238 Token前测不覆盖。随后按用户课堂Demo要求简化普通塑料杯/瓶匹配；对已保存的明确识别名称进行本地重放，杯子可显示可回收物并进入知识题。塑料杯、塑料瓶和不明物品三个代表性浏览器场景及现有13项后端检查通过；简化后没有再次调用真实API。对比与证据见[本次迭代](development_records/iterations/2026-10-31_expanding_rules.md)。

最新课堂演示：4张图片均完成真实API分类及答题，8张截图见[四案例索引](development_records/evidence/2026-10-31_four_live_picture_summary.md)，最终40分/Lv.2；只代表这4个样本的开发测试。
