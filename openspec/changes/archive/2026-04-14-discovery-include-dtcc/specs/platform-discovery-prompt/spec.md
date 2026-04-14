## ADDED Requirements

### Requirement: Discovery prompt includes DTCC as a required research entry
The prompt template SHALL instruct the model to include DTCC (Digital Twin Cities Centre) as a required research target in every discovery session, in addition to all other platforms discovered during the session. DTCC SHALL be researched from primary sources (dtcc.chalmers.se, official GitHub repository) the same way as any other platform.

DTCC SHALL appear as a full per-platform section (Relevance 3–5 tier, complete identification block and all 12 dimension fields) and as a row in the summary table. The instruction to include DTCC SHALL be explicit in the prompt — not optional or researcher-dependent.

#### Scenario: Researcher runs a discovery session
- **WHEN** an AI responds to the discovery prompt
- **THEN** a DTCC per-platform section appears in the response with a full identification block and 12-dimension scoring, regardless of what other platforms were discovered

#### Scenario: DTCC's information has changed since a previous session
- **WHEN** a researcher runs a new discovery session
- **THEN** the model researches DTCC from primary sources and reflects current information, rather than relying on a static description embedded in a prompt

#### Scenario: Researcher prepares rows for comparison
- **WHEN** a researcher selects rows from the discovery summary table to paste into the comparison prompt
- **THEN** the DTCC row is available in the summary table and can be selected and pasted alongside other platforms in the same operation

## MODIFIED Requirements

### Requirement: Discovery prompt requests structured output aligned with inventory
The prompt template SHALL instruct the model to return one `##`-level Markdown section per platform containing two blocks:

1. **Identification block** — five labelled bullet fields: **Organization**, **Link**, **License**, **Type**, **Relevance**
2. **Dimension block** — twelve labelled bullet fields, one per dimension and functional category, each with an inline `X/5` score and a one-sentence rationale: **Technical Architecture (X/5)**, **Openness & Licensing (X/5)**, **City-Scale Capability (X/5)**, **Maturity & Adoption (X/5)**, **Integration Posture (X/5)**, **Governance (X/5)**, **Visualization (X/5)**, **Data Management (X/5)**, **Simulation (X/5)**, **IoT Sensing (X/5)**, **Standards (X/5)**, **Infrastructure (X/5)**

The score scale (1–5) SHALL match the comparison prompt's scoring scale. The prompt SHALL instruct agents to score by judgment using the rubrics supplied via `[PASTE_SCOPE_HERE]`.

The `Relevance` field SHALL contain a bare integer 0–5, not a named criterion label.

The prompt template SHALL include a concrete example section demonstrating the exact field labels, score notation, and two-block structure.

The prompt template SHALL state that the response contains exactly three parts, in order: the metadata block, the summary table, and the per-platform sections. It SHALL forbid extra top-level sections or trailing summary content outside that structure.

DTCC SHALL appear as a required entry with a full per-platform section. The prompt SHALL explicitly instruct the model to include DTCC in addition to all discovered platforms.

#### Scenario: Response is used to populate inventory
- **WHEN** an AI responds to the discovery prompt
- **THEN** each platform section — including DTCC — contains the five identification fields (including a Relevance score) and twelve scored dimension fields, making all data directly transferable to the inventory CSV

#### Scenario: Discovery scores feed into comparison
- **WHEN** a researcher pastes rows from the discovery summary table into the comparison prompt
- **THEN** all twelve dimension and category scores from discovery provide starting signals that comparison refines with deep research

#### Scenario: Two agents respond to the same discovery prompt
- **WHEN** a researcher runs the discovery prompt on two different AI agents
- **THEN** both responses use identical field labels, score notation (`X/5`), and section structure; both include a DTCC section

#### Scenario: DTCC section appears even when DTCC is not found by search
- **WHEN** an AI's web search does not surface DTCC during discovery
- **THEN** the model still includes a DTCC section by researching it directly from primary sources as instructed
