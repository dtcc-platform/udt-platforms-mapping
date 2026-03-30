### Requirement: License analysis prompt file exists
The repository SHALL contain a file at `prompts/license-analysis.md` that provides a self-contained prompt template for AI-assisted evaluation of a platform's license.

#### Scenario: File is present and non-empty
- **WHEN** a researcher navigates to `prompts/license-analysis.md`
- **THEN** the file exists and contains a complete, copy-pasteable prompt

### Requirement: License analysis prompt uses a discovery table row token
The prompt template SHALL include a single `[PASTE_SELECTED_PLATFORM_HERE]` placeholder token where the researcher pastes one row (plus the header row) from the discovery response summary table. The model SHALL derive the platform name from the Name column, use the Link column to locate the license source, and treat the License column value as a seed signal to verify or correct.

The placeholder SHALL be immediately preceded by the canonical guard instruction specifying `[PASTE_SELECTED_PLATFORM_HERE]` as the token to check for, instructing the model to stop and ask the user for the platform row if the placeholder is still present.

#### Scenario: Researcher pastes a discovery row
- **WHEN** a researcher copies the header row and one data row from a discovery summary table and pastes them into `[PASTE_SELECTED_PLATFORM_HERE]`
- **THEN** the model identifies the platform, locates the license from the Link, and produces a full license analysis

#### Scenario: Researcher runs license analysis without a prior discovery session
- **WHEN** a researcher manually constructs a single-row table matching the discovery summary table schema and pastes it into `[PASTE_SELECTED_PLATFORM_HERE]`
- **THEN** the model produces a full license analysis using the provided fields

#### Scenario: Prompt is used via @file reference without filling in the placeholder
- **WHEN** a model receives the prompt with the literal text `[PASTE_SELECTED_PLATFORM_HERE]` still present
- **THEN** the model stops and asks the user to paste the platform row before continuing, and does not generate any license analysis output

### Requirement: License analysis prompt embeds the license family taxonomy
The prompt template SHALL include the license family definitions from `docs/license-review.md` — permissive open source, copyleft (strong), copyleft (weak), open core, and proprietary — so the model classifies using the project's taxonomy.

#### Scenario: Model classifies license using project taxonomy
- **WHEN** an AI responds to the license analysis prompt
- **THEN** the response assigns one of the five license families defined in `docs/license-review.md`

### Requirement: License analysis prompt embeds the openness scoring rubric
The prompt template SHALL include the 1–5 Openness & Licensing scoring rubric from `docs/license-review.md` and instruct the model to assign a score with a rationale.

#### Scenario: Response includes an openness score
- **WHEN** an AI responds to the license analysis prompt
- **THEN** the response includes a numeric score from 1 to 5 and a one-sentence rationale

### Requirement: License analysis prompt covers data licensing
The prompt template SHALL instruct the model to assess data licensing separately from software licensing, noting any open geospatial standards used and any proprietary data format lock-in.

#### Scenario: Response addresses data licensing
- **WHEN** an AI responds to the license analysis prompt
- **THEN** the response includes a separate section on data licensing distinct from software licensing

### Requirement: License analysis prompt output maps to review checklist
The prompt template SHALL instruct the model to address every item in the review checklist defined in `docs/license-review.md`: locate the license, identify the family, note data format lock-in, check for community vs. enterprise tier split, and assign a score.

#### Scenario: Response covers all checklist items
- **WHEN** an AI responds to the license analysis prompt
- **THEN** each of the five checklist items from `docs/license-review.md` is addressed in the response

### Requirement: License analysis prompt output uses portable Markdown syntax
The prompt template SHALL instruct the model to format its response using only CommonMark / GFM syntax, so that saved response files render correctly in any standard Markdown viewer without AI-specific formatting artifacts.

The instruction SHALL appear under the section heading `### Markdown and Formatting Rules` and SHALL use the structured `**Permitted syntax only:**` / `**Prohibited syntax:**` format. It SHALL specify:

- **Permitted syntax only:** ATX headings (`#`), `**bold**`, `_italic_`, `[text](url)` links, fenced code blocks, GFM pipe tables, `-` unordered lists, `1.` ordered lists
- **Citation format:** inline links `[Description](https://...)` only — no numeric brackets (`[1]`), no footnotes (`[^1]`), no AI-specific formats
- **Prohibited syntax:** custom containers (`:::`, `!!!`, `> [!NOTE]`), extended syntax (`==highlight==`, `^superscript^`, `~subscript~`), raw HTML
- **Whitespace:** blank line before and after every heading, table, and code block
- **Score notation:** in the Score field, bare number only (1–5) — do not write `/5`

#### Scenario: Model uses AI-specific citation format
- **WHEN** an AI model would normally respond with numeric bracket citations like `[1]` or `【†source】`
- **THEN** the prompt instruction overrides this and the model uses `[Description](https://...)` inline links instead

#### Scenario: Response is opened in a standard Markdown viewer
- **WHEN** a researcher saves the response as a `.md` file and opens it in GitHub, VS Code, Obsidian, or Typora
- **THEN** all formatting renders correctly with no raw syntax visible and no broken elements

### Requirement: License analysis prompt output begins with a model metadata block
The prompt template SHALL instruct the model to begin its response with a fenced YAML code block containing provenance metadata, so that saved response files are self-documenting.

The metadata block SHALL contain exactly three fields:
- `model` — the AI model's name and version as reported by the model itself
- `date` — the session date in `YYYY-MM-DD` format
- `prompt` — the name of the prompt template used (`license-analysis`)

The metadata block SHALL appear before any other content in the response.

#### Scenario: Response is saved as a file and opened later
- **WHEN** a researcher opens a saved license analysis response file
- **THEN** the first visible element is the metadata block identifying the model, date, and prompt template

#### Scenario: Model self-reports its name and version
- **WHEN** the prompt instructs the model to fill in the `model` field
- **THEN** the model populates the field with its own name and version to the best of its ability

### Requirement: License analysis prompt requires explicit uncertainty handling
The prompt template SHALL instruct the model to state "unknown" or "unclear" when license information cannot be confirmed from primary sources, and to never fabricate license names, URLs, or tier descriptions.

#### Scenario: Model cannot locate a license
- **WHEN** an AI cannot find a platform's license from the repository root, package metadata, or official site
- **THEN** the response states the license is unknown rather than guessing

#### Scenario: Model cannot confirm a tier distinction
- **WHEN** an AI cannot verify whether a community vs. enterprise split exists
- **THEN** the response states "unclear" rather than assuming

### Requirement: License analysis prompt instructs use of primary sources
The prompt template SHALL instruct the model to locate and verify license information from primary sources only — repository root (`LICENSE`, `COPYING`), SPDX identifiers in package metadata, and official site documentation.

#### Scenario: Model locates license from primary source
- **WHEN** an AI responds to the license analysis prompt
- **THEN** the source of the license identification is a direct link to the repository or official documentation, not a secondary summary

### Requirement: License analysis prompt usage header includes save-as filename instruction
The prompt template's usage header SHALL include numbered step-by-step instructions telling the researcher to open the discovery response, copy the header row and the platform row from the summary table, replace `[PASTE_SELECTED_PLATFORM_HERE]` with those rows, and paste the completed prompt into their AI session. It SHALL also tell the researcher what filename to use when saving the response, referencing the pattern defined in `docs/methodology.md`, with a concrete example using the `license` prompt-type token (e.g., `responses/<platform>-license.md`).

The usage header SHALL NOT include a separate blockquote for the license taxonomy source of truth — the taxonomy is embedded in the prompt body.

#### Scenario: Researcher reads the usage header before pasting the prompt
- **WHEN** a researcher reads the usage instructions at the top of `prompts/license-analysis.md`
- **THEN** they see the row-paste steps and the expected filename pattern before they begin the session, with no extra blockquotes beyond the save-as instruction
