## Why

Discovery AI sessions miss platforms across all ecosystem layers when those platforms don't use "digital twin" language, are non-English or government-led, or are niche open-source tools with low visibility (e.g., GeoDatalytics — an urban resilience analytics toolkit absent from all three model responses). There is no structured way to measure recall across model runs or track which discovery gap categories are systematically under-covered.

## What Changes

- Add `tests/discovery-fixtures.md` — curated list of expected platforms grouped by gap category (why a model might miss them), used as the recall test benchmark
- Add `tests/eval-discovery.md` — Claude Code CLI prompt that reads all `responses/global-platforms-discovery-*.md` files, checks each against the fixture, and writes a coverage report
- Add `tests/reports/` — output directory for generated coverage reports (`YYYY-MM-DD-coverage.md`)

## Capabilities

### New Capabilities

- `discovery-fixtures-file`: Defines the structure and content of `tests/discovery-fixtures.md` — the fixture file that groups expected platforms by discovery gap category
- `discovery-eval-prompt`: Defines the structure and behaviour of `tests/eval-discovery.md` — the Claude Code CLI prompt that runs a recall check across all model discovery responses and writes a report to `tests/reports/`
- `discovery-coverage-report`: Defines the format of generated coverage reports in `tests/reports/` — per-gap-category coverage table plus a per-model summary

### Modified Capabilities

(none)

## Impact

- New `tests/` directory with three new files and a `reports/` subdirectory
- No changes to existing prompts, docs, or CSV
- The eval prompt depends on discovery responses following the existing naming pattern `responses/global-platforms-discovery-*.md` and the YAML metadata block format (`model:`, `date:`, `prompt:`)
