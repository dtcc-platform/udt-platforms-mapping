## Why

The prompt-status area is currently governed by two small capabilities even though the report has no independent lifecycle from the audit that produces it. That split adds cognitive load without adding much clarity, so the contract should be simplified to one capability.

## What Changes

- Introduce a single `workflow-prompts-status` capability that governs both the audit prompt and the report it writes.
- Fold the current prompt-path, audit-behavior, status-model, and report-structure requirements into that one capability.
- Remove the two baseline capabilities `prompt-validity-audit-prompt` and `prompt-validity-audit-report`.

## Capabilities

### New Capabilities

- `workflow-prompts-status`: governs the workflow prompt-status audit, including the live prompt path, audit behavior, output path, and required report structure.

### Modified Capabilities

- `prompt-validity-audit-prompt`: remove this separate capability and fold its requirements into `workflow-prompts-status`.
- `prompt-validity-audit-report`: remove this separate capability and fold its requirements into `workflow-prompts-status`.

## Impact

- Affected baseline specs: replace `openspec/specs/prompt-validity-audit-prompt/spec.md` and `openspec/specs/prompt-validity-audit-report/spec.md` with `openspec/specs/workflow-prompts-status/spec.md`
- Affected OpenSpec capability naming for the prompt-status audit
- No change to the live prompt path `workflow/prompts-status/` or to the report path it writes
