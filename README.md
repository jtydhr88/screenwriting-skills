# screenwriting-skills

[中文版](README_ZH.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Français](README_FR.md)

25 agent skills (for [Claude Code](https://docs.anthropic.com/en/docs/claude-code/skills) and [OpenAI Codex](https://developers.openai.com/codex/build-skills)) for screenwriting, television writing and dramaturgy, distilled from 46 craft books and 23 volumes of published scripts, scores and plays (Chinese, American, British, Japanese and Korean).

The `SKILL.md` files follow the open [agentskills.io](https://agentskills.io) standard and are shared by both agents: install once and it works in both.

**Ask in your own language.** The skill bodies are written in Chinese, because most of the sources are Chinese originals or Chinese translations. That is only where the text lives: ask in English, Japanese, Korean or French and you get the answer in that language. See [Multilingual support](#multilingual-support) for why there is a single source tree.

## Install

### Claude Code

#### Plugin marketplace (recommended)

```
/plugin marketplace add jtydhr88/screenwriting-skills
/plugin install screenwriting@screenwriting-skills
```

Skills are then invoked as `/screenwriting:<skill>`, e.g. `/screenwriting:sw-dialogue`.

#### Personal (all projects)

```bash
git clone https://github.com/jtydhr88/screenwriting-skills.git
cp -r screenwriting-skills/plugins/screenwriting/skills/* ~/.claude/skills/
```

#### Project-specific

```bash
mkdir -p .claude/skills
cp -r screenwriting-skills/plugins/screenwriting/skills/* .claude/skills/
```

#### Verify

Skills load automatically when the agent detects relevant context. To list them: `/skills`.

### Codex (CLI / ChatGPT desktop app / IDE extension)

#### Plugin marketplace (recommended)

```bash
codex plugin marketplace add jtydhr88/screenwriting-skills

# Then, in the ChatGPT desktop app or Codex CLI:
# Plugins → select "Screenwriting Skills" → Install
```

The same 25 `SKILL.md` files are shipped through the plugin's `skills/` directory, with no duplication and no rewriting.

#### Personal skills (all projects)

```bash
git clone https://github.com/jtydhr88/screenwriting-skills.git
cp -r screenwriting-skills/plugins/screenwriting/skills/* ~/.agents/skills/
```

#### Project-specific

```bash
mkdir -p .agents/skills
cp -r screenwriting-skills/plugins/screenwriting/skills/* .agents/skills/
```

#### Verify

Run `/skills` to list available skills, or invoke one explicitly with `$sw-story-structure`.

## Usage examples

```
# "Break my 12-episode series into acts and place the act outs"
# → agent uses sw-series-structure

# "My dialogue is all on the nose, fix this scene"
# → agent uses sw-dialogue + sw-scene-craft

# "Turn this 400,000-word novel into a 40-episode Chinese drama outline"
# → agent uses sw-chinese-series-practice + sw-series-engine-bible

# "Set up a project and keep track of where I am"
# → agent uses sw-workflow
```

## Multilingual support

**One source tree, every language at runtime.** The skills are written once, in Chinese, and the agent delivers in whatever language you asked in.

This is a deliberate decision, and it was not the first one. There was an English edition once, a parallel `screenwriting-en` plugin with all 20 skills translated. It was proposed in [#3](https://github.com/jtydhr88/screenwriting-skills/issues/3), built, and merged. It has since been removed. The argument that killed it is the one that applies equally to every other language: if a reader who cannot read Chinese deserves a translated tree, so does a reader who cannot read English, and the next request is Japanese, then Korean, then French, then Russian. Five languages is 230 files that drift independently, with nothing to tell you which one is stale. The translation itself is cheap. The real cost is that forking once removes any principled ground for refusing the second fork.

So the line is drawn at the source, and the runtime does the rest:

- **Output language follows your question.** Ask in French, get French. No flag, no separate install.
- **Terminology is anchored to the original term.** The craft vocabulary of this field is originally English: *logline*, *act out*, *beat sheet*, *showrunner*, *staff writer*. The Chinese in the source books (计程绳, 出幕, 节拍表, 剧目管理人, 试用编剧) is the translation, and different translators chose differently. [`sw-workflow/terms.md`](plugins/screenwriting/skills/sw-workflow/terms.md) maps each concept back to its original term, so the agent restores the word and does not invent one. The same table serves all languages at once, because a Japanese or French screenwriter also says *act out* and *logline*.
- **Terms with no equivalent keep their original form plus a gloss.** 戏眼, 扣子, ト書き and 決定稿 come through as `戏眼 (xìyǎn — the one-line core attraction of an episode)`.
- **Your script stays in your script's language.** Discussing a Chinese screenplay in English is normal; the conversation switches language, the draft does not.

What this trades away is auditability: you cannot read the instruction file itself unless you read Chinese, only the agent's account of it. That is a real cost, and it is the one thing the deleted English edition genuinely bought. It was not worth a permanent five-way maintenance burden.

**READMEs are a different matter** and are translated, because they are short, stable, and the thing a newcomer meets first. The Japanese, Korean and French READMEs deliberately stop at install, structure and this policy; the full skill tables and the source bibliography live here and in the Chinese README, for exactly the reason above.

## How the skills are organised

Four layers. A feature project uses layers 1, 3 and 4; a series or stage project adds layer 2, because the medium layer replaces structure-for-film with the medium's own units.

```
1. General dramaturgy   premise · structure · character · dialogue · scene · format · Truby organic anatomy · project workflow
2. Medium layer         series · episode & season structure · engine & bible · writers' room · half-hour comedy
                        stage  · Chinese opera: banqiang and qupai methods, each with a full-script case library
3. Tradition & trade    America · Japan · Korea & France · mainland China · the business
4. Master corpora       Chekhov · Ozu · Succession · television case studies
```

### 1. General dramaturgy (medium-independent)

| Skill | What it covers | Main sources |
|---|---|---|
| `sw-workflow` | Project orchestrator: a feature/stage stage-map (premise → structure → character → scenes → draft → revision → submission) **and a separate series stage table (S0–S7: engine → character web & season arc → documents → pilot structure → break story → draft → submission)**, naming which skill to call at each stage, per-stage deliverables and advisory exit checks, plus a `story-bible.md` convention (with a series supplement) that keeps project state in one file across sessions | meta-skill, no new sources |
| `sw-story-structure` | Paradigm & plot points, Save the Cat beats and board, McKee's event/scene/sequence/act, inciting incident, progressive complications, crisis-climax-resolution, subplots, Hoxter's nine beats, Hicks' attraction/anticipation/satisfaction, Lu Jun's 起承转合, eight openings, eight endings | Field, Snyder, McKee *Story*, Hoxter, Hicks, Lu Jun |
| `sw-premise-theme` | Premise as tyrant, controlling idea (value + cause), the "third rail" (desire vs misbelief), five premise questions, logline tests, 选材/开掘/视角/戏核 | Egri, McKee, Cron, Hicks, Hoxter, Snyder, Lu Jun |
| `sw-character-conflict` | Three-dimensional character, orchestration, unity of opposites, pivotal character, rising vs static vs jumping conflict; Freud/Erikson/Jung/Campbell/Murdock/Adler/May for motive; 人物要活八要, 对手要强 | Egri, Indick, McKee, Hicks, Cron, Snyder, Lu Jun |
| `sw-dialogue` | Dialogue as action, said/unsaid/unsayable, exposition as ammunition, beats as gerunds, credibility/language/content/design flaws, character-specific vocabulary; 语言要美, 戏曲唱词三好 | McKee *Dialogue*, Walter, Hicks, Lu Jun, Egri, Snyder, Mei Feng |
| `sw-scene-craft` | Scene as value turn, five-step scene analysis, enter late leave early, pacing and transitions, action over talk; 意趣要足, 细节要妙, 道具要精 | McKee, Field, Hicks, Walter, Henson, Hoxter, Mei Feng, Lu Jun |
| `sw-format-adaptation` | Spec format hard rules, typographic grid, element conventions, Fountain output contract with forced markers for Chinese, 场号制 and Japanese 柱・ト書き formats, outline→treatment→script chain, revision, adaptation principles | Henson, Walter, Hicks, Field, McKee, Hoxter, Diamond & Weissman, Bork; grid/Fountain/Asian formats are industry conventions |
| `sw-truby-anatomy` | Organic story anatomy kept side by side with the Field/Snyder page maps, not replacing them: the designing principle (premise expanded into deep structure), the seven key steps and all twenty-two steps as the organic spine, the middle-act machinery the beat sheets lack (ghost, fake-ally opponent, plan, opponent's drive, ally's attack, fake defeat, three revelation-and-decision pairs, audience revelation, visit to death, moral decision), four-corner opposition, the moral-argument chain with the hero-opponent power-balance rule, scene weave with structure-step tags and storyline numbers, the accordion rule | John Truby, *The Anatomy of Story* |

### 2. Medium layer: what a feature does not teach

| Skill | What it covers | Main sources |
|---|---|---|
| `sw-series-structure` | Teasers and cold opens; broadcast four/five/six-act grids with page anchors (17–18 / 30 / 45 / 60); three tests for locating the **invisible acts** in pay-cable and streaming scripts; act-out and cliffhanger taxonomies; Oberg's four information tools (mystery / surprise / dramatic irony / suspense); A/B/C/runner weaving and scene-count ratios; the Calvisi pilot beat sheet with minute marks; five-part scene structure; season shape (tentpoles, movements, bottle and container episodes, two-parters, finales) | Calvisi, Douglas (EN 3e + 中译 2e), Oberg, Landau 1e/2e, Goldberg & Rabkin, Miller, Rabkin, Blum, plus measured tables from the West Wing / Succession / Sopranos / Downton / Fleabag scripts |
| `sw-series-engine-bible` | Series engine / franchise (Rabkin's four elements, Landau's tacit contract, Blum's three tests, the 100-episode and "name three more episodes" tests); story pattern and story landmines; character webs that keep generating conflict; pilot types (premise / typical-episode / hybrid) and three endings; series types and story-types; and every selling document: logline, springboard, pitch document, series format, treatment, bible tiers, plus a storyline-document skeleton | Rabkin, Landau 1e/2e, Oberg, Douglas, Goldberg & Rabkin, Blum, Miller, Calvisi, Smith; engines read off Sopranos, Fleabag, Succession |
| `sw-writers-room` | How an episode is actually made by a group: the showrunner's duties and veto, breaking story (Chase's 35 beats and scissors, Wells's ten chairs, Douglas's grid, Mazzara without an outline), the document chain and its page budgets, the six-week episode and the 14-day draft, spec scripts and pitching to an existing show, taking and giving notes, the staff ladder and step deals, production limits as creative triggers, and single-author alternatives | Goldberg & Rabkin, Douglas, Landau 1e/2e interviews, Smith, Blum (dated), plus first-hand accounts by Chase, Armstrong, Prebble, Sorkin, Fellowes, Waller-Bridge |
| `sw-sitcom-comedy` | Half-hour comedy as a whole-mode switch: premise-driven comedy in three levels, nine predicaments, six character mixes, joke mechanics (two-part setups, punch word last, toppers, running gags, ten comedic nuances, 2–4 laughs per page), cold open / acts / tag, multi-camera vs single-camera vs animation formats and page counts, direct address as a season-long device, dramedy | Evan Smith, Waller-Bridge's *Fleabag*, Landau, Blum, Douglas on dramedy, Miller |

**Stage**

| Skill | What it covers | Main sources |
|---|---|---|
| `sw-chinese-opera-banqiang` | The banqiang-system method (京剧 / 豫剧 / 越剧 / 秦腔 / 评剧 / 沪剧): decide the 体制 first (唱工 / 做工 / 武打), the three schools on concentrating the main line (李渔 / 范钧宏 / 翁偶虹, kept side by side), technical structure and 排场, role type before psychology and writing for a named performer, the lyric method (line-splitting for seven- and ten-character lines, the key line, 垛句, rhyme-group planning across a whole play, the real tolerance of rhyme), the salutation that turns speech into song, duets by shrinking line length, what a writer marks (Peking-opera style vs Yue-opera style, which marks no 板式 at all), the writer–performer–musician interface (板式 is a letter of intent), reworking old plays and commissioned adaptation, and the three contemporary routes (modernising the conventions / absurdist time-crossing / re-coding), each with its own boundary | 范钧宏, 翁偶虹 (two books), 刘吉典, 樊尚林, 张庚 & 郭汉城, 顾仲彝, 罗怀臻, Lu Jun; method conclusions from the corpus |
| `sw-chinese-opera-qupai` | The qupai-system method (元杂剧 / 明清传奇 / 昆曲 / 川剧高腔): the stage school vs the desk school (李渔 vs 吴梅 & 王季烈), "play" and "song" as two separate scales, the 清曲 / 剧曲 switch, the 杂剧 branch (one 折 one mode one rhyme, the sole singer's right = the protagonist's right, 题目正名) and the 传奇 branch (副末开场, upper and lower halves, north–south suites, 集唐 exit poems), filling a tune pattern (前腔 / 换头 / 幺, padding characters, 务头, the forty prohibitions), modes and suites (the seventeen-mode mood table), 排场, the speech-to-song interface, 帮腔, reworking old texts, and the contemporary qupai practice that abandons suites | 李渔, 吴梅 (three books), 王季烈, 孔尚任's 凡例 and 纲领, 关汉卿, 汤显祖; 魏明伦 and 罗怀臻 for the modern practice |
| `sw-chinese-opera-banqiang-cases` | Banqiang full-script corpus with the creative-process record attached: 《锁麟囊》 (翁偶虹's account, 程砚秋's three changes, 范钧宏's critique, the performance score), 《沙家浜》 1965 with the 1970 differences, 《白蛇传》 1955 with 田汉's preface and 王瑶卿's five notes on the tunes, 《朝阳沟》, 《潘金莲》, 罗怀臻's 越剧 and regional plays; an index of some fifty of 翁偶虹's creation records and 范钧宏's seven adaptation notes | the published scripts and scores above |
| `sw-chinese-opera-qupai-cases` | Qupai full-script corpus: 《窦娥冤》《救风尘》《金线池》 (twelve 折 measured for mode, rhyme, singer and song-to-speech ratio), 《牡丹亭》 55 出 with its full scene table and selected arias, 《桃花扇》 44 出 with the 凡例, 《长生殿》 by 王季烈's fifty-折 排场 table, 《巴山秀才》 (modern 高腔, nine 帮腔 passages); each with the passages the theorists called out as breaking the rules | the texts above, from public-domain editions, verified against the originals |

### 3. Tradition and trade

| Skill | What it covers | Main sources |
|---|---|---|
| `sw-american-case-studies` | Worked features: Westerns, screwball, Wilder, Hitchcock, *Adaptation*, *Mildred Pierce*, *Thelma & Louise*, *Fargo*, *Good Will Hunting*, *American Beauty*, *Eternal Sunshine*, Bourne, Zootopia | Mei Feng, Walter, masterclass, Hoxter, Snyder, Field |
| `sw-japanese-screenwriting` | Ten Japanese directors and writers: structure-first vs fragment-first, small-material notebooks, "if + moreover", character = actor + flaw, theme-emerges-later | 泊贵洋 ed., masterclass |
| `sw-korean-french-screenwriting` | Korean and French methods: write the emotion, research first, genre as a promise, two reversals, dialogue written last, collective writing | masterclass (international) |
| `sw-chinese-series-practice` | The mainland-China series layer: taxonomy and running-time rules, the document chain (创意 → 梗概 → 人物小传 → 分集大纲 → 分场大纲 → 剧本) with its word counts, four coexisting Chinese teleplay formats, the episode-end suspense law and four tiers of suspense, adapting novels and IP into 30–50 episode dramas (sell-point migration, copy/delete/adapt), fragment adaptation in the opposite direction, and the production chain (立项/备案/两道审查, delivery gates, screenwriter contracts, content red lines), plus a Chinese–English glossary | 姚扣根, 张巍, 张明智 & 宋培义, 赵彬彬, and the Chinese translations of Douglas and Blum |
| `sw-industry-business` | Buyer's-eye workflow, PROBLEM idea test, logline/query/pitch, agents, options, credits, WGA, gross vs net, film vs TV, career resilience | Diamond & Weissman, Bork, Hicks, Walter, Henson, Snyder, Hoxter, Mei Feng, masterclass |

### 4. Master corpora: complete primary texts, read and tabulated

| Skill | What it covers | Main sources |
|---|---|---|
| `chekhov-dramaturgy` | Chekhov's seven full-length plays and the one-acts as a working method: four-act mood structure without a central climax, off-stage events, three-layer endings, the *Wood Demon* → *Uncle Vanya* rewrite, with act-by-act tables and excerpts | 契诃夫戏剧全集 (焦菊隐/童道明/李健吾译) |
| `ozu-screenplay-style` | Ozu's six screenplays as a working method: shared skeleton, marriage-of-a-daughter structure, dialogue register, format, theme sentences, with scene tables | 小津安二郎剧本集 |
| `succession-series-writing` | All four seasons of *Succession*, 39 shooting scripts, as a working method for the streaming ensemble: the invisible-act tests, container episodes built on a ceremony's running order, pressure chambers, one core question per episode, humiliation passed downward, stage directions carrying subtext and "maybe", reversals turned on one word, writing long, alts, the mega-chart, and engineering an ending once the plot engine loses pressure | Jesse Armstrong, *Succession: The Complete Scripts* I–IV (Faber), with Frank Rich's and Lucy Prebble's essays |
| `sw-series-case-studies` | Worked episodes from primary texts: Sorkin's six *West Wing* teleplays (act-page tables, eight act-out types), Chase's five *Sopranos* scripts, Fellowes's annotated *Downton Abbey* season two (19 storylines, 419 author footnotes), *Fleabag: The Scriptures*, Calvisi's eight minute-by-minute pilot breakdowns, Landau's 47-series structure appendix, Miller's *Hannibal* and *HTGAWM* scene breakdowns, Goldberg & Rabkin's beat sheets, Sakamoto Yuji and Noh Hee-kyung | the published scripts and the case chapters of the books above |

Each skill has a `SKILL.md` (principles, checklists, workflow), and all but one also carry a `reference.md` (tables, worked analyses, excerpts). Three skills split their tables across several files so each can be read in one pass: `sw-series-case-studies` into `reference.md` (the four English script collections), `reference-pilots.md` (pilot beat sheets and structure tables from the craft books) and `reference-asia.md` (the Japanese and Korean texts); `sw-series-engine-bible` into engine teardowns, document field tables and filled samples; `sw-chinese-series-practice` into the craft reference, format and planning samples, the six adaptation cases and the content red lines.

## Stage genres

Film and television are covered. The stage is covered in part, the rest is planned, and there is a rule for what gets a skill and what does not.

**The rule.** A genre gets its own skill only if it makes the model write something with different structure, format or language rules. Subject matter (spy thriller, costume drama, family) and directorial style do not qualify; those are case studies inside an existing skill, unless a complete script corpus exists, as with Ozu.

**Chinese opera is two systems.** The axis that matters for a writer is the vocal system; the regional 剧种 comes second. In the **qupai system** (曲牌体: 元杂剧, 明清传奇, 昆曲) a lyric is filled into a fixed tune pattern with set line counts, lengths and tones; a 杂剧 runs four 折 and one 楔子 with a single role singing an entire 折; a 传奇 runs in 出. In the **banqiang system** (板腔体: 京剧, 豫剧, 越剧, 秦腔, 评剧, 沪剧) a lyric is built from paired seven- or ten-character lines varied by metre (板式), any role may sing, and the unit is the 场. Structure and lyric method both differ, so they are two skills. Regional 剧种 within one system differ only in which rhyme table (京剧十三辙 vs 豫剧中州韵) and which metre table they use, the same method with a different lookup, so they live as reference appendices; China has over three hundred 剧种, and one skill each would be the same combinatorial explosion as one tree per language. Two untidy edges: 粤剧 mixes both systems and is in Cantonese, whose tones and rhymes differ from Mandarin entirely, so whether it needs its own skill depends on whether the model's Cantonese phonology can use the tables, to be tested once material is in; 川剧 uses five vocal styles and its 高腔 is qupai, so it will appear under both.

**What is here now.** Four skills, distilled from 25 sources (twelve method and theory books, thirteen full scripts, scores and collected plays): a method skill for each vocal system and a full-script case library for each. The two method skills open with a boundary table that says, with sources, which general skills apply to an opera script and which do not, and share one file of common aesthetics and staging. Classical texts were taken from public-domain editions and checked against the originals; where a scan could not be verified (some 吴梅 and 白蛇传 passages) the notes say so, and the skills do not build rules on them.

**What is planned, in order.** Two gaps in the opera layer first: a per-tradition rhyme table for 豫剧 (the sources only give the principle, not the table) and a fourth-system edge for 粤剧, whose Cantonese phonology may need its own treatment. Then the spoken-theatre method China's own tradition adds beyond Chekhov: 曹禺's pressure-chamber structure and 老舍's portrait-gallery structure with no main line. Musical theatre last, because song carrying narrative is a genuinely different rule set and none of the current sources covers it.

**What is not planned.** Short-form vertical drama and AI-generated comic drama, whose logic is distribution, with no dramaturgy to distil. Skills split by subject, by director, or by regional 剧种.

**How a medium is added without polluting the general layer.** One new skill; one medium-boundary table inside it declaring what transfers; one row in `sw-workflow`'s entry-path table. The general skills are not edited. The series layer (13 → 20 skills) was added this way and `sw-story-structure` did not change; the opera slot was added the same way, and `sw-dialogue` got shorter.

## Source books

**Screenwriting craft (18):** Syd Field *Screenplay*; Blake Snyder *Save the Cat*; Robert McKee *Story* and *Dialogue*; John Truby *The Anatomy of Story* (中译《故事写作大师班》); Julian Hoxter *Write What You Don't Know*; Neill D. Hicks *Screenwriting 101*; Lajos Egri *The Art of Dramatic Writing*; Lisa Cron *Story Genius*; William Indick *Psychology for Screenwriters*; Richard Walter *Essentials of Screenwriting*; Wendy Jane Henson *Screenwriting Step by Step*; Diamond & Weissman *Bulletproof*; Eric Bork *The Idea*; 梅峰《编剧的自修课》; 刘大鹏编《故事创作大师班（国际卷）》; 陆军《编剧理论与技法》; 泊贵洋编《从零开始做编剧》.

**Television craft (15):** William Rabkin *Writing the Pilot: Creating the Series*; Daniel Calvisi *Story Maps: TV Drama*; Pamela Douglas *Writing the TV Drama Series* (3rd ed.) and its Chinese translation《美剧编剧入门》(2nd ed.); Kam Miller *The Hero Succeeds*; Emmanuel Oberg *Writing a Successful TV Series*; Lee Goldberg & William Rabkin *Successful Television Writing*; Neil Landau *The TV Showrunner's Roadmap* (1st ed., 21 tips) and (2nd ed., 2022); Evan S. Smith *Writing Television Sitcoms*; Richard A. Blum *Television and Screen Writing*（中译《电视与银幕写作》）; 姚扣根《电视剧写作概论》; 张巍等《电视剧改编教程》; 张明智、宋培义主编《电视剧出品人与制片人教程》; 赵彬彬主编《影视剧片段改编教程》.

**Published scripts and plays (12):** 《契诃夫戏剧全集》; 《小津安二郎剧本集》; Jesse Armstrong *Succession: The Complete Scripts*, Seasons One–Four; Aaron Sorkin *The West Wing Script Book*; David Chase et al. *The Sopranos: Selected Scripts from Three Seasons*; Julian Fellowes *Downton Abbey: The Complete Scripts, Season Two*; Phoebe Waller-Bridge *Fleabag: The Scriptures*; 坂元裕二《花束般的恋爱》剧本; 卢熙京《世间最美丽的离别》.

**Chinese opera craft (13):** 李渔《闲情偶寄》词曲部·演习部; 吴梅《顾曲麈谈》《曲学通论》《中国戏曲概论》; 王季烈《螾庐曲谈》; 范钧宏《戏曲编剧论集》; 翁偶虹《翁偶虹编剧生涯》《翁偶虹戏曲论文集》; 张庚、郭汉城主编《中国戏曲通论》; 顾仲彝《编剧理论与技巧》; 刘吉典《京剧音乐概论》(the 板式 chapters only); 樊尚林《豫剧祥符调流派唱腔、板式暨器乐曲牌集萃》(the 板式 notes only); 罗怀臻《罗怀臻戏剧文集》理论·演讲卷.

**Chinese opera scripts and scores (11 volumes, plus three public-domain originals):** 汤显祖《牡丹亭》; 孔尚任《桃花扇》with the 小引 / 凡例 / 纲领 / 本末; 关汉卿《窦娥冤》《救风尘》《金线池》(维基文库, 元曲选 text) with a 戏剧故事选 for plot skeletons; 翁偶虹《锁麟囊》京剧曲谱 (王吟秋 ed.); 北京京剧团《沙家浜》1965; 田汉《白蛇传》1955; 杨兰春《朝阳沟》1978; 魏明伦《潘金莲》《巴山秀才》; 罗怀臻《罗怀臻戏剧文集》越剧卷 and 地方戏卷; 《长生殿》through 王季烈's fifty-折 table.

## Conventions

- `SKILL.md` frontmatter: `name` (kebab-case, matches the folder) and a long English `description` ending in "Use when …", with Chinese keywords in parentheses for triggering.
- Skill bodies are Chinese; numbered principles, tables and checklists; cross-references between skills by folder name. Output language follows the user; see [Multilingual support](#multilingual-support).
- Agent-neutral by design: the skill files name no agent and use no agent-specific syntax, so the same `SKILL.md` works under Claude Code, Codex, or anything else that reads the agentskills.io format. Each plugin carries a `.claude-plugin/plugin.json` and a `.codex-plugin/plugin.json` over one shared `skills/` directory.
- Where the sources disagree, both positions are kept side by side with a note on when to use which, for example Douglas's four-act grid against Oberg's "act breaks are only the size of the sausages", or theme-as-design against theme-as-emergent.
- Industry facts carry the year of their source, because rates, platforms and act counts date quickly; Chinese policy figures are marked 2014/2016.
- `reference.md` holds worked examples and quotations so `SKILL.md` stays under ~40 KB.
- License: for personal study use. Quotations remain the property of their authors and translators.

Sister project, same idea applied to Japanese composition and arranging: [japanese-composition-skills](https://github.com/jtydhr88/japanese-composition-skills).
