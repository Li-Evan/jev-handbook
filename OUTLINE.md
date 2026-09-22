# 书稿规划

这是写作用的工作文档，不进电子书。每章只挑三到五个案例，挑选标准按顺序是：用法有代表性（和本章其他案例不重复）、做法讲得清楚、效果有数据，最后才看热度。每个案例写进正文前，要回到原始出处核对一遍数字。

篇幅目标：正文约 10 万字。第一部分每章 4,000 字左右，第二部分每章 5,000 到 6,000 字，第三部分每章 4,000 字左右。

每个场景章的固定结构：

1. 这个场景的活是什么，以前怎么做，痛点在哪
2. Jev 从哪里切入：用哪种问法，问什么
3. 三到五个案例：做了什么、问题怎么问、效果数据、可以借鉴的地方
4. 一个可以照抄的问题模板（state 怎么组织、问哪几个问题、阈值怎么定）
5. 容易翻车的地方

## 第一部分 认识 Jev

| 章 | 标题（暂定） | 要点 | 状态 |
| --- | --- | --- | --- |
| 前言 | | 为什么写、写给谁、怎么读 | 初稿 |
| 1 | Jev：一个只做判断题的模型 | 选择题和作文的类比、System One 和杰文斯、快和便宜、不做什么 | 初稿 |
| 2 | 三种问法：Choice、Score、Noul | 各自适合什么、怎么写问题、置信度和概率的区别、三档阈值 | 待写 |
| 3 | 半小时跑通第一个请求 | Playground、cURL、Python 和 JS SDK、编程 agent 的 skill | 待写 |

## 第二部分 按场景看用法

| 章 | 场景 | 选用案例（原始链接） | 这章想讲清楚的套路 |
| --- | --- | --- | --- |
| 4 | 金融与交易 | [jev-trader](https://github.com/jarrodwatts/jev-trader)（每个区块判断一次买卖）<br>[Jev + Kimi 欺诈检测](https://github.com/Nutlope/jev-fraud)（低置信度交给大模型复核）<br>[tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier)（两个 Choice 给税表分类）<br>[一晚上搭的交易机器人](https://x.com/MoonGotchi/status/2101320141065609294)（反面：已亏 31,680 美元） | 高频判断、置信度升级、判断和执行分离 |
| 5 | 编程 agent | [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) 与 [Hermes 的反面评测](https://github.com/NousResearch/hermes-agent/blob/main/evals/compaction/results/SCORECARD-2026-09-19-jev.md)<br>[Abide](https://github.com/coldteadotai/abide)（按规则检查每次编辑）<br>[Nitro](https://github.com/daniel-farina/nitro)（每轮只加载要用的工具）<br>[jev-shell-history](https://github.com/mrnugget/jev-shell-history)（命令补全） | 上下文压缩、规则守门、工具裁剪 |
| 6 | 浏览器与电脑操控 | [jev-ultrafast](https://github.com/browser-use/jev-ultrafast)（元素表加推测目标）<br>[typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use)（OCR 后选控件）<br>[Jev + DeepSeek 填表](https://x.com/SUOHA_AI/status/2101640575812239406)（判断和写字分工）<br>[ghosthands](https://github.com/affirmitv/ghosthands)（4 美元硬件驱动真实屏幕） | 从候选里选动作，只在要写字时调大模型 |
| 7 | Agent 编排与路由 | [OpenHuman 工具排序](https://github.com/tinyhumansai/openhuman/tree/main/crates/openhuman-tinyhumans/src/jev)（BM25 加 Choice）<br>[MetaCog](https://github.com/ItIsCuthNotCup/MetaCog)（挑选继续哪条思路）<br>[Pisper](https://github.com/ling-kong-ran/pisper/blob/release/runtime/services/decision-service.mjs)（按阈值自动审批）<br>[SLO Router](https://github.com/zeeshan8281/slo-router)（反面：没改变路由却拖慢了延迟） | 先粗筛再精选、按风险定阈值 |
| 8 | 搜索与 RAG | [官方重排 cookbook](https://docs.typesafe.ai/cookbooks/rerank_typesafe)<br>[Turbo Rerank](https://github.com/dabit3/macos-experiments/tree/main/turbo-rerank)（50 个候选一次重排）<br>[FindSFSymbols](https://github.com/tornikegomareli/FindSFSymbols)（48 个 Noul 驱动物理动画）<br>[neo4jev](https://github.com/jexp/neo4jev)（在图上一跳一跳导航）<br>[RAG 片段分类 cookbook](https://docs.typesafe.ai/cookbooks/classifying_rag_passages) | 概率就是排序分、先召回再判断 |
| 9 | 安全与审核 | [官方护栏 cookbook](https://docs.typesafe.ai/cookbooks/llm_guardrails)<br>[jev-shield](https://github.com/caiovicentino/jev-shield)（MCP 防火墙）<br>[tokengate](https://github.com/Thanh-Mathieu95/jev-model-tokengate)（流式输出时截断）<br>[实时 AI 水文检测](https://x.com/RBilgil/status/2100976648552169805)<br>[越狱基准](https://backnotprop.com/blog/jev-guardrails/)（反面：1% 误报率下几乎抓不到） | 多个 Noul 组成检查单、护栏不是安全边界 |
| 10 | 数据与评测 | [classifier.dev](https://github.com/mrmps/classifier-dev)（零样本分类，低置信度再问推理模型）<br>[LangWatch Instant Evals](https://github.com/langwatch/langwatch/tree/main/platform/app/src/server/app-layer/instant-evals/classifier)<br>[judge-audit](https://github.com/kunko-ai-labs/judge-audit)（审计 AI 评委是否校准）<br>[读完 464,720 篇 AI 论文摘要](https://x.com/DevaiahShrithan/status/2102097862805053950) | 大批量标注、用 Jev 当评委 |
| 11 | 客服与销售 | [Twenty CRM 的 Classify 步骤](https://github.com/twentyhq/twenty/tree/main/packages/twenty-server/src/modules/workflow/workflow-executor/workflow-actions/classify)<br>[Grok + Jev 线索筛选](https://x.com/razeden0/status/2102119174466396250)（3,412 条线索 0.41 美元）<br>[lurk](https://github.com/getanyapi-com/lurk)（在 Reddit 找购买意向）<br>[Mac 应用内帮助](https://x.com/malekoo/status/2100439840575684910)（42/42 全对） | 一条记录问多个问题、Jev 筛选大模型写字 |
| 12 | 电商、营销与内容 | [NewsJack](https://x.com/elvissun/status/2100951347080421409)<br>[全站内链审计](https://x.com/borjafat/status/2101018783976722479)<br>[合成焦点小组](https://x.com/TheMattBerman/status/2101439340588974096)（30 个买家画像刷 723 条广告）<br>[jevmeter](https://github.com/ChetasLua/jevmeter)（给视频逐句打分） | 以前舍不得看的全看一遍 |
| 13 | 实时交互：游戏、语音与机器人 | [Jev 玩 Doom](https://x.com/CompleteSkeptic/status/2099925687465570372)<br>[jev-tetris](https://github.com/trungdq88/jev-tetris)（和大模型对战）<br>[指点加说话的画布](https://x.com/jackcheng/status/2100729670991802386)<br>[语音对话的话轮结束检测](https://x.com/uezochan/status/2100608556823388486)<br>[自动驾驶仿真](https://github.com/vinilana/live-jev) | 判断快到 100 毫秒以后能做的事 |
| 14 | 个人效率与更多行业 | [Intern](https://github.com/dabit3/intern)（每敲一个键就判断一次）<br>[jev-skip](https://github.com/valentynkit/jev-skip)（跳过视频赞助）<br>[系统综述摘要筛选](https://github.com/PistachioAIHQ/jev-synergy-screening)<br>[ReadAloud](https://github.com/wquguru/dasheng)（朗读纠音） | 把判断塞进日常工具的每一步 |

## 第三部分 用好 Jev

| 章 | 标题（暂定） | 要点 | 状态 |
| --- | --- | --- | --- |
| 15 | 六个反复出现的设计模式 | 一次问很多问题、置信度路由、组合打分、先找候选再选、模型读代码算、验证后升级 | 待写 |
| 16 | 它不擅长什么 | 官方列出的短板，加上社区的反面实测：压缩评测、SLO Router、越狱召回、表格数据 | 待写 |
| 17 | 开源复刻与替代 | [Kev](https://github.com/jaredpalmer/kev)、[Laya](https://github.com/NandhaKishorM/laya)、[SemIf](https://github.com/TheoLeeCJ/SemIf)、[openjev-sglang](https://github.com/ekzhang/openjev-sglang)，以及什么时候该用它们 | 待写 |
| 附录 A | 资源导航 | awesome-jev 在线画廊、官方文档、速查表 | 待写 |
| 附录 B | 怎么把这本书导入微信读书 | 网页传书、格式和数量限制 | 待写 |
