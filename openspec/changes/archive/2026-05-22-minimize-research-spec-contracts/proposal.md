## Why

The active specs still carry migration-era wording, duplicated artifact indexes, and stale empty spec directories from previous renames. This makes the repository look less consistent than the current research workflow and increases the chance that future changes update one contract while leaving another stale.

## What Changes

- Simplify `research-artifact-naming` so it defines naming grammar rather than historical migration rules or a hard-coded index of specific spec names.
- Reduce `research-workflow-structure` to the minimum complete phase and artifact-location contract, avoiding duplicate ownership of each individual artifact.
- **BREAKING**: Retire the platform comparison benchmark stub by removing `act-platform-comparison-benchmark` and `act/benchmark-platform-comparison.md`.
- Remove empty obsolete directories under `openspec/specs/` that no longer contain active `spec.md` files.
- Keep active spec names aligned to `<phase>-<object>-<artifact-role>` and keep live `act/` prompt filenames verb-first.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `research-artifact-naming`: remove migration-era wording, remove hard-coded canonical spec name lists, and retain only the current naming grammar.
- `research-workflow-structure`: remove duplicate canonical artifact indexes and describe only the phase structure, artifact classes, and file ownership boundaries.
- `act-platform-comparison-benchmark`: retire the unused comparison benchmark stub capability.

## Impact

- Updates active OpenSpec specs under `openspec/specs/`.
- Removes obsolete empty directories under `openspec/specs/`.
- Removes the unused `act/benchmark-platform-comparison.md` stub and the active `act-platform-comparison-benchmark` spec.
- Does not change research output data, scoring rubrics, entity classification rules, or existing platform comparison/reporting behavior.
