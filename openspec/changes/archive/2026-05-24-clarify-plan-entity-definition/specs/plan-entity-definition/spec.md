## MODIFIED Requirements

### Requirement: Entity definition classifies UDT discovery rows

UDT discovery SHALL classify each included candidate with exactly one output `Type`.

Allowed output `Type` values SHALL be:

- `platform`
- `framework`
- `module`
- `initiative`
- `excluded`

The internal `artifact` concept SHALL group technical UDT artifacts whose output `Type` is `platform`, `framework`, or `module`.

The internal `artifact` concept SHALL NOT be required as an output table value unless another spec explicitly requires an internal classification field.

#### Scenario: Candidate is classified with output Type

- **WHEN** UDT discovery includes a candidate row
- **THEN** the row has exactly one `Type`
- **THEN** the `Type` is one of `platform`, `framework`, `module`, `initiative`, or `excluded`

#### Scenario: Technical artifact uses artifact grouping internally

- **WHEN** entity definition reasons about a candidate with `Type = platform`, `Type = framework`, or `Type = module`
- **THEN** the candidate is treated as part of the internal `artifact` group
- **THEN** the output table still uses the specific `Type` value

### Requirement: Artifact Type means technical UDT artifact

An entity SHALL be treated as an internal `artifact` when it is a distinct technical artifact, product, software system, framework, toolkit, reference implementation, data pipeline, simulator, visualization component, or reusable technical substrate related to Urban Digital Twins.

Technical artifacts SHALL be assigned one output `Type`: `platform`, `framework`, or `module`.

#### Scenario: Candidate is a technical artifact

- **WHEN** a candidate is a distinct technical substrate related to Urban Digital Twins
- **THEN** discovery treats it as part of the internal `artifact` group
- **THEN** entity discovery assigns `Type` as `platform`, `framework`, or `module`

### Requirement: Initiative Type means real-world UDT activity

An entity SHALL be classified as `initiative` when it is mainly presented as a project, programme, deployment, implementation effort, institutional initiative, pilot, or real-world activity related to Urban Digital Twins, and the primary entity being represented is not a distinct technical artifact.

An initiative SHALL NOT be classified as `platform`, `framework`, or `module` only because it uses, funds, deploys, or discusses a technical artifact.

Initiatives SHALL record their technical substrate separately when it is clear.

When the technical substrate is unclear, discovery SHALL preserve uncertainty with `Uses = ?` or equivalent artifact-detail uncertainty.

#### Scenario: Candidate is an initiative

- **WHEN** a candidate is a project, programme, deployment, implementation effort, institutional initiative, or pilot related to Urban Digital Twins
- **THEN** entity discovery assigns `Type = initiative`

#### Scenario: Initiative uses a known artifact

- **WHEN** an initiative clearly uses a known technical artifact
- **THEN** initiative discovery records that artifact as the initiative's technical substrate
- **THEN** the initiative remains `Type = initiative`

#### Scenario: Initiative substrate is unclear

- **WHEN** an initiative is relevant but its platform or technical artifact cannot be identified
- **THEN** initiative discovery records `Uses = ?`

### Requirement: Excluded Type means outside discovery boundary

An entity SHALL be classified as `excluded` when it is not a technical UDT artifact, is not a UDT initiative, or falls outside the study boundary.

Communication tools, presentation tools, narrative mapping tools, and lightweight web-map storytelling tools SHALL be classified as `excluded` unless they expose a distinct technical artifact that satisfies `platform`, `framework`, or `module` criteria or are part of a UDT initiative that satisfies `initiative` criteria.

#### Scenario: Candidate is excluded

- **WHEN** a candidate is outside both the technical artifact boundary and the initiative boundary
- **THEN** entity discovery assigns `Type = excluded`

#### Scenario: Communication or narrative publishing tool is outside scope

- **WHEN** a tool mainly supports communication, presentation, map-based storytelling, or narrative publishing rather than UDT modeling, simulation, integration, or operational use
- **THEN** entity discovery classifies it as `Type = excluded`
- **THEN** the exclusion reason explains that it is outside the technical UDT artifact and UDT initiative boundary

### Requirement: Borderline entities use deterministic tie-breaks

Discovery SHALL classify by observable presentation and role in the UDT ecosystem, not by name alone.

When a candidate resembles multiple entity categories, discovery SHALL apply this order:

1. `platform` when a distinct artifact is presented as a usable or deployable city-scale UDT system.
2. `framework` when a distinct artifact is mainly presented as a reusable architecture, toolkit, API backbone, SDK, reference model, or enabling layer.
3. `module` when a distinct artifact is mainly presented as a bounded capability or component.
4. `initiative` when the primary entity is a project, programme, deployment, implementation effort, institutional initiative, or pilot rather than a separable technical artifact.
5. `excluded` when outside the study boundary.

When an initiative and a technical artifact are both present, discovery SHALL separate the initiative from the artifact when the evidence supports treating them as distinct entities.

#### Scenario: Entity resembles initiative and platform

- **WHEN** a candidate is a programme that exposes a distinct usable city-scale UDT system
- **THEN** the technical artifact is eligible for `Type = platform`
- **THEN** the programme is eligible for `Type = initiative`

#### Scenario: Entity resembles platform and framework

- **WHEN** an artifact exposes APIs but is presented as a usable city-scale UDT system
- **THEN** entity discovery classifies it as `Type = platform`

### Requirement: Weak evidence preserves uncertainty

Discovery SHALL use the strongest observable evidence available.

When evidence is weak or ambiguous, discovery SHALL choose the best supported allowed `Type` and preserve uncertainty in the reason, substrate, or artifact details.

Discovery SHALL NOT introduce ad hoc output `Type` values such as `unknown`, `tool`, or `system`.

#### Scenario: Evidence is ambiguous

- **WHEN** the technical role or initiative substrate of a candidate is unclear
- **THEN** discovery uses the strongest observable evidence
- **THEN** discovery assigns the best supported allowed `Type`
- **THEN** discovery makes the uncertainty visible

#### Scenario: Candidate type is uncertain

- **WHEN** a candidate appears relevant but the evidence does not clearly support one classification
- **THEN** discovery assigns one of `platform`, `framework`, `module`, `initiative`, or `excluded`
- **THEN** discovery explains the uncertainty instead of creating a new `Type`
