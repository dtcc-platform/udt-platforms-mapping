## Why

The platform inventory currently has no record of platforms that were considered and excluded during discovery, making it impossible to audit the inclusion boundary or compare how different models classify borderline platforms. The inventory also lacks a way to distinguish quick discovery-pass scores from deep comparison scores, preventing model-to-model comparisons at both research depths.

## What Changes

- Add formal exclusion criteria to `docs/01-scope.md` (three named categories: Spec or Standard, Single Domain, General Purpose)
- Update the discovery prompt to output excluded platforms in the summary table with `-1` scores and a `Criterion` column (used for both inclusion and exclusion labels)
- Convert `docs/05-platform-inventory.md` → `docs/05-platform-inventory.csv` with URL-only Link column
- Add `Phase` column to the inventory CSV (`discovery` or `comparison`) to distinguish score depth
- Rewrite `prompts/platform-inventory.md` to read both discovery responses (Phase=`discovery`) and comparison responses (Phase=`comparison`) and output CSV rows
- Update the Mermaid diagram in `docs/02-methodology.md` to reference `.csv`

## Capabilities

### New Capabilities

- `platform-inventory-csv`: The inventory file changes format (`.md` → `.csv`) and schema (adds `Phase` column, Link becomes URL-only, `-1` sentinel value for excluded/unresearched categories).

### Modified Capabilities

- `platform-inventory-prompt`: Prompt must now read both discovery and comparison responses, emit a `Phase` column, output CSV rows instead of GFM rows, and use `-1` for excluded platforms' functional category scores.
- `platform-discovery-prompt`: Summary table gains a `Criterion` column; excluded platforms are listed with `-1` scores and an exclusion criterion label; usage header updated to reference new inventory CSV.
- `platform-discovery-scope`: Gains a formal exclusion criteria section (three named criteria mirroring the three inclusion criteria).

## Impact

- `docs/01-scope.md` — exclusion criteria section added
- `docs/02-methodology.md` — Mermaid diagram updated (`.md` → `.csv` reference)
- `docs/05-platform-inventory.md` renamed to `docs/05-platform-inventory.csv`, schema extended
- `prompts/platform-discovery.md` — summary table column added, excluded platforms required
- `prompts/platform-inventory.md` — full rewrite (reads discovery + comparison, outputs CSV)
