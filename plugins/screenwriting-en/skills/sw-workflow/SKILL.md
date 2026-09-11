---
name: sw-workflow
description: English edition. Project orchestrator for the screenwriting skill set (剧本项目主线调度 / 状态存档 / story bible) — a meta-skill that adds no new craft knowledge but routes a screenplay or stage-play project through stages (premise → structure → character → scenes → draft → revision → submission), names which sw-* skill to invoke at each stage, defines each stage's deliverable and advisory exit check, and keeps all project state in a story-bible.md file so work can resume across sessions. Use when starting a new script project, resuming one ("continue my screenplay", "where were we"), when the user asks "what should I do next" on a script, when converting a vague idea into a full development pipeline, or when the other sw-* skills are firing individually and the overall process needs sequencing.
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
3. **Not Found**: Determine the entry path (see Section III). Create a new `story-bible.md` following the template in reference.md, filling only "Project Information" and "Current Stage," leaving the rest blank. Do not ask the user more than four questions at once; infer what can be deduced from the user's words, fill it in first, and label it "(Pending confirmation)."

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
| 6 | Revision | "Diagnostic Checklist" of each skill | Revision target list, itemized completion record, draft number | Ran through structural diagnostics (13 questions), character diagnostics (14 questions), dialogue diagnostics (14 questions), scene diagnostics (13 questions), and format diagnostics (11 questions) |
| 7 | Submission / Industry | `sw-industry-business` | Logline and one-page synopsis, pitch document, target buyers/competitions, credits and registration | Passed PROBLEM seven-element self-check; one-sentence passed stranger test |

**When Reference Skills Enter**:
- `sw-american-case-studies`: Stages 1–2 for genre film lists and clichés; Stage 6 for comparison against genre climaxes.
- `chekhov-dramaturgy`, `ozu-screenplay-style`: From Stage 2 onward as models for structure and tone when writing anticlimax, multi-protagonist narratives, domestic drama, or "events off-screen, reactions on-screen."
- `sw-japanese-screenwriting`, `sw-korean-french-screenwriting`: Alternative paths such as sequence-first, theme-deferred, genre commitment, and writer's room collaboration; introduce at Stage 1 when the user explicitly departs from the three-act classical paradigm.

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
| TV series / serial | 1 → 2 (episode structure + season structure, two tiers) → 3 → Project Proposal | For Project Proposal format, see Omiya Ellie template in `sw-format-adaptation` reference |
| Industry questions (how to sell, credits, agents) | Direct to 7 | Do not create bible |

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
