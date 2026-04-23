## ADDED Requirements

### Requirement: Discovery prompt declares plan/discovery/scope.md as a required input

The prompt template SHALL include a `## Required Inputs` section listing `plan/discovery/scope.md` as the input file that provides the Layer classification criteria.

The entry SHALL take the form:

- `plan/discovery/scope.md` — Layer classification criteria

No other files are declared inputs of the discovery prompt.

#### Scenario: AI CLI opens the discovery prompt

- **WHEN** the AI CLI reads `act/discovery/prompt.md`
- **THEN** it finds `plan/discovery/scope.md` in the Required Inputs section and knows to read that file (CLI mode) or inline it (Web mode)

### Requirement: Discovery prompt supports CLI and Web run modes

The prompt template SHALL comply with the `prompt-run-modes` capability. It SHALL include a `## Run Modes` section instructing the AI to ask the researcher "Run as CLI or Web?" before executing the prompt body.

- In **CLI mode**, the AI reads `plan/discovery/scope.md`, executes the prompt body with that content available as Layer criteria, and saves the response to `observe/discovery/cli-<model-short>.md`
- In **Web mode**, the AI produces a fully resolved prompt with the content of `plan/discovery/scope.md` inlined at the top under a heading naming the file, followed by the prompt body; the researcher pastes the resolved prompt into a web chat and saves the response to `observe/discovery/web-<model-short>.md`

#### Scenario: Researcher chooses CLI mode

- **WHEN** the researcher answers "CLI"
- **THEN** the AI reads `plan/discovery/scope.md`, produces a discovery response, and saves it to `observe/discovery/cli-<model-short>.md`

#### Scenario: Researcher chooses Web mode

- **WHEN** the researcher answers "Web"
- **THEN** the AI emits a resolved prompt with the scope content inlined at the top, ready to paste into a web chat, and notes the save-as path `observe/discovery/web-<model-short>.md`

#### Scenario: Researcher runs the discovery prompt for deep research

- **WHEN** the researcher wants a more thorough Layer classification and chooses Web mode
- **THEN** the resolved prompt is designed to be pasted into a deep research interface; the scope is fully inlined so the deep-research model has the Layer criteria without needing file access

## MODIFIED Requirements

### Requirement: Discovery prompt requests Layer classification output only

The prompt template SHALL instruct the model to return one `##`-level Markdown section per platform containing identification fields and a Layer assignment. No dimension scoring is required or expected.

**For in-scope platforms** (`core-platform`, `backbone`, `domain-module`): identification fields only — Organization, Link, License, Type, Layer.

**For excluded platforms** (`excluded`): identification fields plus a single **Reason** field — one sentence explaining why the platform is outside the study boundary.

The `Layer` field SHALL contain exactly one of: `core-platform`, `backbone`, `domain-module`, or `excluded`, assigned using the Layer criteria from the required inputs.

The prompt template SHALL include a concrete example section demonstrating the exact field labels and Layer field placement for both in-scope and excluded platforms.

The prompt template SHALL state that the response contains exactly three parts, in order: the metadata block, the summary table, and the per-platform sections.

#### Scenario: Response is used to select platforms for rating

- **WHEN** an AI responds to the discovery prompt
- **THEN** each in-scope platform section contains Organization, Link, License, Type, and Layer — enough for the researcher to copy the relevant rows into `plan/rating/platforms.md`

#### Scenario: Discovery session finds an excluded platform

- **WHEN** the model encounters a platform that does not meet any in-scope criteria
- **THEN** the platform appears in the summary table with `Layer=excluded` and a one-sentence Reason in its per-platform section; no dimension scores appear

#### Scenario: Discovery session finds a domain-module platform

- **WHEN** an AI responds to the discovery prompt
- **THEN** domain-specific analytics or simulation tools appear with `Layer=domain-module`, not filtered out for not being full platforms

### Requirement: Discovery prompt usage header includes save-as filename instruction

The prompt template's usage header SHALL direct the researcher to run the prompt through an AI CLI (Claude Code, Codex CLI, Gemini CLI) that asks the CLI-or-Web question on their behalf. The header SHALL NOT instruct the researcher to manually paste scope content or copy from a cut-line — that mechanic is retired.

The header SHALL state the save-as path convention: `observe/discovery/cli-<model-short>.md` for CLI-mode responses, `observe/discovery/web-<model-short>.md` for Web-mode responses. File names SHALL NOT include the cycle type — the folder provides that context; the `cli-` / `web-` prefix is the interface authority.

#### Scenario: Researcher opens the discovery prompt file

- **WHEN** a researcher opens `act/discovery/prompt.md`
- **THEN** the usage header tells them to run the prompt via their AI CLI and explains the CLI-or-Web ask — it does not include cut-line blockquotes or numbered paste instructions

#### Scenario: Researcher saves a web-chat response

- **WHEN** a researcher runs the prompt in Web mode and saves the web-chat response
- **THEN** the save-as filename follows `observe/discovery/web-<model-short>.md`

## REMOVED Requirements

### Requirement: Discovery prompt pastes plan/discovery/scope.md only
**Reason**: The paste mechanic is retired. Scope content is now read by the AI in CLI mode or inlined by the resolver in Web mode — there is no `[PASTE_SCOPE_HERE]` token and no placeholder-guard block. This requirement is subsumed by the new "Discovery prompt declares plan/discovery/scope.md as a required input" and "Discovery prompt supports CLI and Web run modes" requirements.
**Migration**: Replace the `[PASTE_SCOPE_HERE]` token and its preceding guard block in `act/discovery/prompt.md` with a `## Required Inputs` section listing `plan/discovery/scope.md`. Add a `## Run Modes` section per the `prompt-run-modes` capability.
