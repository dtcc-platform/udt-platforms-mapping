### Requirement: Platform comparison prompt file exists
The repository SHALL contain a file at `prompts/platform-comparison.md` that provides a self-contained prompt template for AI-assisted side-by-side comparison of two or more UDT platforms.

#### Scenario: File is present and non-empty
- **WHEN** a researcher navigates to `prompts/platform-comparison.md`
- **THEN** the file exists and contains a complete, copy-pasteable prompt

### Requirement: Comparison prompt uses parameterized platform name tokens
The prompt template SHALL include `[PLATFORM_A]` and `[PLATFORM_B]` placeholder tokens (and optionally more) that the researcher replaces with platform names selected from `docs/platform-inventory.md`.

#### Scenario: Researcher customizes platforms to compare
- **WHEN** a researcher replaces `[PLATFORM_A]` with "DTCC" and `[PLATFORM_B]` with "Cesium"
- **THEN** the model produces a comparison specifically for those two platforms

### Requirement: Comparison prompt accepts inventory context
The prompt template SHALL include a `[PASTE_INVENTORY_ROWS_HERE]` placeholder where the researcher pastes the relevant rows from `docs/platform-inventory.md`, so the model can build on existing research rather than starting from scratch.

#### Scenario: Researcher provides existing inventory context
- **WHEN** a researcher pastes inventory rows for the chosen platforms into `[PASTE_INVENTORY_ROWS_HERE]`
- **THEN** the model acknowledges the known data and focuses its research on dimensions not yet captured in the inventory

### Requirement: Comparison prompt covers the six research dimensions
The prompt template SHALL instruct the model to compare platforms across all six dimensions used in this research: technical architecture, openness and licensing, city-scale capability, platform maturity, integration posture, and governance model.

#### Scenario: Response covers all dimensions
- **WHEN** an AI responds to the comparison prompt
- **THEN** the response addresses each of the six dimensions for every platform being compared

### Requirement: Comparison prompt requests a structured table output
The prompt template SHALL instruct the model to include a summary comparison table with one row per platform and one column per dimension, in addition to any prose analysis.

#### Scenario: Researcher extracts summary data
- **WHEN** an AI responds to the comparison prompt
- **THEN** the response includes a Markdown table suitable for direct inclusion in research notes or docs

### Requirement: Comparison prompt instructs use of primary sources
The prompt template SHALL instruct the model to base its comparison on primary sources (official documentation, repositories, published papers) and to cite sources for each claim.

#### Scenario: Response includes source citations
- **WHEN** an AI responds to the comparison prompt
- **THEN** each substantive claim is accompanied by a source reference or URL

### Requirement: Comparison prompt output uses portable Markdown syntax
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
