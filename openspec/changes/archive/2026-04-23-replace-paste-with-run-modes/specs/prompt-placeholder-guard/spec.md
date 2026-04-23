## REMOVED Requirements

### Requirement: Placeholder guard canonical wording is defined
**Reason**: The paste mechanic is retired, so no `[PASTE_X_HERE]` placeholders remain in any prompt file. With inputs declared via `## Required Inputs` sections and resolved automatically by the AI CLI (per the `prompt-run-modes` capability), there is nothing for a placeholder guard to protect. The canonical guard wording is no longer used anywhere.
**Migration**: Remove all canonical guard blocks from `act/discovery/prompt.md` and `act/rating/prompt.md`. The AI CLI knows which inputs the prompt needs from the Required Inputs section; if an input file is missing, the CLI surfaces the error directly instead of relying on a model-level guard instruction.

### Requirement: Guard instruction is placed immediately before the placeholder
**Reason**: No placeholders remain; no guards are needed.
**Migration**: Delete any remaining guard blocks when rewriting `act/*/prompt.md`. Ensure no placeholder tokens (`[PASTE_SCOPE_HERE]`, `[PASTE_SELECTED_PLATFORMS_HERE]`, or any other `[PASTE_*]`) remain in the prompt bodies.
