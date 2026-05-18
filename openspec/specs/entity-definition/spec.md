# Spec: entity-definition

## Purpose

Defines UDT entity classification behavior for technical artifacts, initiatives, excluded candidates, and initiative-to-artifact substrate relationships.

## Requirements

### Requirement: Entity definition classifies UDT discovery rows

UDT discovery SHALL classify each included candidate with exactly one `EntityKind`.

Allowed `EntityKind` values SHALL be:

- `artifact`
- `initiative`
- `excluded`

When an output contract exposes a `Type` field for entity discovery, allowed `Type` values SHALL be:

- `platform`
- `framework`
- `module`
- `initiative`
- `excluded`

#### Scenario: Candidate is classified

- **WHEN** UDT discovery includes a candidate row
- **THEN** the candidate has exactly one `EntityKind`
- **THEN** the `EntityKind` is one of `artifact`, `initiative`, or `excluded`

#### Scenario: Entity discovery output uses Type

- **WHEN** entity discovery includes a candidate row
- **THEN** the row has exactly one `Type`
- **THEN** the `Type` is one of `platform`, `framework`, `module`, `initiative`, or `excluded`

### Requirement: Artifact Type means technical UDT artifact

An entity SHALL have `EntityKind = artifact` when it is a distinct technical artifact, product, software system, framework, toolkit, reference implementation, data pipeline, simulator, visualization component, or reusable technical substrate related to Urban Digital Twins.

Technical artifacts SHALL be assigned one artifact `Type`: `platform`, `framework`, or `module`.

#### Scenario: Candidate is a technical artifact

- **WHEN** a candidate is a distinct technical substrate related to Urban Digital Twins
- **THEN** discovery classifies it with `EntityKind = artifact`
- **THEN** entity discovery assigns `Type` as `platform`, `framework`, or `module`

### Requirement: Platform Type means usable UDT platform

An artifact SHALL be classified as `platform` when it is presented as a deployable or usable system for city-scale integration, visualization, simulation, or management of urban systems.

An artifact SHALL NOT be classified as `platform` only because it has an ambitious name, belongs to a smart-city initiative, or is mentioned near UDT language.

#### Scenario: Artifact is a platform

- **WHEN** an artifact is presented as a usable city-scale UDT system
- **THEN** entity discovery classifies it as `Type = platform`

### Requirement: Framework Type means reusable enabling structure

An artifact SHALL be classified as `framework` when it is mainly presented as an SDK, API-centered backbone, reusable architecture, toolkit, reference model, or enabling layer for building UDT systems rather than as the primary end-user platform.

#### Scenario: Artifact is a framework

- **WHEN** an artifact is mainly a reusable architecture or enabling layer
- **THEN** entity discovery classifies it as `Type = framework`

### Requirement: Module Type means bounded capability component

An artifact SHALL be classified as `module` when it mainly provides one bounded capability, domain workflow, analytical function, data pipeline, visualization component, simulator, or integration component for use inside or alongside a broader UDT stack.

#### Scenario: Artifact is a module

- **WHEN** an artifact mainly provides one bounded UDT capability
- **THEN** entity discovery classifies it as `Type = module`

### Requirement: Initiative Type means real-world UDT activity

An entity SHALL be classified as `initiative` when it is mainly presented as a project, programme, deployment, implementation effort, institutional initiative, pilot, or real-world activity related to Urban Digital Twins, and the primary entity being represented is not a distinct technical artifact.

Initiatives SHALL record their technical substrate separately when it is clear.

When the technical substrate is unclear, discovery SHALL preserve uncertainty with `Uses = ?` or equivalent artifact-detail uncertainty.

#### Scenario: Candidate is an initiative

- **WHEN** a candidate is a project, programme, deployment, implementation effort, institutional initiative, or pilot related to Urban Digital Twins
- **THEN** discovery classifies it with `EntityKind = initiative`
- **THEN** entity discovery assigns `Type = initiative`

#### Scenario: Initiative uses a known artifact

- **WHEN** an initiative clearly uses a known technical artifact
- **THEN** initiative discovery records that artifact as the initiative's technical substrate

#### Scenario: Initiative substrate is unclear

- **WHEN** an initiative is relevant but its platform or technical artifact cannot be identified
- **THEN** initiative discovery records `Uses = ?`

### Requirement: Excluded Type means outside discovery boundary

An entity SHALL be classified as `excluded` when it is not a technical UDT artifact, is not a UDT initiative, or falls outside the study boundary.

Map storytelling tools, communication tools, presentation tools, and lightweight web-map narrative tools SHALL be classified as `excluded` unless they expose a distinct technical artifact that satisfies `platform`, `framework`, or `module` criteria or are part of a UDT initiative that satisfies `initiative` criteria.

#### Scenario: Candidate is excluded

- **WHEN** a candidate is outside both the technical artifact boundary and the initiative boundary
- **THEN** discovery classifies it as `EntityKind = excluded`
- **THEN** entity discovery assigns `Type = excluded`

#### Scenario: StoryMapJS-style tool is considered

- **WHEN** a tool is mainly presented as map-based storytelling, communication, or narrative publishing
- **THEN** entity discovery classifies it as `Type = excluded`
- **THEN** the exclusion reason explains that it is not a technical UDT artifact or UDT initiative

### Requirement: Borderline entities use deterministic tie-breaks

Discovery SHALL classify by observable presentation and role in the UDT ecosystem, not by name alone.

When a candidate resembles multiple entity categories, discovery SHALL apply this order:

1. `platform` when a distinct artifact is presented as a usable or deployable city-scale UDT system.
2. `framework` when a distinct artifact is mainly presented as a reusable architecture, toolkit, API backbone, SDK, reference model, or enabling layer.
3. `module` when a distinct artifact is mainly presented as a bounded capability or component.
4. `initiative` when the primary entity is a project, programme, deployment, implementation effort, institutional initiative, or pilot rather than a separable technical artifact.
5. `excluded` when outside the study boundary.

#### Scenario: Entity resembles initiative and platform

- **WHEN** a candidate is a programme that exposes a distinct usable city-scale UDT system
- **THEN** the technical artifact is eligible for `Type = platform`
- **THEN** the programme is eligible for `EntityKind = initiative`

#### Scenario: Entity resembles platform and framework

- **WHEN** an artifact exposes APIs but is presented as a usable city-scale UDT system
- **THEN** entity discovery classifies it as `Type = platform`

### Requirement: Weak evidence preserves uncertainty

Discovery SHALL use the strongest observable evidence available.

When evidence is weak or ambiguous, discovery SHALL preserve uncertainty in the reason, substrate, or artifact details.

#### Scenario: Evidence is ambiguous

- **WHEN** the technical role or initiative substrate of a candidate is unclear
- **THEN** discovery uses the strongest observable evidence
- **THEN** discovery makes the uncertainty visible
