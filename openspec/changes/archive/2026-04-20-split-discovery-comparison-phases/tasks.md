## 1. Create new scope files

- [x] 1.1 Create `docs/01-discovery-scope.md` with header, and the single four-row Layer criteria table (Layer | Definition | Criteria)
- [x] 1.2 Create `docs/01-comparison-scope.md` with header and the 12 dimension rubrics (Arch through Infra), extracted from the current `docs/01-scope.md`
- [x] 1.3 Delete `docs/01-scope.md`

## 2. Rewrite prompts/platform-discovery.md

- [x] 2.1 Update paste instruction in usage header to reference `docs/01-discovery-scope.md`
- [x] 2.2 Update the embedded scope placeholder guard to check for `docs/01-discovery-scope.md`
- [x] 2.3 Remove the embedded rubrics block (Relevance rubric + 12 dimensions) — replace with the Layer criteria table placeholder only
- [x] 2.4 Rewrite the output format: per-platform sections contain Organization, Link, License, Type, Layer only (no dimension scoring)
- [x] 2.5 Update the excluded platform template: Organization, Link, License, Type, Layer=excluded, Reason
- [x] 2.6 Rewrite the summary table to: Name | Link | Layer | Reason
- [x] 2.7 Update summary table ordering: core-platform first, then backbone, domain-module, excluded
- [x] 2.8 Update the DTCC required entry instruction to remove dimension scoring requirement
- [x] 2.9 Add a note that the prompt can be run in deep research mode for layer reassessment
- [x] 2.10 Update the example section to show the new field set (no dimensions, Layer field present)
- [x] 2.11 Remove the research dimensions scoring instructions

## 3. Update prompts/platform-comparison.md

- [x] 3.1 Update paste instruction in usage header to reference `docs/01-comparison-scope.md`
- [x] 3.2 Update the embedded scope placeholder guard to check for `docs/01-comparison-scope.md`
- [x] 3.3 Remove the embedded `[PASTE_SCOPE_HERE]` block content (it now only contains the 12 dimension rubrics stub)
- [x] 3.4 Remove `Relevance` column from Part 1 scoring table header and instructions
- [x] 3.5 Remove the Relevance reassessment instruction
- [x] 3.6 Remove the Layer revision instruction — Layer is carried from discovery unchanged
- [x] 3.7 Remove `Relevance` from the Part 1 legend
- [x] 3.8 Update `Layer` legend entry to note it is carried from discovery and not reassessed

## 4. Migrate docs/05-platform-inventory.csv

- [x] 4.1 Remove `Relevance` and `Phase` columns from the header
- [x] 4.2 Delete all discovery-only rows (previously Phase=discovery)
- [x] 4.3 Remove `Relevance` and `Phase` values from all remaining comparison rows
- [x] 4.4 Confirm new column order: Name, Link, Layer, Arch, Open, City, Mature, Integ, Gov, Viz, DM, Sim, IoT, Std, Infra, Model, Date

## 5. Verify

- [x] 5.1 Confirm `docs/01-scope.md` no longer exists
- [x] 5.2 Confirm `docs/01-discovery-scope.md` contains only the Layer criteria table (no rubrics)
- [x] 5.3 Confirm `docs/01-comparison-scope.md` contains only the 12 dimension rubrics (no Layer table)
- [x] 5.4 Confirm discovery prompt paste instruction references `docs/01-discovery-scope.md`
- [x] 5.5 Confirm comparison prompt paste instruction references `docs/01-comparison-scope.md`
- [x] 5.6 Confirm discovery prompt output format contains no dimension scoring fields
- [x] 5.7 Confirm comparison Part 1 table has no Relevance column and Layer is marked as read-only
- [x] 5.8 Confirm CSV header matches: Name, Link, Layer, Arch…Infra, Model, Date
