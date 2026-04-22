## Why

Spec folder names still use the old `platform-*` / `discovery-*` convention from before the AR restructure. They should mirror the file path they govern: `phase-cycle-subfolder` (e.g. `act-discovery-prompt`, `reflect-discovery-benchmarking-prompt`). Cross-cutting specs that don't map to a single file keep descriptive names.

## What Changes

- **BREAKING** Rename 9 spec folders in `openspec/specs/` to match AR path naming
- Update `platform-comparison-prompt` and `platform-comparison-scope-file` to also fix stale paths (still reference old `prompts/` and `docs/` locations)
- Cross-cutting specs (`fixture-alias-column`, `prompt-markdown-format`, `prompt-paste-boundary`, `prompt-placeholder-guard`, `relevance-score`, `ar-folder-layout`) keep their existing names — they don't map to a single AR file path

## Capabilities

### New Capabilities

_(none)_

### Modified Capabilities

- `platform-discovery-prompt` → renamed to `act-discovery-prompt`
- `platform-inventory-prompt` → renamed to `reflect-discovery-reporting-prompt`
- `discovery-eval-prompt` → renamed to `reflect-discovery-benchmarking-prompt`
- `discovery-fixtures-file` → renamed to `reflect-discovery-benchmarking-benchmark`
- `discovery-coverage-report` → renamed to `reflect-discovery-benchmarking-coverage`
- `platform-discovery-scope-file` → renamed to `plan-discovery-scope`
- `platform-inventory-csv` → renamed to `reflect-discovery-reporting-ecosystem`
- `platform-comparison-prompt` → renamed to `act-rating-prompt` + fix stale path `prompts/platform-comparison.md` → `act/rating/prompt.md`
- `platform-comparison-scope-file` → renamed to `plan-rating-scope` + fix stale path `docs/01-comparison-scope.md` → `plan/rating/scope.md`

## Impact

- Spec folder renames only — no content changes except stale path fixes in the two rating specs
- Any OpenSpec tooling that references spec names by folder will need to find them at new paths
- Old spec folders are removed after rename
