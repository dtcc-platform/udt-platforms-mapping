### Requirement: Platform comparison prompt file exists

The repository SHALL contain a file at `prompts/platform-comparison.md` that provides a self-contained prompt template for AI-assisted side-by-side comparison of two or more UDT platforms.

#### Scenario: File is present and non-empty

- **WHEN** a researcher navigates to `prompts/platform-comparison.md`
- **THEN** the file exists and contains a complete, copy-pasteable prompt

### Requirement: Comparison prompt uses a single selection table token

The prompt template SHALL include a single `[PASTE_SELECTED_PLATFORMS_HERE]` placeholder token where the researcher pastes the rows they want to compare from the discovery response summary table, including the header row. The model SHALL treat every data row in the pasted table as a comparison target.

The placeholder SHALL be preceded by the canonical guard instruction specifying `[PASTE_SELECTED_PLATFORMS_HERE]` as the token to check for, instructing the model to stop and ask the user for the table if the placeholder is still present.

The prompt template SHALL also instruct the model that the pasted table is the comparison scope boundary and that it MUST NOT add new comparison candidates outside the pasted rows unless the user explicitly asks for that expansion. When both instructions are present, the guard instruction SHALL appear before the scope-boundary instruction, and the scope-boundary instruction SHALL appear immediately before the placeholder.

#### Scenario: Researcher customizes platforms to compare

- **WHEN** a researcher copies two rows (plus the header) from a discovery summary table and pastes them into `[PASTE_SELECTED_PLATFORMS_HERE]`
- **THEN** the model produces a comparison specifically for those two platforms

#### Scenario: Researcher compares more than two platforms

- **WHEN** a researcher copies three or more rows (plus the header) into `[PASTE_SELECTED_PLATFORMS_HERE]`
- **THEN** the model produces a comparison covering all pasted platforms without requiring any other prompt changes

#### Scenario: Prompt is used via @file reference without filling in the placeholder

- **WHEN** a model receives the prompt with the literal text `[PASTE_SELECTED_PLATFORMS_HERE]` still present
- **THEN** the model stops and asks the user to paste the platform rows before continuing, and does not generate any comparison output

#### Scenario: Research-mode interface tries to broaden scope

- **WHEN** a researcher runs the prompt in a Research or Deep Research interface
- **THEN** the model limits the comparison to the pasted platform rows and does not introduce extra platforms on its own

### Requirement: Comparison prompt covers twelve dimensions with scoring
The prompt template SHALL instruct the model to compare platforms across all twelve dimensions — the six research dimensions (Technical Architecture, Openness & Licensing, City-Scale Capability, Maturity & Adoption, Integration Posture, Governance) and the six functional categories (Visualization, Data Management, Simulation, IoT Sensing, Standards, Infrastructure) — and assign each platform a score of 1–5 per dimension using rubrics defined in the pasted scope content.

The prompt SHALL state that rubrics are supplied via `[PASTE_SCOPE_HERE]` and are not embedded inline.

#### Scenario: Response covers all twelve dimensions with scores
- **WHEN** an AI responds to the comparison prompt
- **THEN** the response addresses each of the twelve dimensions for every platform and assigns a numeric 1–5 score with rationale

#### Scenario: Researcher compares scores across agents
- **WHEN** a researcher runs the same comparison on two different AI agents
- **THEN** both responses use the same dimension labels and scoring scale, making scores comparable

### Requirement: Comparison prompt includes a [PASTE_SCOPE_HERE] guard
The prompt template SHALL include a `[PASTE_SCOPE_HERE]` placeholder where the researcher pastes the full content of `docs/01-scope.md` before running a session. The placeholder SHALL be preceded by a guard instruction telling the model: _if `[PASTE_SCOPE_HERE]` still appears verbatim, stop and ask the user to paste `docs/01-scope.md` before continuing._

The usage header SHALL be updated to include a step directing the researcher to paste `docs/01-scope.md` into the `[PASTE_SCOPE_HERE]` slot as the first preparation step.

#### Scenario: Researcher runs the comparison without pasting scope
- **WHEN** a researcher pastes the comparison prompt into an AI session without replacing `[PASTE_SCOPE_HERE]`
- **THEN** the model stops and asks them to provide the scope content before producing any output

#### Scenario: Researcher runs the comparison after pasting scope
- **WHEN** a researcher pastes `docs/01-scope.md` content into the `[PASTE_SCOPE_HERE]` slot
- **THEN** the model proceeds with all 13 rubrics available and produces a complete comparison response

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

The Part 1 scoring table SHALL include one column per functional category in addition to the six dimension columns. The six functional categories are: `visualization` (abbreviated `Viz`), `data-management` (`DM`), `simulation` (`Sim`), `iot-sensing` (`IoT`), `standards` (`Std`), and `infrastructure` (`Infra`).

Each category column SHALL use the same 1–5 integer scoring format as dimension columns — bare integer, `?` for unknown, no `/5` suffix in table cells.

The prompt SHALL include a legend immediately below the Part 1 table instruction listing each abbreviated column header with its full name and one-line description, for both dimension abbreviations and category abbreviations.

#### Scenario: Researcher reads the Part 1 table

- **WHEN** an AI responds to the comparison prompt
- **THEN** the Part 1 table header contains exactly: `Name`, `Link`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`

#### Scenario: Researcher needs to interpret an abbreviated column

- **WHEN** a researcher reads the Part 1 table instruction in the prompt
- **THEN** a legend block immediately below the instruction lists every abbreviated header with its full name and a one-line description

#### Scenario: Researcher compares functional strengths across platforms

- **WHEN** an AI responds to the comparison prompt
- **THEN** every platform row contains a numeric 1–5 score (or `?`) in every category column

### Requirement: Comparison prompt includes DTCC as a required reference entry

The prompt template SHALL include a description of DTCC (Digital Twin Cities Centre) as a reference platform and SHALL instruct the model to include DTCC as an entry in the comparison, so that every response positions the landscape relative to DTCC.

#### Scenario: Response is used to position DTCC in the landscape

- **WHEN** an AI responds to the comparison prompt
- **THEN** DTCC appears as a platform entry and the landscape observations section explicitly addresses where DTCC sits relative to comparable and complementary platforms

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

The prompt template's usage header SHALL include an instruction telling the researcher what filename to use when saving the AI response, referencing the pattern defined in `docs/02-methodology.md`.

The instruction SHALL show a concrete example filename using the `comparison` prompt-type token and the `vs` join convention for two platforms (e.g., `responses/<platform-a>-vs-<platform-b>-comparison.md`).

The usage header SHALL also include a step directing the researcher to paste into their AI session starting from the cut-line (the blockquote `> Paste into your AI session from this line onwards.`), not from the top of the file.

The usage header SHALL state that the prompt can be used in either an AI web research chat or an AI CLI session. For web chat use, it SHALL tell the researcher to manually save the final Markdown response into `responses/`.

#### Scenario: Researcher reads the usage header before pasting the prompt

- **WHEN** a researcher reads the usage instructions at the top of `prompts/platform-comparison.md`
- **THEN** they see the expected filename pattern, a concrete example, an explicit step telling them to paste from the cut-line onwards, and an explicit note that web-chat sessions require manual save/export into `responses/`

#### Scenario: Researcher pastes only the AI-facing section

- **WHEN** a researcher follows the usage instructions and pastes from the cut-line onwards into a fresh AI session
- **THEN** the model receives no human-facing usage steps, only the AI prompt body, and produces the comparison report without confusion
