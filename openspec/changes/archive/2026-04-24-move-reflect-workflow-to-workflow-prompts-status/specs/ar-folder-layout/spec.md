## MODIFIED Requirements

### Requirement: Repository is organised as action research phases at top level

The repository SHALL use four top-level folders matching the action research phases: `plan/`, `act/`, `observe/`, and `reflect/`. Each phase folder SHALL contain exactly one subfolder per research cycle. The only research cycles are `discovery/` and `rating/`.

The repository MAY also contain a top-level `workflow/` folder for workflow-level artifacts that are not part of a single research cycle.

No files SHALL live at the phase root level — all research-cycle content is inside a cycle subfolder. Each cycle is fully self-contained within its phase folder.

#### Scenario: Researcher navigates the repository

- **WHEN** a researcher opens the repository root
- **THEN** they see four phase folders (`plan/`, `act/`, `observe/`, `reflect/`) and MAY also see `workflow/` plus `README.md`, `AGENTS.md`, and tooling config

#### Scenario: Researcher follows one complete cycle

- **WHEN** a researcher wants to understand the discovery cycle end-to-end
- **THEN** they read `plan/discovery/`, `act/discovery/`, `observe/discovery/`, and `reflect/discovery/` in sequence without navigating outside those paths

### Requirement: reflect/ holds benchmarking and reporting per cycle

`reflect/discovery/` SHALL contain two subfolders: `benchmarking/` and `reporting/`. `reflect/rating/` SHALL be scaffolded with the same two subfolders.

`reflect/discovery/benchmarking/` SHALL contain: `benchmark.md`, `prompt.md` (the eval runner), and `coverage.md` (the generated coverage report). `reflect/discovery/reporting/` SHALL contain: `prompt.md` (the inventory/reporting prompt) and `ecosystem.md`. `reflect/rating/reporting/` SHALL contain: `prompt.md`, `ecosystem.csv`, and `ecosystem-map.html`. `workflow/prompts-status/` SHALL contain: `prompt.md` and `report.md`.

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
