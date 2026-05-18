## REMOVED Requirements

### Requirement: Entity definition classifies UDT discovery rows

**Reason**: Replaced by `plan-entity-definition` to align spec names with research phases.

**Migration**: Use `openspec/specs/plan-entity-definition/spec.md`.

#### Scenario: Candidate is classified

- **WHEN** UDT discovery includes a candidate row
- **THEN** classification behavior is governed by `plan-entity-definition`

### Requirement: Artifact Type means technical UDT artifact

**Reason**: Replaced by `plan-entity-definition`.

**Migration**: Use `openspec/specs/plan-entity-definition/spec.md`.

#### Scenario: Candidate is a technical artifact

- **WHEN** a candidate is a distinct technical substrate related to Urban Digital Twins
- **THEN** artifact classification behavior is governed by `plan-entity-definition`

### Requirement: Platform Type means usable UDT platform

**Reason**: Replaced by `plan-entity-definition`.

**Migration**: Use `openspec/specs/plan-entity-definition/spec.md`.

#### Scenario: Artifact is a platform

- **WHEN** an artifact is presented as a usable city-scale UDT system
- **THEN** platform type behavior is governed by `plan-entity-definition`

### Requirement: Framework Type means reusable enabling structure

**Reason**: Replaced by `plan-entity-definition`.

**Migration**: Use `openspec/specs/plan-entity-definition/spec.md`.

#### Scenario: Artifact is a framework

- **WHEN** an artifact is mainly a reusable architecture or enabling layer
- **THEN** framework type behavior is governed by `plan-entity-definition`

### Requirement: Module Type means bounded capability component

**Reason**: Replaced by `plan-entity-definition`.

**Migration**: Use `openspec/specs/plan-entity-definition/spec.md`.

#### Scenario: Artifact is a module

- **WHEN** an artifact mainly provides one bounded UDT capability
- **THEN** module type behavior is governed by `plan-entity-definition`

### Requirement: Initiative Type means real-world UDT activity

**Reason**: Replaced by `plan-entity-definition`.

**Migration**: Use `openspec/specs/plan-entity-definition/spec.md`.

#### Scenario: Candidate is an initiative

- **WHEN** a candidate is a UDT initiative
- **THEN** initiative type behavior is governed by `plan-entity-definition`

### Requirement: Excluded Type means outside discovery boundary

**Reason**: Replaced by `plan-entity-definition`.

**Migration**: Use `openspec/specs/plan-entity-definition/spec.md`.

#### Scenario: Candidate is excluded

- **WHEN** a candidate is outside the discovery boundary
- **THEN** exclusion behavior is governed by `plan-entity-definition`

### Requirement: Borderline entities use deterministic tie-breaks

**Reason**: Replaced by `plan-entity-definition`.

**Migration**: Use `openspec/specs/plan-entity-definition/spec.md`.

#### Scenario: Entity resembles initiative and platform

- **WHEN** a candidate resembles multiple entity categories
- **THEN** tie-break behavior is governed by `plan-entity-definition`

### Requirement: Weak evidence preserves uncertainty

**Reason**: Replaced by `plan-entity-definition`.

**Migration**: Use `openspec/specs/plan-entity-definition/spec.md`.

#### Scenario: Evidence is ambiguous

- **WHEN** evidence is ambiguous
- **THEN** uncertainty behavior is governed by `plan-entity-definition`
