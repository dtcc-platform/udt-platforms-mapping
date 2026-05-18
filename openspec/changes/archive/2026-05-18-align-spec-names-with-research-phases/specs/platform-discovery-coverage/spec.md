## REMOVED Requirements

### Requirement: Platform discovery uses explicit recall coverage targets

**Reason**: Coverage behavior now belongs to the unified entity discovery action contract.

**Migration**: Use `openspec/specs/act-entity-discovery/spec.md`.

#### Scenario: Discovery has enough evidence

- **WHEN** discovery coverage is evaluated
- **THEN** coverage behavior is governed by `act-entity-discovery`

### Requirement: Platform discovery samples adjacent seed-list families

**Reason**: Seed-list sampling now belongs to the unified entity discovery action contract.

**Migration**: Use `openspec/specs/act-entity-discovery/spec.md`.

#### Scenario: Seed-list candidates are available

- **WHEN** seed-list candidates are available
- **THEN** seed-list sampling behavior is governed by `act-entity-discovery`

### Requirement: Platform discovery separates recall from later filtering

**Reason**: Recall/filtering separation now belongs to the unified entity discovery action contract.

**Migration**: Use `openspec/specs/act-entity-discovery/spec.md`.

#### Scenario: Non-platform candidate is discovered

- **WHEN** a non-platform candidate is discovered
- **THEN** recall behavior is governed by `act-entity-discovery`

### Requirement: Platform discovery targets regional and research-center platform recall

**Reason**: Targeted recall now belongs to the unified entity discovery action contract.

**Migration**: Use `openspec/specs/act-entity-discovery/spec.md`.

#### Scenario: DTCC Platform-style candidate is discoverable

- **WHEN** a regional academic platform is discoverable
- **THEN** targeted recall behavior is governed by `act-entity-discovery`
