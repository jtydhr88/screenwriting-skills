# screenwriting-skills

[中文版](README_ZH.md)

14 unique Claude Code skills for screenwriting and dramaturgy, shipped in two plugins, `screenwriting` with Chinese skill bodies and `screenwriting-en` with English skill bodies. The 26 source entries comprise 24 craft books plus Chekhov's collected plays and Ozu Yasujiro's collected screenplays.

In `screenwriting` the skill bodies are Chinese (the sources and quotations are Chinese translations). In `screenwriting-en` the bodies are English translations of the Chinese files, which stay the source of truth. Frontmatter descriptions are English with Chinese keywords in both plugins, so both languages trigger them.

## Install

```
/plugin marketplace add jtydhr88/screenwriting-skills
/plugin install screenwriting@screenwriting-skills
```

## English edition

```
/plugin install screenwriting-en@screenwriting-skills
```

The `screenwriting-en` plugin carries the same 14 skills with English skill bodies, invoked as `/screenwriting-en:<skill>`. Each file is a translation of its Chinese source with the same headings, tables, and links.

| Skill | English edition | Chinese edition | Files |
|---|---|---|---|
| `sw-workflow` | Workflow & Story Bible | 剧本项目主线调度 | `SKILL.md`, `reference.md` |
| `sw-story-structure` | Story Structure | 故事结构 | `SKILL.md`, `reference.md` |
| `sw-premise-theme` | Premise & Theme | 前提·主题·立意·戏核 | `SKILL.md`, `reference.md` |
| `sw-character-conflict` | Character & Conflict | 人物与冲突 | `SKILL.md`, `reference.md` |
| `sw-dialogue` | Dialogue | 对白 | `SKILL.md`, `reference.md` |
| `sw-scene-craft` | Scene Craft | 场景与段落 | `SKILL.md`, `reference.md` |
| `sw-format-adaptation` | Format, Process & Adaptation | 格式·流程·改编 | `SKILL.md`, `reference.md` |
| `sw-american-case-studies` | American Case Studies | 美国电影剧作案例 | `SKILL.md`, `reference.md` |
| `sw-japanese-screenwriting` | Japanese Screenwriting Methods | 日本编剧方法 | `SKILL.md`, `reference.md` |
| `sw-korean-french-screenwriting` | Korean & French Screenwriting Practice | 韩国与法国编剧方法 | `SKILL.md` |
| `sw-industry-business` | Industry & Business | 行业与生意经 | `SKILL.md`, `reference.md` |
| `chekhov-dramaturgy` | Chekhov Dramaturgy | 契诃夫戏剧法 | `SKILL.md`, `reference.md` |
| `ozu-screenplay-style` | Ozu Screenplay Style | 小津安二郎剧本写法 | `SKILL.md`, `reference.md` |
| `sw-series-showrunning` | Series design | 剧集设计 | `SKILL.md`, `reference.md` |

## Skills

| Skill | What it covers | Main sources |
|---|---|---|
| `sw-workflow` | Project orchestrator: stage map (premise → structure → character → scenes → draft → revision → submission) naming which skill to call, per-stage deliverables and advisory exit checks, entry paths (from scratch / existing draft / adaptation / short form / series), and a `story-bible.md` convention that keeps all project state in one file so work resumes across sessions | (meta-skill, no new sources; see issue #1) |
| `sw-story-structure` | Paradigm & plot points, Save the Cat beats and board, McKee's event/scene/sequence/act, inciting incident, progressive complications, crisis-climax-resolution, subplots, Hoxter's nine beats, Hicks' attraction/anticipation/satisfaction, Lu Jun's 起承转合, eight openings, eight endings | Field, Snyder, McKee *Story*, Hoxter, Hicks, Lu Jun; Yorke |
| `sw-premise-theme` | Premise as tyrant, controlling idea (value + cause), the "third rail" (desire vs misbelief), five premise questions, logline tests, 选材/开掘/视角/戏核/冲突要真/情节要奇 | Egri, McKee, Cron, Hicks, Hoxter, Snyder, Lu Jun; Rabkin |
| `sw-character-conflict` | Three-dimensional character, orchestration, unity of opposites, pivotal character, rising vs static vs jumping conflict, transition; Freud/Erikson/Jung/Campbell/Murdock/Adler/May for motive; 人物要活八要, 对手要强, 给对手一把刀 | Egri, Indick, McKee, Hicks, Cron, Snyder, Lu Jun; Yorke, Rabkin |
| `sw-dialogue` | Dialogue as action, said/unsaid/unsayable, exposition as ammunition, beats as gerunds, credibility/language/content/design flaws, character-specific vocabulary, seven scene analyses; 语言要美 (典雅/通俗, 动作性/性格化/潜台词, 戏曲唱词三好) | McKee *Dialogue*, Walter, Hicks, Lu Jun, Egri, Snyder, Mei Feng; Davies & Cook |
| `sw-scene-craft` | Scene as value turn, five-step scene analysis, enter late leave early, pacing and transitions, action over talk, alternative locations; 意趣要足 (suspense, delay, wit), 细节要妙, 道具要精, 场景要当 | McKee, Field, Hicks, Walter, Henson, Hoxter, Mei Feng, Lu Jun; Curry, Davies & Cook |
| `sw-format-adaptation` | Spec format hard rules, exact typographic grid, element conventions (V.O./O.S., MORE/CONT'D, dual dialogue, montage), Fountain output contract with forced markers for Chinese and PDF/.fdx render paths, Chinese 场号制 and Japanese 柱・ト書き formats, action-paragraph craft, drafts and outlines (step outline → treatment → script), revision, adaptation principles | Henson, Walter, Hicks, Field, McKee, Hoxter, Diamond & Weissman, Bork; typographic grid, Fountain and Asian formats are industry conventions (issue #2), not from the books; Grace |
| `sw-american-case-studies` | Worked examples: Westerns, screwball, Wilder, Hitchcock, *Adaptation*, *Mildred Pierce*, *Thelma & Louise*, *Fargo*, *Good Will Hunting*, *American Beauty*, *Eternal Sunshine*, *American Graffiti*, Bourne, Guardians, Zootopia, Thor | Mei Feng, Walter, masterclass, Hoxter, Snyder, Field |
| `sw-japanese-screenwriting` | Ten Japanese directors/writers: structure-first vs fragment-first methods, small-material notebooks, "if + moreover", character = actor + flaw, tsukkomi systems, theme-emerges-later, originals born from constraints; Arai Haruhiko | 泊贵洋 ed., masterclass (international) |
| `sw-korean-french-screenwriting` | Korean and French methods from the international masterclass: Oh Seung-uk (write the emotion, research before writing, structure as space, find your own angle), Choi Seok-hwan (genre as a promise, make the audience wait, two reversals, desire and crisis), Obitan (French system, write dialogue last, viewpoint and hidden motive, writer on set, collective writing) | masterclass (international) |
| `sw-industry-business` | Buyer's-eye workflow, PROBLEM idea test, logline/query/pitch, agents, options, credits, WGA, gross vs net, notes and rewrites, film vs TV, Oscar logic, career resilience | Diamond & Weissman, Bork, Hicks, Walter, Henson, Snyder, Hoxter, Mei Feng, masterclass; Douglas, Landau, Grace, Curry, Davies & Cook |
| `chekhov-dramaturgy` | Chekhov's seven full-length plays and one-acts as a working method: structure, character, dialogue, sound and stage directions, revision (Wood Demon → Uncle Vanya), with act-by-act tables and excerpts | 契诃夫戏剧全集 (焦菊隐/童道明/李健吾译) |
| `ozu-screenplay-style` | Ozu Yasujiro's six screenplays as a working method: shared skeleton, marriage-of-a-daughter structure, dialogue register, format, theme sentences, with scene tables and excerpts | 小津安二郎剧本集 |
| `sw-series-showrunning` | Series engines, pilots, season arcs, episode act grids, A/B/C stories, continuing serial storylines, and continuity; general craft and production methods link to the existing skills | Rabkin, Douglas, Landau, Grace, Curry, Yorke |

Each skill has a `SKILL.md` (principles, checklists, workflow) and most have a `reference.md` (tables, worked analyses, excerpts).

## Source books and collections (26)

- 悉德·菲尔德《电影剧本写作基础》
- 布莱克·斯奈德《救猫咪》
- 罗伯特·麦基《故事》
- 罗伯特·麦基《对白》
- 朱利安·霍克斯特《编剧的十二条法则》
- 尼尔·D·希克斯《编剧的核心技巧》
- 拉约什·埃格里《编剧的艺术》
- 莉萨·克龙《怎样写故事》
- 威廉·尹迪克《编剧心理学》
- 理查德·沃尔特《剧本》
- 温迪·简·汉森《编剧：步步为营》
- 戴蒙德 & 韦斯曼《好莱坞编剧的生意经》
- 埃里克·博克《如何写出好故事：HBO 大师写作课》
- 梅峰《编剧的自修课：解读美国电影剧作》
- 刘大鹏编《故事创作大师班（国际卷）》
- 陆军《编剧理论与技法：从小型戏剧的文本写作切入》
- 泊贵洋编《从零开始做编剧：10 位日本金牌导演、编剧谈剧本》
- 《契诃夫戏剧全集》
- 《小津安二郎剧本集》
- John Yorke, *Into the Woods: A Five-Act Journey Into Story*
- William Rabkin, *Writing the Pilot: Creating the Series*
- Pamela Douglas, *Writing the TV Drama Series*, third edition
- Neil Landau, *The TV Showrunner's Roadmap: 21 Navigational Tips for Screenwriters to Create and Sustain a Hit TV Series*
- Yvonne Grace, *Writing for Television: Series, Serials and Soaps*
- Chris Curry, *Writing for Soaps*
- Russell T Davies and Benjamin Cook, *Doctor Who: The Writer's Tale: The Final Chapter*

## Conventions

- `SKILL.md` frontmatter: `name` (kebab-case, matches folder) and a long English `description` ending in "Use when …", with Chinese keywords in parentheses for triggering.
- Skill bodies are Chinese; numbered principles, tables and checklists; cross-references between skills by folder name.
- `reference.md` holds worked examples and quotations so `SKILL.md` stays under ~60 KB.
- License: for personal study use. Quotations remain the property of their authors and translators.

Sister project, same idea applied to Japanese composition and arranging: [japanese-composition-skills](https://github.com/jtydhr88/japanese-composition-skills).
