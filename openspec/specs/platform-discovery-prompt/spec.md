### Requirement: Platform discovery prompt file exists
The repository SHALL contain a file at `prompts/platform-discovery.md` that provides a self-contained prompt template for AI-assisted discovery of UDT platforms.

#### Scenario: File is present and non-empty
- **WHEN** a researcher navigates to `prompts/platform-discovery.md`
- **THEN** the file exists and contains a complete, copy-pasteable prompt

### Requirement: Discovery prompt embeds inclusion criteria
The prompt template SHALL include all three inclusion criteria from `docs/methodology.md` — Explicit Urban Digital Twin, City-Scale Capabilities, and Adjacent Architecture or Governance — so the model can apply them without additional context.

#### Scenario: Researcher pastes prompt without supplemental docs
- **WHEN** a researcher copies the prompt and pastes it into an AI chat session without pasting `docs/methodology.md`
- **THEN** the model has sufficient criteria to correctly classify a platform as in-scope or out-of-scope

### Requirement: Discovery prompt requests structured output aligned with inventory
The prompt template SHALL instruct the model to return one `##`-level Markdown section per platform, each containing a fixed bullet list with exactly the following labelled fields: **Organization**, **Link**, **License**, **Type**, **Maturity**, **City-scale capability**, **Integration posture**, **Inclusion criterion**, and **Notes**. This structure SHALL appear before any optional summary content.

The prompt template SHALL include a concrete example of the per-platform section so agents can reproduce the exact shape without interpreting an abstract description.

#### Scenario: Response is used to populate inventory
- **WHEN** an AI responds to the discovery prompt
- **THEN** the response contains one `##` heading per platform followed by exactly the nine labelled bullet fields, making each field directly transferable to a platform-inventory.md row

#### Scenario: Response is opened for manual review
- **WHEN** a researcher opens a saved discovery response
- **THEN** each platform is scannable as a self-contained section with consistent field labels, without needing to cross-reference a table and a separate paragraph block

#### Scenario: Two responses from different agents cover the same platform
- **WHEN** a researcher compares a ChatGPT response and a Claude response for the same platform
- **THEN** both use the same section heading and bullet field structure, making the comparison straightforward

### Requirement: Discovery prompt uses a parameterized search scope token
The prompt template SHALL include a `[SEARCH_SCOPE]` placeholder that the researcher replaces with a specific domain, region, or technology focus before using the prompt.

#### Scenario: Researcher customizes search scope
- **WHEN** a researcher replaces `[SEARCH_SCOPE]` with a value such as "European city-scale platforms" or "platforms using CityGML"
- **THEN** the model scopes its discovery results to that domain without other prompt changes needed

### Requirement: Discovery prompt output uses portable Markdown syntax
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

### Requirement: Discovery prompt output begins with a model metadata block
The prompt template SHALL instruct the model to begin its response with a fenced YAML code block containing provenance metadata, so that saved response files are self-documenting.

The metadata block SHALL contain exactly three fields:
- `model` — the AI model's name and version as reported by the model itself
- `date` — the session date in `YYYY-MM-DD` format
- `prompt` — the name of the prompt template used (`platform-discovery`)

The metadata block SHALL appear before any other content in the response.

#### Scenario: Response is saved as a file and opened later
- **WHEN** a researcher opens a saved discovery response file
- **THEN** the first visible element is the metadata block identifying the model, date, and prompt template

#### Scenario: Model self-reports its name and version
- **WHEN** the prompt instructs the model to fill in the `model` field
- **THEN** the model populates the field with its own name and version to the best of its ability

### Requirement: Discovery prompt usage header includes save-as filename instruction
The prompt template's usage header SHALL include an instruction telling the researcher what filename to use when saving the AI response, referencing the pattern defined in `docs/methodology.md`.

The instruction SHALL show a concrete example filename using the `discovery` prompt-type token (e.g., `responses/<platform>-discovery.md` or `responses/european-platforms-discovery.md` for broad scope sessions).

#### Scenario: Researcher reads the usage header before pasting the prompt
- **WHEN** a researcher reads the usage instructions at the top of `prompts/platform-discovery.md`
- **THEN** they see the expected filename pattern and a concrete example before they begin the session
