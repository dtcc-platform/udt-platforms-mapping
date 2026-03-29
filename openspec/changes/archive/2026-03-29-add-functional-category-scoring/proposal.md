## Why

The current comparison output separates functional categorization (Part 4) into a prose tag list, disconnected from the scored dimensions table. This makes it impossible to compare platforms across functional roles in a single glance, and the tag-list format is inconsistent with the 1–5 scoring used everywhere else in the research workflow.

## What Changes

- Add six functional category columns to the Part 1 scoring table: `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`
- Add 1–5 rubrics for all six functional categories to `prompts/platform-comparison.md` (alongside existing dimension rubrics)
- Add a column legend (abbreviation key) immediately below the Part 1 table instruction in `prompts/platform-comparison.md`
- Add functional category rubrics to `docs/methodology.md` alongside the existing workflow prose
- Update the example profile in `prompts/platform-comparison.md` to include functional category scores
- Remove Part 4 (Functional Categorization) from the prompt output format — now redundant
- Update the spec: three-part output (was four), Part 1 now includes category columns with 1–5 scores

## Capabilities

### New Capabilities

_(none — this change extends an existing capability)_

### Modified Capabilities

- `platform-comparison-prompt`: Part 1 scoring table gains six functional category columns (1–5 scores); Part 4 removed; rubrics and legend added to prompt and methodology.

## Impact

- `prompts/platform-comparison.md` — primary prompt file modified
- `docs/methodology.md` — new functional category rubrics section added
- `openspec/specs/platform-comparison-prompt/spec.md` — four-part output requirement updated to three-part; new category scoring requirement added
