## MODIFIED Requirements

### Requirement: Discovery prompt requests structured output aligned with inventory
The prompt template SHALL instruct the model to return one `##`-level Markdown section per platform containing:

- **For Relevance 3–5 platforms** (in scope): full two-block structure — identification fields (Organization, Link, License, Type, Relevance) plus all 12 scored dimension fields.
- **For Relevance 1–2 platforms** (out of scope): identification fields only (Organization, Link, License, Type, Relevance) plus a single **Reason** field (one sentence explaining why the platform is out of scope). No dimension scoring required.

All discovered platforms SHALL appear in the summary table regardless of Relevance score. The summary table SHALL be ordered by Relevance score descending (5 first, 0 last). Relevance 1–2 per-platform sections SHALL appear after all Relevance 3–5 sections.

The prompt template SHALL instruct the model that the research instruction "Verify it meets a Relevance score of 3 or higher" is replaced by "Score all discovered platforms on the Relevance rubric and include all in the summary table."

#### Scenario: Response is used to populate inventory
- **WHEN** an AI responds to the discovery prompt
- **THEN** the summary table contains all discovered platforms including Relevance 1–2 entries, and per-platform sections exist for all platforms with appropriate depth per Relevance tier

#### Scenario: Future session re-discovers a previously rejected platform
- **WHEN** a researcher runs a new discovery session and the model finds a platform that was previously assessed as Relevance 1–2
- **THEN** the prior session's response contains a record of the rejection reason, allowing the researcher to recognise it as previously assessed

#### Scenario: Discovery session identifies many out-of-scope candidates
- **WHEN** the model discovers 10 platforms of which 4 are Relevance 1–2
- **THEN** all 10 appear in the summary table; the 4 out-of-scope entries have brief sections with a Reason field; the 6 in-scope entries have full 12-dimension sections

### Requirement: Discovery prompt response begins with a required summary table
The summary table SHALL include all discovered platforms. Platforms with Relevance 0 (not assessed) SHALL NOT appear — 0 is reserved for CSV rows that have not been evaluated, not for platforms found during a session. Every platform the model discovers and includes in the response SHALL have a Relevance score of at least 1.

The `Relevance` column SHALL contain a bare integer 1–5 for all rows in a discovery response. Score columns (Arch through Infra) SHALL contain bare numbers 1–5 or `?` for in-scope platforms (Relevance 3–5); they MAY contain `0` for out-of-scope platforms (Relevance 1–2) where dimension scoring was not performed.

#### Scenario: Researcher opens a discovery response to start a comparison
- **WHEN** a researcher opens a saved discovery response
- **THEN** the summary table contains all discovered platforms; out-of-scope platforms are visually distinguishable by their low Relevance score and `0` dimension scores

#### Scenario: Researcher copies rows for comparison
- **WHEN** a researcher selects platforms to paste into the comparison prompt
- **THEN** they can easily skip Relevance 1–2 rows by filtering on the Relevance column
