## MODIFIED Requirements

### Requirement: Discovery prompt response ends with a required summary table
The prompt template SHALL instruct the model to append a summary table after all per-platform sections. The table is required and SHALL use the following columns: **Name**, **Link**, **License**, **Type**, **Arch**, **Open**, **City**, **Mature**, **Integ**, **Gov**, **Inclusion Criterion**.

Score columns (Arch, Open, City, Mature, Integ, Gov) SHALL contain bare numbers (1–5) or `?` for unknown — no `/5` suffix.

#### Scenario: Researcher saves a discovery response and wants to start a comparison
- **WHEN** a researcher opens a saved discovery response
- **THEN** the file ends with a summary table containing all discovered platforms and six dimension scores

#### Scenario: Rows are pasted into the comparison prompt
- **WHEN** a researcher copies rows from the summary table and pastes them into `[PASTE_SELECTED_PLATFORMS_HERE]`
- **THEN** the comparison prompt receives platform names, license, type, and six seed scores as context

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
