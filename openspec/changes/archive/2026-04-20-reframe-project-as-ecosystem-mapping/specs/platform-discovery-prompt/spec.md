## MODIFIED Requirements

### Requirement: Discovery prompt requests structured output aligned with inventory

The prompt template SHALL instruct the model to return one `##`-level Markdown section per platform containing:

- **For Relevance 3–5 platforms** (in scope): full two-block structure — identification fields (Organization, Link, License, Type, Layer, Relevance) plus all 12 scored dimension fields.
- **For Relevance 1–2 platforms** (out of scope): identification fields only (Organization, Link, License, Type, Layer, Relevance) plus a single **Reason** field (one sentence explaining why the platform is out of scope). No dimension scoring required.

The `Layer` field SHALL contain one of: `core-platform`, `backbone`, or `domain-module`, assigned based on the platform's primary architectural role using the layer taxonomy from the pasted scope content.

The score scale (1–5) SHALL match the comparison prompt's scoring scale. The prompt SHALL instruct agents to score by judgment using the rubrics supplied via `[PASTE_SCOPE_HERE]`.

The `Relevance` field SHALL contain a bare integer 0–5, not a named criterion label.

The prompt template SHALL include a concrete example section demonstrating the exact field labels, score notation, two-block structure, and `Layer` field placement.

The prompt template SHALL state that the response contains exactly three parts, in order: the metadata block, the summary table, and the per-platform sections. It SHALL forbid extra top-level sections or trailing summary content outside that structure.

All discovered platforms SHALL appear in the summary table regardless of Relevance score. The summary table SHALL be ordered by Relevance score descending (5 first, 0 last). The summary table SHALL include a `Layer` column. Relevance 1–2 per-platform sections SHALL appear after all Relevance 3–5 sections.

The prompt template SHALL instruct the model that the research instruction "Verify it meets a Relevance score of 3 or higher" is replaced by "Score all discovered platforms on the Relevance rubric and include all in the summary table."

DTCC SHALL appear as a required entry with a full per-platform section. The prompt SHALL explicitly instruct the model to include DTCC in addition to all discovered platforms.

#### Scenario: Response is used to populate inventory

- **WHEN** an AI responds to the discovery prompt
- **THEN** each platform section — including DTCC — contains the identification fields (including Layer and Relevance) and twelve scored dimension fields, making all data directly transferable to the inventory CSV

#### Scenario: Future session re-discovers a previously rejected platform

- **WHEN** a researcher runs a new discovery session and the model finds a platform that was previously assessed as Relevance 1–2
- **THEN** the prior session's response contains a record of the rejection reason, allowing the researcher to recognise it as previously assessed

#### Scenario: Discovery session identifies many out-of-scope candidates

- **WHEN** the model discovers 10 platforms of which 4 are Relevance 1–2
- **THEN** all 10 appear in the summary table with Layer and Relevance values; the 4 out-of-scope entries have brief sections with a Reason field; the 6 in-scope entries have full 12-dimension sections

#### Scenario: Discovery scores feed into comparison

- **WHEN** a researcher pastes rows from the discovery summary table into the comparison prompt
- **THEN** all twelve dimension and category scores plus the Layer value from discovery provide starting signals that comparison refines with deep research

## ADDED Requirements

### Requirement: Discovery prompt instructs multi-layer ecosystem search

The prompt template SHALL explicitly instruct the model to search across all three ecosystem layers — core platforms, infrastructure backbones, and domain-specific analytics/simulation tools — and not to limit discovery to platforms that self-identify as "digital twin" systems. The instruction SHALL reference the three layer values defined in the pasted scope content.

#### Scenario: Discovery session finds a domain-module platform

- **WHEN** an AI responds to the discovery prompt
- **THEN** the response includes domain-specific analytics or simulation tools (e.g., climate risk toolkits, urban traffic simulators) as well as full platforms and backbone components, each assigned the appropriate `Layer` value

#### Scenario: Discovery session finds a backbone component

- **WHEN** an AI responds to the discovery prompt
- **THEN** infrastructure enabling layers (e.g., context brokers, city model databases, rendering engines) appear in the response with `Layer=backbone`, not filtered out because they are not full platforms
