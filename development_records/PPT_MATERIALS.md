# RecycleAI PPT 素材库

课程：香港教育大学 INT6065 Artificial Intelligence in Education。以下为简洁中文素材，便于以后制作英文Presentation；没有生成最终PPT。证据基线：Gemini提交727501e/8016f95；百炼及当前记录机制尚未提交，不能使用8016f95冒充百炼版本。所有截图均是网页/本地演示/错误路径，不是实际云端识别成功证据。

## 1. Problem Identification

- 已确认的项目目标：通过垃圾照片分类建议、投放说明及测验帮助使用者学习分类，兼顾环保积分和小树成长。来源：[初始用户需求原文](prompts/2026-10-29_01_gemini_backend.md)、[10月29日目标](daily/2026-10-29.md)。
- 展示图：[当前主页](screenshots/2026-10-31_current_home.png)，说明“课程原型的设计目标”，不能据此声称用户分类能力已经提高。
- 待补充：需求访谈、错误分类频率或用户痛点调查。没有调查数据，不编造百分比。

## 2. AI Concepts & System Design

- 已实现结构：上传图片 → Flask检查/内存转码 → 图像理解模型识别物品和可见条件 → Pydantic校验 → 本地已核实规则 → 双语解释及可用题目。它是多模态模型调用与规则约束相结合，没有证据表明小组训练或微调了模型。
- Gemini备份默认gemini-3.5-flash-lite；main百炼默认qwen3.5-flash。API提供商是后端配置，密钥不在前端。[main后端](../app.py)、[规则](../rules.json)、[10月31日过程](daily/2026-10-31.md)。
- 成功响应结构不等于识别事实正确；规则未覆盖返回不确定，不让模型自行编造深圳规则。[Gemini阶段记录](daily/2026-10-29.md)。

## 3. Prototype Development

- 顺序：早期HTML原型 → 已修复HTML → Gemini Flask接入 → Git规范 → Gemini独立备份/main百炼 → 每日记录机制。[历史阶段索引](HISTORY.md)。早期原型和修复实际日期待补，不能制作虚构的精确时间轴。
- Gemini阶段：[归档主页](screenshots/2026-10-29_gemini_home_archived.png)；百炼阶段：[归档主页](screenshots/2026-10-31_bailian_home_archived.png)。可对比保留界面及供应商提示，不能标为同一天拍摄的修复前后实验。
- Git确切日期：10月30日首次提交727501e，后有8016f95规范提交；10月31日工作区尚未提交。[10月30日日志](daily/2026-10-30.md)。

## 4. Technical Feasibility

- 本地Windows/Python/Flask可运行；网页通过/api/classify发送Data URL；限制图片格式、大小、像素及元数据；只监听本机。[运行说明](../README.md)、[app.py](../app.py)。
- 旧记录：Gemini7组离线测试；百炼8组离线/模拟测试及浏览器回归通过。当前任务实拍验证主页、本地香蕉皮、缺Key错误。[旧测试文件](../TEST_RESULTS.md)、[10月31日Testing](daily/2026-10-31.md)。这不是最新重复执行全部测试，也不证明真实API连通。
- 适合展示：[缺密钥错误](screenshots/2026-10-31_missing_bailian_key.png)和[本地香蕉皮演示](screenshots/2026-10-31_local_demo_banana.png)。图注注明“Local backend error test”和“Local demo; no AI call”。
- 待补：真实Key下的成功响应、延迟、费用、识别准确率及跨网络测试。不要在PPT写成已实现的实验结论。

## 5. Problems & Iterations

- 安全与规则：用户明确要求失败不造假、电池不能一律判有害；后端错误不回退演示，未核实电池暂停知识题。[原文](prompts/2026-10-29_01_gemini_backend.md)、[10月29日问题记录](daily/2026-10-29.md)。
- 百炼迁移时精确匹配缺Key提示的浏览器测试失败：修正多余空格后重测通过；属于开发自行排查，没有额外用户Prompt。[10月31日问题与测试](daily/2026-10-31.md)。当时失败截图待补，不用今天的页面冒充修复前现场。
- 用户要求先保留Gemini再开发main；使用分支和独立工作目录保护原版本。[实际迁移Prompt](prompts/2026-10-31_01_bailian_migration.md)、[开发记录](../DEVELOPMENT_LOG.md)。未证明更换模型提升性能。
- 可用“问题→用户约束→AI协助修改→实际验证”的叙述，引用真实原文和错误截图；不要写出不存在的用户回合。

## 6. Evaluation & Feedback

- 已确认：开发者用自动化脚本做浏览器回归及模拟接口测试；这是开发测试，不是正式用户研究。[10月29日](daily/2026-10-29.md)、[10月31日](daily/2026-10-31.md)。
- 尚未有：真实用户人数、访谈记录、可用性评分、分类前后测、老师针对原型的具体评价。保留待补充，不把本次用户对记录机制的要求当作学习效果反馈。
- 计划（未执行）：在取得同意后邀请组员完成上传/分类/测验任务，匿名记录完成情况、疑惑、错误建议和改进需求；将记录、样本规模和截图加入当天日志，再更新本栏。

## 7. Limitations & Reflection

- 小白名单、图像和材质歧义、混合垃圾、模型可能误认；Pydantic只能验证结构，不能保证识别或现实规则正确。[规则](../rules.json)、[后端](../app.py)。
- 当前真实Gemini和百炼识别均缺验证；不能比较两模型准确率、速度或费用。[测试记录](../TEST_RESULTS.md)。
- 游戏化设计可以展示，但未证明促进学习；五道核实题最多50分，60分树阶段只用合成状态验证。需要更多有来源的题目才能自然升级。[日志](daily/2026-10-31.md)、[演示50分图](screenshots/2026-10-31_bailian_demo_archived.png)。
- 伦理与隐私：照片交给外部AI处理，必须提示使用者；密钥后端保存、截图和Prompt脱敏；规则不确定应坦诚说明，避免用生成答案误导投放。[规范](../AGENTS.md)、[原始安全要求](prompts/2026-10-31_02_record_mechanism.md)。
- 反思方向（计划）：讨论AI辅助开发与人工核实的分工、保守规则覆盖率和用户体验取舍、测试证据和真实学习效果的区别。不要将反思设想写成已完成调查。
