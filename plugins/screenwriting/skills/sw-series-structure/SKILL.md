---
name: sw-series-structure
description: Episode and season structure for TV series (剧集单集与季的结构) — teasers and cold opens, broadcast four/five/six-act grids with page anchors, three tests for finding the invisible acts in pay-cable and streaming scripts, act-out and cliffhanger taxonomies, Oberg's four information tools (mystery / surprise / dramatic irony / suspense), A/B/C/runner weaving and scene-count ratios, the Calvisi pilot beat sheet, five-part scene structure, and season shape (tentpoles, bottle and container episodes, two-parters, finales). Merged from Calvisi, Pamela Douglas, Oberg, Landau, Goldberg & Rabkin, Kam Miller, Rabkin and Blum, plus act lengths measured from the published West Wing, Succession, Sopranos, Downton Abbey and Fleabag scripts. Use when breaking an episode into acts, deciding how many acts a script needs, placing act outs and cliffhangers, designing a teaser, weaving A/B/C stories and runners, beating out a one-hour pilot, auditing an episode that has no shape, reverse-engineering an existing show's structure, or planning a season's episode order (分幕、出幕、悬念结局、季弧、瓶子集).
---

# 剧集结构（Series Structure：单集与季）

> **输出语言＝提问语言**；术语一律锚回原词，见 [sw-workflow/terms.md](../sw-workflow/terms.md)，不自创译名。

分工：**Calvisi 给 pilot 的逐节拍页码区间，Douglas 给四幕格子与场数，Oberg 给"格式 vs 结构"的地基与信息管理四工具，Landau 给幕数抽样与 cliffhanger 类型学，Goldberg & Rabkin 给经典广播四幕的功能表，Miller 给 landmark 与场结构五件套，Rabkin 给流媒体时代的提速规则，Blum 给各节目类型的幕数页数表，五部剧本集（West Wing / Succession / Sopranos / Downton / Fleabag）给可验证的实测数字。**

表格、完整节拍表与逐集数据见同目录 [reference.md](reference.md)。

本 pack 用的英文术语、严敏中译本的官方译名与一句话定义的四列对照表见 [reference.md](reference.md) 第十二节（含 log line＝"计程绳"、staff writer＝"试用编剧"两处怪译，以及"晚进早出"与 enter late, leave early 同名反义的警告）。

**不在本 skill 里**：series engine / franchise / bible / pilot 类型与卖法 → `sw-series-engine-bible`；半小时喜剧的笑点与格式 → `sw-sitcom-comedy`；编剧室流程与文档链 → `sw-writers-room`；国产剧集数体量与分集体系 → `sw-chinese-series-practice`；逐集结构表全文 → `sw-series-case-studies` / `succession-series-writing`。媒介无关的工艺不重写：**场景价值转折见 `sw-scene-craft`，对白见 `sw-dialogue`，三幕范式与情节点见 `sw-story-structure`。**
## 按任务读哪几节（不要通读）

本节 38 KB，逐节读完通常是浪费。按手上的任务只读对应几节：

| 任务 | 读 | 跳过 |
|---|---|---|
| 破一集的结构 / 排幕 | 二（容器与幕）、三（出幕与信息管理）、四（A/B/C 编织） | 五、七、八 |
| 写或改 pilot | 五（pilot 节拍表）、二 | 七（季形）、六 |
| 诊断一份已有的大纲或剧本 | **九（诊断清单）**，再按失败项回查对应章节 | 其余全部 |
| 排一整季 | 七（季形）、四 | 五、六 |
| 写半小时喜剧 | 仅三、六的媒介无关部分 → 转 `sw-sitcom-comedy` | 二、五的页码（一小时专用） |
| 写国产 45 分钟剧 | 三、四、六 → 时段与场面数转 `sw-chinese-series-practice` | 二、五的页码 |

reference.md 是查表用的，只在 SKILL.md 明确指向某一节时打开。

---


---

## 一、剧集结构与电影结构的根本差异

- **更紧的形式，所以更难不是更容易。** Douglas 中译第 3 章（p0088）："电视剧本要求把所有同样的要素浓缩在更紧凑的形式中。"电影一场可 5–7 页，电视**一场目标 2 页**——"如果你一开始用 4 页纸写一次会面戏，那等于挂红旗"。
- **剧本模拟剪辑后的成片，不是拍摄素材**，要让读者得到"观众看剧"的体验（Calvisi）。
- **编剧亲手给幕贴标签，没地方可藏**（Calvisi 列为电视剧本的第一格式差异）："There is no place to hide."不分页的 pilot 看起来像在 cheat，与调小页边距同属立刻暴露业余的手法。
- **场景编号不是戏剧意义的场。** Douglas：一个建筑物外景"就不是完全戏剧意义上的一场戏"；**一个 dramatic beat 可含多个 slug line，它只与故事的发展同步，与景不同步**。Oberg 的计数规则：**主角或目标变 → 新 dramatic scene；地点或时间变 → 新 logistical scene**；结构文档按 dramatic scene 计数。
- **成片长度与剧本长度是两个数字**（Calvisi）：广播台正片去掉广告只有 45–48 分钟，但 pilot 剧本必须至少 50 页——宁长勿短，"but try not to exceed 60 pages"。
- **剧集的"幕"不是戏剧原理，是广告位。** Oberg 第 1 章把任何规定固定份数与页数的切分法叫 **story format（logistical，物流式）**，源头是戏剧换蜡烛、电影换胶片卷、电视插广告，"But all this is gone."；"香肠串"比喻：物流法只决定"几根香肠、多长"。**本 skill 最重要的判断力：幕数是交付格式，三幕（before / during / after 一个 main dramatic action 或 evolution）是设计工具。**
- **但结构同时是制作排程。** Miller 第 9 章：制作部门拿到剧本第一件事是统计 days in and out；**只写 DAY 或 NIGHT**——写 dawn 制作就会精确安排那天日出时段开拍。
- **结构是继承的。** 剧集沿用 pilot 的幕结构与页码区间（Breaking Bad pilot 与同剧 #308 的幕页对照见 [reference.md](reference.md) 第一节）——**写 pilot 等于给全剧定结构模子。**

---

## 二、单集容器：teaser、幕数与页码锚点

### 2.1 广播四幕的功能链（Goldberg & Rabkin，2003）

**Act One** 介绍角色、冲突、赌注 → **Act Two 幕尾必须把故事推向"startlingly new and unexpected direction"**（Law & Order：警察逮捕了一个意想不到的人）→ **Act Three 幕尾主角以为控住了却发现错了**，"They are all going to die. There is no hope." → **Act Four** 想出办法、达成目标。

> **时效 flag（2003）**：该书称"一小时剧一律四幕"，**已过时**——2006 年起广播网普遍五幕、ABC 新剧一律六幕（Douglas 中译 p0091），流媒体取消幕标记。但**四幕功能链至今有效**：Miller 与 Landau（2021）都仍要求先按四幕 break 再切。

页码锚点（Douglas 中译 p0090–0091，含 teaser 的四幕初稿）的四个页数与"每 13 至 15 分钟一次广告"的成因见 [reference.md](reference.md) 第二节。

> ⚠️ **这些页码只在 48–63 页的美式一小时集内有效，不能按比例换算到国产 45 分钟集。** 两套切法的依据不同：美式按**页数与广告位**切幕，国产按**时段与片断**切（正片约 41.5 分钟，开场 3 分钟＋每 15 分钟一个小扣子＋集尾大关子）。写国产剧时本节只取媒介无关的部分（出幕类型学、一幕尾是"主角被推进没有退路"、Act Two break 改变故事性质、场结构五件套、赌注检验、信息管理四工具），时段与场面数改用 `sw-chinese-series-practice`。
> **半小时剧同样不适用**（30 分钟本约 30 页，幕数与场数都是另一套）：幕长、页码与场数见 `sw-sitcom-comedy` 第四节，**不要把本节的一小时数字缩放过去**。本节下面的诊断 4、5 两条只对美式一小时集有效。

### 2.2 场数：每幕 5–7 场，一集约 28 场

Douglas 的算术、四幕 28 场／五六幕 20 场的总量、Oberg 的 A/B/C 场数配比与 Chase 的"每集约 35 拍"见 [reference.md](reference.md) 第二节。

### 2.3 四幕 → 五幕 / 六幕的改法

Douglas、Peter Blake（House）、Miller 三套改法，以及"Act Six 实际是下一集的 teaser"的六幕尾部设计见 [reference.md](reference.md) 第二节。

### 2.4 Teaser / cold open

- **长度**：Douglas、Landau、Oberg 三家的 teaser 长度数字见 [reference.md](reference.md) 第三节。
- **十种类型**（Douglas 七范式＋Landau 三型）的名目与实例见 [reference.md](reference.md) 第三节。
- **给新手的硬规则**（Douglas 中译 p0098）："坚持以故事而非信息来开场……许多学生……误以为用重大的主题思想或抽象的哲理来开场会给人留下深刻印象。**他们实际上是看到戏剧弧线推进的挑战而畏缩。最佳的引子倾向于最佳的戏剧化。**"
- **teaser flashback 的禁忌**（Oberg）：可以从 dramatic action 的中段甚至末段起叙（The Walking Dead、Breaking Bad），**但绝不能在 teaser 里回答 dramatic question**；取材自结尾就选 climax **之前或之中**（Run All Night），不要之后（John Wick）。
- **teaser 不是必需品**：Landau 2e 与 Oberg 的论据、无 teaser 与"短第一幕充当 teaser"的剧目清单见 [reference.md](reference.md) 第三节。
- **cold open ≠ teaser**（Miller）：Brooklyn Nine-Nine pilot 的 cold open 不影响主线、只启动本集主题，所以该集 point of attack 落在第一幕。

### 2.5 隐形幕：三重判据

付费有线／流媒体剧本常不标幕也不分页（Calvisi 点名 **True Detective、House of Cards、Mad Men 都不标幕，但 Mad Men 在常规幕断处放 FADE OUT**），然而"a pilot script is almost always going to be structured in the conventional 4-6 act template"。从 Succession 剧本逐幕实测出来的三重判据：

三重判据：① **剧情日／时间块标记**——**换日就是换幕**；② **地点与交通工具的切换**；③ **核心问题转向的那一刻**。判定标准：**每幕末尾必须有一次信息或权力的转移**，不必有悬念钩。逐条的 Succession 实测（S3E9、S4E01、S4E05、S4E08、S4E10）见 [reference.md](reference.md) 第四节。

配套规律（Succession S4 十集）：**8/10 集把全集压进一个带固定程序的容器**，**程序节点替代 act break**——**即流媒体编剧仍然在写幕，只是把幕伪装成日程**。逐集容器与场景数见 [reference.md](reference.md) 第四节。

### 2.6 要不要在页面上写 ACT——必须并列保留的分歧

- **五家立场**（Landau 2e 的"story over format"、要看到标注的 showrunner 的反面、Miller 的市场判断、Mazzara 的 TWD 改幕、Alex Pina 的 milestone moments）见 [reference.md](reference.md) 第二节。
- **判据**：为广播网／基础有线／AVOD 写 → 标幕（AVOD 与传统广播网一样不允许跳广告）；为 premium／SVOD 写 → 按四幕 break、交付前删标注或改用剧情日标记；拿不定就照 Miller 的判据走，看内容能上哪个台。

### 2.7 页数与集长

Calvisi / Landau / Miller / Blum 的 pilot 与单集页数区间、Oberg 的各平台集长、Landau 2e 的趋势判断，以及各书年份的时效 flag 见 [reference.md](reference.md) 第二节。

---

## 三、act out 与 cliffhanger 类型学，信息管理四工具

### 3.1 定义、反面教材与判准

- **Calvisi**：每一幕（理想每一场）都要让人想知道接下来发生什么；幕尾常被称为 **"Act-Out"**。
- **Landau 2e 第 12 章**："A cliffhanger is a plot device that leaves one or more characters facing either a dangerous situation or a shocking revelation."
- **Oberg**：cliffhanger"simply an unresolved conflict"——**位置不止集末季末，还包括"离开一条 strand 之前"**。
- **反面教材 schmuck bait**（Landau 2e）：心电图拉平、护士喊 "Code blue!"（插广告）→"I'm getting a pulse"。
- **今天的规则（Landau 2e 最核心的一条）**："**forcing a cliffhanger at the end of each act break is deadly**… Instead, act breaks can land on a **turning point that emerges from characters, not merely from plot**."
- **判准（1e Tip 19 与 2e 第 12 章两处重复）**：cliffhanger 必须 **"grow out of character jeopardy, risk, or fear"**；坏 cliffhanger 只是为震惊值而来的情节点；"even a 'surprise' cliffhanger needs to be (subtly) set up so that the audience feels they **should have seen it coming—but didn't**."
- **位置与时限**：一小时剧把高潮型 cliffhanger 留到集末，多机 sitcom 通常在集中点（结尾要按 reset 键回到常态）；可以延后揭示全部真相，**但务必在本季结束前揭示**（原话见 [reference.md](reference.md) 第五节）。

### 3.2 十种 cliffhanger（Landau）

2e 七型（character in peril｜ticking bomb｜love is in the balance｜surprise twist / aha moment｜death of a character｜discovery of a secret｜life events）与 1e 另列三型（lack of closure｜mini-cliffhangers｜comedy cliffhangers）的逐条定义与实例，以及两个最可迁移的做法（"用一个单词完成反转"、"不在笑点上出幕"）见 [reference.md](reference.md) 第五节。

### 3.3 act out 的八种形式与三条通用律

West Wing 六集实测的八型：**悬念提问／反转台词／情感揭示／无对白动作／道具定格／重复台词语义反转／被剪断的 setup／伏笔兑现的手势**。配套规则：**每幕出幕交给不同的线**；**至少一幕用无对白动作或道具出幕，不要四幕全用台词**——无台词的出幕必须先教语法。八型实例、Two Cathedrals 的教法与 Downton 的四型见 [reference.md](reference.md) 第五节。

**出幕可以完全是信息事件。** Goldberg & Rabkin 附录两集（Martial Law 与 seaQuest 2032 "Depths of Deceit"）共有三条通用律：**① 一幕结尾不是最大危机，而是"主角被推进没有退路的处境"；② Act Two break 一定改变故事的性质而不只是提高危险；③ Act Three 结尾必须让主角的胜利变成新的失败。**两集的逐幕对照见 [reference.md](reference.md) 第五节。

### 3.4 悬念的成分与赌注检验

- **Douglas 的节奏公式**（中译 p0139，英文版 Anticipation — Expectation — Surprise）：**预感 → 期望 → 惊诉**，"然后开始一个新的悬念段落"；NYPD Blue "Hearts and Souls" 六拍冷开场的逐拍示范见 [reference.md](reference.md) 第六节。
- **Landau 2e**：Suspense ＝ **Anticipation + Surprise**，最好是 unexpected, inevitable but not predictable。
- **赌注检验法（最实用的一条）**：问自己"面对危机什么都不做"对这个人物是否是可行选项——"If your character is not compelled to solve a problem by the potential of losing something of value, then your stakes are insufficient."
- **极化模型**：在每一集、每一场、每一幕找出正负（+/−）电荷；与旧做法的区别是**act break 的方向可正可负**——"some acts will end on a win"。

### 3.5 信息管理四工具（Oberg 第 1–2 章）

三维模型：人物是点；加 main dramatic action（conscious want）→ 线；加 main dramatic evolution（unconscious need）→ 面；**加 managing information → 立体**。Managing conflict 回答"Who wants or needs what and why?"，managing information 回答"**Who knows what and when?**"

四工具（**dramatic irony** / **surprise** / **mystery** / **suspense**）的定义与用法表见 [reference.md](reference.md) 第六节。

四条红线（① 不要让主角长期比观众知道得更多；② 做 cliffhanger 优先用"信息炸弹"；③ closed mystery vs open mystery；④ "you can have some mystery over the nature of the antagonist, but not over the reality of the danger it represents."）的逐条展开见 [reference.md](reference.md) 第六节。

Landau 2e 的缝合句："it's not only Who Does What When, but also **Who Knows What When**."

### 3.6 提速：act out 不等于每七八分钟一次假反转

Rabkin 的 24 与 Scandal 对照、"把第四幕末最酷的事挪到 teaser 末尾"的原话、L+3 收视逻辑与"流媒体可以省掉三样"见 [reference.md](reference.md) 第五节。

---

## 四、A/B/C/runner 的编织与配比

### 4.1 定义与排序

四家的定义与排序（Douglas 的"三个独立的故事"与 runner／Calvisi 的"字母按戏份多少排"与 story engine 三要素／Landau 的 A＝franchise、B＝私人故事、runners＝C/D／Oberg 的"每集至少 A+B，最多 4–5 条、只有 A、B 需要设计成三幕"）见 [reference.md](reference.md) 第七节。

### 4.2 编织的硬规则

1. **Franchise（A 线）贯穿每一幕；B 线与 runner 按需插入**，每幕一般 **4–5 个 beat，理想情况下收在 A 线、落在主角的困境上**（Landau）。
2. **极少在 C 线收幕**——"If the story is worthy of an act break, then it's not your C story – it's probably more your A or B story."（Landau 1e/2e 原话一致；Oberg 同条。）
3. **但幕末悬念不一定在 A 线**（Douglas 中译 p0095："它可能是 B 故事的转折点"）。West Wing pilot 实测：teaser 与第三幕的出幕都由 B 线 Sam–Laurie 承担。
4. **不必棋盘式交替，跟随"兴趣线"（line of interest）。** Douglas 用 NYPD Blue "Simone Says" 第 8 场（楼下老妇被流弹打死）示范："它从'棋盘'上剧情发展顺序来看并不需要，但对跟随观众的兴趣线来说至关重要。"
5. **插入另一条线可以制造"省略法"（ellipsis）**——时间已逝的印象，让同一批人物"实际上无法那么快经历之"地重新出现。
6. **没有一场戏是专为呈示部（exposition）撰写的。"如果你需要传递事实的话，那么就把事实置于一个充满情感的语境中。"**（Douglas 中译 p0119）
7. **规划时把各线分开，到写 teleplay 时才编织**（Douglas 给新手的顺序，与她自己分析"Hearts and Souls"四层同时性调度时的顺序相反）。
8. **线的交叉在有主题链接时最有效**（Landau 1e），家庭是最强的链接；**runner 可以长大成主线**；**serial 不必每集写到每个人**；三条的逐例（Terriers 的三级升格、Game of Thrones 的轮换、Mad Men S6E11 Peggy 的老鼠与 elliptical storytelling）见 [reference.md](reference.md) 第七节。

### 4.3 procedural 的 A/B 双轨（Ann Donahue，CSI: Miami，Douglas 第 3 章）

Ann Donahue 的 A＝调查／B＝情感双轨、"warm body by the end of Act One, within the first 17 pages"，以及 The Good Wife / CSI / House 三种编剧室顺序见 [reference.md](reference.md) 第七节。

### 4.4 两种替代破故事法（必须与 A/B/C 并列）

- **Wendy West（Dexter）**：播出无幕，剧集实际退回三幕；"**We break the beats by character and then do a weave.**"白板上每个角色有开头中间结尾，**不按幕 break，按角色 break**，先 break 主角线——"The reversals tend to come where you'd expect — page 40 to 45 out of a 55-page script."
- **Glen Mazzara（The Walking Dead）**：**明确拒绝 A/B/C**——把 Rick 当 A、另一人当 B 再交织，"That doesn't always equal a theme. It just pushes the ball further on each one."；改问 **"What is this episode about?"**（女孩走出谷仓那集、畜栏被尸群冲破那集，每个人物在那个更大的故事里有自己的位置）。**代价他自己说明了：次要人物可能永远只是次要人物。**
- **Oberg 的折中**：多线不等于 theme-led——若各线角色**共享同一外部问题与同一目标**，它是 plot-led 的 co-protagonist 结构（Stranger Things 的 A1 Joyce / A2 Hopper / A3 男孩们 / A4 Jonathan 其实是同一条 A 线）。
- **Downton 的极端值（Fellowes）**：S2 同时跑 8–12 条线的群戏规格与"每集至少一条与本集主危机无关的线"见 [reference.md](reference.md) 第七节。

### 4.5 用格子分析与规划（Douglas 的 grid，中译作"框格"）

基本四幕格子、拆片三步、倒序制造（reverse-engineer）、log line 的要求与 Oberg 的三步替代法（Mapping → Sequencing → Weaving the Strands）见 [reference.md](reference.md) 第七节。

---

## 五、pilot 节拍表

Calvisi 的 Benchmark 页数区间、完整节拍链、AOP 与 DOW 的校验数字、四个"电视化"专属节拍、"This is form, not formula." 的边界、Miller 的六 landmark 模型与 Landau 的 pilot 结尾三策略见 [reference.md](reference.md) 第一节。

**pilot 最关键的取舍（Calvisi）**：决定"要介绍多少人物与多少条线"——塞太多 → too dense；聚焦太少 → 读者感觉不到一个能撑 100 集的大故事。**结尾要好，但不能把所有东西都兑付掉**，否则会"feel too complete or 'closed-ended'—like a feature"；必须"leave us hanging to some degree and wanting more"。

> premise pilot / typical-episode pilot / hybrid 的选择、pilot 的三种收法、bible 与 pitch 文档 → `sw-series-engine-bible`。

---

## 六、场结构五件套与场级检查表

**五件套**（Miller 第 9 章，改编自 Lance Gentile，ER / Third Watch 编剧兼急诊医生）：**hero's want / obstacle / escalations / decision / resolution**。

- **want 与 obstacle 在开场前就已确定**；**第一个 escalation 开场**；**decision ＝ 场的高潮**；**resolution ＝ decision 的结果**，并把人物带进下一场。
- **数量**：至少三个 escalation，"but it's better to have more. More escalations give the scene time to build and breathe."**优先用动作**——"If all of your escalations are oral… **Your TV show turns into a radio show.**"（Hannibal 与 HTGAWM 两场的 escalation 实测见 [reference.md](reference.md) 第八节。）
- **一场只有一个 hero，而且 hero 可以换人**（男厕场是 Will，下一场 Jack–Alana 场是 Jack）。**一人场**：对立的 want 来自世界或环境——OITNB "The Chickening" 里 Piper 的 want 是享受周日早晨仪式，**obstacle 是监狱**。
- **moment / image ≠ scene**："If there isn't a strong character want, it's not a scene. **A moment without a character want is simply a moment, an image.**"而 moment 不能重复已知情绪，必须展示进化中的情绪。
- **收场责任**："**You the writer need to decide how to end the scene.** And you the writer need to decide what emotions your characters are feeling."
- **exposition through conflict**：HTGAWM 树林场里每个人的反对都合理，在争论中交代了难度与 stakes。

**剧集场级的五条附加规格**（2 页的长度目标、不必描写外貌、"ANGLE" 是文学手段、同场多层调度 layering、不要 micromanage 演员）与**舞台指示承担结构任务**的两条（Succession 剧本集）见 [reference.md](reference.md) 第八节。

---

## 七、季形

**7.1 物流层与戏剧层。** Stranger Things S1 的物流三幕 3-3-2 与戏剧三幕分钟数、serial 的季层节奏纪律、集数检查（"Are you starting the story too early?"、减 1 集常能提速）见 [reference.md](reference.md) 第九节。

**7.2 Tentpole。** Landau 1e Tip 13 把 teaser / act break / tag 合称 **tentpoles（帐篷柱）**；其功能链与 tag 的作用见 [reference.md](reference.md) 第九节。

**7.3 Bottle episode：成因是预算。** West Wing "17 People" 的幕长实测、三条规则与"把四个限制逆用成三个选择"见 [reference.md](reference.md) 第九节。

**瓶子集不等于单线。** Sopranos "Pine Barrens" 的 B/C/D 并行、平行剪辑对位与信息衰减链见 [reference.md](reference.md) 第九节。

**7.4 容器集与仪式集（Succession 的两套模板）。** 压力舱集的"通讯受限"设定、仪式集的免费节拍表与"缺席的主角"见 [reference.md](reference.md) 第九节。

**7.5 two-parter。** West Wing "In the Shadow of Two Gunmen" I/II 的幕页实测与上下半分工规则见 [reference.md](reference.md) 第九节。

**7.6 季终与剧终。**
- Downton 的 streamers 与"最后一幕只做 pay-off"、Succession S1 的 140 美元/股对称掉头与 S4 的反向做法、Sopranos 的反高潮式收尾、Sorkin 的意象清单与 Two Cathedrals 幕长实测见 [reference.md](reference.md) 第九节。
- **Landau 2e**："Give yourself and your protagonist(s) a deadline."——它同时能帮你写完 pilot。

**7.7 六集季形（Fleabag 模板）。** 逐集骨架（铺开／欲望／露底／瓶子集／伪胜利／封闭社交场合）、单集形状与两条可迁移装置见 [reference.md](reference.md) 第九节。

**7.8 多线季形（Downton S2）。** 逐集幕数、线的长度分层、"留人机制"与"杀角色前先让观众猜另一个人"见 [reference.md](reference.md) 第九节。

**7.9 替代结构（Landau 2e）。** Linear / Flashback / bookend / zigzag / hopscotch / 三条时间线 / Rashomon / Time Loop / 倒着讲的完整清单、选型五问，以及多时间线作为调性调节阀（Alex Pina）与 Mazzara 的反方见 [reference.md](reference.md) 第十节。

---

## 八、分歧保留表：什么情况用哪个

| 争点 | 立场 A | 立场 B | 判据 |
|---|---|---|---|
| **幕是结构还是格式** | Douglas / Calvisi / Goldberg & Rabkin：四/五/六幕是结构骨架，页码锚点可检验 | Oberg：幕是 logistical、"只是香肠的尺寸"；设计用 dramatic 三幕，交付时再切 | 为有广告的平台交付、或要证明结构能力 → A；诊断"中段松垮""结构公式化"→ B（按 subgoal 切 sequence）。可叠用：A 当工作单元，B 当设计工具 |
| **页面上写不写 ACT** | Landau：按 act break break story，定稿删标注（story over format） | 同书的反面：很多 showrunner 要看到标注作为结构掌握的证据；Miller：内容能上广播网就必须写 | 看内容的目标市场（Miller 判据）：投流媒体剧组可删，投广播网/基础有线必留 |
| **midpoint 有没有意义** | Calvisi：Midpoint 是二幕出幕，必须扭转 A 线并带 ticking clock | Oberg："the midpoint can be safely ignored if you find it confusing"；替代品是 **mid-act climax** | A 线目标能覆盖整个 Act 2 → midpoint；目标中途更换（heist 片、Occupied pilot）→ mid-act climax |
| **中点是假胜利还是必须成功** | Snyder 派／Calvisi：胜利的假象或失败的假象二选一 | Miller：必须是 hero succeeds—almost——"**It's not 'the hero fails'!**" | 写 tragedy／反英雄集时用 Miller 自己的变体：**squeeze 翻正、climax 翻负** |
| **"最坏情况"的位置** | Douglas 四分之三处；Calvisi 的 DOW + All is Lost 在 4/5 处 | Oberg："a series will be successful **despite** these formulaic crutches, not because of them." | 第一次写剧集 → 用锚点自检；已有扎实的 sequence 设计 → 不必摆 |
| **A/B/C 线 vs 其他破故事法** | Douglas / Calvisi / Landau：A/B/C(/D)＋runner，字母按戏份排序，act break 落 A 或 B | Mazzara：拒绝 A/B/C，改问"What is this episode about?"；Wendy West：不按幕 break，按角色 break 再 weave | 群像剧且每集想是"一个完整故事"→ Mazzara；单主角连续剧且反转集中在主角线 → West；procedural 与广播剧 → A/B/C。代价由 Mazzara 自己点出：次要人物可能永远是次要人物 |
| **每幕必须 cliffhanger 吗** | Calvisi：每幕（理想每场）都要让人想翻页；Kelley（Revenge，六幕）："five or six cliffhangers an episode" | Landau 2e："forcing a cliffhanger at the end of each act break is deadly"；Sorkin 实测：一、二幕出幕都很轻，四幕不是 cliffhanger 而是"复位" | 六幕广播剧（五个广告位要填）→ Kelley 的配额；无广告或强作者剧 → Landau/Sorkin。**判准不变**：必须长自人物的 jeopardy/risk/fear |
| **主题统一多线 vs 主题是涌现物** | Landau（Tip 14 / ch11）：主题是把分歧故事线黏在一起的胶水（ER "Stuck on You" 四条线全是"被彼此粘住"） | Johannessen（Homeland/Dexter/24）：24 的房间口号"**We don't do themes.**"；"If you want something that looks and feels real, **throw out the writerly devices**"；替代品是 **operational question**。Mazzara 同侧：先专注故事，退一步才看见主题 | 强写实／惊悚优先 → B（改用"本集的操作性问题"）；群像多线、要把几条无关的线缝起来 → A。注意 Johannessen 自己承认 Dexter S5 的 "Atonement" 是**涌现**的；Landau 也列出不用统一主题的剧（Breaking Bad；Parenthood 与 FNL"不对称地排列"） |
| **要不要 outline** | Landau 1e："**No outline, no paycheck.**"；Calvisi："the Story Map is the ultimate outline template."；Miller：先 grid 再 outline 再写 | Mazzara："I don't use outlines… None of their notes are applicable to script."——替代是两三页 story document ＋ 每拍两三个词的 beat sheet（"Rick kills Shane."）；Sorkin："When I finish one script I have no idea what's going to happen in the next." | 在别人的剧组写集／要拿开发稿费 → 必须 outline（合同节点）；自己是 showrunner 且能边写边守结构 → Mazzara/Sorkin 可行。Mazzara 自己划了边界："All script problems… come down to structure problems." 详见 `sw-writers-room` |
| **Teaser 是不是必需** | Calvisi / Douglas / Goldberg & Rabkin：teaser 是抓人的第一道关 | Oberg：只有服务戏剧目的才要，否则"just pointless"；Landau：很多剧直接从第一幕开始 | 有广告、观众拿着遥控器 → 必有 teaser；强连续剧／刷剧平台 → 可用"短第一幕＋晚打片名"替代（Scandal、Modern Family） |

---

## 九、诊断清单（写完一集后逐条自问）

1. 这一集的**核心问题**能用一句话说出来吗？（Mazzara："What is this episode about?"）
2. 每条线都有一句**挂在主角（而非客座角色）身上的 log line** 吗？它是真正的故事，还是只是一个情境？
3. A 线贯穿每一幕吗？act break 都落在 A 或 B 线上吗？有没有一幕收在 C 线上——如果有，那条线可能其实是 A 或 B。
4. 每幕 4–5 个 beat、5–7 场吗？全集场数在 20（五六幕）到 28–30（四幕）之间吗？ **（场数只对美式一小时集有效：半小时喜剧 15–20 场〔多机〕或 40–50 场〔单机〕见 `sw-sitcom-comedy` 第四节；国产 45 分钟集 25–35 个场面见 `sw-chinese-series-practice`。三个数字差二到三倍，按"拍法＋时长"选，不要缩放。）**
5. **（本条只对美式一小时集有效；半小时与国产剧跳过）** 页码锚点对得上吗？（含 teaser 的四幕 17–18 / 30 / 45 / 60；Calvisi 五幕 teaser≤10、二幕收 30、三幕收 40、四幕收 48；AOP 在 37–40；最坏情况在 4/5 处） **（同上：只对美式一小时集有效，半小时与国产剧不跑这一条）**
6. 有没有一场超过 3 页却不是完整节拍？四页的会面戏就是红旗。
7. 有没有任何一场只是为了 exposition？有没有"没有 character want 的 moment"被当成场用？
8. 每场都有五件套吗（want / obstacle / 至少三个 escalation、优先动作 / decision / resolution）？收场时观众知道 hero 情绪上站在哪里吗？
9. 每个出幕都能说清是什么事件吗？它从人物的 jeopardy/risk/fear 里长出来了吗？"surprise"型出幕铺垫到"本该看出来但没有"了吗？
10. 八种出幕形式用了几种？**至少一幕用无对白动作或道具定格吗**（而它的语法在前面教过吗）？
11. Act Two break 改变了故事的性质，还是只提高了危险？Act Three 末是否让主角的胜利变成了新的失败？
12. 赌注检验：对这个人物来说，"面对危机什么都不做"是可行选项吗？每一幕的 +/− 极性标出来了吗？有没有一幕是以"赢"收尾的？
13. 四个信息工具各用在哪里？主角有没有长期比观众知道得更多（尤其是理解其动机所必需的前史）？本季的大谜会在季末解决吗？
14. teaser 是故事还是讯息？如果用了 teaser flashback，它有没有不小心回答了本集的 dramatic question？
15. 末幕是否只做 pay-off、不引入新信息？（**国产长剧不适用**：国产体系要求每集末尾再卖一个大关子，与本条直接冲突。写国产剧时本条只用于"季终集"，单集集尾按 `sw-chinese-series-practice` 的集尾悬念规则办。）倒数第二幕结束前，观众清楚知道还有哪几笔账没结吗？结尾有东西可"发现"、同时**没有**把所有东西都兑付掉吗？
16. 流媒体剧本：删掉 ACT 标记后，隐形幕还能用三重判据（剧情日／地点切换／核心问题转向）划出来吗？每个幕末是否有一次信息或权力的转移？
17. 季形：这一集在季里的位置对吗（六集季：铺开／欲望／露底／瓶子集／伪胜利／封闭场合结清）？季终与 pilot 有对称的掉头吗？每条线的落子是否同时生成下一季的债务？
18. 提速检查：第四幕结尾那个最酷的事能不能挪到 teaser 末尾？这一集有"第二天人人都在谈的那一场"吗？
19. 制作检查：内外景、日夜戏的配比算过吗？只写了 DAY / NIGHT 吗？有没有把制作限制逆用成 bottle 集的三个选择？

---

## 十、工作流程：从一集的点子到交付稿

1. **定三件事再动笔**（Oberg）：**series type**（procedural / serial / hybrid / limited / anthology / sitcom）、**story-type**（plot-led / character-led / theme-led / hybrid / exception）、**format**（集长＋大类）。任一含糊就先别写大纲。（story-type 判定见 `sw-series-engine-bible`。）
2. **选结构 comp**（Calvisi／Landau 同条）：找一部在语调／类型／题材／受众上与你相近的**成功**剧当结构模板；拿不到剧本就看片写 scene list。问清四件事：**有没有 teaser？几个 act break？每幕几场？有没有 tag／epilogue？** 它同时是你 pitch 时的 comp。**47 部剧的现成抽样表**（剧名｜年份｜format｜network／platform｜幕结构｜premise／non-premise／hybrid pilot｜showrunner；Landau 1e 附录，2014 年口径）见 [reference.md](reference.md) 第十一节，不必自己重新数。
3. **拆 comp 的两三集填格子**（Douglas）：命名 A/B/C，每条线写一句挂在主角上的 log line，逐格填字母。
4. **定本集的核心问题**，以及每条线的**入口场与出口场**（Downton 的线表法：一集 8–12 条线是上限，其中 1–2 条必须与主危机无关）。
5. **倒序制造**（Douglas）：先在格子里填**开场、四分之三处的"最坏情况"、结尾**三处；只做 A 线或 A+B，给 C 留余地；然后从 cliffhanger 倒推前面的 beat。
6. **每条线单独做 landmark 或 dramatic sequence**：用 Miller 的六 landmark（pilot 的 hero committed 要一石二鸟），或 Oberg 的 inciting incident → subgoal → sequence → scene。**此刻各条线分开写，不要编织。**
7. **压成一页 grid**（Miller 第 5 章）：顶端一排幕标签卡，每幕下一列卡片，一卡一场，卡上写 scene heading ＋ **character want**。无广告剧先按 **teaser + 四幕** break，定稿时删标记；要六幕就把第三、四幕各拆两半。一眼检查：landmark 是否落位、act break 是否够硬、主角是否 proactive、本集是否合乎本季。
8. **排 act out**：每幕出幕交给不同的线；从八型里选，保证至少一幕无对白或道具出幕；把 squeeze 留在幕中（它需要演完）。
9. **给每集配一条"程序线"当节拍器**（West Wing 六集的共性）：外部危机（军事打击、使馆围困、手术时长、开票）提供合法打断与"还有一小时"的期限，最后把它的数字交给主角当道德论据；它不承担出幕。
10. **写 outline / beat sheet**：一小时剧情类用 treatment 或 step outline；**Blum 给剧集 treatment 5–10 页、"越短越好"，必须写出 act breaks**（电影 treatment 则 10–20 页）；outline 的每个"节拍"写成该场的 log line。房间流程见 `sw-writers-room`。
11. **到写 teleplay 时才编织**：做同场多层调度、ellipsis、平行剪辑；此时给每场补五件套。
12. **写长再压还是守页数**：Succession 的做法是每集 70+ 页（剪辑时才有重新聚焦的余地）；Calvisi 的反面警告是新人不要超过 60 页。取哪条看你是不是 showrunner、片子是否已开拍。
13. **交付前对格式做一次决定**：标 ACT 还是删 ACT（按 2.6 的判据）；teaser 出幕写 `SMASH CUT TO: MAIN TITLES`，每幕末 `FADE OUT.` ＋ `END OF ACT N`（West Wing 六集 100% 一致）；**pilot 剧本不带场号**（Miller："Pilot scripts do NOT have scene numbers."）。
14. **跑第九节的诊断清单**，然后按 Grace Paley 的收尾方法（Landau 转述）——**"I look for the lies."**

---

## 十一、训练

1. **拆一集填格子**（Douglas 的课堂作业）：命名 A/B/C 线，每条写一句 log line，逐格填字母；标出每个幕末悬念属于哪条线、哪条线在哪一幕才开始、哪条在第三幕就结束。
2. **Goldberg & Rabkin 的双练习**（p0033）：① 看一集，每幕停下，**用一句话写该幕的叙事弧，再用一两行写该幕最后一场**；② 连看多集的 **Act Two break**，分析那个时刻如何改变故事方向。
3. **act out 计数**：取一集，写出五个出幕各属于哪一型（八型表），并判断哪一个是 schmuck bait。
4. **Calvisi 的 Story Map**：用 Basic 17 栏 + Full map 拆一个 pilot，标出 AOP 落在第几页、DOW 是否在 4/5 处；再照同一张表 beat out 自己的 pilot。
5. **Miller 的 landmark 表单**：为自己的 pilot 写六行；再拆一部**结构**（不是题材）与你的 pilot 相似的 pilot，breakdown 须含 scene headings、story beats、character wants、scene ins and outs、act breaks、landmarks。
6. **escalation 拆解**：挑两场 1.5–2 分钟的场，逐条数出 escalation（目标 10 条以上），标出 decision 与 resolution，统计多少是动作、多少是台词。
7. **隐形幕反推**：取一集无 ACT 标记的剧（Succession、Homeland、Sopranos），用三重判据划出幕位，逐幕写出"出幕事件＋划分依据"，与 [reference.md](reference.md) 第四节的 Succession 实测对照。
8. **信息管理改写**：把一个"打到一半切走"的 act out 改成三个版本——一个 surprise、一个新设立的 dramatic irony、一个 mystery；判断哪个让人更想看下一集。
9. **幕数换算**：把一集四幕剧的 outline 分别改成五幕（Act Four 对半）、六幕（三、四幕各拆两半）、无幕（改成剧情日标记），每次都要为新的 act break 找到一个站得住的事件。
10. **提速练习**（Rabkin）：把 pilot 第四幕末那个最酷的事挪到 teaser 末尾，重写全集，看接下来六十页能不能保持同一速度。
11. **预算倒逼**：给自己下四条禁令（无客串、无外景、无新布景、无群众），写一集 bottle——单夜、单建筑，趁机推进季弧里一直没敢说的秘密，并把线数从 4 加到 5。
12. **六集季形**：按 Fleabag 骨架写六集一句话大纲，指定一件**每集换一次手**的物件；季终的最后一个画面只解决主题。
13. **对称练习**（Succession S1）：给第一集找一个数字／物件／台词，让季终用同一个东西完成掉头。
14. **容器集练习**：写一集"所有人被关进一栋楼＋通讯受限"，再写一集"有日程表的仪式日"（列出既定环节，每个环节塞一次冲突）。
