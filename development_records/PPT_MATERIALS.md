# RecycleAI PPT 素材库

课程：香港教育大学 INT6065 Artificial Intelligence in Education。以下为简洁中文素材，便于以后制作英文Presentation；没有生成最终PPT。证据基线：Gemini提交727501e/8016f95；本轮工作期间观察到百炼已提交d92f46d、Gemini文档已提交9aa5aea；首版记录已在2c9b7cf，最终更正仍有未提交内容，不能使用8016f95冒充百炼版本。除任务E的单次真实API返回“不确定”截图外，其他截图为本地演示/错误路径。任务E证明一次连通，不证明物品材质及类别准确。

## 1. Problem Identification

- 已确认的项目目标：通过垃圾照片分类建议、投放说明及测验帮助使用者学习分类，兼顾环保积分和小树成长。来源：[初始用户需求原文](prompts/2026-10-29_01_gemini_backend.md)、[10月29日目标](daily/2026-10-29.md)。
- 展示图：[当前主页](screenshots/2026-10-31_current_home.png)，说明“课程原型的设计目标”，不能据此声称用户分类能力已经提高。
- 待补充：需求访谈、错误分类频率或用户痛点调查。没有调查数据，不编造百分比。

## 2. AI Concepts & System Design

- 已实现结构：上传图片 → Flask检查/内存转码 → 图像理解模型识别物品和可见条件 → Pydantic校验 → 本地已核实规则 → 双语解释及可用题目。它是多模态模型调用与规则约束相结合，没有证据表明小组训练或微调了模型。
- Gemini备份默认gemini-3.5-flash-lite；main百炼默认qwen3.5-flash。API提供商是后端配置，密钥不在前端。[main后端](../app.py)、[规则](../rules.json)、[10月31日过程](daily/2026-10-31.md)。
- 成功响应结构不等于识别事实正确；规则未覆盖返回不确定，不让模型自行编造深圳规则。[Gemini阶段记录](daily/2026-10-29.md)。

## 3. Prototype Development

- **游戏化成长展示（任务I）**：实际答对6道题，每题+10，取得0/30/60分三种树形；重复领奖被阻止，刷新保存。可直接使用[三阶段截图及+10奖励图](evidence/2026-10-31_tree_growth_summary.md)。这是奖励机制验证，不是学习效果研究；没有新增AI调用。

- 顺序：早期HTML原型 → 已修复HTML → Gemini Flask接入 → Git规范 → Gemini独立备份/main百炼 → 每日记录机制。[历史阶段索引](HISTORY.md)。早期原型和修复实际日期待补，不能制作虚构的精确时间轴。
- Gemini阶段：[归档主页](screenshots/2026-10-29_gemini_home_archived.png)；百炼阶段：[归档主页](screenshots/2026-10-31_bailian_home_archived.png)。可对比保留界面及供应商提示，不能标为同一天拍摄的修复前后实验。
- Git确切日期：10月30日首次提交727501e，后有8016f95规范提交；10月31日本轮开始时迁移未提交，工作期间出现d92f46d/9aa5aea，详见当日日志。[10月30日日志](daily/2026-10-30.md)。

## 4. Technical Feasibility

- **2026-11-02 同Wi-Fi演示准备**：Flask监听改为`0.0.0.0:5000`，同源检查兼容LAN网址，保留原网页。14项离线测试通过；电脑访问本机和WLAN网址均200，未调用真实AI或修改防火墙。手机跨设备访问、上传和答题仍待用户验证，不能称为手机测试成功。[当日日志](daily/2026-11-02.md)、[实际HTTP证据](evidence/2026-11-02_lan_access_tests.json)、[操作说明](../README.md#同一-wi-fi-手机访问2026-11-02)。

- **四张图片真实演示（任务H）**：香蕉皮/充电电池/塑料瓶/纸巾分别得到厨余/有害/可回收/其他建议；各完成1道三选一题，最终40分/Lv.2。共4次真实API，7512 Token，已保存8张分类/答题截图。[直接选取PPT截图](evidence/2026-10-31_four_live_picture_summary.md)。是开发演示验证，不是居民学习效果或大样本准确率实验。

- 2026-10-31任务E实测：用户饮料杯照片经真实北京qwen3.5-flash返回200；模型称“塑料杯”，但材质未核实且无匹配规则，网页显示不确定、无测验，双语结果切换正常。供应商usage总1238 Token（输入1195、输出43）；不代表费用或免费额度已验证。[真实证据](evidence/2026-10-31_real_bailian_cup_test.json)、[实测结果截图](screenshots/2026-10-31_real_bailian_cup_result.png)。适合PPT标注“Live API connectivity verified; waste category unresolved”。

- 2026-10-31任务D补充：依据用户提供的官方文档将默认接入修正为北京标准域名，后端限制北京/qwen3.5-flash。图片缩放、关闭思考、短JSON和512输出上限用于控制请求规模，未实测节省比例或费用。10项离线及浏览器回归通过；用户报告已申请Key、剩余免费额度和用完即停设置，但真实API和免费扣量仍待验证。[配置/截图证据](evidence/2026-10-31_beijing_api_configuration.json)、[当日日志任务D](daily/2026-10-31.md)。

- 本地Windows/Python/Flask可运行；网页通过/api/classify发送Data URL；限制图片格式、大小、像素及元数据；10月31日版本只监听本机，11月2日已开放可信局域网监听。[运行说明](../README.md)、[app.py](../app.py)。
- 旧记录：Gemini7组离线测试；百炼8组离线/模拟测试及浏览器回归通过。当前任务实拍验证主页、本地香蕉皮、缺Key错误。[旧测试文件](../TEST_RESULTS.md)、[10月31日Testing](daily/2026-10-31.md)。这不是最新重复执行全部测试，也不证明真实API连通。
- 适合展示：[缺密钥错误](screenshots/2026-10-31_missing_bailian_key.png)和[本地香蕉皮演示](screenshots/2026-10-31_local_demo_banana.png)。图注注明“Local backend error test”和“Local demo; no AI call”。
- 任务E已有一次真实Key响应（200），但纯模型延迟、费用、识别准确率及跨网络测试仍待验证；不能将单张照片当作完整实验。

## 5. Problems & Iterations

- **2026-11-02 iPhone相册兼容尝试与回退**：用户报告拍照识别正常，但相册`IMG_8150.jpeg`可预览、后端拒绝。确认错误发生在AI调用前的格式/帧数校验；未取得原文件，具体HEIC或MPO根因待核。任务B尝试浏览器转成单帧JPEG，16项后端及桌面回归通过，无真实AI调用；随后用户反馈不行并要求回退，任务C已将程序恢复到57d5df9（保留局域网配置），恢复后14项后端检查通过。相册问题仍未解决，不能把该尝试当作当前功能或手机修复成功。[日志任务B/C](daily/2026-11-02.md)、[历史测试证据](evidence/2026-11-02_iphone_upload_tests.json)、[历史桌面截图](screenshots/2026-11-02_normalized_photo_local_test_03.png)。图为生成样例，不是原照片或手机成功图。英文素材："A JPEG normalization attempt passed desktop tests, but the user requested a rollback after reporting it did not work. We restored the previous version and retained the evidence. The iPhone Photos issue remains unresolved, highlighting the need for real-device testing."

- **课堂Demo反馈后的简化**：规则从6扩至16（新增10条）。严格后测仍不确定（真实1717 Token），用户要求普通塑料杯/瓶直接按已知名称匹配，把清空清洁放题目。已改为“AI分类建议”，用3个代表场景验证问答和积分；简化后的杯子可回收物截图为本地重放，不是第三次真实调用。[完整前后对比](iterations/2026-10-31_expanding_rules.md)、[本地重放图](screenshots/2026-10-31_simple_cup_local_replay.png)。可用英文："We expanded the verified rules, then simplified common-item matching for a classroom demo. Cleaning steps became learning prompts rather than recognition barriers. Results are AI sorting suggestions, not guarantees."

- **Design Iteration — Expanding Waste Classification Rules（先记录原始问题）**：真实API已返回饮料杯相关名称，但杯体材质未核实且原6条规则无匹配，因此保持不确定。拟根据深圳官方资料扩大条件化规则及双语知识题，而不是把图像识别等同正确分类。[完整迭代记录](iterations/2026-10-31_expanding_rules.md)、[不可覆盖的真实前测截图](screenshots/2026-10-31_real_bailian_cup_result.png)。后续结果单独追加，不覆盖前测。

- 安全与规则：用户明确要求失败不造假、电池不能一律判有害；后端错误不回退演示，未核实电池暂停知识题。[原文](prompts/2026-10-29_01_gemini_backend.md)、[10月29日问题记录](daily/2026-10-29.md)。
- 百炼迁移时精确匹配缺Key提示的浏览器测试失败：修正多余空格后重测通过；属于开发自行排查，没有额外用户Prompt。[10月31日问题与测试](daily/2026-10-31.md)。当时失败截图待补，不用今天的页面冒充修复前现场。
- 模型选型调整及双分支保存属于 Design Iteration：完整原因、依据及验证边界见[迁移记录](../DEVELOPMENT_LOG.md#design-iteration)；下方保留一份可用于PPT的英文说明。原[迁移Prompt](prompts/2026-10-31_01_bailian_migration.md)及[本次背景补充](prompts/2026-10-31_03_design_iteration.md)按真实顺序保留，不声称更换模型已提升性能。
- 可用“问题→用户约束→AI协助修改→实际验证”的叙述，引用真实原文和错误截图；不要写出不存在的用户回合。

### Design Iteration: Gemini to Alibaba Cloud Bailian

We initially selected Gemini for its image-understanding capabilities to analyse waste photos. However, our team reported being unable to access Google AI Studio with a school Google account. RecycleAI targets users in Shenzhen, mainland China, which is not listed among Gemini API's supported regions. Google's terms also restrict service access and the availability of API clients by region. To better support practical use in mainland China, we switched the main development branch to Alibaba Cloud Bailian's qwen3.5-flash, while retaining the Gemini version as a backup. This was a design decision driven by access constraints; real API operation in Shenzhen and testing with target users remain unvalidated.

来源与讲解备注：Google[图像理解文档](https://ai.google.dev/gemini-api/docs/image-understanding)、[地区名单](https://ai.google.dev/gemini-api/docs/available-regions)、[服务条款](https://ai.google.dev/gemini-api/terms)，2026-10-31核对。学校账号问题是项目成员报告，本次未独立复现；地区/条款是官方资料核对，不能混称全部为实测。未进行模型性能对比实验。完整过程见[当日日志任务C](daily/2026-10-31.md)和[迁移记录](../DEVELOPMENT_LOG.md)。

## 6. Evaluation & Feedback

- 已确认：开发者用自动化脚本做浏览器回归及模拟接口测试；这是开发测试，不是正式用户研究。[10月29日](daily/2026-10-29.md)、[10月31日](daily/2026-10-31.md)。
- 尚未有：真实用户人数、访谈记录、可用性评分、分类前后测、老师针对原型的具体评价。保留待补充，不把本次用户对记录机制的要求当作学习效果反馈。
- 计划（未执行）：在取得同意后邀请组员完成上传/分类/测验任务，匿名记录完成情况、疑惑、错误建议和改进需求；将记录、样本规模和截图加入当天日志，再更新本栏。

## 7. Limitations & Reflection

- 小白名单、图像和材质歧义、混合垃圾、模型可能误认；Pydantic只能验证结构，不能保证识别或现实规则正确。[规则](../rules.json)、[后端](../app.py)。
- Gemini尚未真实验证；百炼仅单张照片首次连通（任务E），未知规则保持不确定，材质未人工核实，仍不能比较两模型准确率、速度或费用。[测试记录](../TEST_RESULTS.md)。
- 游戏化设计可以展示，但未证明促进学习；该历史阶段五题最多50分；任务F已扩至16题，并通过模拟识别后的实际答题流程达到Lv.3，树机制不变。[日志](daily/2026-10-31.md)、[演示50分图](screenshots/2026-10-31_bailian_demo_archived.png)。
- 伦理与隐私：照片交给外部AI处理，必须提示使用者；密钥后端保存、截图和Prompt脱敏；规则不确定应坦诚说明，避免用生成答案误导投放。[规范](../AGENTS.md)、[原始安全要求](prompts/2026-10-31_02_record_mechanism.md)。
- 反思方向（计划）：讨论AI辅助开发与人工核实的分工、保守规则覆盖率和用户体验取舍、测试证据和真实学习效果的区别。不要将反思设想写成已完成调查。
