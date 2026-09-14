---
name: sw-workflow
description: Project orchestrator for the screenwriting skill set (剧本项目主线调度 / 状态存档 / story bible) — a meta-skill that adds no new craft knowledge but routes a screenplay or stage-play project through stages (premise → structure → character → scenes → draft → revision → submission) and a TV / streaming series project (电视剧 / 剧集 / pilot / 一季) through a separate series stage table (engine → character network & season arc → documents/bible → pilot structure → break story & outline → draft → submission), names which sw-* skill to invoke at each stage, defines each stage's deliverable and advisory exit check, and keeps all project state in a story-bible.md file so work can resume across sessions. Use when starting a new script project, resuming one ("continue my screenplay", "where were we"), when the user asks "what should I do next" on a script, when converting a vague idea into a full development pipeline, or when the other sw-* skills are firing individually and the overall process needs sequencing.
---

# 剧本项目主线调度（Workflow & Story Bible）

本 skill 不含新的编剧知识，只做两件事：**排顺序**（哪个阶段调用哪个 skill、交什么、什么算过关）和**存状态**（把每阶段结论写进 `story-bible.md`，下次会话接着做）。所有方法都在其他 sw-* skill 里，本 skill 只负责在正确的时刻把它们叫出来。

设计依据来自一次对照实验：同一题目，按流程先填工作单再写，与不用流程直接写相比，篇幅、主角主动性、对手强度、潜台词全部不同；差别不在知识，在于"动笔前必须填的表、写完后必须过的清单"。本 skill 就是那张表和那份清单的调度器。

story-bible 模板与各阶段工作单见 [reference.md](reference.md)；跨语言输出时的术语锚定表见 [terms.md](terms.md)。

---

## 一、会话协议（每次开始与结束都执行）

### 开始

1. 在当前目录（或用户指定的剧本目录）找 `story-bible.md`。
2. **找到**：只读"当前阶段""已定决策""决策日志"三节，用三句话向用户复述：项目是什么、做到哪一步、上次定了什么。然后直接进入当前阶段，不重新讨论已定决策，除非用户主动推翻。
3. **一次性交付不建 bible**：用户要的是一份当场交出去的文档（开发方案、提案、一页梗概、分集大纲），且明显不会有下一次会话来接——这时建 bible 是净成本，直接在同一会话里按阶段表跑完即可。bible 解决的是**跨会话丢上下文**，不是"流程要有表"。
4. **没找到且是持续项目**：判断入口路径（见第三节），按 reference.md 模板新建 `story-bible.md`，只填"项目信息"和"当前阶段"，其余留空。不要一次问用户四个以上的问题；能从用户的话里推断的先填上，标"（待确认）"。

### 进行中

- 每完成一个阶段的交付物，立刻写进 story-bible 对应节，并把"当前阶段"推进一格。
- 任何改变既定决策的动作（换前提、换结尾、删人物）都在"决策日志"加一行：日期、改了什么、为什么。
- story-bible 保持在一次能读完的长度（约 25K token，中文 1.5 万字以内）。产物只写结论，不写推导过程；大纲、处理台本、剧本正文放独立文件，bible 里只记文件名和一句状态。

### 结束

- 会话结束前确认 story-bible 已更新到最新，最后一行写"下一步："一句话。

---

## 二、阶段图

| # | 阶段 | 调用的 skill | 交付物（写入 story-bible 的节） | 建议通过标准 |
|---|---|---|---|---|
| 0 | 启动 / 续写 | 本 skill | 项目信息、入口路径、当前阶段 | 知道要做什么类型、多长、给谁 |
| 1 | 选材与前提 | `sw-premise-theme` | 闪念与"为什么在乎"、主旨一句、假设问题、**前提**（人物特质＋导致＋结局）、**主控思想**（价值＋原因）、第三条轨道（渴望 vs 错误信念）、戏核、一句话故事、logline | 前提只有一个；能向陌生人一句话说清；戏核抽掉戏不成立；主题词定了 |
| 2 | 结构 | `sw-story-structure` | 结尾、开端、情节点Ⅰ/Ⅱ、中点性质（胜利假象/失败假象）、BS2 页码表、幕比例、次情节与主控思想的关系 | 四件事（结尾/开端/两个情节点）都知道；铺垫≤25 页；中点与"失去一切"互为反面；最后一幕最短 |
| 3 | 人物与冲突 | `sw-character-conflict` | 主要人物三维表、具体类别、对主题态度、对立统一的绑定物、对手的刀、成长阶梯、原初场景 | 主角最多维；对手总和强于主角；没有两人同型；有"最强的对手是自己"的一面；没有祥云 |
| 4 | 场景清单 / 处理台本 | `sw-scene-craft` ＋ `sw-format-adaptation` | 步骤大纲（每场一两句＋价值转折＋结构位置）、演示板 40 卡（+/-、><）、道具与形象系统、处理台本（可选） | 每场价值有转折；第三幕不止两张卡；相邻场景有过渡要素；无纯解说场 |
| 5 | 初稿 | `sw-dialogue` ＋ `sw-format-adaptation`（格式与输出契约）＋ 参照类 skill | 剧本文件（好莱坞式交 `.fountain`，中文场号制或日式交纯文本，见 `sw-format-adaptation` 二之二）、页数、每日进度 | 页数在目标 ±15%；格式硬规则全过；对白遮名可辨 |
| 6 | 修改 | 各 skill 的"诊断清单" | 修改目标清单、逐项完成记录、稿次 | 结构诊断 13 问、人物诊断 14 问、对白诊断 14 问、场景诊断 13 问、格式诊断（A 通用 12 问＋所采用体例那一组）都跑过一遍 |
| 7 | 提交 / 行业 | `sw-industry-business` | logline 与一页梗概、推销稿、目标买家/比赛、署名与登记 | PROBLEM 七要素自检通过；一句话经过陌生人测试 |

**参照类 skill 何时进入**：
- `sw-american-case-studies`：阶段 1–2 找同类型片单和陈词滥调；阶段 6 对照同类型高潮。
- `chekhov-dramaturgy`、`ozu-screenplay-style`：写反高潮、多主人公、家庭题材、"事件画外反应画内"时，从阶段 2 起作为结构与语气的样板。
- 戏曲四个 skill（`sw-chinese-opera-banqiang`、`sw-chinese-opera-qupai` 与两个 `-cases`）：项目是戏曲时不走本节的长片阶段表，改走三之三的 X 表或 Q 表；两个方法 skill 开头的媒介边界表决定通用 skill 哪几层能用。
- `sw-japanese-screenwriting`、`sw-korean-french-screenwriting`：片段优先、主题后置、类型承诺、集体创作等替代路径；用户明确不走三幕经典设计时在阶段 1 就引入。
- `sw-truby-anatomy`（有机故事解剖）：页码地图与有机骨架并排——阶段 2 的 BS2 板定稿后做有机校验（七大步骤倒查＋22 步骤中段组件）；阶段 3 人物表配四角对立工作单；阶段 4 步骤大纲的结构位置列可标 22 步骤名＋线号；阶段 6 中段松散跑它的诊断十问。契诃夫／小津式反高潮、多主人公项目与剧集项目不适用其中心对决组件。
- 剧集类 skill（`sw-series-structure`、`sw-series-engine-bible`、`sw-writers-room`、`sw-sitcom-comedy`、`sw-chinese-series-practice`、`succession-series-writing`、`sw-series-case-studies`）：只在入口路径判为剧集时进入，走三之二的剧集阶段表。

**阶段可以回退**：阶段 5 发现对白写不动，通常是阶段 3 的人物或阶段 1 的前提有洞，回去补，然后在决策日志记一笔。

---

## 三、入口路径

| 用户情况 | 从哪个阶段开始 | 特别处理 |
|---|---|---|
| 从零写长片 / 多幕剧 | 0 → 1 → … → 7 全走 | 标准路径 |
| 手里已有初稿要改 | 先做阶段 1–3 的**反向填表**（从稿子里提取前提、结构、人物填进 bible），再进阶段 6 | 填表时把稿子里没有的项标"缺"，这些缺项就是修改清单 |
| 改编小说 / 舞台剧 / 真实事件 | 0 → `sw-format-adaptation` 改编四问 → 1 → 2 … | 阶段 1 先答"原素材的冲突主要在哪一层面、要重新发明什么"；真人故事先确认授权；**戏曲题材不走本行，走三之三的 X0.5／Q0.5** |
| 短片 / 小戏 / 独幕剧 | 1 → 2（用陆军起承转合与八法代替 BS2）→ 3 → 5 | 演示板缩到 10–15 卡；人物≤5；戏核必须先有 |
| 戏曲·板腔体（京剧 / 豫剧 / 越剧 / 秦腔 / 评剧 / 沪剧 / 川剧弹戏胡琴） | 走三之三的**板腔体 X0–X6**，不走长片阶段表 | 先定体制再定结构；唱段只给重场戏；宾白走 `sw-dialogue`，唱词与板式走 `sw-chinese-opera-banqiang`；全本对照看 `sw-chinese-opera-banqiang-cases` |
| 戏曲·曲牌体（元杂剧 / 明清传奇 / 昆曲 / 川剧高腔） | 走三之三的**曲牌体 Q0–Q6** | 先答"场上还是案头""杂剧还是传奇"两个开关；填词走 `sw-chinese-opera-qupai`；全本对照看 `sw-chinese-opera-qupai-cases`；川剧本子两表都看 |
| 只有一个点子，不知道能不能写 | 1（只到一句话故事）→ 7 的 PROBLEM 自检 | 通过再回 2；不通过就换点子，bible 里保留被否的点子和原因 |
| 电视剧 / 剧集 / pilot / 一季 | 走第三节之二的**剧集阶段表**（S0–S7），不走上面的长片阶段表 | 引擎与 bible 先于剧本；国产剧另加 `sw-chinese-series-practice` 的文档链；企画书格式见 `sw-format-adaptation` reference 的大宫艾丽模板 |
| 半小时喜剧 / 情景喜剧 | 剧集阶段表，但 S2、S5 换用 `sw-sitcom-comedy` | 页数、格式、笑点密度整体切换 |
| 行业问题（怎么卖、署名、经纪人） | 直接 7 | 不建 bible |

### 三之二、剧集阶段表（电视剧 / 流媒体剧 / 迷你剧）

剧集与长片的差别不是"更长的电影"：电影是闭合弧、一次性问题；剧集是可重复的**引擎**＋不闭合的关系张力，按出幕（act out）切段，多线并行，bible 先于剧本，集体创作并由 showrunner 统稿。所以顺序倒过来：**先证明引擎能跑一百集，再写第一集。**

| # | 阶段 | 调用的 skill | 交付物（写入 story-bible 的节） | 建议通过标准 |
|---|---|---|---|---|
| S0 | 启动 / 续写 | 本 skill | 平台与格式（广播 / 有线 / 流媒体；一小时 / 半小时；集数、季数）、入口路径 | 知道幕数由谁决定（广告位还是自己）、目标页数 |
| S1 | 引擎与前提 | `sw-series-engine-bible` ＋ `sw-premise-theme` | 主题对立命题、franchise 四元素（concept / conflict / theme / story pattern）、核心问题写成"过程句"、tacit contract 一句话、5–6 条 sample story areas | "pilot 之后想不出三集"即不通过；五条 story area 来源或结局雷同即不通过 |
| S2 | 人物网与季弧 | `sw-series-engine-bible` ＋ `sw-character-conflict` | 3–4 位主角（各 ≤1 页）与冲突网（谁和谁绑定、专长分工、家庭动力学）、季弧表（集 × 人物 want/状态）、season question 与 tentpole | 主角之间不能"微笑着同意对方"；每人有可失之物；季末回答的是"今年这个版本的问题"而不是总问题 |
| S3 | 文档 | `sw-series-engine-bible`（+ `sw-chinese-series-practice` 若为国产剧） | logline 与跳板、pitch document / series format、bible（选档）、故事线文档（每条线的目的/推动者/入口出口/跨集节拍）；国产剧另交剧情简介→梗概→人物小传→分集大纲 | 文档能让陌生人复述"每周会发生什么"；国产剧分集大纲每集有收口悬念 |
| S4 | pilot 与单集结构 | `sw-series-structure`（半小时喜剧换 `sw-sitcom-comedy`） | pilot 类型选择（premise / typical-episode / hybrid）、幕数与页码锚点、act out 清单、A/B/C 线的入口出口、Story Map 17 栏 | 每个 act out 提出新问题；C 线不收幕；隐形幕能说出三重依据 |
| S5 | 破故事与大纲 | `sw-writers-room` ＋ `sw-scene-craft` | beat sheet（每幕 6–7 场）→ outline（locked）；单集 6 周日程 | outline 每场一个 beat，含幕内位置；改结尾必须回大纲 |
| S6 | 初稿与改稿 | `sw-dialogue` ＋ `sw-format-adaptation` ＋ `sw-writers-room`（接 note） | 剧本文件（teaser / ACT 标记或 day 标记）、页数、warm read 与 cold read 记录 | 页数在格式区间内（一小时 48–63、半小时单机 ≈30、多机 ≈50）；cold read 能答"下一集是什么" |
| S7 | 提交 / 行业 | `sw-industry-business`（美国）/ `sw-chinese-series-practice`（国内：立项、备案、审查、交付节点） | pitch 20 分钟稿、leave-behind 一页、目标平台清单 | 一次会议只 pitch 一个；国产剧过内容与技术两道审查的自检 |

**参照类 skill 何时进入**：`succession-series-writing`（流媒体群像、隐形幕、季形对称、结局工程）从 S2 起作样板；`sw-series-case-studies`（West Wing 四幕、Sopranos pilot、Downton 多线、Fleabag 六集季、Calvisi 八个 pilot 节拍表、坂元裕二、卢熙京）在 S1 找同类 comp、S4 对照节拍。`chekhov-dramaturgy` 与 `ozu-screenplay-style` 是**跨阶段表通用参照**（不专属长片）：写反高潮、多主人公、家庭题材、"事件画外反应画内"时，剧集线从 S2 起同样调用，但先过 `ozu-screenplay-style` 二之 1 与二之 14 的容量前件与剧集换算。**长片 skill 的媒介无关部分照用**：对白、场景价值转折、三维人物、前提——不要因为是剧集就跳过它们。

**S5 的两套场级工具分工**：剧集的场级方法**优先用 `sw-series-structure` 六的五件套**（一场一个目的、进出点、价值转折、信息差、下一场的钩），破 beat sheet 与写 outline 时逐场过；`sw-scene-craft` 的**演示板 40 卡与"删掉会怎样"在 outline 成形后补一遍**（40 卡按本季集数摊，不是每集 40 卡），用来删无转折场。两套都不跑才算漏步骤，只跑五件套不算。

**回退**：S4 写不出第二集的 act out，通常是 S1 的引擎问题；S6 对白写不动，通常是 S2 的人物网没有可失之物。回去补，记决策日志。

### 三之三、戏曲阶段表（板腔体 / 曲牌体）

戏曲不走长片阶段表，也不走剧集阶段表：它的结构单位是场／折／出，唱段先于对白，体制（唱工戏还是做工戏）先于结构，而且**要先判声腔体系再选 skill**。判法：京剧、豫剧、越剧、秦腔、评剧、沪剧、川剧弹戏胡琴 → 板腔体（X 表）；元杂剧、明清传奇、昆曲、川剧高腔 → 曲牌体（Q 表）；川剧本子一本之内可跨两体系，两表都看。两张表的方法在 `sw-chinese-opera-banqiang` 与 `sw-chinese-opera-qupai`，全本语料在 `sw-chinese-opera-banqiang-cases` 与 `sw-chinese-opera-qupai-cases`；两体系共用的美学与排演层在 `sw-chinese-opera-banqiang/reference-common.md`。

**板腔体 X0–X6**

| # | 阶段 | 调用的 skill | 交付物（写入 story-bible 的节） | 建议通过标准 |
|---|---|---|---|---|
| X0 | 启动 | 本 skill | 剧种、体系、是新编／整理老戏／现代戏／命题改编、为哪位演员或行当写 | 剧种与体系判定不含糊；剧本体例定京剧式还是越剧式 |
| X0.5 | 真人／史料题材（有则做） | `sw-chinese-opera-banqiang`（第十一节改编四问） | 一张对照表：每条关目是史载、传说、还是我编的；最大的一处虚构及其约束 | 虚构只发生在史料留白处；不替主角卸责；四问在戏曲 skill 内答完，不读 `sw-format-adaptation` |
| X1 | 定体制 | `sw-chinese-opera-banqiang`（体制与体裁）＋ `sw-premise-theme`（戏核） | 唱工／做工／武打／并重之一，及其依据（人物行动性与行当、情节繁简与舞蹈条件、风格）；戏核一句 | 体制定了再往下；"顺向开辟"自检过（不逆剧种气质） |
| X2 | 主线与技术结构 | `sw-chinese-opera-banqiang`（主线的集中、技术结构与排场） | 主线一句（纵的集中）；场次表（每场事件＋唱念做打配比＋冷热）；重场戏两三场；过场清单 | 排场交替律过；上板段集中在重场戏；过场不给主角加唱 |
| X3 | 行当与人物 | `sw-chinese-opera-banqiang`（行当决定写法、为演员写戏）＋ `sw-character-conflict` | 人物表带行当；主演的技艺清单与剧目缺口；行当禁忌核对 | 没有净角唱反二黄之类的禁忌违反；一赶多（若有）成立 |
| X4 | 唱段设计 | `sw-chinese-opera-banqiang`（唱词、对唱、编剧要标什么） | 唱段表（场次／人物／板式意向／句数／辙口）；每段的重点句先写；垛句位置；辙口全剧布局 | 上下句分句法过；下句押、上句可不押；奇数句只在扫头；对唱段有递减或交锋结构 |
| X5 | 初稿 | `sw-chinese-opera-banqiang`（宾白与唱白衔接、程式的用法）＋ `sw-dialogue`（宾白）＋ `sw-chinese-opera-banqiang-cases`（对照语料） | 剧本（唱／白／科介；若选京剧式则另标板式与锣鼓；越剧式或不标板式一路见 `sw-chinese-opera-banqiang` 第九节） | 每段唱前一行是称呼语；程式取舍清单写明；现代戏不留自报家门定场诗 |
| X6 | 审腔与修改 | `sw-chinese-opera-banqiang`（与演员琴师的接口、诊断清单） | 修改记录；板式标注是意向书，改词必改腔的清单 | 诊断清单跑完；分歧处注明选了哪一方 |

**曲牌体 Q0–Q6**

| # | 阶段 | 调用的 skill | 交付物 | 建议通过标准 |
|---|---|---|---|---|
| Q0 | 启动 | 本 skill | 杂剧还是传奇还是昆曲折子；场上还是案头（剧曲 vs 清曲）；新填还是改老本 | 两个开关都答了 |
| Q0.5 | 真人／史料题材（有则做） | `sw-chinese-opera-qupai`（改编与改本）＋ `sw-chinese-opera-banqiang` 第十一节改编四问 | 同 X0.5：史载／传说／自编对照表 | 同 X0.5 |
| Q1 | 立主脑与体制 | `sw-chinese-opera-qupai`（开篇立场、杂剧支／传奇支）＋ `sw-premise-theme` | 一人一事一句；折数或出数；主唱权归谁（杂剧）或副末开场怎么写（传奇） | 主唱权＝主角权成立；题目正名／副末开场有了 |
| Q2 | 宫调与排场 | `sw-chinese-opera-qupai`（宫调与套数、排场与剧情） | 每折／出的宫调与套式意向；排场表（冷热、过场短剧、南北曲用途） | 一折一宫调一韵（杂剧）；排场交替律过；南北曲分工说得出理由 |
| Q3 | 人物与行当 | `sw-chinese-opera-qupai`（四色四气）＋ `sw-character-conflict` | 人物表带脚色与色气归类 | 净丑有结构功能不只是笑料 |
| Q4 | 填词 | `sw-chinese-opera-qupai`（填词法）＋ `reference.md` 曲牌表 | 曲牌表（折／曲牌／务头句／韵）；每支先定务头再填 | 格律按谱（或注明走现代新编"零金碎玉"路线）；四十禁格律半过 |
| Q5 | 初稿 | `sw-chinese-opera-qupai`（宾白→曲接口、帮腔）＋ `sw-dialogue` ＋ `sw-chinese-opera-qupai-cases` | 剧本（曲／白／科介／帮腔） | 每支曲前一句白引出首句；名作违律表对过 |
| Q6 | 修改 | `sw-chinese-opera-qupai`（改编与改本、诊断清单） | 修改记录 | 诊断清单跑完；改本三种结果对照过（合律毁文是常见失败） |

**本节两表未点名的影视格式类 skill（`sw-format-adaptation` 等）不进入戏曲项目；要用先查对应戏曲 skill 的媒介边界表。**

**一次性交付**（写一段唱词、改一折）不建 bible，直接进对应 skill 的那一节。

---

## 四、每阶段的最小动作

不必把对应 skill 全文读一遍。每阶段先读该 skill 的"工作流程"和"诊断清单"两节，需要具体方法再读对应章节，需要范例再读 reference.md。

**阶段 1**：按 `sw-premise-theme` 第十二节 12 步走；产物填入 bible 的"前提与主题"节。若用户给的是歌、画、新闻等外部素材，先只取叙事骨架与意象，编号、名字、句子另编。

**阶段 2**：先定结尾；再按目标页数换算 BS2 页码（110 页表按比例缩放：主题 5%、触发 11%、二幕 23%、中点 50%、失去一切 68%、三幕 77%）；填页码表；写"中点是什么假象、失去一切是什么反面"。

**阶段 3**：每个主要人物填三维表一行；单独写"对立统一的绑定物是什么、只有谁的哪个特性消亡才能打破"；给对手至少一把刀；列主角的镣铐。

**阶段 4**：步骤大纲每场一行：`场次 | 内外·地点·日夜 | 一句话 | 押上的价值 开→结 | 结构位置`；然后过一遍"删掉会怎样"，价值不变的场删。

**阶段 5**：每天写完更新 bible 的"进度"一行（页数、写到第几场）；发现设计缺陷不在稿子里硬改，回 bible 改设计再改稿。

**阶段 6**：把五份诊断清单的问题逐条列成修改目标，一条一条销；先第二幕，再对白，最后格式。

**阶段 7**：从 bible 的"前提与主题"节直接生成 logline 与一页梗概；跑 PROBLEM 七要素。

---

## 五、通过标准怎么用

- 标准是**建议门槛**，不是硬阻断。用户要跳步就跳，但在 bible 的"当前阶段"旁标"（跳过阶段 3 人物表）"，并在进入阶段 5 前提醒一次。
- 对 AI 自己：每阶段结束用该 skill 的诊断清单自问，把没过的项写进 bible 而不是默默放过。
- 通过标准里凡是能量化的都量化（页数、卡片数、人物数、问号数）。
- **甲方的格式要求优先于任何 skill 的体例。** 用户或委托方给了页数、字数、栏目、模板、集数，就按他们的；skill 里的体例（分集大纲的三件、步骤大纲的行格式、文档的字段表）是**默认值**，只用来填对方没规定的空白。冲突时压缩体例、不要超格式，并把展开版另存一份自己用。**不要为了交齐 skill 要求的字段而交出一份不合甲方规格的文件。**

---

## 六、Subagent 与并行

- **不要**按阶段拆给不同 agent：前提、结构、人物是一体的，拆开会互相矛盾且丢失创作上下文。主线始终在一个会话里。
- **可以并行**的两类工作：
  1. 阶段 6 的多角度审读：结构诊断、人物诊断、对白诊断、场景诊断各派一个只读 agent 跑清单，回收成一份修改目标表。
  2. 大块检索：需要某本 reference.md 里的具体范例或某部作品的逐幕表时，派 agent 去读并只带回结论，避免主线上下文膨胀。
- 并行 agent 只读 bible 和稿子，不改 bible；改动由主线汇总后写入。

---

## 六之二、输出语言与术语

skill 正文只有中文一份，**不为每种语言维护平行译本**——见 README 的"多语言支持"一节。语言这一层按下面三条处理，本 skill 对全部 sw-* skill 生效。

1. **输出语言＝提问语言。** 用户用英语、日语、韩语、法语提问，就用那种语言交付；正文是中文不影响输出语言。用户显式指定语言时以指定为准（"用英文写这版大纲"）。
2. **术语回锚到原词，不自创译名。** 这一行的术语大多原本就是英文（logline、act out、beat sheet、showrunner），中文书里的"计程绳""出幕""剧目管理人"是译文。输出非中文时，凡 [terms.md](terms.md) 收录的概念一律使用它的**英文原词**；表里没有的，先判断原词属于哪个语言再锚，不要静默发明。
3. **无对应物的词保留原词＋一句释义。** 国产特有词（戏眼、扣子、分集梗概、备案公示）与日式术语（柱、ト書き、決定稿）在任何语言下都不硬译，写成 `戏眼 (xìyǎn — the one-line core attraction of an episode)` 这样的形式。

**剧本正文本身另算**：剧本要用作品的语言写，格式按 `sw-format-adaptation` 选体例（英文稿走 spec／Fountain，中文稿走场号制，日文稿走柱・ト書き）。用户用英语讨论一个中文剧本是常态——**讨论用英语，剧本正文仍是中文**，不要因为对话语言换掉作品语言。

---

## 六之三、编剧与导演的分工

交稿之后这一段的规矩，来源：罗怀臻《当代戏曲编导的觉悟》p0120–0125。

1. 编剧落笔时形式已诞生，但那是平面的；使它立体的是导演（p0120）。
2. 导演的样式与剧本方向吻合就配合；完全背道而驰、只为试验导演本人的形式，"及早谢绝"（p0120）。
3. 接受了的修改意见**自己动手改**，不让人代笔（p0121）；不做的后果是陈西汀《红楼梦》署名权诉讼（p0121–0122）。
4. 二度创作的底线是**准确**：可发现与呈现剧本精神，不可大劈大砍另作解读（p0121）。
5. 合作是**乘法**关系，不是减法，也不是单纯的加法（p0122）。
6. 编剧不兼导演的理由：自己排只能照文本画瓢，排除了再创造一次的可能（p0123）。
7. 选导演看四条：准确解读、能提建设性意见、敬业、对排练场有控制力；"张狂"无碍，一味迁就、没有决断才是灾难（p0122–0123）。

**可改／不可改**（《西施归越》四个版本，p0123–0124）：

| 不可改 | 可改 |
|---|---|
| 主题、构架 | 韵脚 |
| 主要人物关系 | 场次增减 |
| 基本戏剧情节 | 开场与结尾的处理、整体风格（虚／实） |

一句判据：**文学精神坚定不移。** 本节对戏曲 X／Q 表与影视阶段表同样生效。

---

## 七、反模式

- 直接从点子跳到写剧本（"冒牌的处理台本"）。
- 每次会话把 bible 从头重写，或者忽略"已定决策"重新讨论前提。
- 把推导过程全塞进 bible，导致下次读不完。
- 一次问用户十个问题；应先按推断填上，标"待确认"，让用户改。
- 让"通过标准"变成拒绝继续的理由。
- 用 subagent 分阶段写。
- 因为 skill 正文是中文就用中文回答英语／日语／韩语／法语的提问；或者反过来，因为对话语言是英语就把中文剧本正文也改成英文。
- 给 terms.md 里已有原词的概念现编一个译名。

---

## 八、自检

1. 当前目录有没有 `story-bible.md`？读了"当前阶段/已定决策/决策日志"了吗？
2. 这次会话推进了至少一个阶段的交付物并写回了吗？
3. bible 还能一次读完吗？
4. 有没有改动已定决策而没记日志？
5. 结束时写了"下一步："吗？
6. 输出语言和提问语言一致吗？术语锚回 terms.md 的原词了吗？剧本正文的语言没有被对话语言带偏吧？
