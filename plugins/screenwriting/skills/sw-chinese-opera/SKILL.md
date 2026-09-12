---
name: sw-chinese-opera
description: Chinese opera (戏曲 / 京剧 / 豫剧 / 越剧 / 昆曲 / 沪剧 / 小戏) playwriting, the stage-opera layer of the pack — currently the lyric-writing method (唱词) from Lu Jun with worked examples (choose the rhyme 韵辙 from the character and from the key line first, wide vs narrow rhymes 宽韵/险韵, same-word rhyme 同字韵, vary the line pattern instead of uniform seven- and ten-character lines, place sung passages in the heavy scenes 重场戏 rather than scattering them), plus a medium-boundary table saying which general skills apply to an opera script and which do not (起承转合 and the eight openings yes; BS2, spec format and enter-late-leave-early no). Use when writing or revising 戏曲 唱词, choosing a rhyme for a character or a passage, deciding where a sung passage belongs, or when the project is a Chinese-opera script and the general dramaturgy skills need a boundary drawn before they are applied.
---

# 戏曲编剧（Chinese Opera Playwriting）

> **输出语言＝提问语言**；术语一律锚回原词，见 [sw-workflow/terms.md](../sw-workflow/terms.md)，不自创译名。戏曲术语（韵辙、板式、行当、程式、宾白）没有英文对应物，任何语言下保留原词加一句释义。

本 skill 是这套 skill 的**舞台层**里戏曲那一格。它现在只装了陆军的唱词方法（从 `sw-dialogue` 搬来，那里不该有它），再加一张媒介边界表。板式、剧种韵辙、跨剧种的结构方法与大师语料还没进来，缺口在第一节列得很清楚——**description 只承诺已有的部分**，缺的不会因为写在这里就被触发。

唱词范例见 [reference.md](reference.md)。

---

## 〇、媒介边界：通用层哪些能用在戏曲上，哪些不能

戏曲项目照样先走 `sw-workflow`，但通用 skill 进来之前要按这张表取舍：

| 通用 skill 的哪一层 | 能不能用在戏曲上 |
|---|---|
| `sw-story-structure` 第六节：**起承转合、八种开头、找核＋加减乘除、高潮四病、结尾八法、变化要多** | **能，而且是首选**。陆军这一节本来就是从小戏与戏曲经验里写出来的，例证多半是戏曲（《包公赔情》《阿二接妻》《打铜锣》） |
| `sw-story-structure` 的 BS2 十五节拍、演示板 40 卡、页码表 | **不能**。页码锚点是 110 页电影的产物；戏曲按折／出与唱段切分，不按页 |
| `sw-premise-theme`：前提、主控思想、戏核 | **能**，直接可用。「戏核要好」本来就是陆军提法 |
| `sw-character-conflict`：三维人物、对立统一、对手 | **能**，但**行当**（生旦净丑）会先于三维决定一个角色怎么写，这一层本 skill 尚未收录，见第一节缺口 |
| `sw-dialogue` 第六节：**语言要美、典雅美／本色美、对话三要求** | **能**，用于**宾白**。「戏曲唱词的本色美应更胜于典雅美」那句就是为戏曲写的 |
| `sw-dialogue` 的美式禁忌（不用括注、不写小对话、遮名可辨） | **部分能**。遮名可辨对唱词同样成立；「不用括注」不适用，戏曲本子里的科介是正文 |
| `sw-scene-craft`：进出、价值转折、道具 | **能**，但**晚进早出不适用**——戏曲的自报家门、定场诗是程式，不是可删的铺垫 |
| `sw-format-adaptation` 的三种体例（spec／场号制／柱・ト書き） | **不能**。戏曲剧本体例（唱／白／科介的排法、曲牌或板式标记）本 skill 尚未收录 |
| 剧集层七个 skill | **不能**。戏曲连台本戏与剧集的「引擎」是两回事，不要套 |

**一句话**：陆军能用，页码不能用，程式不是铺垫。

---

## 一、本 skill 的覆盖范围与缺口

**已有**（第二节，来源陆军《编剧理论与技法》）：唱词的选韵、句式、布局三条规则，配 reference 里六组范例。

**缺口**（按补入顺序）：

1. **跨剧种的结构方法**：一人一事（李渔《闲情偶寄·词曲部》）、折／出的单位、行当决定写法、程式（自报家门、定场诗、下场诗、背供）、唱念做打的分配。来源：翁偶虹《翁偶虹编剧生涯》、范钧宏《戏曲编剧技巧浅论》、李渔。
2. **剧种附录**（放 reference，一剧种一节，是表格不是方法论）：京剧十三辙与西皮二黄各板式（导板／慢板／原板／快板／散板）要几字句、配什么情绪；豫剧中州韵与慢板／二八板／流水板／飞板；越剧、昆曲另议。
3. **剧本体例**：唱／白／科介如何排、板式或曲牌怎么标，补进 `sw-format-adaptation` 或本 skill。
4. **大师语料**（对标 `chekhov-dramaturgy` 的做法，全本逐折拆）：翁偶虹《锁麟囊》、陈亚先《曹操与杨修》、杨兰春《朝阳沟》。

缺口补进来之前，遇到板式、行当、程式的问题**直说没有**，不要用通用层的东西硬凑。

---

## 二、唱词三好（陆军）

- **韵选好**：根据人物性格定韵（泼辣的李玉桃"交消"韵"回来了回来了我队长娘子李玉桃"；热心的蹄膀娘"江阳"韵；体弱温和的小艾"衣溪"韵）；根据重点句定韵（先写闪光的重点唱句——体现主题/描写心情/揭示关系变化——再由它定韵：《竹园曲》"你一个'狠'字随风过"定"乌乎"韵，铺开"廿年"排比"我为谁付出廿年血和泪"）；宽韵（人辰江阳言前，字多易写易雷同）与险韵（也斜发花，字少但贴切则耳目一新：《一夜生死恋》"癞蛤蟆……十人见了九摇头"倒数）；**同字韵**的魅力（几十个"手"、近百个"人"、"你""我"：洪医生"骗你其实是爱护你……一辈子没有一个安宁的你"）。
- **结构编织好**：忌一律七字十字；借用不同曲牌句式（"阴阳血"问答、"赋子板"叙事）；随环境与演出样式变（抬轿舞的三重唱合唱旁唱对唱）；回文可表回肠之情（"闷无心我负人，人负我心无闷"）——句式曲格力避呆板划一。
- **布局好**：忌"当唱不唱、不当唱偏唱""东唱一段西唱一段鸡零狗碎"；精心设计重点场面（男女主人公情感抒发、冲突激烈、命运转折的关键时刻）成整块音乐场面，历代流传唱段都从重场戏中凸现。

**与宾白的分工**：宾白走 `sw-dialogue` 的对话三要求（动作性／性格化／潜台词）；唱词承担抒情与转折，所以布局规则的实质是**把唱段留给价值转折最大的那一场**，这一点与 `sw-scene-craft` 的价值转折是同一件事的两种写法。

---

## 三、诊断清单

1. 这段唱的韵是从人物性格定的，还是顺手押的？换一个性格相反的人物来唱，韵该不该变？
2. 重点句先有了吗？韵是重点句定的，还是重点句迁就了韵？
3. 数句式：是不是一律七字或十字？有没有借曲牌句式、问答、回文打破？
4. 唱段落在重场戏上吗？把全剧唱段列出来，最长的一段是不是在价值转折最大的一场？
5. 有没有"当唱不唱"——冲突顶点用宾白滑过去了；有没有"不当唱偏唱"——过场戏也来一段？
6. 用了险韵的地方，贴切吗？不贴切就退回宽韵。

---

## 四、工作流程

1. 先按 `sw-workflow` 入口路径「短片 / 小戏 / 独幕剧」那一行走通用阶段：戏核（`sw-premise-theme` 第十节）→ 起承转合与八种开头（`sw-story-structure` 第六节）→ 人物。
2. 列全剧场次，标出价值转折最大的两三场，**唱段只分配给它们**。
3. 每个唱段先写重点句，由重点句定韵，再铺开。
4. 宾白按 `sw-dialogue` 对话三要求写，唱词按第二节写；跑第三节诊断清单。
5. 板式、行当、体例的问题，在第一节缺口补入之前，明确告知用户本 skill 尚未覆盖。
