---
name: sw-workflow
description: Project orchestrator for the screenwriting skill set (剧本项目主线调度 / 状态存档 / story bible) — a meta-skill that adds no new craft knowledge but routes a screenplay or stage-play project through stages (premise → structure → character → scenes → draft → revision → submission) and a TV / streaming series project (电视剧 / 剧集 / pilot / 一季) through a separate series stage table (engine → character network & season arc → documents/bible → pilot structure → break story & outline → draft → submission), names which sw-* skill to invoke at each stage, defines each stage's deliverable and advisory exit check, and keeps all project state in a story-bible.md file so work can resume across sessions. English edition. Use when starting a new script project, resuming one ("continue my screenplay", "where were we"), when the user asks "what should I do next" on a script, when converting a vague idea into a full development pipeline, or when the other sw-* skills are firing individually and the overall process needs sequencing.
---

# Workflow & Story Bible (剧本项目主线调度)

This skill contains no new screenwriting craft knowledge. It only does two things: **sequencing** (which skill to invoke at which stage, what to deliver, what counts as passing) and **state persistence** (writing each stage's conclusions into `story-bible.md` so work can resume next session). All methods live in the other sw-* skills; this skill is solely responsible for calling them forward at the right moment.

The design rationale comes from a controlled experiment: for the same premise, following the workflow to complete the worksheets before writing versus writing directly without a workflow produced differences across page count, protagonist agency, antagonist strength, and subtext; the difference was not knowledge, but "the forms that must be filled before writing, and the checklists that must be cleared after writing." This skill is the scheduler for that form and that checklist.

For the story-bible template and stage worksheets, see [reference.md](reference.md).

---

## I. Session Protocol (Execute at Every Start and Finish)

### Starting

1. Look for `story-bible.md` in the current directory (or the script directory specified by the user).
2. **Found**: Read only three sections: "Current Stage," "Locked Decisions," and "Decision Log." Restate to the user in three sentences: what the project is, what step it has reached, and what was settled last time. Then proceed directly into the current stage without reopening settled decisions, unless the user takes the initiative to overturn them.
3. **A one-off deliverable needs no bible**: the user wants a document handed over in this session (a development plan, a pitch, a one-page synopsis, an episode outline) and plainly will not come back for a second session — building a bible is pure overhead there; just run the stage table inside the same session. A bible solves **context lost between sessions**, not "a process ought to have paperwork."
4. **Not Found and this is an ongoing project**: Determine the entry path (see Section III). Create a new `story-bible.md` following the template in reference.md, filling only "Project Information" and "Current Stage," leaving the rest blank. Do not ask the user more than four questions at once; infer what can be deduced from the user's words, fill it in first, and label it "(Pending confirmation)."

### In Progress

- Whenever a stage's deliverable is completed, immediately write it into the corresponding story-bible section, and advance the "Current Stage" by one step.
- Any action altering a locked decision (changing the premise, changing the ending, cutting a character) adds a row to the "Decision Log": date, what changed, and why.
- Keep the story-bible at a length readable in a single pass (roughly 25K tokens). Record only conclusions for deliverables, not the derivation process; keep outlines, treatments, and script pages in standalone files, noting only the file name and a one-sentence status in the bible.

### Finishing

- Confirm the story-bible is updated to the latest state before ending the session, with the last line stating a single-sentence "Next Step:".

---

## II. Stage Map

| # | Stage | Skill Invoked | Deliverable (Section Written to story-bible) | Advisory Exit Check |
|---|---|---|---|---|
| 0 | Launch / Resume | This skill | Project info, entry path, current stage | Know what genre, what length, for whom |
| 1 | Material & Premise | `sw-premise-theme` | Spark and "why care," one-sentence core idea, hypothetical question, **premise** (character trait + leads to + outcome), **Controlling Idea** (value + cause), the third track (want vs. misbelief), Dramatic Core, one-sentence story, logline | Premise is singular; can be stated clearly to a stranger in one sentence; story falls apart if Dramatic Core is removed; thematic words locked |
| 2 | Structure | `sw-story-structure` | Ending, opening, Plot Points I/II, Midpoint nature (false victory/false defeat), BS2 beat sheet with page numbers, act ratios, relationship between subplots and Controlling Idea | Four things (ending/opening/two Plot Points) are known; setup ≤ 25 pages; Midpoint and All Is Lost are opposite mirror images; final act is shortest |
| 3 | Character & Conflict | `sw-character-conflict` | Three-Dimensional Character table for principals, specific categories, attitude toward theme, binding agent of Unity of Opposites, antagonist's edge, growth ladder, primal scene | Protagonist is most dimensional; aggregate antagonist force is stronger than protagonist; no two characters share an archetype; includes a "greatest enemy is oneself" dimension; no auspicious clouds |
| 4 | Scene List / Treatment | `sw-scene-craft` + `sw-format-adaptation` | Step outline (one or two sentences per scene + Value Turn + structural position), The Board with 40 cards (+/-, ><), prop and image system, treatment (optional) | Every scene has a Value Turn; Act III has more than two cards; adjacent scenes share transitional elements; no pure exposition scenes |
| 5 | First Draft | `sw-dialogue` + `sw-format-adaptation` (formatting and output contract) + reference skills | Script file (deliver `.fountain` for Hollywood style; deliver plain text for Chinese Scene Numbering Format or Japanese style, see `sw-format-adaptation` Section II-2), page count, daily progress | Page count within target ±15%; formatting hard rules all passed; dialogue recognizable with character names covered |
| 6 | Revision | "Diagnostic Checklist" of each skill | Revision target list, itemized completion record, draft number | Ran through structural diagnostics (13 questions), character diagnostics (14 questions), dialogue diagnostics (14 questions), scene diagnostics (13 questions), and format diagnostics (group A universal, 12 questions, plus the group for the notation in use) |
| 7 | Submission / Industry | `sw-industry-business` | Logline and one-page synopsis, pitch document, target buyers/competitions, credits and registration | Passed PROBLEM seven-element self-check; one-sentence passed stranger test |

**When Reference Skills Enter**:
- `sw-american-case-studies`: Stages 1–2 for genre film lists and clichés; Stage 6 for comparison against genre climaxes.
- `chekhov-dramaturgy`, `ozu-screenplay-style`: From Stage 2 onward as models for structure and tone when writing anticlimax, multi-protagonist narratives, domestic drama, or "events off-screen, reactions on-screen."
- `sw-japanese-screenwriting`, `sw-korean-french-screenwriting`: Alternative paths such as sequence-first, theme-deferred, genre commitment, and writer's room collaboration; introduce at Stage 1 when the user explicitly departs from the three-act classical paradigm.
- The series skills (`sw-series-structure`, `sw-series-engine-bible`, `sw-writers-room`, `sw-sitcom-comedy`, `sw-chinese-series-practice`, `succession-series-writing`, `sw-series-case-studies`): only when the entry path is judged to be a series, in which case run the series stage table in Section III-2.

**Stages Can Roll Back**: If dialogue stalls at Stage 5, Stage 3 character or Stage 1 premise usually has a hole; roll back to patch it, then log an entry in the decision log.

---

## III. Entry Paths

| User Situation | Starting Stage | Special Handling |
|---|---|---|
| Feature / multi-act play from scratch | Run all: 0 → 1 → … → 7 | Standard path |
| Existing first draft needing revision | First perform **reverse sheet-filling** for Stages 1–3 (extract premise, structure, and character from draft into bible), then proceed to Stage 6 | Mark missing draft elements as "Missing" during sheet-filling; these missing items become the revision checklist |
| Adapting novel / stage play / true event | 0 → `sw-format-adaptation` Four Adaptation Questions → 1 → 2 … | In Stage 1, answer first "on what level does source conflict primarily sit, what must be reinvented"; verify rights first for true stories |
| Short film / short-form play / one-act play | 1 → 2 (use Lu Jun's Introduction, Elaboration, Turn, Resolution and eight techniques instead of BS2) → 3 → 5 | The Board shrinks to 10–15 cards; characters ≤ 5; Dramatic Core must be established first |
| Only an idea, unsure if viable | 1 (up to one-sentence story only) → 7's PROBLEM self-check | If passed, return to 2; if failed, switch ideas, keeping rejected ideas and reasons in bible |
| TV series / serial / pilot / a season | Run the **series stage table** (S0–S7) in Section III-2, not the feature stage table above | Engine and bible come before script; a mainland-Chinese series adds the document chain in `sw-chinese-series-practice`; for the project-proposal format see the Omiya Ellie template in `sw-format-adaptation` reference |
| Half-hour comedy / sitcom | The series stage table, but S2 and S5 switch to `sw-sitcom-comedy` | Page count, format and joke density all switch together |
| Industry questions (how to sell, credits, agents) | Direct to 7 | Do not create bible |

### III-2. Series Stage Table (TV / streaming / limited series)

A series is not "a longer film": a film is a closed arc and a one-time question; a series is a repeatable **engine** plus relationship tension that never closes, cut into segments by act outs, running several lines in parallel, with the bible preceding the script and a room writing collectively under a showrunner's final pass. So the order inverts: **prove the engine can run a hundred episodes before you write the first one.**

| # | Stage | Skills invoked | Deliverable (written into the story-bible section) | Suggested passing criteria |
|---|---|---|---|---|
| S0 | Launch / Resume | This skill | Platform and format (broadcast / cable / streaming; one-hour / half-hour; episode and season count), entry path | You know who decides the act count (ad breaks or you) and the target page count |
| S1 | Engine and premise | `sw-series-engine-bible` + `sw-premise-theme` | Thematic opposition, the four franchise elements (concept / conflict / theme / story pattern), the central question written as a process sentence, the tacit contract in one line, 5–6 sample story areas | "Cannot think of three episodes after the pilot" is a fail; five story areas with the same source or the same ending is a fail |
| S2 | Character network and season arc | `sw-series-engine-bible` + `sw-character-conflict` | 3–4 leads (≤1 page each) and the conflict network (who is bound to whom, division of expertise, family dynamics), season arc grid (episode × character want/state), season question and tentpoles | Leads must not "smile and agree with each other"; everyone has something to lose; the season finale answers this year's version of the question, not the series question |
| S3 | Documents | `sw-series-engine-bible` (+ `sw-chinese-series-practice` for a mainland-Chinese series) | Logline and springboard, pitch document / series format, bible (pick a tier), story-line documents (purpose / driver / entry and exit per line / cross-episode beats); a Chinese series adds 剧情简介 → 梗概 → 人物小传 → 分集大纲 | The documents let a stranger restate "what happens every week"; a Chinese episode outline closes every episode on a hook |
| S4 | Pilot and episode structure | `sw-series-structure` (half-hour comedy switches to `sw-sitcom-comedy`) | Pilot type (premise / typical-episode / hybrid), act count and page anchors, act-out list, entry and exit for the A/B/C lines, the 17-column Story Map | Every act out poses a new question; the C line does not close an act; you can state three reasons for each invisible act break |
| S5 | Breaking story and outline | `sw-writers-room` + `sw-scene-craft` | Beat sheet (6–7 scenes per act) → locked outline; the six-week schedule for one episode | One beat per scene in the outline, each with its position inside the act; changing the ending sends you back to the outline |
| S6 | First draft and revisions | `sw-dialogue` + `sw-format-adaptation` + `sw-writers-room` (taking notes) | Script file (teaser / ACT markers or day markers), page count, warm-read and cold-read records | Page count inside the format band (one-hour 48–63, half-hour single-camera ≈30, multi-camera ≈50); the cold read can answer "what is the next episode?" |
| S7 | Submission / industry | `sw-industry-business` (US) / `sw-chinese-series-practice` (China: 立项, 备案, censorship, delivery milestones) | The 20-minute pitch, the one-page leave-behind, the target-platform list | One pitch per meeting; a Chinese series self-checks against both the content and the technical review |

**When reference skills enter**: `succession-series-writing` (streaming ensemble, invisible acts, season-shape symmetry, finale engineering) serves as a model from S2 on; `sw-series-case-studies` (West Wing four acts, the Sopranos pilot, Downton's multiple lines, Fleabag's six-episode season, Calvisi's eight pilot beat sheets, Sakamoto Yuji, Noh Hee-kyung) for finding comps at S1 and checking beats at S4. **The medium-independent parts of the feature skills still apply**: dialogue, the scene value turn, three-dimensional character, premise — do not skip them because this is a series.

**Rolling back**: if you cannot write the act outs of episode two at S4, the problem is usually the S1 engine; if dialogue stalls at S6, the S2 character network usually gives no one anything to lose. Roll back, patch, and log the decision.

---

## IV. Minimum Actions for Each Stage

No need to read the entire corresponding skill file. For each stage, read only the skill's "Workflow" and "Diagnostic Checklist" sections first; consult specific sections only when concrete craft methods are needed, and consult reference.md when examples are needed.

**Stage 1**: Follow the 12 steps in Section XII of `sw-premise-theme`; write deliverables into the "Premise and Theme" section of the bible. If the user provides external source material such as a song, painting, or news item, extract only the narrative skeleton and imagery first; construct numbering, character names, and sentences anew.

**Stage 2**: Lock the ending first; then convert target page count into BS2 beat sheet page numbers (scale the 110-page sheet proportionally: Theme Stated 5%, Catalyst 11%, Break into Two 23%, Midpoint 50%, All Is Lost 68%, Break into Three 77%); fill out the page number table; write "what false victory/defeat the Midpoint is, and what opposite the All Is Lost represents."

**Stage 3**: Fill one row in the Three-Dimensional Character table for each principal; write separately "what the binding agent of Unity of Opposites is, and which character's specific trait must perish to break it"; give the antagonist at least one cutting edge; list the protagonist's shackles.

**Stage 4**: One line per scene in the step outline: `Scene # | INT/EXT - LOCATION - DAY/NIGHT | One-sentence summary | Value at stake: Opening -> Ending | Structural Position`; then run the "what happens if cut" check, eliminating scenes where value does not turn.

**Stage 5**: Update the bible's "Progress" row after daily writing (page count, which scene reached); do not brute-force structural design flaws in the draft itself—return to the bible to adjust design before revising draft text.

**Stage 6**: Convert questions from all five diagnostic checklists item by item into revision targets, clearing them one by one; tackle Act II first, then dialogue, and formatting last.

**Stage 7**: Generate logline and one-page synopsis directly from the bible's "Premise and Theme" section; run the PROBLEM seven-element check.

---

## V. How to Use Passing Criteria

- Criteria serve as **advisory thresholds**, not hard blockers. If the user wants to skip steps, allow the skip, but mark "(Skipped Stage 3 character sheet)" next to "Current Stage" in the bible, and issue one reminder before entering Stage 5.
- For AI self-checks: at the end of each stage, run the diagnostic checklist from that skill, logging unmet items into the bible instead of quietly letting them slide.
- Quantify everything that can be quantified in passing criteria (page counts, card counts, character counts, question mark counts).
- **A client's format requirements outrank any skill's conventions.** If the user or the commissioning party specifies page counts, character counts, columns, templates or episode counts, follow theirs; the conventions in these skills (the three parts of an episode outline, the line format of a step outline, the field tables of a document) are **defaults**, used only to fill blanks the other side left unspecified. On a conflict, compress the convention rather than overrun the format, and keep the expanded version in a separate file for your own use. **Do not hand over a file that breaks the client's spec just to satisfy every field a skill asks for.**

---

## VI. Subagents and Parallel Execution

- **Do NOT** split across different agents by stage: premise, structure, and character form an organic whole; separating them causes mutual contradictions and loses creative context. The mainline must remain within a single session.
- Two types of work **can run in parallel**:
  1. Multi-angle review in Stage 6: assign one read-only agent each for structural diagnostics, character diagnostics, dialogue diagnostics, and scene diagnostics to run checklists, synthesizing findings into a unified revision target sheet.
  2. Bulk retrieval: when looking up specific examples in reference.md or beat-by-beat breakdowns of a work, dispatch an agent to read and return only conclusions, preventing mainline context inflation.
- Parallel agents remain strictly read-only toward the bible and draft text; mainline collects and incorporates changes.

---

## VII. Anti-Patterns

- Jumping straight from raw idea to script drafting ("the counterfeit treatment").
- Rewriting the bible from scratch every session, or ignoring "Locked Decisions" to debate premise anew.
- Stuffing entire derivation processes into the bible, making it unreadable in a single pass next time.
- Asking the user ten questions at once; infer and fill them first, label "Pending confirmation," and let the user correct them.
- Turning "passing criteria" into an excuse to refuse forward progress.
- Using subagents to write separate stages.

---

## VIII. Self-Check

1. Does `story-bible.md` exist in the current directory? Were "Current Stage / Locked Decisions / Decision Log" read?
2. Did this session advance at least one stage's deliverable and write it back?
3. Can the bible still be read in a single pass?
4. Were any locked decisions altered without a corresponding log entry?
5. Does the session finish with a "Next Step:" line?
