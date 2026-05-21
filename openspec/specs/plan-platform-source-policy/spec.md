# Spec: plan-platform-source-policy

## Purpose

Defines acceptable source and citation behavior for platform comparison.

## Requirements

### Requirement: Platform comparison uses acceptable evidence sources

Platform comparison SHALL base final factual claims on acceptable evidence sources.

Acceptable evidence sources SHALL include official documentation, peer-reviewed publications, official project repositories, official organizational communications, technical reports, and reputable secondary sources when stronger sources are unavailable or insufficient.

Platform comparison SHALL NOT rely on Wikipedia, anonymous forum posts, AI-generated summaries, or undated web pages without clear authorship as final evidence.

#### Scenario: Comparison cites evidence

- **WHEN** platform comparison makes a factual claim about a platform
- **THEN** the claim is supported by an acceptable evidence source

### Requirement: Platform comparison prefers stronger source types

Platform comparison SHALL prefer higher-reliability sources when multiple sources are available.

The preferred source order SHALL be official documentation, peer-reviewed publications, official repositories, official organizational communications, technical reports, and reputable secondary sources.

#### Scenario: Sources conflict

- **WHEN** sources conflict
- **THEN** platform comparison prefers the stronger source type
- **THEN** significant discrepancies are noted in the comparison output when relevant

### Requirement: Platform comparison uses inline source links

Platform comparison SHALL use inline Markdown links for final citations.

Platform comparison SHALL NOT use product-native citation markers, numeric citation brackets, or footnote citation syntax.

#### Scenario: Source is cited

- **WHEN** platform comparison cites a source
- **THEN** the citation appears as an inline Markdown link

### Requirement: Paywalled sources are limited to accessible evidence

When a source is paywalled, platform comparison SHALL mark it as paywalled and SHALL NOT infer content beyond accessible abstracts or excerpts.

#### Scenario: Source is paywalled

- **WHEN** platform comparison uses a paywalled source
- **THEN** the citation marks the source as paywalled
- **THEN** the claim is limited to accessible content

### Requirement: Weak evidence limits scoring certainty

Platform comparison SHALL preserve uncertainty when evidence is weak, missing, or conflicting.

When evidence is insufficient for a scoring judgment, platform comparison SHALL use `?` or explain the uncertainty according to the output contract.

#### Scenario: Evidence is insufficient

- **WHEN** evidence is insufficient to support a score
- **THEN** platform comparison preserves uncertainty rather than inventing a score
