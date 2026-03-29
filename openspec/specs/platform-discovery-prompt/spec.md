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
The prompt template SHALL instruct the model to return one `##`-level Markdown section per platform containing two blocks:

1. **Identification block** — five labelled bullet fields: **Organization**, **Link**, **License**, **Type**, **Inclusion criterion**
2. **Dimension block** — six labelled bullet fields, one per comparison dimension, each with an inline `X/5` score and a one-sentence rationale: **Technical Architecture (X/5)**, **Openness & Licensing (X/5)**, **City-Scale Capability (X/5)**, **Maturity & Adoption (X/5)**, **Integration Posture (X/5)**, **Governance (X/5)**

The score scale (1–5) SHALL match the comparison prompt's scoring scale. The prompt SHALL instruct agents to score by judgment — no rubric tables are required in the discovery prompt.

The prompt template SHALL include a concrete example section demonstrating the exact field labels, score notation, and two-block structure.

#### Scenario: Response is used to populate inventory
- **WHEN** an AI responds to the discovery prompt
- **THEN** each platform section contains the five identification fields and six scored dimension fields, making all data directly transferable to platform-inventory.md

#### Scenario: Discovery scores feed into comparison
- **WHEN** a researcher pastes rows from the discovery summary table into the comparison prompt
- **THEN** the dimension scores from discovery provide a starting signal that comparison refines with its full rubrics

#### Scenario: Two agents respond to the same discovery prompt
- **WHEN** a researcher runs the discovery prompt on ChatGPT and on Claude
- **THEN** both responses use identical field labels, score notation (`X/5`), and section structure

### Requirement: Discovery prompt response ends with a required summary table
The prompt template SHALL instruct the model to append a summary table after all per-platform sections. The table is required and SHALL use the following columns: **Name**, **Link**, **License**, **Type**, **Arch**, **Open**, **City**, **Mature**, **Integ**, **Gov**, **Inclusion Criterion**.

Score columns (Arch, Open, City, Mature, Integ, Gov) SHALL contain bare numbers (1–5) or `?` for unknown — no `/5` suffix.

#### Scenario: Researcher saves a discovery response and wants to start a comparison
- **WHEN** a researcher opens a saved discovery response
- **THEN** the file ends with a summary table containing all discovered platforms and six dimension scores

#### Scenario: Rows are pasted into the comparison prompt
- **WHEN** a researcher copies rows from the summary table and pastes them into `[PASTE_SELECTED_PLATFORMS_HERE]`
- **THEN** the comparison prompt receives platform names, license, type, and six seed scores as context

### Requirement: Discovery prompt enforces agent-agnostic output structure
The prompt template SHALL include a concrete example of the per-platform section structure and SHALL specify the following formatting constraints:

- **Permitted syntax:** ATX headings (`#`), `**bold**`, `_italic_`, `[text](url)` links, fenced code blocks, GFM pipe tables, `-` unordered lists, `1.` ordered lists
- **Citation format:** inline links `[Description](https://...)` only — no numeric brackets (`[1]`), no footnotes (`[^1]`), no AI-specific citation formats
- **Prohibited syntax:** custom containers (`:::`, `!!!`, `> [!NOTE]`), extended syntax (`==highlight==`, `^superscript^`, `~subscript~`), raw HTML
- **Whitespace:** blank line before and after every heading, table, and code block
- **Platform heading level:** `##` for every platform section
- **Score notation:** `**Dimension (X/5):**` inline in sections; bare number in table cells; `?` for unknown

#### Scenario: Two agents respond to the same discovery prompt
- **WHEN** a researcher runs the discovery prompt on two different agents
- **THEN** both responses use the same heading level, field labels, and score notation with no agent-specific formatting artifacts

### Requirement: Discovery prompt uses a parameterized search scope token
The prompt template SHALL include a `[SEARCH_SCOPE]` placeholder that the researcher replaces with a specific domain, region, or technology focus before using the prompt.

#### Scenario: Researcher customizes search scope
- **WHEN** a researcher replaces `[SEARCH_SCOPE]` with a value such as "European city-scale platforms" or "platforms using CityGML"
- **THEN** the model scopes its discovery results to that domain without other prompt changes needed


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

### Requirement: Discovery prompt requires explicit uncertainty handling
The prompt template SHALL instruct the model to state `?` when a dimension score cannot be assessed from available sources, and to never fabricate platform details, license names, or deployment claims.

#### Scenario: Model cannot assess a dimension
- **WHEN** an AI cannot find sufficient information to score a dimension
- **THEN** the response uses `?` rather than guessing

#### Scenario: Model cannot verify a platform detail
- **WHEN** an AI cannot confirm a license name or deployment from primary sources
- **THEN** the response states the information is unknown rather than fabricating it

### Requirement: Discovery prompt instructs use of primary sources
The prompt template SHALL instruct the model to base its findings on primary sources only — official websites, public repositories, published papers, and official documentation.

#### Scenario: Researcher pastes prompt without supplemental context
- **WHEN** an AI responds to the discovery prompt
- **THEN** all platform details are sourced from primary sources, not secondary summaries or AI-generated assumptions
