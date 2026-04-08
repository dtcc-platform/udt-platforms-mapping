### Requirement: Platform comparison prompt file exists

The repository SHALL contain a file at `prompts/platform-comparison.md` that provides a self-contained prompt template for AI-assisted side-by-side comparison of two or more UDT platforms.

#### Scenario: File is present and non-empty

- **WHEN** a researcher navigates to `prompts/platform-comparison.md`
- **THEN** the file exists and contains a complete, copy-pasteable prompt

### Requirement: Comparison prompt uses a single selection table token

The prompt template SHALL include a single `[PASTE_SELECTED_PLATFORMS_HERE]` placeholder token where the researcher pastes the rows they want to compare from the discovery response summary table, including the header row. The model SHALL treat every data row in the pasted table as a comparison target.

The placeholder SHALL be immediately preceded by the canonical guard instruction specifying `[PASTE_SELECTED_PLATFORMS_HERE]` as the token to check for, instructing the model to stop and ask the user for the table if the placeholder is still present.

#### Scenario: Researcher customizes platforms to compare

- **WHEN** a researcher copies two rows (plus the header) from a discovery summary table and pastes them into `[PASTE_SELECTED_PLATFORMS_HERE]`
- **THEN** the model produces a comparison specifically for those two platforms

#### Scenario: Researcher compares more than two platforms

- **WHEN** a researcher copies three or more rows (plus the header) into `[PASTE_SELECTED_PLATFORMS_HERE]`
- **THEN** the model produces a comparison covering all pasted platforms without requiring any other prompt changes

#### Scenario: Prompt is used via @file reference without filling in the placeholder

- **WHEN** a model receives the prompt with the literal text `[PASTE_SELECTED_PLATFORMS_HERE]` still present
- **THEN** the model stops and asks the user to paste the platform rows before continuing, and does not generate any comparison output

### Requirement: Comparison prompt covers the six research dimensions with scoring

The prompt template SHALL instruct the model to compare platforms across all six dimensions — technical architecture, openness and licensing, city-scale capability, platform maturity, integration posture, and governance model — and assign each platform a score of 1–5 per dimension using a rubric defined in the prompt. The rubric for each dimension SHALL be self-contained in the prompt so the model can apply it without additional context.

#### Scenario: Response covers all dimensions with scores

- **WHEN** an AI responds to the comparison prompt
- **THEN** the response addresses each of the six dimensions for every platform and assigns a numeric 1–5 score with rationale

#### Scenario: Researcher compares scores across agents

- **WHEN** a researcher runs the same comparison on two different AI agents
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

### Requirement: Comparison prompt defines functional category rubrics

The prompt template SHALL define a 1–5 scoring rubric for each of the six functional categories. Each rubric SHALL be self-contained in the prompt and SHALL provide anchor descriptions for scores 1, 3, and 5 at minimum.

The same rubrics SHALL appear in `docs/methodology.md` in a dedicated section alongside the existing workflow prose, so researchers have a stable reference without reading the full prompt.

#### Scenario: AI scores a platform's visualization capability

- **WHEN** an AI assigns a `Viz` score to a platform
- **THEN** the score reflects the rubric anchors defined in the prompt — 5 for purpose-built primary visualization, 3 for moderate capability not the primary strength, 1 for absent or negligible

#### Scenario: Researcher consults methodology for category definitions

- **WHEN** a researcher opens `docs/methodology.md`
- **THEN** a section lists all six functional category rubrics with their 1–5 anchor descriptions

#### Scenario: Two agents score the same platform's functional category

- **WHEN** a researcher runs the comparison prompt on two different AI agents
- **THEN** both agents apply the same rubric anchors, producing comparable category scores

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

### Requirement: Comparison prompt requires explicit uncertainty handling

The prompt template SHALL instruct the model to distinguish inferred claims from verified facts, state "unknown" or "unclear" when information is not findable, and never fabricate URLs, license names, or deployment claims.

#### Scenario: Model cannot find license information

- **WHEN** an AI cannot locate a platform's license from primary sources
- **THEN** the response states "unknown" rather than guessing or inferring

#### Scenario: Model infers a score from indirect evidence

- **WHEN** an AI assigns a dimension score based on indirect evidence
- **THEN** the response explicitly flags this as an inference (e.g., "likely X based on [evidence]")

### Requirement: Comparison prompt instructs use of primary sources

The prompt template SHALL instruct the model to base its comparison on primary sources (official documentation, repositories, published papers) and to cite sources for each claim.

#### Scenario: Response includes source citations

- **WHEN** an AI responds to the comparison prompt
- **THEN** each substantive claim is accompanied by a source reference or URL

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

The prompt template's usage header SHALL include an instruction telling the researcher what filename to use when saving the AI response, referencing the pattern defined in `docs/methodology.md`.

The instruction SHALL show a concrete example filename using the `comparison` prompt-type token and the `vs` join convention for two platforms (e.g., `responses/<platform-a>-vs-<platform-b>-comparison.md`).

The usage header SHALL also include a step directing the researcher to paste into their AI session starting from the cut-line (the blockquote `> Paste into your AI session from this line onwards.`), not from the top of the file.

#### Scenario: Researcher reads the usage header before pasting the prompt

- **WHEN** a researcher reads the usage instructions at the top of `prompts/platform-comparison.md`
- **THEN** they see the expected filename pattern, a concrete example, and an explicit step telling them to paste from the cut-line onwards

#### Scenario: Researcher pastes only the AI-facing section

- **WHEN** a researcher follows the usage instructions and pastes from the cut-line onwards into a fresh AI session
- **THEN** the model receives no human-facing usage steps, only the AI prompt body, and produces the comparison report without confusion
