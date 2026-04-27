## ADDED Requirements

### Requirement: UDT initiatives cycle maps projects and deployments

The repository SHALL define a canonical `udt-initiatives` cycle for mapping UDT initiatives, projects, programmes, and deployment efforts.

The `udt-initiatives` cycle SHALL treat initiatives as primary rows in their own table rather than as metadata columns inside the technical-artifact cycle.

#### Scenario: Researcher asks what UDT city efforts exist

- **WHEN** a researcher wants to know what UDT initiatives or projects exist
- **THEN** they use the `udt-initiatives` cycle rather than the technical-artifact cycle

### Requirement: UDT initiatives cycle uses an initiative summary table

The `udt-initiatives` cycle SHALL produce a summary table with exactly these columns:

- `Initiative`
- `Link`
- `Uses`
- `Reason`

`Uses` SHALL contain either:

- a comma-separated list of artifact names from `udt-platforms`, or
- `?` if the technical substrate is unclear

`Reason` SHALL be blank for in-scope rows and a brief phrase for excluded rows if exclusion is used in the cycle output.

#### Scenario: Initiative clearly uses known artifacts

- **WHEN** a project or initiative clearly uses multiple artifacts
- **THEN** the `Uses` cell lists those artifact names as a comma-separated string

#### Scenario: Initiative technical substrate is unclear

- **WHEN** a project or initiative is meaningful but its technical substrate cannot be confidently resolved
- **THEN** the `Uses` cell contains `?`

### Requirement: UDT initiatives cycle is contextual rather than a direct comparison source

The `udt-initiatives` cycle SHALL support the repository's understanding of deployments and real-world context, but SHALL NOT directly define the candidate set for `udt-platform-comparison`.

#### Scenario: Researcher prepares a comparison cycle

- **WHEN** a researcher assembles a comparison set
- **THEN** they do not select directly from `udt-initiatives`
