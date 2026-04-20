## 1. Update docs/01-scope.md

- [x] 1.1 Rewrite the file's opening paragraph to frame the project goal as UDT ecosystem mapping (covering all three layers), not a platform review
- [x] 1.2 Add a "Ecosystem Layer Taxonomy" section defining the three layer values (`core-platform`, `backbone`, `domain-module`) with a table, and a note that Layer and Relevance are orthogonal
- [x] 1.3 Update the "What Is a UDT Platform?" definition to reference the three layers explicitly as the search boundary

## 2. Update data/platform-inventory.csv

- [x] 2.1 Add `Layer` column to the CSV header between `Phase` and `Relevance`
- [x] 2.2 Backfill `Layer` values for all existing rows using best-guess assignment from platform names and existing scores

## 3. Update prompts/platform-discovery.md

- [x] 3.1 Add `Layer` field to the per-platform identification block (both the in-scope and out-of-scope output templates)
- [x] 3.2 Add `Layer` column to the summary table template
- [x] 3.3 Add explicit multi-layer search instruction telling the model to search across all three layers and not limit discovery to platforms that self-identify as digital twins
- [x] 3.4 Update the example section to include the `Layer` field with a sample value

## 4. Update prompts/platform-comparison.md

- [x] 4.1 Add `Layer` column to the Part 1 scoring table (between `Link` and `Relevance`)
- [x] 4.2 Add instruction for the model to reassess and revise the `Layer` assignment during deep research, with rationale required in the per-platform profile when reclassifying
- [x] 4.3 Update the Part 1 legend to include the `Layer` column description

## 5. Verify

- [x] 5.1 Confirm CSV header order is: `Name`, `Link`, `Phase`, `Layer`, `Relevance`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`, `Model`, `Date`
- [x] 5.2 Confirm all existing CSV rows have a `Layer` value (no blanks in backfill)
- [x] 5.3 Confirm discovery prompt example shows `Layer` field
- [x] 5.4 Confirm comparison Part 1 table header includes `Layer` before `Relevance`
