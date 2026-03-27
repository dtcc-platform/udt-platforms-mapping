### Requirement: License analysis prompt file exists
The repository SHALL contain a file at `prompts/license-analysis.md` that provides a self-contained prompt template for AI-assisted evaluation of a platform's license.

#### Scenario: File is present and non-empty
- **WHEN** a researcher navigates to `prompts/license-analysis.md`
- **THEN** the file exists and contains a complete, copy-pasteable prompt

### Requirement: License analysis prompt uses a parameterized platform token
The prompt template SHALL include a `[PLATFORM_NAME]` placeholder and a `[LICENSE_URL_OR_TEXT]` placeholder that the researcher fills in before use.

#### Scenario: Researcher customizes prompt for a specific platform
- **WHEN** a researcher replaces `[PLATFORM_NAME]` with "CityGML" and provides a license URL or pasted license text in `[LICENSE_URL_OR_TEXT]`
- **THEN** the model analyzes the specific license for that platform

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

The instruction SHALL specify:
- Permitted syntax: ATX headings (`#`), `**bold**`, `_italic_`, `[text](url)` links, fenced code blocks, GFM pipe tables, `-` unordered lists, `1.` ordered lists
- Citation format: inline links `[Description](https://...)` only — no numeric brackets (`[1]`), no footnotes (`[^1]`), no AI-specific formats
- Prohibited syntax: custom containers (`:::`, `!!!`, `> [!NOTE]`), extended syntax (`==highlight==`, `^superscript^`, `~subscript~`), raw HTML
- Whitespace: blank line before and after every heading, table, and code block

#### Scenario: Model uses AI-specific citation format
- **WHEN** an AI model would normally respond with numeric bracket citations like `[1]` or `【†source】`
- **THEN** the prompt instruction overrides this and the model uses `[Description](https://...)` inline links instead

#### Scenario: Response is opened in a standard Markdown viewer
- **WHEN** a researcher saves the response as a `.md` file and opens it in GitHub, VS Code, Obsidian, or Typora
- **THEN** all formatting renders correctly with no raw syntax visible and no broken elements
