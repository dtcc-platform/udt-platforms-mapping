## REMOVED Requirements

### Requirement: Prompt files contain a cut-line separating usage instructions from AI prompt body
**Reason**: The paste mechanic is retired. With the introduction of the `prompt-run-modes` capability, `act/*/prompt.md` files are executed through an AI CLI that asks the researcher "Run as CLI or Web?" and handles input resolution automatically. Researchers no longer manually copy and paste prompt content, so there is no longer a cut-line to mark the paste start.
**Migration**: Remove the `> Paste into your AI session from this line onwards.` blockquote from `act/discovery/prompt.md` and `act/rating/prompt.md`. Researchers now run these prompts via an AI CLI, which resolves inputs and (in Web mode) emits a copy-ready resolved prompt as its output.

### Requirement: Usage instructions in prompt files reference the cut-line
**Reason**: The cut-line no longer exists; usage instructions no longer need to reference it.
**Migration**: Remove any numbered step in `act/discovery/prompt.md` and `act/rating/prompt.md` that says to paste starting from the cut-line blockquote. Replace the numbered paste steps with an instruction to run the prompt via an AI CLI — the CLI will ask for CLI-or-Web mode and handle the rest.
