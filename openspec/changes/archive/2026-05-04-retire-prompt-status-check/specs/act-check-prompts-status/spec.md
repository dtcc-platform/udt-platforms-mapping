## REMOVED Requirements

### Requirement: Prompt-status check exists as a CLI maintenance prompt under act

**Reason**: The repository no longer maintains a separate prompt-status audit prompt under `act/`.

**Migration**: Use the active prompt specs and `openspec validate --all --strict` for governed repository validation.

### Requirement: Prompt-status check verifies live prompts against governing files

**Reason**: The live audit mapping duplicated governing spec relationships and required manual upkeep after prompt/spec restructuring.

**Migration**: Use each prompt's own baseline spec as the source of truth.

### Requirement: Prompt-status check distinguishes freshness dependencies from runtime inputs

**Reason**: The prompt-status freshness model is retired with the maintenance prompt.

**Migration**: Treat runtime-input changes and prompt/spec changes through their file-specific governing specs and normal review.

### Requirement: Prompt-status check writes a structured report

**Reason**: The generated report is a stale live artifact once the prompt-status workflow is retired.

**Migration**: Do not generate or maintain `act/check-prompts-status-report.md`.
