## 1. Update Prompt — Scoring Table and Legend

- [x] 1.1 Add six category columns (`Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`) to the Part 1 table header in `prompts/platform-comparison.md`
- [x] 1.2 Add a column legend block immediately below the Part 1 table instruction, listing all abbreviated headers (both dimension and category) with full names and one-line descriptions
- [x] 1.3 Update the Part 1 table instruction text to reference "six dimension columns and six functional category columns"

## 2. Update Prompt — Functional Category Rubrics

- [x] 2.1 Add a `Functional Categories` subsection to the Research Dimensions section in `prompts/platform-comparison.md` with a 1–5 rubric table for each of the six categories (`visualization`, `data-management`, `simulation`, `iot-sensing`, `standards`, `infrastructure`)
- [x] 2.2 Ensure each rubric provides anchor descriptions for scores 1, 3, and 5 at minimum

## 3. Update Prompt — Remove Part 4 and Update Output Format

- [x] 3.1 Remove the Part 4 (Functional Categorization) section from the Output Format in `prompts/platform-comparison.md`
- [x] 3.2 Update the Output Format preamble to reference three parts (not four)
- [x] 3.3 Update the example profile in `prompts/platform-comparison.md` to add a `Functional Categories` row or note showing how category scores appear in the table (scores live in Part 1 only, not in profiles — clarify this in the example or a note)

## 4. Update Methodology

- [x] 4.1 Add a `## Functional Category Rubrics` section to `docs/methodology.md` with the same six rubrics (1–5 anchors) from the prompt
- [x] 4.2 Add the column legend (abbreviation key) to the same section so researchers have a complete reference

## 5. Update Spec

- [x] 5.1 Apply the delta spec at `openspec/changes/add-functional-category-scoring/specs/platform-comparison-prompt/spec.md` to `openspec/specs/platform-comparison-prompt/spec.md`:
  - Replace the four-part output requirement with the three-part version
  - Add the functional category column requirement
  - Add the functional category rubric requirement
