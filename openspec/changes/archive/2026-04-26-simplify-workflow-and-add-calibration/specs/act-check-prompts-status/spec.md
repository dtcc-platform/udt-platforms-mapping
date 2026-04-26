## ADDED Requirements

### Requirement: Prompt-status check exists as a CLI maintenance prompt under act
The repository SHALL contain a file at `act/check-prompts-status.md`. This file SHALL be a CLI-only maintenance prompt that audits live repository prompt files for validity and freshness. It SHALL NOT be a Web-mode prompt.

The prompt SHALL instruct the AI to inspect live prompt files under `act/` and `reflect/` only.

#### Scenario: Researcher runs the prompt-status check
- **WHEN** a researcher tells their AI CLI to run `act/check-prompts-status.md`
- **THEN** the AI executes the audit directly in CLI mode without asking for run mode selection

#### Scenario: Archived or calibration prompts exist
- **WHEN** prompt-like files exist under `openspec/changes/`, `openspec/changes/archive/`, or `calibration/`
- **THEN** the audit ignores them and checks only the live prompts under `act/` and `reflect/`

### Requirement: Prompt-status check verifies live prompts against governing files
For each live prompt file, the audit SHALL identify:
- its governing baseline prompt spec under `openspec/specs/`
- any shared baseline contract spec the prompt explicitly relies on
- any files declared under its `## Required Inputs` section, if present

The audit SHALL verify that:
- the prompt file exists
- each declared required-input file exists
- the prompt's declared input set is compatible with the governing spec
- the prompt's stated behavior does not directly contradict the governing spec

The audit mapping for live prompts SHALL use the current baseline set. In particular:
- `reflect/discovery/benchmarking/prompt.md` SHALL be checked against `openspec/specs/reflect-discovery-benchmarking/spec.md`
- `reflect/discovery/reporting/prompt.md` SHALL be checked against `openspec/specs/reflect-discovery-reporting-prompt/spec.md`
- `reflect/rating/reporting/prompt.md` SHALL be checked against `openspec/specs/reflect-rating-reporting/spec.md`

#### Scenario: Prompt has a missing required input file
- **WHEN** a live prompt declares a required input path that does not exist
- **THEN** the audit marks that prompt as `invalid` and records the missing path in the report

#### Scenario: Prompt omits a required input required by spec
- **WHEN** a governing spec requires an input file declaration that the prompt does not include
- **THEN** the audit marks that prompt as `invalid` and records the mismatch in the report

#### Scenario: Rating reporting has a governing baseline spec
- **WHEN** the audit checks `reflect/rating/reporting/prompt.md`
- **THEN** it uses `openspec/specs/reflect-rating-reporting/spec.md` as the governing baseline spec

### Requirement: Prompt-status check distinguishes freshness dependencies from runtime inputs
The audit SHALL distinguish freshness dependencies from runtime inputs.

Freshness dependencies SHALL include the governing baseline prompt spec and any shared baseline contract spec the prompt explicitly relies on. Runtime inputs SHALL include files named under `## Required Inputs`.

A newer freshness dependency than the prompt SHALL produce status `review-needed`. A newer runtime-input file than the prompt SHALL NOT by itself make the prompt stale.

#### Scenario: Governing spec changed after prompt
- **WHEN** the latest git change to a prompt's governing baseline spec is newer than the latest git change to the prompt file
- **THEN** the audit marks the prompt as `review-needed`

#### Scenario: Per-run data changed after prompt
- **WHEN** `plan/rating/platforms.md` has a newer git change than `act/rating/prompt.md`
- **THEN** the audit does not mark the prompt stale on that fact alone

### Requirement: Prompt-status check uses three statuses and writes a report
The audit SHALL assign exactly one status to each audited prompt:
- `valid`
- `review-needed`
- `invalid`

The audit SHALL write its results to `act/check-prompts-status-report.md`, overwriting any existing file.

The report file at `act/check-prompts-status-report.md` SHALL contain a header block followed by a single flat summary table with one row per audited prompt.

The header block SHALL state:
- audit date
- number of prompts checked
- the directories scanned

The summary table SHALL contain exactly these columns:
- `Prompt`
- `Status`
- `Governing Spec`
- `Shared Contracts`
- `Required Inputs`
- `Reason`

After the summary table, the report SHALL contain one `##` section per audited prompt in path order.

Each prompt section SHALL include:
- the final status
- the governing spec path
- the declared required inputs
- the freshness dependencies considered
- the latest git commit reference for the prompt
- the latest git commit reference for any newer freshness dependency, if applicable
- a flat bullet list of findings

#### Scenario: Researcher reruns the prompt-status check
- **WHEN** a researcher reruns the prompt-status check
- **THEN** the previous `act/check-prompts-status-report.md` is replaced with a new report reflecting the current repository state

#### Scenario: Prompt passes all checks
- **WHEN** a prompt has existing dependencies, matching declarations, and no newer freshness dependencies
- **THEN** the audit records status `valid`

#### Scenario: Prompt contradicts governing contract
- **WHEN** a prompt's declared behavior directly conflicts with its governing baseline spec
- **THEN** the audit records status `invalid`
