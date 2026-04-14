## REMOVED Requirements

### Requirement: Discovery prompt embeds inclusion criteria
**Reason:** Inclusion criteria are no longer embedded inline in the discovery prompt. All rubric definitions — including the Relevance rubric that replaces the three inclusion criteria — are supplied at run time by pasting `docs/01-scope.md` into the `[PASTE_SCOPE_HERE]` slot.
**Migration:** The model receives rubrics via the pasted scope content. The `[PASTE_SCOPE_HERE]` guard ensures the session cannot proceed without them.

## MODIFIED Requirements

### Requirement: Discovery prompt requests structured output aligned with inventory
The prompt template SHALL instruct the model to return one `##`-level Markdown section per platform containing two blocks:

1. **Identification block** — five labelled bullet fields: **Organization**, **Link**, **License**, **Type**, **Relevance**
2. **Dimension block** — twelve labelled bullet fields, one per dimension and functional category, each with an inline `X/5` score and a one-sentence rationale: **Technical Architecture (X/5)**, **Openness & Licensing (X/5)**, **City-Scale Capability (X/5)**, **Maturity & Adoption (X/5)**, **Integration Posture (X/5)**, **Governance (X/5)**, **Visualization (X/5)**, **Data Management (X/5)**, **Simulation (X/5)**, **IoT Sensing (X/5)**, **Standards (X/5)**, **Infrastructure (X/5)**

The score scale (1–5) SHALL match the comparison prompt's scoring scale. The prompt SHALL instruct agents to score by judgment using the rubrics supplied via `[PASTE_SCOPE_HERE]`.

The `Relevance` field SHALL contain a bare integer 0–5, not a named criterion label.

The prompt template SHALL include a concrete example section demonstrating the exact field labels, score notation, and two-block structure.

The prompt template SHALL state that the response contains exactly three parts, in order: the metadata block, the summary table, and the per-platform sections. It SHALL forbid extra top-level sections or trailing summary content outside that structure.

#### Scenario: Response is used to populate inventory
- **WHEN** an AI responds to the discovery prompt
- **THEN** each platform section contains the five identification fields (including a Relevance score) and twelve scored dimension fields, making all data directly transferable to the inventory CSV

#### Scenario: Discovery scores feed into comparison
- **WHEN** a researcher pastes rows from the discovery summary table into the comparison prompt
- **THEN** all twelve dimension and category scores from discovery provide starting signals that comparison refines with deep research

#### Scenario: Two agents respond to the same discovery prompt
- **WHEN** a researcher runs the discovery prompt on two different AI agents
- **THEN** both responses use identical field labels, score notation (`X/5`), and section structure

### Requirement: Discovery prompt response begins with a required summary table
The prompt template SHALL instruct the model to output the summary table immediately after the metadata block and before any per-platform sections. The table is required and SHALL use the following columns:

**Name**, **Link**, **License**, **Type**, **Relevance**, **Arch**, **Open**, **City**, **Mature**, **Integ**, **Gov**, **Viz**, **DM**, **Sim**, **IoT**, **Std**, **Infra**

The `Relevance` column SHALL contain a bare integer 0–5. A value of 0 means not assessed. Score columns (Arch through Infra) SHALL contain bare numbers 1–5 or `?` for unknown — no `/5` suffix. There is no `-1` sentinel; 0 in the Relevance column indicates an out-of-scope or unassessed platform.

Platforms with Relevance 0 or 1 MAY appear in the summary table but per-platform `##` sections are NOT required for them.

#### Scenario: Researcher opens a discovery response to start a comparison
- **WHEN** a researcher opens a saved discovery response
- **THEN** the summary table appears at the top (after the metadata block) with a Relevance column and all twelve score columns

#### Scenario: Rows are pasted into the comparison prompt
- **WHEN** a researcher copies rows of included platforms from the summary table and pastes them into the comparison prompt
- **THEN** the comparison prompt receives all twelve seed scores plus the Relevance score as context

#### Scenario: Discovery session identifies out-of-scope platforms
- **WHEN** the model encounters platforms that are out of scope
- **THEN** those platforms receive Relevance 0 or 1 in the summary table; there is no separate `-1` or named exclusion label

### Requirement: Discovery prompt includes a [PASTE_SCOPE_HERE] guard
The prompt template SHALL include a `[PASTE_SCOPE_HERE]` placeholder where the researcher pastes the full content of `docs/01-scope.md` before running a session. The placeholder SHALL be preceded by a guard instruction telling the model: _if `[PASTE_SCOPE_HERE]` still appears verbatim, stop and ask the user to paste `docs/01-scope.md` before continuing._

The usage header SHALL be updated to include a step directing the researcher to paste `docs/01-scope.md` into the `[PASTE_SCOPE_HERE]` slot as the first preparation step.

#### Scenario: Researcher runs the prompt without pasting scope
- **WHEN** a researcher pastes the discovery prompt into an AI session without replacing `[PASTE_SCOPE_HERE]`
- **THEN** the model stops and asks them to provide the scope content before producing any output

#### Scenario: Researcher runs the prompt after pasting scope
- **WHEN** a researcher pastes `docs/01-scope.md` content into the `[PASTE_SCOPE_HERE]` slot
- **THEN** the model proceeds with all 13 rubrics available and produces a complete discovery response

### Requirement: Discovery prompt does not request deep research
The prompt template SHALL NOT instruct the model to use a Research or Deep Research mode. Discovery is a first-pass survey; depth of research is not required. Primary source requirements are relaxed compared to the comparison prompt — the model MAY use judgment and secondary sources to score dimensions, and SHOULD note when claims are approximate.

#### Scenario: Discovery prompt is pasted into a Research-capable interface
- **WHEN** a researcher uses the discovery prompt in an interface that supports Research mode
- **THEN** the prompt does not activate Research mode; a lightweight first-pass response is produced

#### Scenario: Model applies judgment-based scoring
- **WHEN** an AI scores a platform during discovery
- **THEN** it uses the rubrics from the pasted scope content and applies judgment; it does not need to verify every claim against a primary source

### Requirement: Discovery prompt enforces agent-agnostic output structure
The prompt template SHALL comply with the shared Markdown contract defined in `prompt-markdown-format` and SHALL specify these discovery-specific formatting constraints:

- **Platform heading level:** `##` for every platform section
- **Score notation:** `**Dimension (X/5):**` inline in sections; bare number in table cells; `?` for unknown
- **Citation override note:** the Markdown rules section SHALL explicitly state that the inline-link citation rule overrides the model's default citation format
- **Research-mode suppression:** the prompt SHALL instruct the model to return only the final deliverable with no exposed research plan, executive summary, or provider-specific wrapper

#### Scenario: Two agents respond to the same discovery prompt
- **WHEN** a researcher runs the discovery prompt on two different agents
- **THEN** both responses use the same heading level, field labels, and score notation
