## MODIFIED Requirements

### Requirement: reflect/ holds benchmarking and reporting per cycle

`reflect/discovery/` SHALL contain two subfolders: `benchmarking/` and `reporting/`. `reflect/rating/` SHALL be scaffolded with the same two subfolders.

`reflect/discovery/benchmarking/` SHALL contain: `benchmark.md`, `prompt.md` (the eval runner), and `coverage.md` (the generated coverage report). `reflect/discovery/reporting/` SHALL contain: `prompt.md` (the inventory/reporting prompt) and `ecosystem.md`. `reflect/rating/reporting/` SHALL contain: `prompt.md`, `ecosystem.csv`, and `ecosystem-map.html`. `workflow/prompts-status/` SHALL contain: `prompt.md` and `report.md`. `workflow/presentation/` SHALL contain: `prompt.md` and `deck.md`.

Each subfolder follows the same pattern: a `prompt.md` that drives the work, outputs at the same level.

#### Scenario: Researcher runs the benchmarking eval

- **WHEN** a researcher runs the discovery benchmarking eval
- **THEN** the prompt is at `reflect/discovery/benchmarking/prompt.md` and the output lands at `reflect/discovery/benchmarking/coverage.md`

#### Scenario: Researcher generates the ecosystem report

- **WHEN** a researcher runs the reporting prompt
- **THEN** the prompt is at `reflect/discovery/reporting/prompt.md` and the output is `ecosystem.md` in the same folder

#### Scenario: Researcher runs the workflow audit

- **WHEN** a researcher runs the prompt-validity audit
- **THEN** the prompt is at `workflow/prompts-status/prompt.md` and the report is written to `workflow/prompts-status/report.md`

#### Scenario: Researcher generates the workflow presentation deck

- **WHEN** a researcher runs the workflow presentation prompt
- **THEN** the prompt is at `workflow/presentation/prompt.md` and the generated deck is written to `workflow/presentation/deck.md`
