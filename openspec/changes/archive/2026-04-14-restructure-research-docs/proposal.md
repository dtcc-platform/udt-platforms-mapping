## Why

The scoring rubrics for all 13 dimensions (Relevance + 12 research dimensions) are duplicated across `docs/02-methodology.md` and the prompt files, creating a maintenance burden whenever rubrics evolve. The discovery and comparison prompts also diverge unnecessarily — they cover different columns and have different inclusion logic — when the only meaningful difference should be research depth.

## What Changes

- **`docs/01-scope.md`**: Replace binary include/exclude criteria with a single **Relevance (0–5)** rubric. This becomes the canonical definition of what belongs in the study.
- **`docs/02-methodology.md`**: Remove all scoring rubrics (Arch, Open, City, Mature, Integ, Gov, Viz, DM, Sim, IoT, Std, Infra). Keep only workflow, file naming conventions, and the CSV column reference. Rubrics are now owned by the prompts and seeded from `01-scope.md`.
- **`prompts/platform-discovery.md`**: **BREAKING** — add all 12 scoring dimensions (currently only 6); replace binary include/exclude with Relevance column (0–5); replace `-1` sentinel with `0` (not assessed); add `[PASTE_SCOPE_HERE]` guard requiring `01-scope.md` to be pasted before running; remove deep-research instruction.
- **`prompts/platform-comparison.md`**: Add `[PASTE_SCOPE_HERE]` guard; remove inline rubric definitions (now supplied via pasted scope); retain deep-research instruction as the sole structural difference from discovery.
- **`docs/05-platform-inventory.csv`**: **BREAKING** — add `Relevance` column; existing `-1` scores replaced with `0`.

## Capabilities

### New Capabilities

- `relevance-score`: Rubric defining Relevance 0–5 as the replacement for the binary include/exclude gate in scope and discovery

### Modified Capabilities

- `platform-discovery-scope`: Scope criteria change from binary (include/exclude with three named criteria each) to a single 0–5 Relevance scale
- `platform-discovery-prompt`: Discovery prompt gains 6 functional columns (Viz/DM/Sim/IoT/Std/Infra), Relevance column, `[PASTE_SCOPE_HERE]` guard, drops deep-research requirement and drops `-1` sentinel
- `platform-comparison-prompt`: Comparison prompt gains `[PASTE_SCOPE_HERE]` guard and removes inline rubric definitions
- `platform-inventory-csv`: CSV schema gains `Relevance` column; `-1` sentinel removed

## Impact

- `docs/01-scope.md` — content replaced
- `docs/02-methodology.md` — rubric sections removed
- `prompts/platform-discovery.md` — structure and column set changed
- `prompts/platform-comparison.md` — guard added, inline rubrics removed
- `docs/05-platform-inventory.csv` — schema change (new column, sentinel value change)
- Existing discovery response files in `responses/` are not affected (historical records)
- Anyone pasting prompts directly must now also paste `01-scope.md` into the `[PASTE_SCOPE_HERE]` slot
