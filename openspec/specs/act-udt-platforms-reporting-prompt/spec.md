# Spec: act-udt-platforms-reporting-prompt

## Purpose

Defines the flattened `act/udt-platforms-reporting.md` reporting prompt for the `udt-platforms` thread.

## Requirements

### Requirement: UDT platforms reporting prompt lives in act

The repository SHALL contain `act/udt-platforms-reporting.md`.

The prompt SHALL instruct the model to read flattened `observe/udt-platforms-web-*.md` files without requiring manual path input.

The prompt SHALL treat as qualifying only files whose YAML block contains `prompt: udt-platforms`.

#### Scenario: Researcher runs platforms reporting prompt

- **WHEN** a researcher runs `act/udt-platforms-reporting.md`
- **THEN** the prompt scans flattened observed web outputs for `udt-platforms`
- **THEN** the prompt qualifies files by YAML metadata

### Requirement: UDT platforms reporting prompt writes ecosystem summary

The output file SHALL contain one table only using exactly these columns:

- `Name`
- `Link`
- `Type`
- `Reason`

The prompt SHALL write its output to `reflect/udt-platforms-ecosystem.md`.

#### Scenario: Platforms reporting completes

- **WHEN** the platforms reporting prompt completes
- **THEN** it writes the ecosystem summary as a direct file under `reflect/`
