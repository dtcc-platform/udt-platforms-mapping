## Context

The comparison prompt currently produces a four-part output. Part 1 is a scoring table covering six research dimensions. Part 4 is a separate functional categorization table that assigns platforms to tag categories using a comma-separated list. The tag format is inconsistent with the 1–5 scoring used throughout the rest of the prompt and is disconnected from the main scoring table — a researcher cannot sort or scan functional roles alongside dimension scores in a single view.

## Goals / Non-Goals

**Goals:**

- Extend the Part 1 scoring table with six functional category columns using the same 1–5 integer format
- Define 1–5 rubrics for each functional category, consistent in structure with the six existing dimension rubrics
- Provide an abbreviation legend immediately below the Part 1 table instruction so column headers are unambiguous
- Surface the same rubrics in `docs/methodology.md` as a reference for researchers not reading the full prompt
- Remove Part 4 (now redundant)

**Non-Goals:**

- Changing the six existing research dimension rubrics or scores
- Adding new functional categories beyond the current six
- Changing the Part 2 profile structure (category scores live only in the table, not in profiles)

## Decisions

**1-5 scores over boolean for categories**

Binary presence markers (✓/–) would answer "does this platform do X?" A 1–5 scale answers "how well?" — for example, CesiumJS and deck.gl are both visualization tools but differ meaningfully in scope and purpose. The 1–5 scale produces analytically useful gradations and keeps the table format uniform. No additional formatting rules are needed since the existing score notation rules apply directly.

**Abbreviations with inline legend, not full column headers**

Full category names (`data-management`, `iot-sensing`) make the 14-column table unwieldy in any Markdown viewer. Abbreviated headers (`DM`, `IoT`) are short enough to render acceptably. A legend block immediately below the Part 1 table instruction in the prompt resolves ambiguity without requiring the reader to consult a separate file. The same legend appears in `docs/methodology.md`.

**Rubrics in prompt and methodology, not a standalone file**

The dimension rubrics live in the prompt and are self-contained there. Mirroring category rubrics into `docs/methodology.md` gives researchers a stable reference without duplicating the full prompt. A new dedicated file would fragment the reference surface unnecessarily.

**Part 4 removal**

With category scores in Part 1, Part 4 adds no information. Removing it shortens the output and eliminates the inconsistency between tag-list and numeric formats.

## Risks / Trade-offs

**Table width** → The 14-column table may wrap in narrow viewports (e.g., GitHub mobile). Abbreviations mitigate this but do not eliminate it. Acceptable given that the primary use is desktop Markdown viewers.

**Rubric subjectivity for categories** → Like dimension rubrics, category rubrics require researcher judgment. The 1–5 anchor points for categories are coarser (fewer concrete criteria) than dimension rubrics, which are grounded in observable technical properties. The rubrics should be written with concrete anchor examples to minimise drift.

**Existing responses become incompatible** → Saved comparison responses in `responses/` will not have category columns. No migration is needed — they remain valid for their dimensions; category scoring applies to future sessions only.
