## Why

Running a prompt today requires the researcher to open a scope file, copy its full content, paste it into a `[PASTE_X_HERE]` placeholder, copy again from a cut-line, and paste into an AI chat. This works but adds friction and human-error risk on every session — and it duplicates the work that an AI CLI can already do (reading files).

The mechanic splits prompts into two awkward audiences: the human (who orchestrates the paste) and the model (which needs the resolved text). Collapsing both into a single CLI-driven flow — where the CLI asks the researcher "CLI or Web?" and then either executes the prompt or emits a fully resolved version for web-chat copy — removes that split entirely. Web mode is still supported (and still the right choice for deep research) but the researcher copies one resolved blob, not two.

Two side effects fall out of the change: the `prompt-paste-boundary` spec (cut-line) and `prompt-placeholder-guard` spec (the "If placeholder still literal, stop" block) become dead weight and are retired. A new `plan/rating/platforms.md` file replaces the old `[PASTE_SELECTED_PLATFORMS_HERE]` interaction — per-run platform selections become a git-diffable artifact instead of an ephemeral paste.

## What Changes

- **BREAKING** Remove the paste mechanic from `act/discovery/prompt.md` and `act/rating/prompt.md`: no cut-line blockquote, no `[PASTE_SCOPE_HERE]`, no `[PASTE_SELECTED_PLATFORMS_HERE]`, no canonical placeholder-guard block
- Each `act/*/prompt.md` declares its inputs in a `## Required Inputs` markdown section (list of repository-relative file paths)
- Each `act/*/prompt.md` includes a `## Run Modes` section instructing the AI to ask the researcher "Run as CLI or Web?" before executing
  - **CLI**: AI reads each required input file, runs the prompt, and saves the response to `observe/<cycle>/cli-<model-short>.md`
  - **Web**: AI produces a fully resolved prompt with inputs inlined at the top, emits it as a copy-ready block; researcher pastes into a web chat and saves the response to `observe/<cycle>/web-<model-short>.md`
- Introduce `plan/rating/platforms.md` — a three-column GFM table (Name, Link, Layer) holding the platform subset selected for the current rating cycle run; carries the comparison-scope boundary and must include DTCC
- `plan/rating/source-policy.md` becomes a declared input of the rating prompt (inlined in both CLI and Web modes, especially valuable in Web deep research)
- Response filenames gain a `cli-` or `web-` prefix — the single authority on which interface produced the response
- Existing `observe/discovery/*.md` and `observe/rating/*.md` files are renamed with the `web-` prefix (all existing files were web-chat responses)
- `README.md` gains a `## Design` section documenting the run-modes model, the definition-vs-per-run-data distinction in `plan/`, and the filename convention

The YAML response metadata block (`model`, `date`, `prompt`) is unchanged — the filename prefix carries the interface, so no `interface:` field is added.

The run-modes contract applies only to `act/*/prompt.md`. Reflect-phase prompts are CLI-only by nature (one writes CSV+HTML, the other scans bulk response files) and do not participate in the mode ask.

## Capabilities

### New Capabilities

- `prompt-run-modes`: Shared contract for the CLI/Web run-mode selection — the Required Inputs section format, the mode-ask interaction, the per-mode behaviors, and the response filename prefix convention
- `plan-rating-platforms`: Defines `plan/rating/platforms.md` — its schema, its role as comparison-scope boundary, the DTCC inclusion requirement, and its semantics as per-run data distinct from slow-moving definitions

### Modified Capabilities

- `act-discovery-prompt`: Placeholder and cut-line requirements removed; adds Required Inputs declaration and run-mode handling; usage-header wording updated
- `act-rating-prompt`: Placeholder, cut-line, and inline source-policy requirements removed; adds Required Inputs for `rubrics.md`, `platforms.md`, and `source-policy.md`; DTCC reference now anchored to `platforms.md` rather than a pasted table row
- `ar-folder-layout`: `observe/*/` filenames carry a `cli-` or `web-` interface prefix

### Removed Capabilities

- `prompt-paste-boundary`: Cut-line contract retired entirely
- `prompt-placeholder-guard`: Placeholders are gone — nothing left to guard

## Impact

- `act/discovery/prompt.md` and `act/rating/prompt.md` rewritten — paste-era machinery removed, run-modes machinery added
- `plan/rating/platforms.md` created with initial rows (DTCC plus the current cycle's selected platforms)
- Existing `observe/*/<model>.md` files renamed to `observe/*/web-<model>.md`
- `reflect/discovery/benchmarking/prompt.md` and `reflect/discovery/reporting/prompt.md` updated to account for the new filename convention
- `README.md` gains a `## Design` section
- Researchers stop hand-pasting scope and selection tables; all act/ prompts are run through an AI CLI that asks CLI-or-Web and handles input resolution

No tool-level changes are required — the "CLI" here refers to any file-aware AI CLI (Claude Code, Codex CLI, Gemini CLI).
