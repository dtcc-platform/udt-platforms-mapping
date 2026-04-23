## ADDED Requirements

### Requirement: Rating prompt declares rubrics, platforms, and source-policy as required inputs

The prompt template SHALL include a `## Required Inputs` section listing three files:

- `plan/rating/rubrics.md` — dimension rubrics used for scoring
- `plan/rating/platforms.md` — the comparison scope (rows of Name, Link, Layer)
- `plan/rating/source-policy.md` — acceptable source types and citation conventions

All three files SHALL be treated as inputs in both CLI and Web modes. In particular, `source-policy.md` is inlined into the resolved prompt in Web mode so that deep-research web interfaces operate under the project's source policy.

#### Scenario: AI CLI opens the rating prompt

- **WHEN** the AI CLI reads `act/rating/prompt.md`
- **THEN** it finds `plan/rating/rubrics.md`, `plan/rating/platforms.md`, and `plan/rating/source-policy.md` in the Required Inputs section

#### Scenario: Rating prompt runs in Web deep research

- **WHEN** a researcher runs the rating prompt in Web mode and pastes the resolved prompt into a deep-research interface
- **THEN** the source-policy content is part of the resolved prompt and constrains the deep-research model's source selection

### Requirement: Rating prompt supports CLI and Web run modes

The prompt template SHALL comply with the `prompt-run-modes` capability. It SHALL include a `## Run Modes` section instructing the AI to ask the researcher "Run as CLI or Web?" before executing the prompt body.

- In **CLI mode**, the AI reads all three required inputs, executes the prompt body, and saves the response to `observe/rating/cli-<model-short>.md`
- In **Web mode**, the AI produces a fully resolved prompt with the content of all three required inputs inlined at the top (each under a heading naming the file), followed by the prompt body; the researcher pastes the resolved prompt into a web chat and saves the response to `observe/rating/web-<model-short>.md`

#### Scenario: Researcher chooses CLI mode

- **WHEN** the researcher answers "CLI"
- **THEN** the AI reads rubrics.md, platforms.md, and source-policy.md, produces a rating response, and saves it to `observe/rating/cli-<model-short>.md`

#### Scenario: Researcher chooses Web mode for deep research

- **WHEN** the researcher answers "Web" and pastes the resolved prompt into a deep-research interface
- **THEN** the resolved prompt includes inlined rubrics, platforms, and source policy; the deep-research model has everything it needs without file access

## MODIFIED Requirements

### Requirement: Comparison prompt covers twelve dimensions with scoring

The prompt template SHALL instruct the model to compare platforms across all twelve dimensions — the six research dimensions (Technical Architecture, Openness & Licensing, City-Scale Capability, Maturity & Adoption, Integration Posture, Governance) and the six functional categories (Visualization, Data Management, Simulation, IoT Sensing, Standards, Infrastructure) — and assign each platform a score of 1–5 per dimension using the rubrics from the required inputs.

The prompt SHALL state that rubrics are supplied via the `plan/rating/rubrics.md` required input and are not embedded inline in the prompt body.

#### Scenario: Response covers all twelve dimensions with scores

- **WHEN** an AI responds to the rating prompt
- **THEN** the response addresses each of the twelve dimensions for every platform and assigns a numeric 1–5 score with rationale, using the rubrics from `plan/rating/rubrics.md`

#### Scenario: Researcher compares scores across agents

- **WHEN** a researcher runs the same rating on two different AI agents
- **THEN** both responses use the same dimension labels and scoring scale, making scores comparable

### Requirement: Comparison prompt includes DTCC as a required reference entry

The prompt template SHALL NOT include a hardcoded description of DTCC. Instead, the prompt SHALL instruct the model to treat the DTCC row in `plan/rating/platforms.md` as the reference platform for landscape observations in Part 3.

The prompt SHALL note that the DTCC row MUST be present in `plan/rating/platforms.md` for Part 3 landscape observations to orient around DTCC — this requirement is documented in the `plan-rating-platforms` capability.

#### Scenario: Response positions DTCC in the landscape

- **WHEN** an AI responds to the rating prompt with DTCC present in `plan/rating/platforms.md`
- **THEN** DTCC appears as a platform entry and the landscape observations section explicitly addresses where DTCC sits relative to comparable and complementary platforms

#### Scenario: DTCC platform evolves and description drifts

- **WHEN** DTCC's capabilities change between research sessions
- **THEN** the researcher re-runs discovery to get an updated DTCC row and updates `plan/rating/platforms.md`, rather than editing `act/rating/prompt.md`

#### Scenario: Researcher omits DTCC from platforms.md

- **WHEN** a researcher runs the rating prompt without a DTCC row in `plan/rating/platforms.md`
- **THEN** Part 3 landscape observations (DTCC's Position, Comparable Platforms, Complementary Platforms) cannot orient around DTCC; the prompt surfaces the missing DTCC row as a scope error

### Requirement: Comparison prompt usage header includes save-as filename instruction

The prompt template's usage header SHALL direct the researcher to run the prompt through an AI CLI (Claude Code, Codex CLI, Gemini CLI) that asks the CLI-or-Web question on their behalf. The header SHALL NOT instruct the researcher to manually paste rubrics or selection rows, or to copy from a cut-line — that mechanic is retired.

The header SHALL state the save-as path convention: `observe/rating/cli-<model-short>.md` for CLI-mode responses, `observe/rating/web-<model-short>.md` for Web-mode responses. File names SHALL NOT include the cycle type — the folder provides that context; the `cli-` / `web-` prefix is the interface authority.

#### Scenario: Researcher opens the rating prompt file

- **WHEN** a researcher opens `act/rating/prompt.md`
- **THEN** the usage header tells them to run the prompt via their AI CLI and explains the CLI-or-Web ask — it does not include cut-line blockquotes or numbered paste instructions

#### Scenario: Researcher saves a web-chat response

- **WHEN** a researcher runs the prompt in Web mode and saves the web-chat response
- **THEN** the save-as filename follows `observe/rating/web-<model-short>.md`

## REMOVED Requirements

### Requirement: Comparison prompt uses a single selection table token
**Reason**: The paste mechanic is retired. The platforms to compare are now declared in `plan/rating/platforms.md` and read or inlined by the AI CLI based on the chosen run mode — there is no `[PASTE_SELECTED_PLATFORMS_HERE]` token. This requirement is subsumed by the new "Rating prompt declares rubrics, platforms, and source-policy as required inputs" requirement and the `plan-rating-platforms` capability.
**Migration**: Remove the `[PASTE_SELECTED_PLATFORMS_HERE]` token and its preceding guard and scope-boundary instruction blocks from `act/rating/prompt.md`. Move the Name/Link/Layer rows into `plan/rating/platforms.md` and add that file to the `## Required Inputs` section of the prompt.

### Requirement: Comparison prompt includes a [PASTE_SCOPE_HERE] guard
**Reason**: The paste mechanic is retired. The rubrics file is now a declared input read or inlined by the AI CLI — there is no `[PASTE_SCOPE_HERE]` token and no placeholder-guard block. This requirement is subsumed by the new "Rating prompt declares rubrics, platforms, and source-policy as required inputs" requirement.
**Migration**: Remove the `[PASTE_SCOPE_HERE]` token and its preceding guard block from `act/rating/prompt.md`. Add `plan/rating/rubrics.md` to the `## Required Inputs` section.
