---
name: sw-sitcom-comedy
description: Half-hour television comedy craft (半小时情景喜剧/笑点力学/困境机器/多机位单机位格式) — merged from Evan S. Smith's Writing Television Sitcoms (premise-driven comedy in three levels, nine predicaments, six character mixes, setup/punchline mechanics, toppers, running gags, ten comedic nuances, format rules), Neil Landau's sitcom seven-step formula and comedy-room models, Richard Blum's act-length and set-count parameters, Phoebe Waller-Bridge's Fleabag scripts (direct address as a season-long device, six-episode skeleton), Pamela Douglas on dramedy, Kam Miller on complementary comic traits, and Jesse Armstrong on jokes carrying tragedy. Use when writing or fixing a sitcom episode or spec, raising joke density per page, designing a comic predicament that generates stories, choosing between multi-camera and single-camera format and page counts, structuring cold open/acts/tag, writing a half-hour pilot, running a comedy punch-up, or making a drama funny without shifting genre.
---

# 半小时喜剧（Sitcom & Half-Hour Comedy）

> **输出语言＝提问语言**；术语一律锚回原词，见 [sw-workflow/terms.md](../sw-workflow/terms.md)，不自创译名。

核心命题：**好笑不是后期往台词里塞的，是从故事前提里长出来的。** 喜剧作者在三层上叠加张力——premise → sequence/scene → dialogue/action；种在前一层的喜剧会在后一层"自动产出更多、更大、更无缝的笑"（Smith《Writing Television Sitcoms》p0042）。所以第一个动作不是想笑话，是问"这个前提本身是不是一台 joke-producing machine"。

写半小时剧不是把一小时剧的参数改小，而是**整体切换**：页数、排版、场数、笑点密度、结构单位、人物关系的运转逻辑一起换。本 skill 管这套切换。通用方法不重写——对白见 `sw-dialogue`，场景价值转折见 `sw-scene-craft`，一小时剧幕结构与 act out 类型学见 `sw-series-structure`，引擎与 bible 见 `sw-series-engine-bible`，编剧室全貌见 `sw-writers-room`，Fleabag 逐集表见 `sw-series-case-studies`。

格式规范、笑点技法目录与结构模板见同目录 [reference.md](reference.md)。
## 按任务读哪几节（不要通读）

| 任务 | 读 | 跳过 |
|---|---|---|
| 判断一个喜剧点子成不成立 | 二（三层法与困境） | 六、十 |
| 写或改笑点 | **三（笑话力学）**，例库转 reference.md | 四、九、十 |
| 排半小时结构 | 四（含幕长/页码的选择规则） | 三、七 |
| 选格式、定页数 | 六；中文稿先看 `sw-chinese-series-practice` 的页数折算 | 一–五 |
| 直接对镜 / 装置喜剧 | 七 | 二、六 |
| 诊断一份已有的喜剧稿 | **十二（诊断清单）** | 其余 |

⚠️ reference.md 第一节是**美式排版规范**（字符位、边距、行距）：写中文稿时整节不适用，不要读。

---


## 来源与各书关系

- **Smith《Writing Television Sitcoms》（Revised & Expanded, 2009）给全部骨架**：三层法、九 predicament、六 character mix、笑话力学、beat 数与三幕页数、三套格式（Appendix A 按字符位给边距）、pilot 与 series format。本 skill 的编号体系基本是他的。
- **Landau《The TV Showrunner's Roadmap》1e Tip 21 给公式与页数表**（七步公式、"恶狗追上树"、多机页数分配、多机 vs 单机差异）；**2e 第 13 章给喜剧编剧室**（四种房间模型、alts 与 candy bag、table read 的功能之争）。
- **Blum《电视与银幕写作》第 11–12 章给制作约束**：teaser/幕/tag 分钟数、多机格式规则、**布景 3 个理想 5 个上限**、一周拍摄计划。
- **Waller-Bridge《Fleabag: The Scriptures》给装置喜剧与六集季骨架**；**Douglas《Writing the TV Drama Series》3e 的 Dramedy 专题给边界**；**Miller《...And the Hero Succeeds》给 complementary traits**；**Armstrong《Succession》剧本集给"喜剧承载悲剧"**。

---

## 一、半小时喜剧与一小时剧的区别：整体切换表

| 维度 | 半小时喜剧 | 一小时剧 | 出处 |
|---|---|---|---|
| 页数 | film/single-cam **27–30**；tape/multi-cam **45–50**；animation **40–50** | 48–63 | Smith, Appendix A；Landau 1e p0296 |
| 幕 | cold open ＋ 2 幕（多机）或 2–4 幕（单机）＋ tag | teaser ＋ 4/5/6 幕 | Landau 1e Tip 21 |
| 幕长 | teaser 30–60 秒；每幕 10–12 分钟；tag ≤1 分钟 | 每幕 10–15 分钟 | Blum p0135 |
| 第一幕 | **极短（30 页里 1–5 页）**，人物与世界已建立 | 约 1/4 | Smith p0121 |
| 场数 | 多机一集 **15–20 场**、每幕 3–5 场、场面长；单机场多而短（HIMYM 常 40–50，有时 80） | 视格式 | Landau 1e Tip 21 |
| 布景 | **3 个理想（1 主＋2 副），上限 5** | 多得多 | Blum p0143 |
| 结构单位 | beat：主线 5–9，subplot 3–5，thread 每条 3–6 | 场与 act out | Smith p0117–0119 |
| 笑点密度 | **每页 2–4 个实笑点**；多机几乎每句台词都被期待出笑话 | 仍需幽默视角 | Smith p0039/p0083 |
| 赌注 | 小而对人物至关重要（**"tremendous trifle"**）；"sitcoms are smaller" | 生死／职业／制度 | Landau 1e p0298；Smith p0119 |
| 沉默 | 多机的沉默＝dead air；单机的沉默可以 cringe "but in a good way" | 沉默是资源 | Landau 1e Tip 21 |
| 人物成长 | 单集"自私→醒悟→学到教训……下集归零"；长期靠**扩展**而非改变 | 跨季弧 | Smith p0139；Lloyd |

1. **引擎是关系密度，不是事件。** Blum 记录制片人对"角色彼此之间的亲密程度"吹毛求疵，因为那是让喜剧稳步发展的关键（p0148）。Fleabag 第一集没有"事件把主角推进新处境"，只是把一张互相伤害的关系网铺开。
2. **多机与单机是两种写作动作，不是两种排版。** 多机像舞台剧：场少、场长、必须不断设计人物在同一布景里的进出场（Michael Patrick King 认为**多机更难**，因为单机"you could just CUT TO: the next scene"）；单机像"每周一部小长片"，靠碎片场面与交叉剪辑，更依赖视觉笑点。有高管认为两者有"HUGE creative differences"、招单机剧只看单机 spec——**两种样本都要备**。

---

## 二、premise-driven comedy：三层法

三句话（Smith p0092–93）：**① 把好笑的元素织进故事前提；② 在 sequence/scene 层剥削并复合它们；③ 从故事自带的幽默里长出对白与动作。"It's all about building rather than repairing."**

### 2.1 第一层：premise 的四个喜剧来源

**Predicaments／Character Mix／Style of Comedy／Casting**（p0045–0061）。

**困境是 joke-producing machine。** 场景里的困境只管几页；织进 premise 的持续困境一直生产笑点直到它被解决，而且**未解决的困境让观众带着期待看戏，连无关的笑话都显得更好笑**（p0046）。系列永久困境（《Gilligan's Island》的"no phone, no lights, no motorcar"）是找单集故事的第一处矿。前置条件：观众相信人物不会真受伤，且已被提示"这是喜剧"。

**九种经典 predicament** 与 **六种 character mix** 的名目、原例与使用限定见 [reference.md](reference.md) §二。

### 2.2 "每个剧就是它自己的一个 genre"
子类别（domestic、odd couple）不是 genre：《Two and a Half Men》与《The Simpsons》都是家庭剧但属性完全不同，**每个剧的 premise 规定一套观众期待的属性**。写既有剧前先答风格问题清单：幽默主要来自困境、人物关系还是环境？belly laughs 还是 smiles-and-nods？视觉为主还是对白为主？结尾有爆发式 comedy run 还是全程均匀？
**两个新手错误**：**Too Funny to Pass Up**（再好笑也要扔掉不属于这个剧的点子）；**The Genre Shuffle**（"blending genres throughout is not the same as shifting"）。最理想的一集 **"expands (but does not change) a show's premise"**。

### 2.3 第二层：sequence 与 scene 的复合

sequence＝一串连续场景承载一个持续动作；scene＝一个地点一段时间，地点或时间一变就是新场。三个动作：
① **Compound Story Predicaments**——在故事层复合困境，张力"不是翻倍而是指数级上升"（p0063）；可叠同类（Big Lie → Bigger Lies）也可 Mix and Match；这一层的困境"more finite, occur in real time"，在一个连续段落内出现—展开—解决。② **Stir Up the Character Mix**——临时结成"unnatural alliance"，观众同时等故事困境解决**和**这个联盟崩溃，结尾恢复原有配比。
③ **三条提醒**：**Escalation**（升到结尾的 comedy climax，很多剧固定在每集末放一段 raucous comedy block）；**Look to the Series Premise**（最好的故事来自主角的 foibles）；**Be Consistent**（写对白前就检查各段落笑点强度——等你被自己的妙句迷住就晚了）。
人物学基础（Sheldon Bull）：sitcom 人物"没有 self-edit button"，行动更冲动，对常人能一笑置之的问题做出巨大反应。

---

## 三、笑话力学（第三层）

模型：**setup**（straight line）引入话题并暗示某种 complication/incongruity→制造张力；**punchline** 用意外方向的转折解决它→释放张力。"setups are the true unsung heroes"（p0068）。Smith 的限定必须一起记：这些术语的最大价值在**改与修，不在造**（editing and repairing, not creating）。

### 3.1 Setup 五条

1. **平常可信**——先用合理的 setup 把观众拉进来，再用意外的 punchline 敲头；setup 一显得古怪，观众就知道有埋伏。
2. **两段式**：至少含 ① 话题＋ ② **一两拍 development**（由 complication 或 incongruity 造成）。没有第二段，张力不够，punchline 只像补充信息。Smith 的对照实验（把《30 Rock》pilot 里 Jack 剖析 Liz 人生的长篇砍成一句）结论是"仍好笑但不如原来，而且显得更公开地敌意，不忠于人物"（p0071）——**development 段同时决定笑点强度和人物真实度**。
3. **可以拆散铺远**：各部分可散在一场戏里甚至提前几场埋好。
4. **不许暗示**："You brought a whole beer keg."→"Yeah. Where can I fill it up?"；多问一句"Is that thing full?"笑话就死了。
5. **生活本身是半个 setup**：共同的生活苦难与共享文化经验可充当第一段。

### 3.2 Punchline 六条

定义："a sudden twist that makes both sense and nonsense"——它解决 setup，但来自观众被引导去期待的那个方向之外（p0077）。

1. **Last things last**：punch word 放句尾。"I think that he thinks it's a paper for people who work. Daily." 远胜"it's a daily paper for people who work"。（同一原理见 `sw-dialogue` 的掉尾句。）
2. **Don't go past the joke**：punchline 通常也在一段台词末尾，说完还接着说会踩坏它。例外：啰嗦是这个人物的节奏。
3. **Topper**：一个 setup 出两三个递进 punchline（"Sex."→"It's illegal... Next best thing."→"Torture."）。三条限制：**最多 top 两次**（再多观众会察觉）；有些笑话该单独留着（承担戏剧时刻、控制节奏）；**dramedy 里通常不用 topper**。
4. **Running gag / callback**：一个完整笑话后面回来 2–3 次；回指原笑话的新 punchline 叫 callback。三种做法：同一人物在新情境重说／不同人物重说／不同人物说同一 setup 的变体。每次回来带第二层含义，**最后一次常是反讽或反转收大笑**。术语提醒：running gag 也叫 runner，但 runner 也常指"很小的 subplot"，未必好笑。
5. **卡住就回去改 setup**（换一个 incongruity 或加大 contrast）——而不是继续磨 punchline。
6. **Go for Literal**：取字面义（"Call me a taxi." / "Okay, you're a taxi."）。literal joke 多出自**极笨或极聪明**的人物。

### 3.4 人物专属的笑法
十种 comedic nuance：Understated Response／Exaggerated Response／Irony／Nervous Babbling／Pulls No Punches／Space-Shot POV／Wordplay／Double Entendre（＋两种情绪驱动的变体）。每一种是**人物的固定笑法**而不是作者的技巧库：**写对白前先定这个人物用哪一两种，其余不给他。**

### 3.5 五条通则

- **Hanging a lantern on it**：让一个人物喊"That's crazy!"来让离谱设定过关（p0178）。不可信的事要先 foreshadow，并且**种了种子就要收割**。
- **Bigger Really Is Better**：不是告诉邻居而是向全国广播老板秃头；不是冒犯一个同事而是给全办公室讲多元化。只要不违背人物天性与剧集前提，**往大想**。
- **Small Truths, Big Laughs**："Surf's up, Jim. Watch me ride this wave of inspiration! (GRINS, INTO PHONE) Yes, I'll hold."
- **Reiss 三条件**：每个笑话必须同时**好笑、服务剧情、不让人物变得讨厌**；而且再难的位置也一定有一个笑话在那里，"你可能要找两小时，但你会找到"。

### 3.6 密度标准

**每页 2–4 个实笑点**（p0039/p0083）。执行方式不是估计而是**数**：用红笔圈出真笑点，不足就修；开头几场要逐个数——读者不会因为这是 pilot 就宽容，也不会等到第六页"喜剧才真正开始"（p0297）。另一端：没有制片人会说"这剧本太好笑了"，但也不能 **too jokey**——**笑点的量与类型从头到尾要稳定**。观众反应分三档 **smile / chuckle / laugh**（肢体喜剧出 laugh，机智对白出 smile）。**topper 与 running gag 是提高 joke count 最经济的手段。**

---

## 四、半小时结构

### 4.1 beat sheet（一页）

**主线 5–9 个 beats；每条 subplot 3–5 个；thread structure（Seinfeld 式四条等重线）每条 3–6 个。** beat＝改变主角目标或抬高张力的时刻／发现／事件，常是"action→reaction"两半，缩写成一句："Character One blabs secret—claims (new lie) to cover up."多线先各自列再编织；**每个 beat 以中心人物的名字开头**再改写成他的反应（Ellen Sandler）。这张纸上的故事如果不 build、不合逻辑、不好笑、不意外，就回画板。术语 flag：正剧剧组的"beat sheet"另指多页、编号场景、电报体的 outline。
术语 flag：正剧剧组的"beat sheet"另指多页、编号场景、电报体的 outline。

### 4.2 单主线的三幕与页码

典型路径：主角遇新问题／机会→用**离谱**（而非合理，否则没故事）的手段追求→障碍升级、目标更急迫→结尾反噬、暴露、难堪，"learns the error of his ways. Sort of."
**第一幕极短**（一两个 beat 内出 inciting incident）；**第二幕最长**（占 1/2–2/3，"think development, not repetition"，常以大揭示＋重大抉择结尾）；**第三幕约 1/4**（加速、升到高潮、对质、真相、解决）。
**页数（film format 30 页、单主线）：1–5 页／15–20 页／5–10 页。** thread 剧四条线各约 1/4（7–8 页），各幕落在哪页无法预言。

> ⚠️ **这组页码与切换表里"每幕 10–12 分钟"是两套互斥方案，对第一幕的要求差四倍（1–5 分钟 vs 10–12 分钟）。选择规则：先定幕数。**
> - **两幕**（cold open＋2 幕＋tag，多机位常见）：每幕 10–12 分钟，第一幕不短。
> - **三幕单主线**（film format 30 页）：1–5／15–20／5–10 页，第一幕极短，因为人物与世界已建立。
> - **pilot 例外**：第 1 集要建世界与人物，第一幕必然长于 1–5 页，**不要按这条判不合格**。
> 诊断 ⑦ 只适用于三幕单主线的非 pilot 集。

### 4.4 dramatic structure vs broadcast format

"act"两义：戏剧结构的幕 vs 广告之间的段。**广告位不一定与戏剧幕转合拍**——广播意义上第一幕之后的那个广告，可能落在戏剧意义的第二幕中间。你在 outline／剧本里打的 `ACT ONE, ACT TWO` 是 broadcast format。做法：先 beat sheet，再在 outline 里把关键 plot point 挪到该剧惯常的广告位之前；不能全对齐也没关系，但能放大 beat 就放——**新人在 spec 里写出强 act break 会大大加分**。

### 4.5 Landau 的七步公式
七步全文（tremendous trifle 的定义、中点反转放在哪一幕末、恶狗追上树的比喻、tag 的功能）见 [reference.md](reference.md) §三。

### 4.6 key dramatic moment 与 block comedy scene

Matt Williams：每集都要建向一个 **key dramatic moment**（决定／发现／和解），一切朝它走、再从它走开，而它**九成落在 block comedy scene 里**（p0126）。推论：先定这一刻，再决定它落在哪一场；那一场必须同时是本集最大的喜剧段落。

### 4.8 六集季（单一作者、流媒体半小时）

Fleabag 两季各 6 集的逐集骨架、单集 cold open → TITLES → 段落 → button 的模板、以及两条收尾规则（季终 button 解决主题；一件物件贯穿全季、每集换一次手）见 [reference.md](reference.md) §四。

---

## 五、人物：谁值得被放进这台机器

- **不必讨喜，但必须有 drive、purpose、软肋、独特技能**——至少要有"some small spark of passion"（p0296）。Michael Scott 是自大又常刻薄的蠢蛋，但他是公司顶级销售，而且总想做对的事（然后没做到）。**"in comedy, it's usually the troublemakers that we like best."**
- **Proximity counts**：前提里**必须有某个场景或戏剧装置，定期把人物挤在一起**，让他们一集又一集地互相撞上。不必又做办公室／客厅剧（单机允许到处跑），但这个装置不能缺。
- **冲突要发生在常规人物之间**：两个常驻角色为"卷纸该朝哪边挂"吵起来，观众就会看。
- **complementary traits**（Miller）：**情景不好笑，人物才好笑**——孵化器、公寓、医院、餐馆本身都不 funny。传统路线是亚里士多德式"imitation of men worse than the average"（It's Always Sunny、Curb）；当代有一条 softening trend：**complementary character traits**（有缺陷但善意）更 relatable。Modern Family pilot 人物表的三个可复制做法：**每人都用正面措辞描述；任意两人配对都能出笑点；每人的观点各有 validity。**
- **十种行为型人物**：Supportive Parent／Idiot Savant／Idiot Idiot／Clown／Operator／Mentor／Confidant／Irritant／Romantic Interest／Critic。限定很重要：这些是**临时行为模式**而非固定标签——Frasier 这集对父亲是 supportive parent、下集是 childlike idiot。
- **配角命名法**（Fleabag）：用**一个特征**命名并终身不改（Arsehole Guy、Bus Rodent、Bank Manager、Godmother），主角无名。命名方式本身要是主角的能力／缺陷——她一生都能把人缩成"一个公交老鼠"或"一个混蛋男"——所以后面要有一集让她为此付代价（Priest＝她第一个无法贴标签的人）。

---

## 六、三套格式与页数硬指标

三套格式＝**live-action film（single-camera）／live-action tape（multi-camera）／animation**；真正的区别是单机还是多机。**写既有剧的 spec 就去拿那部剧的真剧本，精确复制版式**。三套格式的页数、边距（按字符位）、行距、场景编号、进出场下划线、`END OF COLD OPEN`／`END OF ACT ONE`／`TAG`／`END OF EPISODE` 的标记写法、spec 刻意不写的项目、布景经济学与动画两条，见 [reference.md](reference.md) §一。

---

## 七、直接对镜与装置喜剧（Fleabag）

直接对镜（`(to camera)`）**不是风格而是人物的心理防御**：她某天醒来发现有观众在看她，于是做了唯一能做的事——"she put on a show"（〈Who is Fleabag?〉）。这个定性决定了它能在第二季变成剧情。三种基本用法：旁白式铺陈（"You know that feeling when..."）／对话中间的一句内心批注（说 A，转头对我们说 B，再转回去说 C）／无声的一瞥（"She looks at the camera." 作为反应镜头）。

1. **装置先做可行性测试，再写剧本。** 一年破不了改编难题，最后是 Vicky Jones 用手机拍她在厨房对镜头说话五分钟，放下手机："It works."——**把装置当成可测试的假设，而不是写作决定。**
2. **三连＋第四拍由别人翻转。** 先给形容词、再给证据，**证据总比形容词低一档**："He's a feminist." / "I have a sister."；或"别说—别说—说了"（五拍内三次转头）。**翻转权交给对手，不交给主角。**
3. **对镜头只说笑话，对人说真话。** 全季给她一次且只有一次**不对镜头**的长独白（告解室），那就是全剧的情感最高点。
4. **装置本身就是季弧。** 第一季它是同谋；季终第一次反转（她躲镜头，镜头追她到墙角、把闪回逼出来）；第二季让**一个人物看见它**并逐级升级：发现（"Where did you just go?"）→质问（"it's like you disappear"）→命令她停止→她推开它→她请它别跟（最后一句台词是写给镜头的舞台指示"Goodbye."）。**装置走完这条路，剧就结束了。**
5. **视觉句子（visual sentences）**：把创伤写成一张 2–4 秒的画面（Boo 站在马路对面、车流掠过），在主角"看起来很好"的时刻插进去（笑、做爱、走在街上），观众立刻知道她不好——不要让人物复述。导演给出这个画面时说"that was all we needed"。

**情感场面的标准节拍是"痛—笑—痛"**：真话→一个视觉笑点或一句贱话→回到真话。配套两条：**让主角输掉辩论**（她慷慨陈词后用一个道具当场证明她站错队，再让配角两句话把主题升级）；**季终表白允许说三次、回答只给两个字**，然后用 anti-climax 七拍收尾（表白→温柔拒绝→对方回赠→一个日常的倒霉→一个纯喜剧道具→一个与亡者相关的物件→装置告别）。

---

## 八、dramedy 与"喜剧承载悲剧"

**dramedy 的判据（Douglas）**：1960 年代美国网络把"半小时＝sitcom、一小时＝drama"制度化，至今办公室还物理上分 comedy／drama 两边，pitch 也只能对一个 VP。dramedy 的属性是人物与故事线连续、有 backstory 深度与戏剧弧，**而不是按固定间隔出 setup/joke**；笑是 wry／ironic 的。两条规则：**超过三分钟的任何形式都不可能靠 joke-to-joke 写作过关**；**除儿童冒险外没人能写通篇无幽默视角的正剧，冲向悲剧的集尤其要带喜剧**（莎翁在最悲的场前放小丑）。Douglas 的教训：Frank's Place 因观众嫌"不够好笑"被迫改成纯喜剧——**观众的期待由时段与格式设定，dramedy 要主动告知观众该期待什么**。

**Succession 的六条做法**：

- **用笑话承接最黑的坦白。** Kendall 说出他撞死侍者之后，Roman 用笑话把罪名一级一级往下砍（murderer→irresponsibler→"at worst you're a manslaughter-er"），Shiv 跟上"Oh yeah I've killed a coupla kids. Sure. Just little ones."；剧本自注 **"It is so dark that it is kind of funny."** 机制：**接纳不以安慰的形式出现，而以家族内部的残忍玩笑形式出现，因为这是这家人唯一会说的爱的语言。**
- **喜剧支线当调温器，不是稀释剂。** Greg 的 Luxembourg 王位线在最黑的段落之间反复插入——而且最后正是在这条线里把 Tom 逼出决定。**判据：喜剧支线必须同时承担一个情节功能，否则就是注水。**
- **给剧终集一场没有剧情推进的退行游戏**（厨房"meal fit for a king"）：全员第一次也是最后一次同一意图，**笑点必须是合作性的**；让唯一一句想说温情的话被打断——那个未完成的停顿就是结局的预告。
- **排序规则**：房间里最有力的提案永远是"向现实而非神话的诉求"，**只偶尔输给最好笑的那个**。

---

## 九、sitcom pilot 与 series format

**默认写 typical-episode pilot。** premise pilot 演出"创造该剧前提的那个事件"，钩子本身就是素材，但**它示范不了普通集长什么样**（"that Martian won't crash-land in someone's yard every week"）且重播效果差。所以**多数网络高管偏好 typical-episode pilot**——一集"就像这部剧第 17、52、89 集那样"的半小时，见到新人物时几乎不给 exposition（p0296）。Fleabag 第一集就是典型例。

九条做法里最可执行的：**第一页就好笑并字面上去数开头几场的笑点**；**人物吸引力优先**（主角必须 fresh、relatable、appealing）；**proximity counts**；**保持简单并尽量延后 exposition**；**Know your rights**——"You can't sell what you don't own."，改编任何素材在写之前就去 option；投出去前登记版权。

**series format 文档（10–15 页、十一节）** 的三条判断：必须证明 **legs**（前提丰富到能生出一百集以上）；**premise 那一节介绍人物只用一个短语**，让行动与台词去定义她；**format 本身就是写作样本**——读起来像年报的文件卖不掉喜剧。
**pitch 执行规则**：pitch 单集带 **10–15 个 springboard**（每个 3–5 句，先讲短版）；**pitch 新剧只带那一个大点子＋一两个备用**，大点子被接受后立刻停讲备用。并且 **"Try to pitch funny—you're supposed to be a comedy writer."** 通用 pitch 文档与 bible 三档见 `sw-series-engine-bible`。

---

## 十、喜剧编剧室

**基本分工**：集体破故事 → 个人写初稿 → 集体 punch-up。**roundtable writing**（tabling）：5–15 人逐行改稿塞笑话，资深制片人裁决；有的剧雇 **punch-up person**。一本剧本改五次以上不稀奇，**许多编剧觉得原对白有一半活到拍摄稿就算幸运**。流程与职级见 `sw-writers-room`。

**alts 与 candy bag**（Landau 2e ch13）：初稿被集体解剖并 pitch 新台词与笑点，新台词叫 **alts / alternates**。Schur 的数据：**剧本会连同 alts 胀到 50–60 页，再砍回规定的 30 页。** 被弃用的笑点存起来留给未来集数，Greg Daniels 称之为 **"the candy bag"**（Michael Patrick King 的版本叫 "the whipped cream"）。**但不要囤好料**——Schur："忠诚的观众是珍稀商品"；Daniels 的说法是 **"Pack the sausage; put it all in."** 折中：**结构性的大点子要烧掉，笑话可以存。**
**现场 alts**（Succession 的版本，通用）：开拍前一两天挑出 0–15 句可能"funnier or better or truer"的台词，发给 3–5 位编剧征 alts，从 10–20 个选项筛到 5–10 个揣在口袋里，拍完剧本版后视情况喂给演员。

| 房间模型 | 做法 | 适用 |
|---|---|---|
| Parks & Rec（Schur） | 集体 break，各自写自己那集；集体写整集会落入"边际效益递减" | 群像、声音相近 |
| Mindy Kaling | 索引卡＋白板；季初向平台 pitch 三四个"story area documents"求批准；每集派一两人写初稿（求"wonderful patchwork of voices"）；初稿交上来后剧本成为全屋共有财产 | 想保留多种声音 |
| Insecure（Issa Rae） | 集体写每一集，**并在编剧室里由编剧／制片人分角色大声围读**（在与演员的 table read 之前） | 声音统一的作者剧 |
| Schitt's Creek（Dan Levy） | 四到六人小房间，几乎全程一起，严格 A/B/C；**把节拍写成对白之后才分稿** | 预算小、要求调性精确 |

**"节拍写成对白"值得单列。** beats 停在"有人被抓住、要摆脱尴尬、最后被另一个人的尴尬中和掉"这种层面时，没人问"**这个尴尬是什么？它此刻如何服务这个人物？这段肢体喜剧能不能同时承担一个情感功能？**"——后果是那条线在整集里感觉很怪。解法：beats 定完后**回到开头把 teaser 的全部对白写出来，验证它成不成立**。

**喜剧可以集体写，戏剧不能**（Bays）：房间会大改喜剧，但"戏剧时刻我尽量不在房间里碰或 punch——戏剧必须是私人的，不能由委员会写"。

---

## 十一、分歧表（什么情况用哪个）

| 议题 | A 方 | B 方 | 怎么选 |
|---|---|---|---|
| 喜剧能不能教 | Landau：结构、潜文本、对白可教，**笑本身是天赋**——"no one can teach you how to be funny"，可教的只有套路 | 同书第 13 章四位 showrunner 给的全是可教流程（前传问卷、从情绪 break、alts/candy bag、节拍写成对白、室内围读） | **流程可教，笑点品味只能校准**；靠流程抬高下限 |
| 集体写 vs 个人初稿 | Schur：集体写整集边际效益递减；Kaling：个人初稿求"声音的拼布" | Issa Rae：集体写每一集＋室内围读；Dan Levy：小房间全程一起 | 按**剧的声音**定：单一作者声音→集体 break＋个人写；群像多声音→可全集体但要有人裁决 |
| table read 的功能 | Smith／Landau／Lloyd：验笑点与节奏，依它改稿 | Dan Levy：只验结构，**不验笑点** | 笑点在台词里→验笑点；在反应／肢体／剪辑里→只验结构 |
| 每幕结尾要不要 cliffhanger | Smith：每幕结尾 cliff-hanger，强 act break 给 spec 加分 | Dan Levy：几乎从不以 cliffhanger 收尾也不玩 will-they-won't-they——"It's emotional stakes" | 有广告位→必须有 act out；无广告＋情感赌注型→可用"挣得的时刻"替代 | ⚠️ **写中文剧集时注意**：`sw-chinese-series-practice` 的对照表要求"每集末尾必须再卖一个大关子"，与本行的"可用挣得的情感时刻替代"方向相反。裁决见该 skill 的该行：无广告的情感型半小时喜剧按本行办，但要在分集大纲里留一笔指定兑付的账。
| 新人该不该在房间里说话 | Lapiduss：新人"almost better to kind of not speak up too much" | Sandy Frank："在房间里你的工作就是 pitch 笑话"；Matt Williams 要看你是 punch mind / joke mind / story mind / character mind | **看资深制片人的信号**：他们 pitch 个不停就别自我审查；不喜欢半成形建议就挑着说 |

**时效 flag**：Smith 是 **2009** 修订版——稿酬（pilot 剧本最低＝单集最低的 150%，2009/5–2010/5 为 $33,349.50）、new-media 清单、"broadcast vs 基础有线"格局均已过时；工艺部分（笑点、结构、格式、房间）基本未过期。Blum 是 **2001** 年——动画编剧不受 WGA 基本协议完整覆盖、Animation Writers Caucus 年费 $75、软件模板数量、Becker 周表都是历史记录。Landau 1e 是 **2014** 年——"当年单机喜剧不被看好"、Web Therapy 的赞助网络剧模式属时代产物。

---

## 十二、诊断清单

**前提层** ① 这个 premise 本身是不是一台 joke-producing machine？要靠台词硬造 wordplay 才好笑，就回去改前提。② 困境是持续的还是只管几页？它什么时候被解决？③ character mix 里有没有两个人贡献同一种东西？④ 这一集"expands but does not change"剧集前提吗？有 Too Funny to Pass Up 或 Genre Shuffle 吗？⑤ 前提里有把人物反复挤在一起的装置吗？

**结构层** ⑥ 主线有 5–9 个 beat、subplot 3–5 个吗？每个 beat 都改变目标或抬高张力吗？⑦ 第一幕是不是太长（30 页里应是 1–5 页）？**仅适用于三幕单主线的非 pilot 集**；两幕剧与 pilot 不跑这一条，见第四节的选择规则。⑧ 本集的 key dramatic moment 是哪一刻？它落在 block comedy scene 里吗？⑨ 困境在向结尾升级吗？⑩ 强 act break 写出来了吗？每幕末是笑话还是新 plot point？⑪ 每条线各由一个不同人物领衔吗？主角在驱动故事还是被来访者牵着走？⑫ 场景 start late / finish early 了吗？有 button 吗？⑬ 新布景超过 2 个、总布景超过 5 个了吗？

**笑点层** **这条是多机位棚拍的 standing set 经济学**（常设景要搭起来长期占棚），**单机位实景剧不按它算**：改数**拍摄场地数与转场次数**——同一栋楼里的门厅、展厅、办公室、库房、后院是一个场地，不是五个布景。单机位的相应判据是"这一集要不要为一场戏单独进一次新场地"。
⑭ **用红笔圈一遍：这一页有 2–4 个真笑点吗？开头三页有吗？** ⑮ 每个 setup 有第二段 development 吗？有没有暗示 punchline？⑯ punch word 在句尾吗？说完就停了吗？⑰ 有没有 top 超过两次？dramedy 里用了 topper 吗？⑱ running gag 回来 2–3 次、最后一次反转了吗？种下的种子都收割了吗？⑲ 有 punchline 死活写不出来吗？→改 setup，或取字面义。⑳ 每个笑话同时满足 Reiss 三条件吗？㉑ 人物用的是他自己那一两种 comedic nuance 吗？遮住人名能分辨谁在说吗？㉒ 笑点的量与类型从头到尾一致吗？㉓ 有没有哪一场本该用 take／stage business／视觉笑点而写成了台词？

**格式层** ㉔ 这个剧是 film 还是 tape？页数对吗（27–30／45–50／40–50）？舞台指示的大小写、对白行距、场景编号、进出场下划线都按那一套来了吗？㉕ spec 里混进了 scene numbers／cast list／音效 slug／镜头指令／"First Draft"／日期吗？dialogue cue 是不是太多？

**调性层** ㉖ 写 dramedy 的话：笑是 wry/ironic 的吗，还是变成了 joke-to-joke？㉗ 冲向悲剧的那一集里有喜剧吗？最黑的坦白之后有人用玩笑接住它吗？㉘ 喜剧支线除了调温还承担了什么情节功能？（只调温的砍掉。）㉙ 这条情节同时完成几件事？**少于两件的砍掉。**

---

## 十三、工作流程：从零到二稿

**0 选剧与研究**（写 spec 时）选你真喜欢、播了至少一季且还会再播的剧；**为 SHOW X 写的 spec 是为了投给别的剧**。**读剧本比看剧更重要**——纸面与屏幕不是一回事，而你的作品是纸面的。做 Smith 的分析表：场景起始页码／一句话标识场景／标 A、B、C 的竖列记各线 beat／**给广告前的最后一场画下划线**标出 act break。

**1 生点子** 从主角的情绪与目标出发问"What if"（"Dwight 和 Jim 互相痛恨——如果他们出差必须同住一间呢？"）。**算数的是情绪而不是情境**。筛选时查 **lag time**（时事四个月后还成立吗）、别写名人客串、避开节日集。

**2 springboard（3–5 句）** 前一两句给 hook，后几句暗示好笑的 complications；**不一定给结尾**（"想听结尾，可以付钱让你写"）；而且**必须用好笑的措辞写**。判断：几行说不清本质，概念就太浑浊了——而且浑浊的概念不会自己变清楚。

**3 beat sheet（一页）** 按 4.1 的 beat 数生成；多线先各自列再编织。自检：它 build 吗？逻辑通吗？好笑吗？有意外吗？

**4 在 premise 层补喜剧** 对着 beat sheet 问：这是哪一种（或哪几种复合的）predicament？character mix 在哪一拍被搅动？style of comedy 与该剧一致吗？**答不出来就不要往下写。**

**5 outline（5–7 页单倍行距，或按剧组习惯 8–12 页双倍）** **"An outline is a selling tool."** 每个细节都问"读者非知道不可才能跟上故事吗？"答否就删——**新手标志是急于教育读者**。排入 broadcast format，把重要 plot point 挪到 break 之前。两三页内至少一条线钩住读者；每场描述简短且**含会看到的笑点**；**Play It, Don't Say It**；"这里会很好笑"不算数；对白片段极短且必须极好（别把笑话都用掉）。
Matt Williams 的警告当体检标准：**十次有九次，outline 是在 2/3 处崩掉的**——会 set up、会 complicate，到 2/3 不知道这集是关于什么。所以**写完 outline 先翻到 2/3 处问"这一集是关于什么"**。

**6 初稿（30 页约 1–2 周）** 第一天不要雕第一页——"Blair through the script"，一天写两三场甚至整个第一幕。**大改前退回重做 beat sheet 和 outline**。写完第一件事是**用红笔数笑点**。

**7 改稿（优先级不可颠倒）** **story → sequences → scenes → moments → dialogue，每一级都盯 comedy**；顺序反了就是"a bad patch job"。听反馈时**别说话**——要为一个创作决定辩解，它大概就需要再看一遍。处理 notes：**vague note 通常指错了地方**（"地下室那场不好笑"的真问题可能在三场前没建立困境）；交回来的东西必须反映房间里谈的；**二稿最大的罪是懒**。
freelance 各阶段交付时间表（口头 pitch／outline／改 outline／一稿／二稿）见 [reference.md](reference.md) §五。

---

## 十四、训练

1. **数笑点**：取一集真剧本，逐页圈实笑点、算出密度，并标出每个属于哪一类（setup-punchline／topper／running gag／take／stage business／visual／sound）。再对自己的稿子做一遍。
2. **改 setup**：挑三个最弱的 punchline，**不改 punchline，只改 setup**，看能不能各长出六个新 punchline。
7. **装置测试**：任何非常规叙事装置，先用手机拍五分钟自演片段，确认"它成立"再开工。
10. **punch-up 模拟**：对别人的一场戏写 10–20 条 alts，再自己筛到 5–10 条；被筛掉的进你的 candy bag。
