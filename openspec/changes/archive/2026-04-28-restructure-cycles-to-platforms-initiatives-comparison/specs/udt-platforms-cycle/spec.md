## ADDED Requirements

### Requirement: UDT platforms cycle maps technical artifacts

The repository SHALL define a canonical `udt-platforms` cycle for mapping technical UDT artifacts from literature and current ecosystem evidence.

The `udt-platforms` cycle SHALL be responsible for classifying technical artifacts only. It SHALL NOT treat initiatives or projects as primary rows in its main artifact table.

#### Scenario: Researcher asks what software artifacts exist

- **WHEN** a researcher wants to know what technical UDT artifacts exist
- **THEN** they use the `udt-platforms` cycle rather than `udt-initiatives`

### Requirement: UDT platforms cycle uses a technical-artifact summary table

The `udt-platforms` cycle SHALL produce a summary table with exactly these columns:

- `Name`
- `Link`
- `Type`
- `Reason`

`Type` SHALL be one of:

- `platform`
- `framework`
- `module`
- `excluded`

`Reason` SHALL be blank for in-scope rows and a brief phrase for `excluded` rows.

#### Scenario: Technical artifact is a reusable UDT platform

- **WHEN** a row describes a usable city-scale platform
- **THEN** the row uses `Type = platform`

#### Scenario: Technical artifact is enabling infrastructure

- **WHEN** a row describes a reusable development or enabling structure rather than the main end-user platform
- **THEN** the row uses `Type = framework`

#### Scenario: Technical artifact is a narrower capability component

- **WHEN** a row describes a domain or capability-specific component
- **THEN** the row uses `Type = module`

#### Scenario: Candidate is outside the study boundary

- **WHEN** a row does not belong to the study scope
- **THEN** the row uses `Type = excluded` and records a brief `Reason`

### Requirement: UDT platforms cycle is the only direct source for platform comparison candidates

Only rows from `udt-platforms` with `Type = platform` SHALL be eligible for `udt-platform-comparison`.

Rows classified as `framework`, `module`, or `excluded` SHALL NOT be direct comparison candidates.

#### Scenario: Researcher prepares a comparison cycle

- **WHEN** a researcher selects candidates for `udt-platform-comparison`
- **THEN** they choose only rows whose `Type` is `platform`
