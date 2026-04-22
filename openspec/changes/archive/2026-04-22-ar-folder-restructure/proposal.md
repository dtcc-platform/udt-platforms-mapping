## Why

The repository currently has an ad-hoc folder layout (`docs/`, `prompts/`, `responses/`, `evals/`) that does not reflect the underlying research methodology. Restructuring to explicit action research phases makes the loop readable at a glance and prepares the project to host multiple research cycles cleanly.

## What Changes

- **BREAKING** Rename and reorganise all top-level folders into four AR phase folders: `plan/`, `act/`, `observe/`, `reflect/`
- Within each phase, the second level is the cycle type: `discovery/` and `rating/`
- Files lose cycle-type prefixes in their names (folder path carries that context)
- `responses/` contents move to `observe/<cycle>/`
- `prompts/` contents move to `act/<cycle>/prompt.md`
- `docs/` scope and policy files move to `plan/<cycle>/`; `methodology.md` is removed (README replaces it)
- `evals/discovery/` moves to `reflect/discovery/benchmarking/`; `run.md` renamed to `prompt.md`
- Inventory CSV and HTML move to `reflect/discovery/reporting/` alongside a `prompt.md`
- `rating/` cycle scaffolded empty under all four phases
- `source-policy.md` moves to `plan/rating/` only (discovery does not use it)
- README rewritten to explain the two-cycle action research structure

## Capabilities

### New Capabilities

- `ar-folder-layout`: The repository folder structure as an action research layout — phase → cycle → content, with README documenting the two-cycle loop

### Modified Capabilities

- `platform-discovery-prompt`: File path changes from `prompts/platform-discovery.md` to `act/discovery/prompt.md`
- `platform-discovery-scope-file`: File path changes from `docs/01-discovery-scope.md` to `plan/discovery/scope.md`
- `platform-inventory-prompt`: File path changes from `prompts/platform-inventory.md` to `reflect/discovery/reporting/prompt.md`
- `platform-inventory-csv`: File path changes from `docs/05-platform-inventory.csv` to `reflect/discovery/reporting/ecosystem.csv`
- `discovery-eval-prompt`: File path changes from `evals/discovery/run.md` to `reflect/discovery/benchmarking/prompt.md`
- `discovery-fixtures-file`: File path changes from `evals/discovery/benchmark.md` to `reflect/discovery/benchmarking/benchmark.md`
- `discovery-coverage-report`: File path changes from `evals/discovery/reports/coverage.md` to `reflect/discovery/benchmarking/coverage.md`

## Impact

- All internal path references in prompts and eval scripts need updating
- AGENTS.md and any agent skill files referencing old paths need updating
- README.md rewritten
- `docs/02-methodology.md` deleted
