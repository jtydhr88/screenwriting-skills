# screenwriting-skills（编剧技能集）

[English](README.md)

把 32 本编剧/剧作理论书籍与 12 卷出版剧本（中、美、英、日、韩）提炼成的 20 个 Claude Code skill，覆盖电影长片、电视剧集、舞台剧。

skill 正文用中文（来源多为中文原著或中译本），frontmatter 的 description 用英文并附中文关键词，中英文提问都能触发。

## 安装

```
/plugin marketplace add jtydhr88/screenwriting-skills
/plugin install screenwriting@screenwriting-skills
```

## 英文版

```
/plugin install screenwriting-en@screenwriting-skills
```

`screenwriting-en` 插件收录全部 20 个 skill，正文为英文，用 `/screenwriting-en:<skill>` 调用。skill 正文就是 agent 实际执行的指令集；英文版的意义在于让看不懂中文的读者能够审查并学习 agent 到底在跑什么。中文文件仍是唯一真源，英文文件是它的译本。两个版本装一个即可，不要同时安装。

## 四层结构

写长片用第 1、3、4 层；写剧集要用全部四层——剧集层不是加在通用层旁边，而是用"引擎＋季"替换掉"为一部电影设计的结构"。

```
1. 通用剧作层   前提 · 结构 · 人物 · 对白 · 场景 · 格式 · 项目调度
2. 剧集层       单集与季结构 · 引擎与 bible · 编剧室 · 半小时喜剧
3. 传统与行业层 美国 · 日本 · 韩法 · 中国大陆 · 行业生意
4. 大师语料层   契诃夫 · 小津 · 继承之战 · 剧集案例库
```

### 第 1 层 通用剧作层（媒介无关）

| 技能 | 内容 | 主要来源 |
|---|---|---|
| `sw-workflow` 主线调度与状态存档 | 长片/舞台剧阶段图（前提→结构→人物→场景→初稿→修改→提交）**与独立的剧集阶段表（S0–S7：引擎→人物网与季弧→文档→pilot 结构→破故事→初稿→提交）**，指明每阶段调用哪个 skill、交付什么、建议通过标准；`story-bible.md` 约定（含剧集补充节）把全部项目状态存在一个文件里，跨会话续写 | 调度用元技能，无新来源 |
| `sw-story-structure` 故事结构 | 范式与情节点、BS2 十五节拍与演示板、麦基结构层级/激励事件/进展纠葛/危机高潮结局/次情节、九节拍、吸引力/预期/满意、起承转合、开头八法、结尾八法 | 菲尔德、斯奈德、麦基《故事》、霍克斯特、希克斯、陆军 |
| `sw-premise-theme` 前提与主题 | 前提是暴君、主控思想＝价值＋原因、第三条轨道（渴望 vs 错误信念）、前提五问、一句话故事与 logline、选材/开掘/视角/戏核 | 埃格里、麦基、克龙、希克斯、霍克斯特、斯奈德、陆军 |
| `sw-character-conflict` 人物与冲突 | 三维人物、编排、对立统一、主使人物、静止/跳跃/升级冲突与过渡；弗洛伊德/荣格/坎贝尔/阿德勒等动机工具箱；人物要活八要、对手要强、给对手一把刀 | 埃格里、尹迪克、麦基、希克斯、克龙、斯奈德、陆军 |
| `sw-dialogue` 对白 | 对白是行动、已说/未说/不能说、解说当弹药、动名词节拍、四类瑕疵、角色专属词汇；语言要美、戏曲唱词三好 | 麦基《对白》、沃尔特、希克斯、陆军、埃格里、斯奈德、梅峰 |
| `sw-scene-craft` 场景与段落 | 场景＝价值转折、五步场景分析、晚进早出、节奏与过渡、动作优于对白；意趣要足、细节要妙、道具要精 | 麦基、菲尔德、希克斯、沃尔特、汉森、霍克斯特、梅峰、陆军 |
| `sw-format-adaptation` 格式·流程·改编 | 推销剧本格式硬规则、版面规格表、元素级约定、Fountain 输出契约（含中文强制记号）、中文场号制与日式柱・ト書き、大纲→处理台本→草稿链、修改、改编原则 | 汉森、沃尔特、希克斯、菲尔德、麦基、霍克斯特、戴蒙德&韦斯曼、博克；版面规格与 Fountain 为行业通行做法 |

### 第 2 层 剧集层（电影编剧书不教的部分）

| 技能 | 内容 | 主要来源 |
|---|---|---|
| `sw-series-structure` 单集与季结构 | teaser 与 cold open；广播网四/五/六幕格子与页码锚点（17–18 / 30 / 45 / 60）；付费台与流媒体剧本**隐形幕的三重判据**；出幕与悬念结局类型学；奥贝格的信息管理四工具（mystery / surprise / dramatic irony / suspense）；A/B/C 线与 runner 的编织与场数配比；卡尔维西的 pilot 节拍表（带分钟刻度）；场结构五件套；季形（tentpole、movement、瓶子集与容器集、双集、季终与剧终） | 卡尔维西、道格拉斯（英文三版＋中译二版）、奥贝格、兰道一/二版、戈德堡&拉布金、米勒、拉布金、布鲁姆，以及从《白宫风云》《继承之战》《黑道家族》《唐顿庄园》《伦敦生活》剧本实测的结构表 |
| `sw-series-engine-bible` 引擎与 bible | 系列引擎 / franchise（拉布金四元素、兰道 tacit contract、布鲁姆三问、一百集检验与"再说三集"检验）；故事模式与潜台词地雷；能持续生产冲突的人物网；pilot 类型（premise / 典型集 / 混合）与三种收法；剧集类型学与 story-type；以及全部推销文档——logline、跳板、pitch document、series format、treatment、bible 三档，外加一份故事线文档骨架 | 拉布金、兰道一/二版、奥贝格、道格拉斯、戈德堡&拉布金、布鲁姆、米勒、卡尔维西、史密斯；引擎拆解取自《黑道家族》《伦敦生活》《继承之战》 |
| `sw-writers-room` 编剧室与制作现实 | showrunner 的职责与否决权；破故事（蔡斯的 35 拍与剪刀胶带、威尔斯的十把椅子、道格拉斯的格子、马扎拉的无大纲法）；文档链与各自的页数预算；单集六周与初稿十四天法；spec 剧本与向既有剧 pitch 单集；接 note 与给 note；职级阶梯与阶段交易；制作限制作为创作触发；单一作者的替代方案 | 戈德堡&拉布金、道格拉斯、兰道一/二版访谈、史密斯、布鲁姆（标时效），以及蔡斯、阿姆斯特朗、普雷布尔、索尔金、费罗斯、沃勒-布里奇的一手自述 |
| `sw-sitcom-comedy` 半小时喜剧 | 半小时喜剧是"整体切换"：前提驱动的三层喜剧法、九种困境、六种人物配比、笑点力学（两段式 setup、punch word 置尾、topper、running gag、十种喜剧微调、每页 2–4 个笑点）、cold open/幕/tag、多机位与单机位与动画三套格式与页数、直接对镜作为季弧装置、dramedy | 埃文·史密斯、沃勒-布里奇《伦敦生活》、兰道、布鲁姆、道格拉斯（dramedy）、米勒 |

### 第 3 层 传统与行业层

| 技能 | 内容 | 主要来源 |
|---|---|---|
| `sw-american-case-studies` 美国案例 | 西部片、神经喜剧、怀尔德、希区柯克、《改编剧本》《米尔德丽德·皮尔斯》《塞尔玛与路易丝》《法尔戈》《心灵捕手》《美国美人》《纯洁心灵的永恒阳光》、伯恩、疯狂动物城 | 梅峰、沃尔特、大师班、霍克斯特、斯奈德、菲尔德 |
| `sw-japanese-screenwriting` 日本编剧方法 | 十位日本导演编剧：结构优先 vs 片段优先、小素材笔记、"如果＋而且"、人物＝演员＋缺点、主题后置 | 泊贵洋编、大师班国际卷 |
| `sw-korean-french-screenwriting` 韩国与法国方法 | 把情绪描绘出来、先探访后写作、忠于类型是对观众的承诺、两个反转、对话放最后写、集体创作 | 大师班国际卷 |
| `sw-chinese-series-practice` 国产剧体系与制片链 | 类型学与时长硬约束；文档链（创意→梗概→人物小传→分集大纲→分场大纲→剧本）及各自字数；四种并存的中文剧本格式；每集收口的悬念法则与四级悬念；小说/IP 改成 30–50 集长剧（卖点迁移、复制-删除-改编）；反方向的片段改编；制片链（立项/备案/两道审查、交付节点、编剧合同、内容红线）；中英术语字典 | 姚扣根、张巍、张明智&宋培义、赵彬彬，以及道格拉斯与布鲁姆的中译本 |
| `sw-industry-business` 行业与生意经 | 买家视角流程、PROBLEM 七要素、一句话/询问信/推销、经纪人、期权、署名、WGA、毛利 vs 净利、电影 vs 电视、职业心态 | 戴蒙德&韦斯曼、博克、希克斯、沃尔特、汉森、斯奈德、霍克斯特、梅峰、大师班 |

### 第 4 层 大师语料层（完整一手文本，逐幕逐集拆过）

| 技能 | 内容 | 主要来源 |
|---|---|---|
| `chekhov-dramaturgy` 契诃夫戏剧法 | 七部多幕剧与独幕剧作为写作方法：无中心高潮的四幕情绪结构、事件画外、三层结尾、《林妖》→《万尼亚舅舅》的改写，附逐幕结构表与原文范例 | 《契诃夫戏剧全集》（焦菊隐/童道明/李健吾译） |
| `ozu-screenplay-style` 小津剧本风格 | 六部剧本作为写作方法：共同骨架、嫁女结构、对白语气、格式、主题句，附逐场结构表 | 《小津安二郎剧本集》 |
| `succession-series-writing` 继承之战群像剧写法 | 四季 39 集拍摄稿作为流媒体群像剧的写作方法：隐形幕判据、用仪式程序搭容器集、压力舱、每集一个核心问题、羞辱向下传导、舞台指示承担潜台词与 maybe、一个单词完成反转、写长、alts、mega-chart，以及引擎失压后如何工程化一个结局 | Jesse Armstrong《Succession: The Complete Scripts》I–IV（Faber），含 Frank Rich 与 Lucy Prebble 的文章 |
| `sw-series-case-studies` 剧集案例库 | 一手剧本的逐集拆解：索尔金六集《白宫风云》（幕页码表、八种出幕）、蔡斯五集《黑道家族》、费罗斯带注的《唐顿庄园》第二季（19 条线、419 条作者脚注）、《伦敦生活》剧本集、卡尔维西八个 pilot 的逐分钟节拍表、兰道 47 部剧结构总表、米勒的《汉尼拔》与《金牌律师》场拆解、戈德堡&拉布金的 beat sheet、坂元裕二与卢熙京 | 上述出版剧本与各书的案例章 |

每个 skill 有 `SKILL.md`（原理、清单、工作流程），除一个之外都另有 `reference.md`（表格、逐集分析、原文引文）。有三个 skill 的表格分成多个文件，保证每个都能一次读完：`sw-series-case-studies` 分为 `reference.md`（四部英语剧本集）、`reference-pilots.md`（方法书里的 pilot 节拍表与结构总表）、`reference-asia.md`（日韩两部文本）；`sw-series-engine-bible` 分为引擎拆解、文档模板字段表、填好的样例三册；`sw-chinese-series-practice` 分为实务册、格式与策划样本册、张巍六案例册、片段索引与内容红线册。

## 来源书目

**编剧理论（17 本）**：悉德·菲尔德《电影剧本写作基础》；布莱克·斯奈德《救猫咪》；罗伯特·麦基《故事》《对白》；朱利安·霍克斯特《编剧的十二条法则》；尼尔·D·希克斯《编剧的核心技巧》；拉约什·埃格里《编剧的艺术》；莉萨·克龙《怎样写故事》；威廉·尹迪克《编剧心理学》；理查德·沃尔特《剧本》；温迪·简·汉森《编剧：步步为营》；戴蒙德&韦斯曼《好莱坞编剧的生意经》；埃里克·博克《如何写出好故事：HBO 大师写作课》；梅峰《编剧的自修课》；刘大鹏编《故事创作大师班（国际卷）》；陆军《编剧理论与技法》；泊贵洋编《从零开始做编剧》。

**电视剧编剧（15 本）**：William Rabkin《Writing the Pilot: Creating the Series》；Daniel Calvisi《Story Maps: TV Drama》；Pamela Douglas《Writing the TV Drama Series》（英文第三版）与其中译《美剧编剧入门》（第二版）；Kam Miller《The Hero Succeeds》；Emmanuel Oberg《Writing a Successful TV Series》；Lee Goldberg & William Rabkin《Successful Television Writing》；Neil Landau《The TV Showrunner's Roadmap》（2014 年 21 条版）与（2022 年第二版）；Evan S. Smith《Writing Television Sitcoms》；理查德·A·布鲁姆《电视与银幕写作》；姚扣根《电视剧写作概论》；张巍等《电视剧改编教程》；张明智、宋培义主编《电视剧出品人与制片人教程》；赵彬彬主编《影视剧片段改编教程》。

**出版剧本（12 卷）**：《契诃夫戏剧全集》；《小津安二郎剧本集》；Jesse Armstrong《Succession: The Complete Scripts》第一至第四季；Aaron Sorkin《The West Wing Script Book》；David Chase 等《The Sopranos: Selected Scripts from Three Seasons》；Julian Fellowes《Downton Abbey: The Complete Scripts, Season Two》；Phoebe Waller-Bridge《Fleabag: The Scriptures》；坂元裕二《花束般的恋爱》剧本；卢熙京《世间最美丽的离别》。

## 约定

- frontmatter：`name` 与文件夹同名（kebab-case）；`description` 英文长句以 "Use when …" 收尾，括号内附中文关键词。
- 正文中文，编号原则、表格、清单；skill 之间用文件夹名互相引用。
- 来源之间有分歧时并列保留，并注明什么情况用哪个——例如道格拉斯的四幕格子对奥贝格的"幕断只是香肠的尺寸"，主题预设派对主题涌现派。
- 行业事实一律带来源年份（费率、平台格局、幕数变得很快）；国产剧政策数据标注 2014/2016。
- `reference.md` 承载范例与引文，使 `SKILL.md` 保持在约 40 KB 以内。
- 仅供个人学习使用；引文版权归原作者与译者。

同一思路做的另一套 skill（日本作曲编曲）：[japanese-composition-skills](https://github.com/jtydhr88/japanese-composition-skills)。
