# 书稿规划

这是写作用的工作文档，不进电子书。每章只挑三到五个案例，挑选标准按顺序是：用法有代表性（和本章其他案例不重复）、做法讲得清楚、效果有数据，最后才看热度。每个案例写进正文前，都回到原始出处核对过数字；核对不了的数字不写，或者换案例。

全书初版 2026 年 9 月 22 日写完，约 8.7 万个汉字。以后改稿时，数字仍以原始出处为准，书中数据截至 2026 年 9 月下旬。

每个场景章的固定结构：

1. 这个场景的活是什么，以前怎么做，痛点在哪
2. Jev 从哪里切入：用哪种问法，问什么
3. 三到五个案例：做了什么、问题怎么问、效果数据、可以借鉴的地方
4. 一个可以照抄的问题模板（state 怎么组织、问哪几个问题、阈值怎么定）
5. 容易翻车的地方

全书 82 张图：30 张示意图和数据图为本书绘制，源文件在 `assets/figures/src/`，用 `uv run tools/figures.py` 渲染；52 张截图和视频画面来自各案例作者，存放在 `assets/shots/`，图注里注明出处。图号由 `tools/book.lua` 在构建时生成，正文图注不写编号。

全书代码用 `typesafe-sdk` 0.7.1 的写法，每段都在本地模拟的 API 上跑通过；第 3 章的 TypeScript 片段用 `@typesafe-ai/sdk` 0.6.0 做过类型检查。

## 第一部分 认识 Jev

| 章 | 标题 | 要点 | 状态 |
| --- | --- | --- | --- |
| 前言 | | 为什么写、写给谁、怎么读 | 初稿 |
| 1 | Jev：一个只做判断题的模型 | 选择题和作文的类比、System One 和杰文斯、快和便宜、不做什么 | 初稿 |
| 2 | 三种问法：Choice、Score、Noul | 各自适合什么、怎么写问题、置信度和概率的区别、三档阈值、等价问题不一致 | 初稿 |
| 3 | 半小时跑通第一个请求 | 控制台和 Playground、cURL 逐字段、预览版接口的坑、Python 和 JS SDK、官方 skill、计费和限流 | 初稿 |

## 第二部分 按场景看用法

| 章 | 场景 | 选用案例 | 这章讲清楚的套路 |
| --- | --- | --- | --- |
| 4 | 金融与交易 | tax-doc-classifier、Jev 加 Kimi 查诈骗邮件、QuantDinger 交易前闸门、jev-trader；反面：MoonGotchi 自称亏损的帖子（附的是模拟盘录像）和 WquGuru 的回测 | 取最弱一步的置信度、升级给大模型、判断和执行分离 |
| 5 | 编程 agent | fast-jev-compaction 和 Hermes 评分卡、Abide、Nitro、jev-auto-approve；旁证 jcm-router | 上下文压缩、规则守门、工具裁剪、PR 分诊、缓存 |
| 6 | 浏览器与电脑操控 | jev-ultrafast、typesafe-computer-use、agent-desktop 的 jev-desktop、ghosthands；旁证梭哈.AI 填表 | 候选表加 Choice、推测式目标、分层选、写字交给谁 |
| 7 | Agent 编排与路由 | OpenHuman 工具搜索、MetaCog、Pisper、hermes-jev-approvals；反面：SLO Router | 先粗筛再精选、按风险定阈值、路由和审批朝相反方向退 |
| 8 | 搜索与 RAG | 官方重排 cookbook、hev reranker、Turbo Rerank、官方 RAG 片段分类 cookbook（附 jev-reranker）、neo4jev | 概率当排序分、把关问题、在图上逐跳导航 |
| 9 | 安全与审核 | 官方护栏 cookbook、jev-shield、tokengate、1940s.nyc 审核实验；反面：越狱基准 | 一条规则一个 Noul、在不同位置设卡、低误报率下的召回 |
| 10 | 数据与评测 | 46 万篇论文摘要、classifier.dev、官方特征发现 cookbook、LangWatch Instant Evals、judge-audit | 全量标注、判断变特征、Jev 当评委、先校准再用 |
| 11 | 客服与销售 | Warmbly、customer-work、Mac 应用内帮助、lurk、Twenty 的 Classify 节点 | 一条记录问多个问题、Jev 筛选大模型写字、只能更保守 |
| 12 | 电商、营销与内容 | NewsJack、全站内链审计（borja 与 jev-linkmap）、亚马逊评论打包、合成焦点小组、jevmeter | 从抽查到全量、组合数先用代码砍、Score 的等级写法 |
| 13 | 实时交互 | Jev 玩 Doom、jev-tetris、AIAvatarKit 话轮检测、jev-canvas、jev-drone；旁证 live-jev | 延迟预算、画面和声音先变文字、Jev 只坐最慢的一层 |
| 14 | 个人效率与更多行业 | Intern、jev-skip、ADHD 系统综述初筛、FGV 判决编码、大声读；旁证 Inbox Zero | 按步提问、专业场景只做初筛和分流 |

换掉的建议案例和原因：

- 第 5 章 jev-shell-history：不在编程 agent 的循环里，也没有效果数据，换成 PR 分诊。
- 第 6 章 Jev 加 DeepSeek 填表：只有帖子没有代码，降为旁证；补进做了分层选的 jev-desktop。
- 第 8 章 FindSFSymbols：请求形状和 Turbo Rerank 相同，也没有效果数据，换成有横向对比的 hev reranker。
- 第 9 章实时 AI 水文检测：原帖没有代码和数据，换成 1940s.nyc 审核实验。
- 第 11 章 Grok 加 Jev 线索筛选：没有仓库，报告的速度超出官方默认限流十倍以上，核实不了，换成 Warmbly 和 customer-work。
- 第 13 章自动驾驶仿真 live-jev：没有效果数据，降为旁证，换成有对照组的 jev-drone。

## 第三部分 用好 Jev

| 章 | 标题 | 要点 | 状态 |
| --- | --- | --- | --- |
| 15 | 六个反复出现的设计模式 | 一次问完、置信度路由、组合打分、先找候选再选、模型读代码算、验证后升级 | 初稿 |
| 16 | 它不擅长什么 | 官方九类短板加社区反面实测，中文和表格数据，什么时候干脆别用 | 初稿 |
| 17 | 开源复刻与替代 | SemIf、openjev-sglang、Kev、Laya、LocalJev，校准差在哪，什么时候该换 | 初稿 |
| 附录 A | 资源导航 | awesome-jev、官方文档关键页、SDK、社区渠道、仿冒站点 | 初稿 |
