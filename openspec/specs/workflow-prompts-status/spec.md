# Spec: workflow-prompts-status

## Purpose

Defines the workflow prompt-status audit at `workflow/prompts-status/`, including the CLI audit prompt, the status model it uses, and the structure of the report it writes.

## Requirements

### Requirement: Workflow prompt-status audit exists as a CLI maintenance workflow

The repository SHALL contain a file at `workflow/prompts-status/prompt.md`. This file SHALL be a CLI-only maintenance prompt that audits live repository prompt files for validity and freshness. It SHALL NOT be a Web-mode prompt.

The prompt SHALL instruct the AI to inspect live prompt files under `act/` and `reflect/` only.

#### Scenario: Researcher runs the prompt-status audit
- **WHEN** a researcher tells their AI CLI to run `workflow/prompts-status/prompt.md`
- **THEN** the AI executes the audit directly in CLI mode without asking for run mode selection

#### Scenario: Archived change prompts exist
- **WHEN** prompt-like files exist under `openspec/changes/` or `openspec/changes/archive/`
- **THEN** the audit ignores them and checks only the live prompts under `act/` and `reflect/`

### Requirement: Workflow prompt-status audit checks each prompt against governing files

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
- `reflect/discovery/benchmarking/prompt.md` SHALL be checked against `openspec/specs/reflect-discovery-benchmarking/spec.md` without requiring a separate discovery benchmarking coverage shared-contract spec
- `reflect/discovery/reporting/prompt.md` SHALL be checked against `openspec/specs/reflect-discovery-reporting-prompt/spec.md` without requiring a separate discovery-reporting ecosystem shared-contract spec
- `reflect/rating/reporting/prompt.md` SHALL be checked against `openspec/specs/reflect-rating-reporting/spec.md`

#### Scenario: Prompt has a missing required input file
- **WHEN** a live prompt declares a required input path that does not exist
- **THEN** the audit marks that prompt as `invalid` and records the missing path in the report

#### Scenario: Prompt omits a required input required by spec
- **WHEN** a governing spec requires an input file declaration that the prompt does not include
- **THEN** the audit marks that prompt as `invalid` and records the mismatch in the report

#### Scenario: Discovery benchmarking no longer has a separate coverage shared contract
- **WHEN** the audit checks `reflect/discovery/benchmarking/prompt.md`
- **THEN** it does not require a separate discovery benchmarking coverage spec as a freshness dependency

#### Scenario: Discovery reporting no longer has a no-op shared contract
- **WHEN** the audit checks `reflect/discovery/reporting/prompt.md`
- **THEN** it does not require a separate discovery-reporting ecosystem shared-contract spec as a freshness dependency

#### Scenario: Rating reporting has a governing baseline spec
- **WHEN** the audit checks `reflect/rating/reporting/prompt.md`
- **THEN** it uses `openspec/specs/reflect-rating-reporting/spec.md` as the governing baseline spec rather than treating the prompt as unguided

### Requirement: Workflow prompt-status audit distinguishes freshness dependencies from runtime inputs

The audit SHALL distinguish freshness dependencies from runtime inputs.

Freshness dependencies SHALL include the governing baseline prompt spec and any shared baseline contract spec the prompt explicitly relies on. Runtime inputs SHALL include files named under `## Required Inputs`.

A newer freshness dependency than the prompt SHALL produce status `review-needed`. A newer runtime-input file than the prompt SHALL NOT by itself make the prompt stale.

#### Scenario: Governing spec changed after prompt
- **WHEN** the latest git change to a prompt's governing baseline spec is newer than the latest git change to the prompt file
- **THEN** the audit marks the prompt as `review-needed`

#### Scenario: Per-run data changed after prompt
- **WHEN** `plan/rating/platforms.md` has a newer git change than `act/rating/prompt.md`
- **THEN** the audit does not mark the prompt stale on that fact alone

### Requirement: Workflow prompt-status audit uses three statuses

The audit SHALL assign exactly one status to each audited prompt:
- `valid`
- `review-needed`
- `invalid`

The audit SHALL use these meanings:
- `valid` — no missing files, no direct contract mismatch, and no newer freshness dependency
- `review-needed` — the prompt remains runnable, but a freshness dependency is newer or a likely drift signal exists
- `invalid` — the prompt has a missing dependency, broken declaration, or direct contradiction with its governing contract

#### Scenario: Prompt passes all checks
- **WHEN** a prompt has existing dependencies, matching declarations, and no newer freshness dependencies
- **THEN** the audit records status `valid`

#### Scenario: Prompt contradicts governing contract
- **WHEN** a prompt's declared behavior directly conflicts with its governing baseline spec
- **THEN** the audit records status `invalid`

### Requirement: Workflow prompt-status audit writes a structured report

The audit SHALL write its results to `workflow/prompts-status/report.md`, overwriting any existing file.

The prompt SHALL be runnable by a researcher telling the AI CLI either `run workflow/prompts-status/prompt.md` or `run the prompt validity audit`.

The report file at `workflow/prompts-status/report.md` SHALL contain a header block followed by a single flat summary table with one row per audited prompt.

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

If a runtime-input file is newer than a prompt but does not create a contract mismatch, the report SHALL NOT classify the prompt as stale on that basis alone.

The report MAY mention the newer runtime-input change in the detailed findings, but the status SHALL remain `valid` unless another freshness or validity problem is found.

#### Scenario: Researcher reruns the audit after a change
- **WHEN** a researcher reruns the prompt-status audit
- **THEN** the previous `workflow/prompts-status/report.md` is replaced with a new report reflecting the current repository state

#### Scenario: Researcher opens the report
- **WHEN** a researcher opens `workflow/prompts-status/report.md`
- **THEN** they first see the audit header and then a flat table summarizing every audited prompt

#### Scenario: Prompt is review-needed because spec is newer
- **WHEN** a prompt's governing spec has a newer git change than the prompt
- **THEN** the prompt's detail section names both paths and records the freshness finding

#### Scenario: Prompt is invalid because of a missing file
- **WHEN** a required input file is missing
- **THEN** the prompt's detail section lists the missing path in its findings bullets

#### Scenario: Per-run platforms file changed
- **WHEN** `plan/rating/platforms.md` changed after `act/rating/prompt.md` and the prompt contract still matches its governing spec
- **THEN** the report does not mark `act/rating/prompt.md` as `review-needed` or `invalid` on that basis alone
