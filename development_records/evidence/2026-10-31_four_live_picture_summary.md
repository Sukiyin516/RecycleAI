# 2026-10-31 四张图片真实测试

用户指定 test_picture 中四张单图，排除 all(no_test).png。北京qwen3.5-flash真实调用4次，非模拟；全部供应商/Flask HTTP200，分类显示和简单三选一答题均完成。

| 文件 | AI名称 | 建议垃圾桶 | 分类截图 | 答题截图 |
|---|---|---|---|---|
| banana.jpg | 香蕉皮 | 厨余垃圾 | [分类页](../screenshots/2026-10-31_live_banana_classification.png) | [答题页](../screenshots/2026-10-31_live_banana_quiz_answer.png) |
| battery.png | 锂电池 | 有害垃圾 | [分类页](../screenshots/2026-10-31_live_battery_classification.png) | [答题页](../screenshots/2026-10-31_live_battery_quiz_answer.png) |
| bottle.jpg | 塑料瓶 | 可回收物 | [分类页](../screenshots/2026-10-31_live_bottle_classification.png) | [答题页](../screenshots/2026-10-31_live_bottle_quiz_answer.png) |
| tissue.jpg | 纸巾 | 其他垃圾 | [分类页](../screenshots/2026-10-31_live_tissue_classification.png) | [答题页](../screenshots/2026-10-31_live_tissue_quiz_answer.png) |

四题各+10分，最终40分、Lv.2。供应商usage合计7512 Token；免费扣量没有登录控制台核对。素材由用户选择，不构成大样本准确率或真实居民学习效果实验。

为电池案例仅增加一条已核实充电电池规则和双语题，目前17条规则；不将所有电池一律视为有害垃圾。同类型多个物品按一个主要类型识别。网页设计与积分/树机制未改。现有13项后端检查通过。

[脱敏真实响应及usage](2026-10-31_four_live_picture_tests.json)。原四张照片不复制进仓库，截图仅分类结果与答题页面。旧杯子截图和记录不修改。助手未Commit或Push。
