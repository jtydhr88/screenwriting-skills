# story-bible.md Template and Worksheets for Each Phase (story-bible.md 模板与各阶段工作单)

> Use in conjunction with SKILL.md. Copy the entire "Template" section into `story-bible.md` in the screenplay directory, filling in each section stage by stage. Bracketed text indicates instructions for filling out each entry; delete them once completed. Keep the entire document within 15,000 words.

---

## I. story-bible.md Template

```markdown
# "Title" Story Bible

## Project Information
- Genre / Medium: [Feature 100 min / One-act play 30 min / Series 12 episodes ...]
- Entry Path: [From scratch / Revision / Adaptation / Short film / Idea validation]
- Target Audience and Budget Tier: [...]
- Reference Film List: [3–5 films in the same genre, each with one sentence on "how it handles the climax"]
- Related Files: [One line each for outline.md, treatment.md, script.txt, including last update date]

## Current Phase
- Phase: [0–7], [Skipped: ...]
- Next Step: [One sentence]

## Settled Decisions (Record conclusions only; any change must be logged)
- Premise:
- Controlling Idea:
- Ending:
- Protagonist and Antagonist:
- Other Decisions No Longer Up for Discussion:

## 1 Premise and Theme
- Initial Spark / Why Care:
- Core Idea in One Sentence (can be conventional):
- What-If Question:
- Premise (character trait + leads to + ending):
- Controlling Idea (value + cause; idealistic / pessimistic / ironic):
- The Third Rail: Desire =    ; Misbelief =    ; Origin Scene =    ; Three Turning-Point Scenes =
- Thematic Keywords and Attitude Shifts: Starting attitude -> Ending attitude (Protagonist); (Antagonist)
- Dramatic Core / Engine / Pivot:
- Hicks's Five Questions: Who / Antagonist / Why oppose / What changes in the outcome / Why now
- One-Sentence Story (Snyder's four elements):
- Logline (protagonist + Inciting Incident + challenge + stakes + theme):
- World Rules (must be revealed within the first 25 pages):

## 2 Structure
- Ending:
- Opening (Opening Image):
- Plot Point I / II:
- Midpoint: [False victory / False defeat], inverse relationship with "All Is Lost":
- BS2 Page Table: (See worksheet below, scaled to target page count)
- Act Ratios and Length of Final Act:
- Relationship Between Subplot and Controlling Idea: [Contradiction / Resonance / Foreshadowing / Complication]
- Tonal Image of Climax:
- Ending Type (Lu Jun's Eight Methods):

## 3 Character and Conflict
| Character | Physical | Social | Psychological / Personal Premise | Specific Category | Attitude Toward Theme | Relationship to Protagonist |
|---|---|---|---|---|---|---|
- Unity of Opposites Binding Agent:    ; Can only be broken by the demise of    's   
- Antagonist's Weapon (>=1):
- Protagonist's Shackles:
- Protagonist Growth Arc (Starting point -> Ending point, intermediate steps):
- Image System / Core Prop:

## 4 Scene List
- Step Outline File: [Filename]; Scene count:   ; Card count:   (Act III:   cards)
- Deleted Scenes and Reasons:

## 5 First Draft Progress
- [Date] Scene x / Page y

## 6 Revision
| Goal | Source Checklist | Status |
|---|---|---|

## 7 Submission
- Logline:
- One-Page Synopsis File:
- PROBLEM Self-Check Results:
- Target: [Buyer / Contest / Representation]

## Decision Log
- [Date] What was changed <- Why
```

---

## I-2. series-bible variant (television)

Internal planning form, not a published book template. Insert after project info. Keep the other bible sections; fill applicable series fields, not feature-only counters.

```markdown
## Series bible

- Stage/state: `sw-workflow`
- Engine (`sw-series-showrunning` / `sw-premise-theme`): concept, conflict, and theme that generate episodes; Rabkin one-sentence repeated pattern
- Arena (Landau / `sw-series-showrunning`): the world the show lives in
- Franchise (Landau / `sw-series-showrunning`): weekly verbs the show can replay
- Form (Grace / Landau / `sw-series-showrunning`): series, serial, or soap; closed, serialized, or hybrid as distinct choices
- Six future ideas (Landau / `sw-series-showrunning`): springboards that test the engine
- Pilot (Landau / Rabkin / `sw-series-showrunning`): first-episode design
- Season arc (`sw-series-showrunning`; Yorke via `sw-story-structure` and `sw-character-conflict`): season-long story shape
- Episode grid (`sw-series-showrunning`): pointer to the external per-episode file; actual act count; A/B/C beat-to-scene mappings; optional teaser/tag only if the format uses them; Douglas four-act example is not a fixed grid
- Continuity (Curry / Rabkin / Grace / `sw-series-showrunning`; document layout `sw-format-adaptation`): incoming and outgoing cliff; emotional state and known facts; open landmines; natural lengths
```

---

## II. Phase 2 Worksheet: BS2 Page Count Conversion

Based on 110 pages as a baseline, multiply by the target page count and round to the nearest whole number:

| Beat | Ratio | 100 Pages | 90 Pages | 30-Page Short |
|---|---|---|---|---|
| Opening Image | 1% | 1 | 1 | 1 |
| Theme Stated | 5% | 5 | 4 | 2 |
| Catalyst | 11% | 11–12 | 10 | 3 |
| Break into Two | 23% | 23–25 | 21 | 7 |
| B Story | 27% | 27 | 25 | 8 |
| Midpoint | 50% | 50 | 45 | 15 |
| All Is Lost | 68% | 68–70 | 61 | 20 |
| Dark Night of the Soul | 68–77% | 70–77 | 61–69 | 20–23 |
| Break into Three | 77% | 77–79 | 69 | 23 |
| Final Image | 100% | 100 | 90 | 30 |

Table format: `Beat | Page | One-sentence summary`. Verification after completion: Setup <= 25%; Catalyst <= Page 20; the final act is the shortest.

---

## III. Phase 4 Worksheet: Step Outline Row Format

```
Scene # | INT./EXT. LOCATION - DAY/NIGHT | One sentence (who did what, outcome differed from expectation) | Value Start->End | Structural Position | +/- | ><
```

- Write values as positive/negative binary pairs: `obedience(+) -> violation(-)`, `trust(-) -> trust(+)`. Delete scenes where start and end values are identical.
- For `><`, write "who wants what, who blocks, who wins". Write only one conflict per scene.
- For structural position, use the BS2 beat name or the act/sequence number.
- Divide 40 cards into four rows: 1–25% / 25–50% / 50–75% / 75–100%; if Act III has fewer than 6 cards, go back and inspect the subplots and the six key structural deficiencies.

---

## IV. Phase 6 Worksheet: Sources for Revision Goal Table

Run through in order, copying failed items into a one-line revision target:

1. `sw-story-structure` Section 10: 13 Structural Diagnostic Questions
2. `sw-character-conflict` Section 8: 14 Character Diagnostic Questions
3. `sw-scene-craft` Section 9: 13 Scene Diagnostic Questions
4. `sw-dialogue` Section 9: 14 Dialogue Diagnostic Questions
5. `sw-format-adaptation` Section 6: 11 Format Diagnostic Questions
6. Snyder's Nine Diagnostic Questions (at the end of `sw-story-structure` Section 11)

When reviewing in parallel, each agent runs only one checklist, with the standardized output format: `Checklist ID-Question # | Location (Scene/Page) | Issue in one sentence | Recommendation in one sentence`.

---

## V. Example Entry (Abbreviated, Fictional Project)

```markdown
# "Night Shift" Story Bible

## Project Information
- Genre / Medium: Feature 95 min, family drama
- Entry Path: From scratch
- Reference Film List: *Tokyo Story* (events occurring offscreen), *Manchester by the Sea* (unreconciled ending), *Yi Yi* (multi-strand resonance)

## Current Phase
- Phase: 3
- Next Step: Give the father a weapon (he holds his daughter's tuition money)

## Settled Decisions
- Premise: Excessive sense of duty leads to estrangement between loved ones
- Controlling Idea: Family members lose each other because each carries burdens on the other's behalf instead of speaking to one another (pessimistic)
- Ending: The daughter moves away; the father cooks for himself for the first time, burns the food, and finishes eating it anyway
- Protagonist and Antagonist: Daughter vs. Father; Binding agent = the shared house and the mother's illness

## 1 Premise and Theme
- Thematic Keyword: Responsibility; Daughter's starting attitude "carrying the burden is love" -> Ending attitude "saying it out loud is love"; Father from start to finish "carrying the burden is love" (unchanging, constituting the tragedy)
- Dramatic Core: A family of three, each keeping the same secret from the other two (the mother's medical condition)
- World Rules: The mother's illness must be stated in one sentence by a doctor on page 8, never explained again in the rest of the film

## 2 Structure
- Midpoint: The daughter thinks her father agreed to let her move away (false victory); All Is Lost: The father uses her tuition money to pay for the mother's surgery
- BS2: Theme p5 / Catalyst p11 / Act II p24 / Midpoint p48 / All Is Lost p66 / Act III p74 / Final Image p95
- Tonal Image: The burnt meal

## Decision Log
- 2026-09-06 Ending changed from "father-daughter reconciliation" to "father finishes the burnt meal" <- The original ending was too neat and contradicted the pessimistic Controlling Idea
```

---

## VI. Opening Script for Resumed Sessions (For AI Use)

After reading the bible, speak three sentences to the user:

> Project "X", [genre/length]. Last session ended at Phase N ([Phase Name]); settled: [premise in one sentence], [ending in one sentence]. The next step is [the "Next Step" from the bible]. I will proceed from here unless you would like to revise any of the above.

Do not rehash the entire bible; do not re-interrogate settled decisions.
