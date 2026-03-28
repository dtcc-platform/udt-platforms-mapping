## MODIFIED Requirements

### Requirement: Discovery prompt requests structured output aligned with inventory
The prompt template SHALL instruct the model to return one `##`-level Markdown section per platform containing two blocks:

1. **Identification block** — five labelled bullet fields: **Organization**, **Link**, **License**, **Type**, **Inclusion criterion**
2. **Dimension block** — six labelled bullet fields, one per comparison dimension, each with an inline `X/5` score and a one-sentence rationale: **Technical Architecture (X/5)**, **Openness & Licensing (X/5)**, **City-Scale Capability (X/5)**, **Maturity & Adoption (X/5)**, **Integration Posture (X/5)**, **Governance (X/5)**

The score scale (1–5) SHALL match the comparison prompt's scoring scale. The prompt SHALL instruct agents to score by judgment — no rubric tables are required in the discovery prompt.

The prompt SHALL include a concrete example section demonstrating the exact field labels, score notation, and two-block structure.

#### Scenario: Response is used to populate inventory
- **WHEN** an AI responds to the discovery prompt
- **THEN** each platform section contains the five identification fields and six scored dimension fields, making all data directly transferable to platform-inventory.md

#### Scenario: Discovery scores feed into comparison
- **WHEN** a researcher pastes marked rows from the discovery summary table into the comparison prompt
- **THEN** the dimension scores from discovery provide a starting signal that comparison refines with its full rubrics

#### Scenario: Two agents respond to the same discovery prompt
- **WHEN** a researcher runs the discovery prompt on ChatGPT and on Claude
- **THEN** both responses use identical field labels, score notation (`X/5`), and section structure

### Requirement: Discovery prompt response ends with a required summary table
The prompt template SHALL instruct the model to append a summary table after all per-platform sections. The table is required and SHALL use the following columns: **Name**, **Link**, **License**, **Type**, **Arch**, **Open**, **City**, **Mature**, **Integ**, **Gov**, **Inclusion Criterion**, **Select**.

Score columns (Arch, Open, City, Mature, Integ, Gov) SHALL contain bare numbers (1–5) or `?` for unknown — no `/5` suffix. The **Select** column SHALL be left empty in the model's response.

#### Scenario: Researcher saves a discovery response and wants to start a comparison
- **WHEN** a researcher opens a saved discovery response
- **THEN** the file ends with a summary table containing all discovered platforms, six dimension scores, and an empty Select column ready to be marked

#### Scenario: Marked rows are pasted into the comparison prompt
- **WHEN** a researcher copies `x`-marked rows from the summary table and pastes them into `[PASTE_SELECTED_PLATFORMS_HERE]`
- **THEN** the comparison prompt receives platform names, license, type, and six seed scores as context

### Requirement: Discovery prompt enforces agent-agnostic output structure
The prompt template SHALL include a concrete example of the per-platform section structure and SHALL specify the following formatting constraints:

- **Permitted syntax:** ATX headings (`#`), `**bold**`, `_italic_`, `[text](url)` links, fenced code blocks, GFM pipe tables, `-` unordered lists, `1.` ordered lists
- **Prohibited syntax:** custom containers (`:::`, `!!!`, `> [!NOTE]`), extended syntax (`==highlight==`, `^superscript^`, `~subscript~`), raw HTML, numeric citations `[1]`, footnotes `[^1]`, AI-specific formats
- **Whitespace:** blank line before and after every heading, table, and code block
- **Platform heading level:** `##` for every platform section
- **Score notation:** `**Dimension (X/5):**` inline in sections; bare number in table cells; `?` for unknown

#### Scenario: Two agents respond to the same discovery prompt
- **WHEN** a researcher runs the discovery prompt on two different agents
- **THEN** both responses use the same heading level, field labels, and score notation with no agent-specific formatting artifacts
