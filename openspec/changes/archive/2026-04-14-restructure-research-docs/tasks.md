## 1. Rewrite docs/01-scope.md

- [x] 1.1 Replace binary inclusion/exclusion criteria with the Relevance 0–5 rubric table (level descriptions for 0–5)
- [x] 1.2 Add all 12 dimension rubrics (Arch, Open, City, Mature, Integ, Gov, Viz, DM, Sim, IoT, Std, Infra) after the Relevance rubric
- [x] 1.3 Update the seed list to annotate each platform with its Relevance score (e.g., DTCC = 5, Cesium = 3)
- [x] 1.4 Retain brief prose context explaining the study purpose (keep file useful as standalone onboarding doc)

## 2. Trim docs/02-methodology.md

- [x] 2.1 Remove the functional category rubrics section (Viz, DM, Sim, IoT, Std, Infra) — rubrics now live in 01-scope.md
- [x] 2.2 Update the workflow description to include the two-step paste (paste 01-scope.md into [PASTE_SCOPE_HERE], then paste prompt)
- [x] 2.3 Update the CSV column legend to include the new Relevance column and remove the -1 sentinel reference

## 3. Update prompts/platform-discovery.md

- [x] 3.1 Add `[PASTE_SCOPE_HERE]` placeholder and guard instruction at the rubric location
- [x] 3.2 Add 6 functional columns (Viz, DM, Sim, IoT, Std, Infra) to the summary table definition and per-platform output
- [x] 3.3 Add `Relevance` column to the summary table (bare integer 0–5); remove `Criterion` column
- [x] 3.4 Replace all `-1` references with `0`; remove named exclusion criterion labels
- [x] 3.5 Remove the deep-research instruction (discovery is first-pass only)
- [x] 3.6 Remove inline rubric definitions (now supplied via pasted scope)
- [x] 3.7 Update usage header to include the two-step paste instruction as step 1
- [x] 3.8 Update the example platform section to show Relevance field and all 12 dimension fields

## 4. Update prompts/platform-comparison.md

- [x] 4.1 Add `[PASTE_SCOPE_HERE]` placeholder and guard instruction at the rubric location
- [x] 4.2 Remove inline rubric definitions for all 12 dimensions (now supplied via pasted scope)
- [x] 4.3 Update usage header to include the two-step paste instruction as step 1
- [x] 4.4 Verify the `[PASTE_SELECTED_PLATFORMS_HERE]` guard still reads correctly after scope guard is added

## 5. Migrate docs/05-platform-inventory.csv

- [x] 5.1 Add `Relevance` column after `Phase` column; set all existing rows to `0`
- [x] 5.2 Replace all `-1` values in score columns with `0`
- [x] 5.3 Verify column order matches: Name, Link, Phase, Relevance, Arch, Open, City, Mature, Integ, Gov, Viz, DM, Sim, IoT, Std, Infra, Model, Date
