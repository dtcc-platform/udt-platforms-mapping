## ADDED Requirements

### Requirement: UDT platform comparison reporting prompt lives in act

The repository SHALL contain `act/udt-platform-comparison-reporting.md`.

The prompt SHALL instruct the model to read flattened `observe/udt-platform-comparison-web-*.md` files.

The prompt SHALL treat as qualifying only files whose YAML block contains `prompt: udt-platform-comparison`.

#### Scenario: Researcher runs comparison reporting prompt

- **WHEN** a researcher runs `act/udt-platform-comparison-reporting.md`
- **THEN** the prompt scans flattened observed web outputs for `udt-platform-comparison`
- **THEN** the prompt qualifies files by YAML metadata

### Requirement: UDT platform comparison reporting prompt writes map artifacts

The prompt SHALL write:

- `reflect/udt-platform-comparison-ecosystem.csv`
- `reflect/udt-platform-comparison-ecosystem-map.html`

#### Scenario: Comparison reporting prompt completes

- **WHEN** the comparison reporting prompt completes
- **THEN** it writes both reporting outputs as direct files under `reflect/`
