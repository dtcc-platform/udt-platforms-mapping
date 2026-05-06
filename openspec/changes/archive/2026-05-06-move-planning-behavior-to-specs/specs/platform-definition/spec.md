## ADDED Requirements

### Requirement: Platform discovery classifies technical artifacts by Type

Platform discovery SHALL assign each discovered technical artifact exactly one `Type`.

Allowed `Type` values SHALL be:

- `platform`
- `framework`
- `module`
- `excluded`

#### Scenario: Artifact is classified

- **WHEN** platform discovery includes a technical artifact
- **THEN** the artifact has exactly one `Type`
- **THEN** the `Type` is one of `platform`, `framework`, `module`, or `excluded`

### Requirement: Platform Type means usable UDT platform

An artifact SHALL be classified as `platform` when it is presented as a deployable or usable system for city-scale integration, visualization, simulation, or management of urban systems.

An artifact SHALL NOT be classified as `platform` only because it has an ambitious name, belongs to a smart-city initiative, or is mentioned near UDT language.

#### Scenario: Artifact is a platform

- **WHEN** an artifact is presented as a usable city-scale UDT system
- **THEN** platform discovery classifies it as `platform`

### Requirement: Framework Type means reusable enabling structure

An artifact SHALL be classified as `framework` when it is mainly presented as an SDK, API-centered backbone, reusable architecture, toolkit, reference model, or enabling layer for building UDT systems rather than as the primary end-user platform.

#### Scenario: Artifact is a framework

- **WHEN** an artifact is mainly a reusable architecture or enabling layer
- **THEN** platform discovery classifies it as `framework`

### Requirement: Module Type means bounded capability component

An artifact SHALL be classified as `module` when it mainly provides one bounded capability, domain workflow, analytical function, data pipeline, visualization component, simulator, or integration component for use inside or alongside a broader UDT stack.

#### Scenario: Artifact is a module

- **WHEN** an artifact mainly provides one bounded UDT capability
- **THEN** platform discovery classifies it as `module`

### Requirement: Excluded Type means outside platform discovery boundary

An artifact SHALL be classified as `excluded` when it is not a technical UDT artifact, is only an initiative or project without identifiable technical substrate, or falls outside the study boundary.

Initiatives, programmes, deployments, and projects SHALL be tracked in initiative discovery unless they expose a distinct technical artifact that can be classified by platform discovery.

#### Scenario: Artifact is excluded

- **WHEN** an item has no identifiable technical artifact
- **THEN** platform discovery classifies it as `excluded`

### Requirement: Borderline artifacts use deterministic tie-breaks

Platform discovery SHALL classify by observable presentation and role in the UDT ecosystem, not by name alone.

When an artifact resembles multiple types, platform discovery SHALL apply this order:

1. `platform` when presented as a usable or deployable city-scale UDT system.
2. `framework` when mainly presented as a reusable architecture, toolkit, API backbone, SDK, reference model, or enabling layer.
3. `module` when mainly presented as a bounded capability or component.
4. `excluded` when outside the study boundary.

#### Scenario: Artifact resembles platform and framework

- **WHEN** an artifact exposes APIs but is presented as a usable city-scale UDT system
- **THEN** platform discovery classifies it as `platform`

### Requirement: Weak evidence preserves uncertainty

Platform discovery SHALL use the strongest observable evidence available.

When evidence is weak or ambiguous, platform discovery SHALL preserve uncertainty in the reason or artifact details.

#### Scenario: Evidence is ambiguous

- **WHEN** the technical role of an artifact is unclear
- **THEN** platform discovery uses the strongest observable evidence
- **THEN** platform discovery makes the uncertainty visible
