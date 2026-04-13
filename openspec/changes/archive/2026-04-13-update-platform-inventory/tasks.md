## 1. Scope document — exclusion criteria

- [x] 1.1 Add an "Exclusion Criteria" section to `docs/01-scope.md` with three named criteria: **Spec or Standard**, **Single Domain**, **General Purpose** — each with a one-sentence definition and at least one named example platform

## 2. Discovery prompt — Criterion column and excluded platforms

- [x] 2.1 Update summary table column list in `prompts/platform-discovery.md` to include a `Criterion` column (after `Gov`)
- [x] 2.2 Add instruction text stating that excluded platforms SHALL appear in the summary table with `-1` in all score columns and their exclusion criterion label in the `Criterion` column
- [x] 2.3 Add instruction that per-platform `##` sections are NOT required for excluded platforms
- [x] 2.4 Update the example output in the prompt to show an excluded platform row (if an example table is present)

## 3. Inventory file — convert to CSV

- [x] 3.1 Rename `docs/05-platform-inventory.md` to `docs/05-platform-inventory.csv`
- [x] 3.2 Rewrite the header row to the new column order: `Name,Link,Phase,Arch,Open,City,Mature,Integ,Gov,Viz,DM,Sim,IoT,Std,Infra,Model,Date`
- [x] 3.3 Convert all existing rows: strip Markdown link syntax from `Link` (keep URL only), add `Phase=comparison` for all existing rows
- [x] 3.4 Verify the CSV parses cleanly (no stray pipes, no Markdown in cells)

## 4. Inventory prompt — full rewrite

- [x] 4.1 Rewrite `prompts/platform-inventory.md` usage header to state the output target is `docs/05-platform-inventory.csv`
- [x] 4.2 Rewrite Step 1 to identify two qualifying file types: `prompt: platform-discovery` and `prompt: platform-comparison`
- [x] 4.3 Rewrite Step 2/3 to extract discovery summary table rows with `Phase=discovery` and set Viz/DM/Sim/IoT/Std/Infra to `-1`
- [x] 4.4 Rewrite Step 2/3 to extract comparison Part 1 rows with `Phase=comparison`
- [x] 4.5 Update output column order to: `Name,Link,Phase,Arch,Open,City,Mature,Integ,Gov,Viz,DM,Sim,IoT,Std,Infra,Model,Date`
- [x] 4.6 Update output format from GFM table rows to CSV rows
- [x] 4.7 Update preamble output instructions to describe CSV output and note skipped files

## 5. Methodology diagram update

- [x] 5.1 Update the Mermaid diagram in `docs/02-methodology.md`: change `05-platform-inventory.md` reference to `05-platform-inventory.csv`
- [x] 5.2 Add a `dresp -->|"auto-scan"| inv` edge to the Mermaid diagram (discovery responses also feed the inventory prompt, not only comparison responses)
