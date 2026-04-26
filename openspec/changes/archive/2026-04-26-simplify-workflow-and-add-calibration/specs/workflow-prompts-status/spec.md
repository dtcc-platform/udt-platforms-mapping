## REMOVED Requirements

### Requirement: Workflow prompt-status audit exists as a CLI maintenance workflow
**Reason**: Prompt-status is being simplified into a maintained `act/` entry point rather than a separate workflow-level area.
**Migration**: Use `act/check-prompts-status.md` as the maintained prompt-status entry point.

### Requirement: Workflow prompt-status audit checks each prompt against governing files
**Reason**: The prompt-status behavior remains needed, but it is now governed under the new `act-check-prompts-status` capability.
**Migration**: Move all prompt-status behavior and path assumptions to `openspec/specs/act-check-prompts-status/spec.md`.

### Requirement: Workflow prompt-status audit distinguishes freshness dependencies from runtime inputs
**Reason**: Freshness and runtime-input audit rules are preserved under the new `act-check-prompts-status` capability rather than a workflow-level folder.
**Migration**: Use `openspec/specs/act-check-prompts-status/spec.md` as the active contract.

### Requirement: Workflow prompt-status audit uses three statuses
**Reason**: The status model remains active, but this capability is retired in favor of an `act/` entry point.
**Migration**: Use `act/check-prompts-status.md` and its governing capability instead.

### Requirement: Workflow prompt-status audit writes a structured report
**Reason**: Report-writing behavior remains active, but the report path and prompt path move out of `workflow/`.
**Migration**: Write the report to `act/check-prompts-status-report.md` under the new capability.
