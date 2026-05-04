# Retire Prompt Status Check

## Why

The repository now uses flattened prompt entrypoints and `openspec validate --all --strict` as the primary consistency check. The prompt-status maintenance prompt overlaps with that validation flow, requires manual upkeep of its own audit mapping, and its generated report has become a stale artifact.

Retiring the check removes a secondary review path that no longer adds enough value for the maintenance cost.

## What Changes

- Remove `act/check-prompts-status.md`.
- Remove the generated `act/check-prompts-status-report.md`.
- Retire the `act-check-prompts-status` capability spec.
- Update repository-structure expectations so `act/` contains only canonical thread prompts.

## Impact

- Prompt/status freshness review is no longer a first-class repository workflow.
- Researchers should use baseline specs and `openspec validate --all --strict` for governed prompt/spec consistency.
- Archived history remains intact.
