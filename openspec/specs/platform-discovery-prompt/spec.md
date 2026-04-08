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

The prompt template SHALL define the only allowed values for **Inclusion criterion** as: `Explicit UDT`, `City-Scale Capabilities`, and `Adjacent Architecture or Governance`. The same canonical values SHALL be used in both the summary table and the per-platform sections.

The prompt template SHALL state that the response contains exactly three parts, in order: the metadata block, the summary table, and the per-platform sections. It SHALL forbid extra top-level sections or trailing summary content outside that structure.

#### Scenario: Response is used to populate inventory
- **WHEN** an AI responds to the discovery prompt
- **THEN** each platform section contains the five identification fields and six scored dimension fields, making all data directly transferable to platform-inventory.md

#### Scenario: Discovery scores feed into comparison
- **WHEN** a researcher pastes rows from the discovery summary table into the comparison prompt
- **THEN** the dimension scores from discovery provide a starting signal that comparison refines with its full rubrics

#### Scenario: Two agents respond to the same discovery prompt
- **WHEN** a researcher runs the discovery prompt on ChatGPT and on Claude
- **THEN** both responses use identical field labels, score notation (`X/5`), and section structure

#### Scenario: Model would normally shorten category labels
- **WHEN** an AI would otherwise emit abbreviated or paraphrased inclusion labels
- **THEN** it uses only `Explicit UDT`, `City-Scale Capabilities`, or `Adjacent Architecture or Governance`

#### Scenario: Model would otherwise append a closing note
- **WHEN** an AI would otherwise add a `Sources`, `Notes`, or summary section after the platform sections
- **THEN** it omits that extra content and ends the response after the last required platform section

### Requirement: Discovery prompt response begins with a required summary table
The prompt template SHALL instruct the model to output the summary table immediately after the metadata block and before any per-platform sections. The table is required and SHALL use the following columns: **Name**, **Link**, **License**, **Type**, **Arch**, **Open**, **City**, **Mature**, **Integ**, **Gov**, **Inclusion Criterion**.

Score columns (Arch, Open, City, Mature, Integ, Gov) SHALL contain bare numbers (1–5) or `?` for unknown — no `/5` suffix.

#### Scenario: Researcher opens a discovery response to start a comparison
- **WHEN** a researcher opens a saved discovery response
- **THEN** the summary table appears at the top (after the metadata block), before any per-platform detail sections, so rows can be copied immediately without scrolling

#### Scenario: Rows are pasted into the comparison prompt
- **WHEN** a researcher copies rows from the summary table and pastes them into `[PASTE_SELECTED_PLATFORMS_HERE]`
- **THEN** the comparison prompt receives platform names, license, type, and six seed scores as context

### Requirement: Discovery prompt enforces agent-agnostic output structure
The prompt template SHALL include a concrete example of the per-platform section structure and SHALL comply with the shared Markdown contract defined in `prompt-markdown-format`.

In addition to that shared contract, the prompt SHALL specify these discovery-specific formatting constraints:

- **Platform heading level:** `##` for every platform section
- **Score notation:** `**Dimension (X/5):**` inline in sections; bare number in table cells; `?` for unknown
- **Citation override note:** the Markdown rules section SHALL explicitly state that the inline-link citation rule overrides the model's default citation format

The prompt template SHALL state that no extra headings or sections are permitted beyond the required metadata block, summary table, and `##` platform sections.

#### Scenario: Two agents respond to the same discovery prompt
- **WHEN** a researcher runs the discovery prompt on two different agents
- **THEN** both responses use the same heading level, field labels, and score notation with no agent-specific formatting artifacts

#### Scenario: Model uses AI-specific citation format by default
- **WHEN** an AI model would normally respond with bracket citations or `【†source】` style references
- **THEN** the prompt override instruction suppresses this and the model uses `[Description](https://...)` inline links instead

#### Scenario: Model would normally add extra sections
- **WHEN** an AI model would normally add a heading such as `## Sources` or `## Notes`
- **THEN** the prompt instruction suppresses that and the response contains only the required headings

### Requirement: Discovery prompt uses a parameterized search scope token
The prompt template SHALL include a `[SEARCH_SCOPE]` placeholder that the researcher replaces with a specific domain, region, or technology focus before using the prompt. If the literal text `[SEARCH_SCOPE]` has not been replaced, the model SHALL treat the scope as: global city-scale Urban Digital Twin platforms and foundational building blocks (commercial and open-source).

#### Scenario: Researcher customizes search scope
- **WHEN** a researcher replaces `[SEARCH_SCOPE]` with a value such as "European city-scale platforms" or "platforms using CityGML"
- **THEN** the model scopes its discovery results to that domain without other prompt changes needed

#### Scenario: Researcher forgets to replace the scope token
- **WHEN** a researcher pastes the prompt without replacing `[SEARCH_SCOPE]`
- **THEN** the model defaults to a global UDT scope rather than erroring or producing a generic result


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
The prompt template's usage header SHALL include numbered step-by-step instructions telling the researcher to replace `[SEARCH_SCOPE]` with their focus area, paste the completed prompt into their AI session, and save the response using the filename pattern defined in `docs/methodology.md`, with a concrete example using the `discovery` prompt-type token (e.g., `responses/european-platforms-discovery.md`).

#### Scenario: Researcher reads the usage header before pasting the prompt
- **WHEN** a researcher reads the usage instructions at the top of `prompts/platform-discovery.md`
- **THEN** they see numbered steps and the expected filename pattern before they begin the session

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

The prompt template SHALL instruct the model that factual claims in the per-platform identification and dimension bullets MUST be supported with inline Markdown links to primary sources, and that unsupported claims SHALL be written as unknown or `?` rather than sourced from secondary materials.

#### Scenario: Researcher pastes prompt without supplemental context
- **WHEN** an AI responds to the discovery prompt
- **THEN** all platform details are sourced from primary sources, not secondary summaries or AI-generated assumptions

#### Scenario: Only a secondary source is available for a claim
- **WHEN** an AI can find a secondary article but no primary source for a platform fact
- **THEN** it leaves that fact unknown or uses `?` instead of citing the secondary article

#### Scenario: Platform detail sections contain factual prose
- **WHEN** an AI writes factual content in the identification and scored dimension bullets
- **THEN** those factual sentences include inline Markdown links to primary sources
