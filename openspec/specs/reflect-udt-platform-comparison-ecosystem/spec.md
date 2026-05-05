# Spec: reflect-udt-platform-comparison-ecosystem

## Purpose

Defines the flattened synthesized ecosystem artifacts for the `udt-platform-comparison` thread.

## Requirements

### Requirement: UDT platform comparison ecosystem artifacts live in reflect

The repository SHALL contain:

- `reflect/udt-platform-comparison-ecosystem.csv`
- `reflect/udt-platform-comparison-ecosystem-map.html`

These files SHALL be synthesized reflection artifacts for `udt-platform-comparison`.

#### Scenario: Researcher opens comparison synthesis

- **WHEN** a researcher opens `reflect/`
- **THEN** the comparison ecosystem CSV is available as a direct file
- **THEN** the comparison ecosystem map is available as a direct file
