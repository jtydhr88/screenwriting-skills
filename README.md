# screenwriting-skills

[中文版](README_ZH.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Français](README_FR.md)

21 agent skills (for [Claude Code](https://docs.anthropic.com/en/docs/claude-code/skills) and [OpenAI Codex](https://developers.openai.com/codex/build-skills)) for screenwriting, television writing and dramaturgy, distilled from 32 craft books and 12 volumes of published scripts and plays (Chinese, American, British, Japanese and Korean).

The `SKILL.md` files follow the open [agentskills.io](https://agentskills.io) standard and are shared by both agents — install once, works everywhere.

**Ask in your own language.** The skill bodies are written in Chinese, because most of the sources are Chinese originals or Chinese translations. That is an implementation detail, not a restriction: ask in English, Japanese, Korean or French and you get the answer in that language. See [Multilingual support](#multilingual-support) for why there is one source tree and not five.

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

The same 21 `SKILL.md` files are shipped through the plugin's `skills/` directory — no duplication, no rewriting.

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

This is a deliberate decision, and it was not the first one. An English edition — a parallel `screenwriting-en` plugin with all 20 skills translated — was proposed in [#3](https://github.com/jtydhr88/screenwriting-skills/issues/3), built, and merged. It has since been removed. The argument that killed it is the one that applies equally to every other language: if a reader who cannot read Chinese deserves a translated tree, so does a reader who cannot read English, and the next request is Japanese, then Korean, then French, then Russian. Five languages is 230 files that drift independently, with nothing to tell you which one is stale. The cost is not the translation; it is that forking once removes any principled ground for refusing the second fork.

So the line is drawn at the source, and the runtime does the rest:

- **Output language follows your question.** Ask in French, get French. No flag, no separate install.
- **Terminology is anchored, not re-improvised.** The craft vocabulary of this field is originally English — *logline*, *act out*, *beat sheet*, *showrunner*, *staff writer*. The Chinese in the source books (计程绳, 出幕, 节拍表, 剧目管理人, 试用编剧) is the translation, and different translators chose differently. [`sw-workflow/terms.md`](plugins/screenwriting/skills/sw-workflow/terms.md) maps each concept back to its original term, so the agent restores the word instead of inventing one — and it serves all languages at once, because a Japanese or French screenwriter also says *act out* and *logline*.
- **Terms with no equivalent keep their original form plus a gloss.** 戏眼, 扣子, ト書き and 決定稿 are not forced into English; they come through as `戏眼 (xìyǎn — the one-line core attraction of an episode)`.
- **Your script stays in your script's language.** Discussing a Chinese screenplay in English is normal; the conversation switches language, the draft does not.

What this trades away is auditability: you cannot read the instruction file itself unless you read Chinese, only the agent's account of it. That is a real cost, and it is the one thing the deleted English edition genuinely bought. It was not worth a permanent five-way maintenance burden.

**READMEs are a different matter** and are translated, because they are short, stable, and the thing a newcomer meets first. The Japanese, Korean and French READMEs deliberately stop at install, structure and this policy; the full skill tables and the source bibliography live here and in the Chinese README rather than being copied four times — for exactly the reason above.

## How the skills are organised

Four layers. A feature project uses layers 1, 3 and 4; a series or stage project adds layer 2, because the medium layer replaces structure-for-film with the medium's own units rather than sitting next to it.

```
1. General dramaturgy   premise · structure · character · dialogue · scene · format · project workflow
2. Medium layer         series · episode & season structure · engine & bible · writers' room · half-hour comedy
                        stage  · Chinese opera, banqiang system (lyric method and boundary); qupai system planned
3. Tradition & trade    America · Japan · Korea & France · mainland China · the business
4. Master corpora       Chekhov · Ozu · Succession · television case studies
```

### 1. General dramaturgy — medium-independent

| Skill | What it covers | Main sources |
|---|---|---|
| `sw-workflow` | Project orchestrator: a feature/stage stage-map (premise → structure → character → scenes → draft → revision → submission) **and a separate series stage table (S0–S7: engine → character web & season arc → documents → pilot structure → break story → draft → submission)**, naming which skill to call at each stage, per-stage deliverables and advisory exit checks, plus a `story-bible.md` convention (with a series supplement) that keeps project state in one file across sessions | meta-skill, no new sources |
| `sw-story-structure` | Paradigm & plot points, Save the Cat beats and board, McKee's event/scene/sequence/act, inciting incident, progressive complications, crisis-climax-resolution, subplots, Hoxter's nine beats, Hicks' attraction/anticipation/satisfaction, Lu Jun's 起承转合, eight openings, eight endings | Field, Snyder, McKee *Story*, Hoxter, Hicks, Lu Jun |
| `sw-premise-theme` | Premise as tyrant, controlling idea (value + cause), the "third rail" (desire vs misbelief), five premise questions, logline tests, 选材/开掘/视角/戏核 | Egri, McKee, Cron, Hicks, Hoxter, Snyder, Lu Jun |
| `sw-character-conflict` | Three-dimensional character, orchestration, unity of opposites, pivotal character, rising vs static vs jumping conflict; Freud/Erikson/Jung/Campbell/Murdock/Adler/May for motive; 人物要活八要, 对手要强 | Egri, Indick, McKee, Hicks, Cron, Snyder, Lu Jun |
| `sw-dialogue` | Dialogue as action, said/unsaid/unsayable, exposition as ammunition, beats as gerunds, credibility/language/content/design flaws, character-specific vocabulary; 语言要美, 戏曲唱词三好 | McKee *Dialogue*, Walter, Hicks, Lu Jun, Egri, Snyder, Mei Feng |
| `sw-scene-craft` | Scene as value turn, five-step scene analysis, enter late leave early, pacing and transitions, action over talk; 意趣要足, 细节要妙, 道具要精 | McKee, Field, Hicks, Walter, Henson, Hoxter, Mei Feng, Lu Jun |
| `sw-format-adaptation` | Spec format hard rules, typographic grid, element conventions, Fountain output contract with forced markers for Chinese, 场号制 and Japanese 柱・ト書き formats, outline→treatment→script chain, revision, adaptation principles | Henson, Walter, Hicks, Field, McKee, Hoxter, Diamond & Weissman, Bork; grid/Fountain/Asian formats are industry conventions |

### 2. Medium layer — what a feature does not teach

| Skill | What it covers | Main sources |
|---|---|---|
| `sw-series-structure` | Teasers and cold opens; broadcast four/five/six-act grids with page anchors (17–18 / 30 / 45 / 60); three tests for locating the **invisible acts** in pay-cable and streaming scripts; act-out and cliffhanger taxonomies; Oberg's four information tools (mystery / surprise / dramatic irony / suspense); A/B/C/runner weaving and scene-count ratios; the Calvisi pilot beat sheet with minute marks; five-part scene structure; season shape (tentpoles, movements, bottle and container episodes, two-parters, finales) | Calvisi, Douglas (EN 3e + 中译 2e), Oberg, Landau 1e/2e, Goldberg & Rabkin, Miller, Rabkin, Blum, plus measured tables from the West Wing / Succession / Sopranos / Downton / Fleabag scripts |
| `sw-series-engine-bible` | Series engine / franchise (Rabkin's four elements, Landau's tacit contract, Blum's three tests, the 100-episode and "name three more episodes" tests); story pattern and story landmines; character webs that keep generating conflict; pilot types (premise / typical-episode / hybrid) and three endings; series types and story-types; and every selling document — logline, springboard, pitch document, series format, treatment, bible tiers, plus a storyline-document skeleton | Rabkin, Landau 1e/2e, Oberg, Douglas, Goldberg & Rabkin, Blum, Miller, Calvisi, Smith; engines read off Sopranos, Fleabag, Succession |
| `sw-writers-room` | How an episode is actually made by a group: the showrunner's duties and veto, breaking story (Chase's 35 beats and scissors, Wells's ten chairs, Douglas's grid, Mazzara without an outline), the document chain and its page budgets, the six-week episode and the 14-day draft, spec scripts and pitching to an existing show, taking and giving notes, the staff ladder and step deals, production limits as creative triggers, and single-author alternatives | Goldberg & Rabkin, Douglas, Landau 1e/2e interviews, Smith, Blum (dated), plus first-hand accounts by Chase, Armstrong, Prebble, Sorkin, Fellowes, Waller-Bridge |
| `sw-sitcom-comedy` | Half-hour comedy as a whole-mode switch: premise-driven comedy in three levels, nine predicaments, six character mixes, joke mechanics (two-part setups, punch word last, toppers, running gags, ten comedic nuances, 2–4 laughs per page), cold open / acts / tag, multi-camera vs single-camera vs animation formats and page counts, direct address as a season-long device, dramedy | Evan Smith, Waller-Bridge's *Fleabag*, Landau, Blum, Douglas on dramedy, Miller |

**Stage**

| Skill | What it covers | Main sources |
|---|---|---|
| `sw-chinese-opera-banqiang` | The banqiang-system opera slot (京剧 / 豫剧 / 越剧 and the 小戏 tradition; 杂剧 / 传奇 / 昆曲 are the qupai system, a separate planned skill): Lu Jun's lyric method (choose the rhyme from the character and from the key line first, wide vs narrow rhymes, same-word rhyme, vary the line pattern, put sung passages in the heavy scenes) with worked examples, and a medium-boundary table for applying the general skills to an opera script. States its own gaps: 板式 and 韵辙 tables per 剧种, 行当 and 程式, script format and master corpora are listed as planned, not claimed | Lu Jun; planned: 翁偶虹, 范钧宏, 李渔《闲情偶寄》 |

### 3. Tradition and trade

| Skill | What it covers | Main sources |
|---|---|---|
| `sw-american-case-studies` | Worked features: Westerns, screwball, Wilder, Hitchcock, *Adaptation*, *Mildred Pierce*, *Thelma & Louise*, *Fargo*, *Good Will Hunting*, *American Beauty*, *Eternal Sunshine*, Bourne, Zootopia | Mei Feng, Walter, masterclass, Hoxter, Snyder, Field |
| `sw-japanese-screenwriting` | Ten Japanese directors and writers: structure-first vs fragment-first, small-material notebooks, "if + moreover", character = actor + flaw, theme-emerges-later | 泊贵洋 ed., masterclass |
| `sw-korean-french-screenwriting` | Korean and French methods: write the emotion, research first, genre as a promise, two reversals, dialogue written last, collective writing | masterclass (international) |
| `sw-chinese-series-practice` | The mainland-China series layer: taxonomy and running-time rules, the document chain (创意 → 梗概 → 人物小传 → 分集大纲 → 分场大纲 → 剧本) with its word counts, four coexisting Chinese teleplay formats, the episode-end suspense law and four tiers of suspense, adapting novels and IP into 30–50 episode dramas (sell-point migration, copy/delete/adapt), fragment adaptation in the opposite direction, and the production chain (立项/备案/两道审查, delivery gates, screenwriter contracts, content red lines), plus a Chinese–English glossary | 姚扣根, 张巍, 张明智 & 宋培义, 赵彬彬, and the Chinese translations of Douglas and Blum |
| `sw-industry-business` | Buyer's-eye workflow, PROBLEM idea test, logline/query/pitch, agents, options, credits, WGA, gross vs net, film vs TV, career resilience | Diamond & Weissman, Bork, Hicks, Walter, Henson, Snyder, Hoxter, Mei Feng, masterclass |

### 4. Master corpora — complete primary texts, read and tabulated

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

**Chinese opera is two systems, not one genre.** The axis that matters for a writer is the vocal system, not the regional 剧种. In the **qupai system** (曲牌体: 元杂剧, 明清传奇, 昆曲) a lyric is filled into a fixed tune pattern with set line counts, lengths and tones; a 杂剧 runs four 折 and one 楔子 with a single role singing an entire 折; a 传奇 runs in 出. In the **banqiang system** (板腔体: 京剧, 豫剧, 越剧, 秦腔, 评剧, 沪剧) a lyric is built from paired seven- or ten-character lines varied by metre (板式), any role may sing, and the unit is the 场. Structure and lyric method both differ, so they are two skills. Regional 剧种 within one system differ only in which rhyme table (京剧十三辙 vs 豫剧中州韵) and which metre table they use, the same method with a different lookup, so they are reference appendices rather than skills; China has over three hundred 剧种, and one skill each would be the same combinatorial explosion as one tree per language. Two untidy edges: 粤剧 mixes both systems and is in Cantonese, whose tones and rhymes differ from Mandarin entirely, so whether it needs its own skill depends on whether the model's Cantonese phonology can use the tables, to be tested once material is in; 川剧 uses five vocal styles and its 高腔 is qupai, so it will appear under both.

**What is here now.** `sw-chinese-opera-banqiang` holds the lyric-writing method (唱词) from Lu Jun with worked examples (all his examples are 越剧, 沪剧 and 小戏, so banqiang), and a medium-boundary table saying which general skills apply to an opera script and which do not. It was moved out of `sw-dialogue`, where a general-purpose skill had been carrying an opera trigger clause. The skill states plainly what it does not yet cover, and its description promises only what is there.

**What is planned, in order.** For banqiang: the cross-剧种 method (一人一事, 场, 行当, 程式, 唱念做打) from 范钧宏, 翁偶虹, 汪曾祺, 张庚/郭汉城, 王安祈 and 罗怀臻; per-剧种 appendices as tables (京剧十三辙 and the 西皮二黄 metres from 刘吉典, 豫剧中州韵 and its metres); opera script format; master corpora on the Chekhov model (《锁麟囊》《曹操与杨修》《朝阳沟》《白蛇传》《沙家浜》, 越剧《红楼梦》, 魏明伦). Then `sw-chinese-opera-qupai`: the filling method, modes and suites, and the single-singer structure, from 李渔《闲情偶寄》, 吴梅 and 王季烈, with 《窦娥冤》《西厢记》《牡丹亭》《桃花扇》《长生殿》 as corpora. Then the spoken-theatre method China's own tradition adds beyond Chekhov: 曹禺's pressure-chamber structure and 老舍's portrait-gallery structure with no main line. Musical theatre last, because song carrying narrative is a genuinely different rule set and none of the current 32 books covers it.

**What is not planned.** Short-form vertical drama and AI-generated comic drama, whose logic is distribution rather than dramaturgy. Skills split by subject, by director, or by regional 剧种.

**How a medium is added without polluting the general layer.** One new skill; one medium-boundary table inside it declaring what transfers; one row in `sw-workflow`'s entry-path table. The general skills are not edited. The series layer (13 → 20 skills) was added this way and `sw-story-structure` did not change; the opera slot was added the same way, and `sw-dialogue` got shorter.

## Source books

**Screenwriting craft (17)** — Syd Field *Screenplay*; Blake Snyder *Save the Cat*; Robert McKee *Story* and *Dialogue*; Julian Hoxter *Write What You Don't Know*; Neill D. Hicks *Screenwriting 101*; Lajos Egri *The Art of Dramatic Writing*; Lisa Cron *Story Genius*; William Indick *Psychology for Screenwriters*; Richard Walter *Essentials of Screenwriting*; Wendy Jane Henson *Screenwriting Step by Step*; Diamond & Weissman *Bulletproof*; Eric Bork *The Idea*; 梅峰《编剧的自修课》; 刘大鹏编《故事创作大师班（国际卷）》; 陆军《编剧理论与技法》; 泊贵洋编《从零开始做编剧》.

**Television craft (15)** — William Rabkin *Writing the Pilot: Creating the Series*; Daniel Calvisi *Story Maps: TV Drama*; Pamela Douglas *Writing the TV Drama Series* (3rd ed.) and its Chinese translation《美剧编剧入门》(2nd ed.); Kam Miller *The Hero Succeeds*; Emmanuel Oberg *Writing a Successful TV Series*; Lee Goldberg & William Rabkin *Successful Television Writing*; Neil Landau *The TV Showrunner's Roadmap* (1st ed., 21 tips) and (2nd ed., 2022); Evan S. Smith *Writing Television Sitcoms*; Richard A. Blum *Television and Screen Writing*（中译《电视与银幕写作》）; 姚扣根《电视剧写作概论》; 张巍等《电视剧改编教程》; 张明智、宋培义主编《电视剧出品人与制片人教程》; 赵彬彬主编《影视剧片段改编教程》.

**Published scripts and plays (12)** — 《契诃夫戏剧全集》; 《小津安二郎剧本集》; Jesse Armstrong *Succession: The Complete Scripts*, Seasons One–Four; Aaron Sorkin *The West Wing Script Book*; David Chase et al. *The Sopranos: Selected Scripts from Three Seasons*; Julian Fellowes *Downton Abbey: The Complete Scripts, Season Two*; Phoebe Waller-Bridge *Fleabag: The Scriptures*; 坂元裕二《花束般的恋爱》剧本; 卢熙京《世间最美丽的离别》.

## Conventions

- `SKILL.md` frontmatter: `name` (kebab-case, matches the folder) and a long English `description` ending in "Use when …", with Chinese keywords in parentheses for triggering.
- Skill bodies are Chinese; numbered principles, tables and checklists; cross-references between skills by folder name. Output language is the user's, not the file's — see [Multilingual support](#multilingual-support).
- Agent-neutral by design: the skill files name no agent and use no agent-specific syntax, so the same `SKILL.md` works under Claude Code, Codex, or anything else that reads the agentskills.io format. Each plugin carries a `.claude-plugin/plugin.json` and a `.codex-plugin/plugin.json` over one shared `skills/` directory.
- Where the sources disagree, both positions are kept side by side with a note on when to use which — for example Douglas's four-act grid against Oberg's "act breaks are only the size of the sausages", or theme-as-design against theme-as-emergent.
- Industry facts carry the year of their source, because rates, platforms and act counts date quickly; Chinese policy figures are marked 2014/2016.
- `reference.md` holds worked examples and quotations so `SKILL.md` stays under ~40 KB.
- License: for personal study use. Quotations remain the property of their authors and translators.

Sister project, same idea applied to Japanese composition and arranging: [japanese-composition-skills](https://github.com/jtydhr88/japanese-composition-skills).
