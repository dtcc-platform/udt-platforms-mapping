## ADDED Requirements

### Requirement: Platform comparison uses acceptable evidence sources

Platform comparison SHALL base final factual claims on acceptable evidence sources.

Acceptable evidence sources SHALL include official product or project documentation, repositories, standards documents, peer-reviewed publications, credible institutional pages, and directly relevant technical reports.

#### Scenario: Comparison cites evidence

- **WHEN** platform comparison makes a factual claim about a platform
- **THEN** the claim is supported by an acceptable evidence source

### Requirement: Platform comparison uses inline source links

Platform comparison SHALL use inline Markdown links for final citations.

Platform comparison SHALL NOT use product-native citation markers, numeric citation brackets, or footnote citation syntax.

#### Scenario: Source is cited

- **WHEN** platform comparison cites a source
- **THEN** the citation appears as an inline Markdown link

### Requirement: Weak evidence limits scoring certainty

Platform comparison SHALL preserve uncertainty when evidence is weak, missing, or conflicting.

When evidence is insufficient for a scoring judgment, platform comparison SHALL use `?` or explain the uncertainty according to the output contract.

#### Scenario: Evidence is insufficient

- **WHEN** evidence is insufficient to support a score
- **THEN** platform comparison preserves uncertainty rather than inventing a score
