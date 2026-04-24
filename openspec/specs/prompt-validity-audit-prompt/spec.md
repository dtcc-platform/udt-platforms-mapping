# Spec: prompt-validity-audit-prompt

## Purpose

Defines the CLI maintenance prompt at `reflect-workflow/prompt-validity/prompt.md` that audits live repository prompts for validity and freshness against their governing specs and related files.

## Requirements

### Requirement: Prompt-validity audit prompt exists as a CLI maintenance prompt

The repository SHALL contain a file at `reflect-workflow/prompt-validity/prompt.md`. This file SHALL be a CLI-only maintenance prompt that audits live repository prompt files for validity and freshness. It SHALL NOT be a Web-mode prompt.

The prompt SHALL instruct the AI to inspect live prompt files under `act/` and `reflect/` only.

#### Scenario: Researcher runs the prompt-validity audit
- **WHEN** a researcher tells their AI CLI to run `reflect-workflow/prompt-validity/prompt.md`
- **THEN** the AI executes the audit directly in CLI mode without asking for run mode selection

#### Scenario: Archived change prompts exist
- **WHEN** prompt-like files exist under `openspec/changes/` or `openspec/changes/archive/`
- **THEN** the audit ignores them and checks only the live prompts under `act/` and `reflect/`

### Requirement: Audit prompt checks each prompt against governing files

For each live prompt file, the audit prompt SHALL identify:
- its governing baseline prompt spec under `openspec/specs/`
- any shared baseline contract spec the prompt explicitly relies on
- any files declared under its `## Required Inputs` section, if present

The audit SHALL verify that:
- the prompt file exists
- each declared required-input file exists
- the prompt's declared input set is compatible with the governing spec
- the prompt's stated behavior does not directly contradict the governing spec

#### Scenario: Prompt has a missing required input file
- **WHEN** a live prompt declares a required input path that does not exist
- **THEN** the audit marks that prompt as `invalid` and records the missing path in the report

#### Scenario: Prompt omits a required input required by spec
- **WHEN** a governing spec requires an input file declaration that the prompt does not include
- **THEN** the audit marks that prompt as `invalid` and records the mismatch in the report

### Requirement: Audit prompt distinguishes freshness dependencies from runtime inputs

The audit prompt SHALL distinguish freshness dependencies from runtime inputs.

Freshness dependencies SHALL include the governing baseline prompt spec and any shared baseline contract spec the prompt explicitly relies on. Runtime inputs SHALL include files named under `## Required Inputs`.

A newer freshness dependency than the prompt SHALL produce status `review-needed`. A newer runtime-input file than the prompt SHALL NOT by itself make the prompt stale.

#### Scenario: Governing spec changed after prompt
- **WHEN** the latest git change to a prompt's governing baseline spec is newer than the latest git change to the prompt file
- **THEN** the audit marks the prompt as `review-needed`

#### Scenario: Per-run data changed after prompt
- **WHEN** `plan/rating/platforms.md` has a newer git change than `act/rating/prompt.md`
- **THEN** the audit does not mark the prompt stale on that fact alone

### Requirement: Audit prompt uses three statuses

The audit prompt SHALL assign exactly one status to each audited prompt:
- `valid`
- `review-needed`
- `invalid`

The prompt SHALL use these meanings:
- `valid` — no missing files, no direct contract mismatch, and no newer freshness dependency
- `review-needed` — the prompt remains runnable, but a freshness dependency is newer or a likely drift signal exists
- `invalid` — the prompt has a missing dependency, broken declaration, or direct contradiction with its governing contract

#### Scenario: Prompt passes all checks
- **WHEN** a prompt has existing dependencies, matching declarations, and no newer freshness dependencies
- **THEN** the audit records status `valid`

#### Scenario: Prompt contradicts governing contract
- **WHEN** a prompt's declared behavior directly conflicts with its governing baseline spec
- **THEN** the audit records status `invalid`

### Requirement: Audit prompt writes a report file

The audit prompt SHALL write its results to `reflect-workflow/prompt-validity/report.md`, overwriting any existing file.

The prompt SHALL be runnable by a researcher telling the AI CLI either `run reflect-workflow/prompt-validity/prompt.md` or `run the prompt validity audit`.

#### Scenario: Researcher reruns the audit after a change
- **WHEN** a researcher reruns the prompt-validity audit
- **THEN** the previous `reflect-workflow/prompt-validity/report.md` is replaced with a new report reflecting the current repository state
