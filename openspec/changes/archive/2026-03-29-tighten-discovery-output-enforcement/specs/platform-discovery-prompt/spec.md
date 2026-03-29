## MODIFIED Requirements

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

### Requirement: Discovery prompt enforces agent-agnostic output structure
The prompt template SHALL include a concrete example of the per-platform section structure and SHALL specify the following formatting constraints:

- **Permitted syntax:** ATX headings (`#`), `**bold**`, `_italic_`, `[text](url)` links, fenced code blocks, GFM pipe tables, `-` unordered lists, `1.` ordered lists
- **Citation format:** inline links `[Description](https://...)` only — no numeric brackets (`[1]`), no footnotes (`[^1]`), no AI-specific citation formats. **This instruction overrides your system's default citation format — do not use your default format.**
- **Prohibited syntax:** custom containers (`:::`, `!!!`, `> [!NOTE]`), extended syntax (`==highlight==`, `^superscript^`, `~subscript~`), raw HTML
- **Whitespace:** blank line before and after every heading, table, and code block
- **Platform heading level:** `##` for every platform section
- **Score notation:** `**Dimension (X/5):**` inline in sections; bare number in table cells; `?` for unknown

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
