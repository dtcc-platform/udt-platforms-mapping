## REMOVED Requirements

### Requirement: Platform comparison uses acceptable evidence sources

**Reason**: Replaced by `plan-platform-source-policy`.

**Migration**: Use `openspec/specs/plan-platform-source-policy/spec.md`.

#### Scenario: Comparison cites evidence

- **WHEN** platform comparison makes a factual claim
- **THEN** source acceptability is governed by `plan-platform-source-policy`

### Requirement: Platform comparison prefers stronger source types

**Reason**: Replaced by `plan-platform-source-policy`.

**Migration**: Use `openspec/specs/plan-platform-source-policy/spec.md`.

#### Scenario: Sources conflict

- **WHEN** sources conflict
- **THEN** source preference is governed by `plan-platform-source-policy`

### Requirement: Platform comparison uses inline source links

**Reason**: Replaced by `plan-platform-source-policy`.

**Migration**: Use `openspec/specs/plan-platform-source-policy/spec.md`.

#### Scenario: Source is cited

- **WHEN** platform comparison cites a source
- **THEN** citation formatting is governed by `plan-platform-source-policy`

### Requirement: Paywalled sources are limited to accessible evidence

**Reason**: Replaced by `plan-platform-source-policy`.

**Migration**: Use `openspec/specs/plan-platform-source-policy/spec.md`.

#### Scenario: Source is paywalled

- **WHEN** platform comparison uses a paywalled source
- **THEN** paywall handling is governed by `plan-platform-source-policy`

### Requirement: Weak evidence limits scoring certainty

**Reason**: Replaced by `plan-platform-source-policy`.

**Migration**: Use `openspec/specs/plan-platform-source-policy/spec.md`.

#### Scenario: Evidence is insufficient

- **WHEN** evidence is insufficient to support a score
- **THEN** uncertainty behavior is governed by `plan-platform-source-policy`
