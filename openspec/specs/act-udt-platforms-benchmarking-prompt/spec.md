# Spec: act-udt-platforms-benchmarking-prompt

## Purpose

Defines the flattened `act/udt-platforms-benchmarking.md` benchmarking prompt for the `udt-platforms` thread.

## Requirements

### Requirement: UDT platforms benchmarking prompt lives in act

The repository SHALL contain `act/udt-platforms-benchmarking.md`.

The prompt SHALL scan flattened `observe/udt-platforms-web-*.md` files and write `observe/udt-platforms-benchmarking-coverage.md`.

#### Scenario: Researcher runs benchmarking prompt

- **WHEN** a researcher runs `act/udt-platforms-benchmarking.md`
- **THEN** the prompt reads flattened observed web outputs for `udt-platforms`
- **THEN** the prompt writes benchmarking coverage as a direct file under `observe/`
