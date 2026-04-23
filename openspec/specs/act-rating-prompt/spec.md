# Spec: act-rating-prompt

## Purpose

Defines the platform rating prompt template at `act/rating/prompt.md` — structure, required inputs, run modes, scoring contract, three-part output, and save-as conventions for rating sessions.
## Requirements
### Requirement: Platform comparison prompt file exists

The repository SHALL contain a file at `act/rating/prompt.md` that provides a self-contained prompt template for AI-assisted side-by-side comparison of two or more UDT platforms.

#### Scenario: File is present and non-empty

- **WHEN** a researcher navigates to `act/rating/prompt.md`
- **THEN** the file exists and contains a complete, copy-pasteable prompt

### Requirement: Comparison prompt covers twelve dimensions with scoring

The prompt template SHALL instruct the model to compare platforms across all twelve dimensions — the six research dimensions (Technical Architecture, Openness & Licensing, City-Scale Capability, Maturity & Adoption, Integration Posture, Governance) and the six functional categories (Visualization, Data Management, Simulation, IoT Sensing, Standards, Infrastructure) — and assign each platform a score of 1–5 per dimension using the rubrics from the required inputs.

The prompt SHALL state that rubrics are supplied via the `plan/rating/rubrics.md` required input and are not embedded inline in the prompt body.

#### Scenario: Response covers all twelve dimensions with scores

- **WHEN** an AI responds to the rating prompt
- **THEN** the response addresses each of the twelve dimensions for every platform and assigns a numeric 1–5 score with rationale, using the rubrics from `plan/rating/rubrics.md`

#### Scenario: Researcher compares scores across agents

- **WHEN** a researcher runs the same rating on two different AI agents
- **THEN** both responses use the same dimension labels and scoring scale, making scores comparable

### Requirement: Comparison prompt requests a three-part structured output

The prompt template SHALL instruct the model to produce output in exactly three parts, in this order:

1. **Scoring table** — one row per platform, six dimension score columns, six functional category score columns, plus a link column
2. **Per-platform profiles** — one structured profile per platform with all six dimension analyses, sources, and scores
3. **Landscape observations** — four `####` subheadings, each followed by a bullet list: `#### Landscape Gaps`, `#### DTCC's Position`, `#### Comparable Platforms`, `#### Complementary Platforms`

#### Scenario: Researcher extracts summary data

- **WHEN** an AI responds to the comparison prompt
- **THEN** Part 1 contains a Markdown table with one row per platform, numeric dimension scores per dimension column, and numeric category scores per category column

#### Scenario: Researcher reads a platform profile

- **WHEN** a researcher reads Part 2 of the response
- **THEN** each platform has a self-contained profile with organization, link, license, type, dimension analyses with scores, and a sources section

#### Scenario: Researcher understands DTCC's position

- **WHEN** a researcher reads Part 3
- **THEN** the response contains exactly four `####` subheadings — `#### Landscape Gaps`, `#### DTCC's Position`, `#### Comparable Platforms`, `#### Complementary Platforms` — each followed by a bullet list

#### Scenario: Researcher scans Part 3 across two agent responses

- **WHEN** a researcher opens two comparison responses run on different AI agents
- **THEN** Part 3 has the same four subheadings in the same order in both responses

### Requirement: Comparison prompt Part 1 scoring table includes functional category columns

The Part 1 scoring table SHALL include a `Layer` column and the six dimension columns and six functional category columns. It SHALL NOT include a `Relevance` column — Relevance is retired.

The `Layer` column SHALL appear immediately after `Link`. It SHALL carry the Layer value from the corresponding row in `plan/rating/platforms.md` unchanged. The comparison AI SHALL NOT reassess or revise the Layer assignment — Layer is owned by the discovery phase.

Each score column SHALL use the same 1–5 integer scoring format — bare integer, `?` for unknown, no `/5` suffix in table cells.

The prompt SHALL include a legend immediately below the Part 1 table instruction listing each abbreviated column header with its full name and one-line description.

#### Scenario: Researcher reads the Part 1 table

- **WHEN** an AI responds to the comparison prompt
- **THEN** the Part 1 table header contains exactly: `Name`, `Link`, `Layer`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`

#### Scenario: Researcher compares functional strengths across platforms

- **WHEN** an AI responds to the comparison prompt
- **THEN** every platform row contains a numeric 1–5 score (or `?`) in every dimension and category column, and the Layer value from the discovery row

#### Scenario: Layer value is carried through unchanged

- **WHEN** `plan/rating/platforms.md` contains a platform row with `Layer=backbone`
- **THEN** the Part 1 table contains `backbone` in the Layer column for that platform; the comparison AI does not reassess or revise it

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

### Requirement: Comparison prompt enforces agent-agnostic output structure

The prompt template SHALL include a concrete example of the per-platform profile structure so any agent can reproduce the exact shape mechanically. The prompt SHALL comply with the shared Markdown contract defined in `prompt-markdown-format`.

In addition to that shared contract, the prompt SHALL specify:

- **Profile heading level:** every platform profile SHALL use `###` as the top-level heading so profiles nest consistently under part headings
- **Score notation:** dimension scores SHALL always be written as `X/5` (e.g., `4/5`) — no other formats (`★★★★☆`, `4 out of 5`, `80%`, bold numbers) are permitted
- **Score placement:** in profiles, scores SHALL appear inline with the dimension label as `**Dimension (X/5):**` — e.g., `**Technical Architecture (4/5):**`
- **Score in table:** in the scoring table, score cells SHALL contain only the numeric value (e.g., `4`) with `?` for unknown — no `/5` suffix in table cells
- **Research-mode suppression:** if the interface supports Research or Deep Research, the prompt SHALL instruct the model to do planning internally and return only the required three-part comparison output, with no generated research plan, executive summary, source appendix, methodology section, or provider-specific report wrapper

The prompt SHALL include a concrete example profile for one fictional platform demonstrating the exact heading levels, field labels, score notation, and sources section structure.

#### Scenario: Two agents respond to the same prompt

- **WHEN** a researcher runs the comparison prompt on ChatGPT and on Claude
- **THEN** both responses use identical heading levels, field labels, and score notation — the only difference is the content

#### Scenario: Response is opened in a standard Markdown viewer

- **WHEN** a researcher saves the response as a `.md` file and opens it in GitHub, VS Code, Obsidian, or Typora
- **THEN** all formatting renders correctly with no raw syntax visible, no broken elements, and no AI-specific artifacts

#### Scenario: Model uses AI-specific citation format

- **WHEN** an AI model would normally respond with numeric bracket citations or footnotes
- **THEN** the prompt instruction overrides this and the model uses `[Description](https://...)` inline links instead

#### Scenario: Research-mode interface would normally emit a report shell

- **WHEN** a researcher runs the comparison prompt in a Research or Deep Research web interface
- **THEN** the response omits any exposed research plan, executive summary, or provider-native report shell and contains only the required three parts in the required order

### Requirement: Comparison prompt requires explicit uncertainty handling

The prompt template SHALL instruct the model to distinguish inferred claims from verified facts, state "unknown" or "unclear" when information is not findable, and never fabricate URLs, license names, or deployment claims.

The prompt template SHALL also instruct the model to avoid broadening the comparison with unsupported claims about the whole market and to keep unsupported dimensions explicitly marked as unknown.

#### Scenario: Model cannot find license information

- **WHEN** an AI cannot locate a platform's license from primary sources
- **THEN** the response states "unknown" rather than guessing or inferring

#### Scenario: Model infers a score from indirect evidence

- **WHEN** an AI assigns a dimension score based on indirect evidence
- **THEN** the response explicitly flags this as an inference (e.g., "likely X based on [evidence]")

#### Scenario: Research-mode interface encourages broad market framing

- **WHEN** an AI would otherwise add unsupported claims about the wider market beyond the selected platforms
- **THEN** it limits itself to supported observations and uses "unknown" or "unclear" where evidence is incomplete

### Requirement: Comparison prompt instructs use of primary sources

The prompt template SHALL instruct the model to base its comparison on primary sources (official documentation, repositories, published papers) and to cite sources for each claim.

The prompt template MAY allow secondary sources to be used only to discover relevant primary sources or candidate documentation paths, but final factual claims and saved output citations SHALL rely on primary sources.

#### Scenario: Response includes source citations

- **WHEN** an AI responds to the comparison prompt
- **THEN** each substantive claim is accompanied by a source reference or URL

#### Scenario: Model first finds a platform detail through a secondary article

- **WHEN** an AI uses a secondary source to discover a possible claim or document location
- **THEN** it verifies the claim against a primary source before including it in the final comparison

### Requirement: Comparison prompt requires a per-platform sources section

The prompt template SHALL instruct the model to include a **Sources** section within each per-platform profile, listing at least one primary source per dimension as an inline Markdown link with an access date.

#### Scenario: Researcher verifies a claim

- **WHEN** a researcher wants to verify a dimension claim for a platform
- **THEN** the platform's Sources section contains a direct link to the primary source used

### Requirement: Comparison prompt output begins with a model metadata block

The prompt template SHALL instruct the model to begin its response with a fenced YAML code block containing provenance metadata, so that saved response files are self-documenting.

The metadata block SHALL contain exactly three fields:

- `model` — the AI model's name and version as reported by the model itself
- `date` — the session date in `YYYY-MM-DD` format
- `prompt` — the name of the prompt template used (`platform-comparison`)

The metadata block SHALL appear before any other content in the response.

#### Scenario: Response is saved as a file and opened later

- **WHEN** a researcher opens a saved comparison response file
- **THEN** the first visible element is the metadata block identifying the model, date, and prompt template

#### Scenario: Model self-reports its name and version

- **WHEN** the prompt instructs the model to fill in the `model` field
- **THEN** the model populates the field with its own name and version to the best of its ability

### Requirement: Comparison prompt usage header includes save-as filename instruction

The prompt template's usage header SHALL direct the researcher to run the prompt through an AI CLI (Claude Code, Codex CLI, Gemini CLI) that asks the CLI-or-Web question on their behalf. The header SHALL NOT instruct the researcher to manually paste rubrics or selection rows, or to copy from a cut-line — that mechanic is retired.

The header SHALL state the save-as path convention: `observe/rating/cli-<model-short>.md` for CLI-mode responses, `observe/rating/web-<model-short>.md` for Web-mode responses. File names SHALL NOT include the cycle type — the folder provides that context; the `cli-` / `web-` prefix is the interface authority.

#### Scenario: Researcher opens the rating prompt file

- **WHEN** a researcher opens `act/rating/prompt.md`
- **THEN** the usage header tells them to run the prompt via their AI CLI and explains the CLI-or-Web ask — it does not include cut-line blockquotes or numbered paste instructions

#### Scenario: Researcher saves a web-chat response

- **WHEN** a researcher runs the prompt in Web mode and saves the web-chat response
- **THEN** the save-as filename follows `observe/rating/web-<model-short>.md`

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
