# Spec: act-check-prompts-status

## Purpose

Defines the prompt-status check at `act/check-prompts-status.md`, including the CLI maintenance prompt, the status model it uses, and the structure of the report it writes.

## Requirements

### Requirement: Prompt-status check exists as a CLI maintenance prompt under act

The repository SHALL contain a file at `act/check-prompts-status.md`. This file SHALL be a CLI-only maintenance prompt that audits live repository prompt files for validity and freshness.

### Requirement: Prompt-status check verifies live prompts against governing files

The audit mapping for live prompts SHALL use the current baseline set. In particular:

- `act/udt-platforms/prompt.md` SHALL be checked against `openspec/specs/act-udt-platforms-prompt/spec.md`
- `act/udt-platform-comparison/prompt.md` SHALL be checked against `openspec/specs/act-udt-platform-comparison-prompt/spec.md`
- `reflect/udt-platforms/benchmarking/prompt.md` SHALL be checked against `openspec/specs/reflect-udt-platforms-benchmarking/spec.md`
- `reflect/udt-platforms/reporting/prompt.md` SHALL be checked against `openspec/specs/reflect-udt-platforms-reporting-prompt/spec.md`
- `reflect/udt-platform-comparison/reporting/prompt.md` SHALL be checked against `openspec/specs/reflect-udt-platform-comparison-reporting/spec.md`

The audit SHALL ignore archived change artifacts and calibration artifacts.

### Requirement: Prompt-status check distinguishes freshness dependencies from runtime inputs

A newer governing spec or shared contract than the prompt SHALL produce status `review-needed`.
A newer runtime-input file than the prompt SHALL NOT by itself make the prompt stale.

### Requirement: Prompt-status check writes a structured report

The audit SHALL assign exactly one status to each audited prompt:

- `valid`
- `review-needed`
- `invalid`

The audit SHALL write its results to `act/check-prompts-status-report.md`.
