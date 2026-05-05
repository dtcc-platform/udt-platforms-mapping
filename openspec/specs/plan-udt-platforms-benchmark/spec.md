# Spec: plan-udt-platforms-benchmark

## Purpose

Defines the flattened `plan/udt-platforms-benchmark.md` benchmarking fixture input for the `udt-platforms` thread.

## Requirements

### Requirement: UDT platforms benchmark fixture lives in plan

The repository SHALL contain `plan/udt-platforms-benchmark.md`.

The file SHALL contain a single flat table with columns:

- `Name`
- `Link`
- `Type`
- `Aliases`
- `Tags`

#### Scenario: Researcher reviews benchmark fixture

- **WHEN** a researcher opens `plan/`
- **THEN** `udt-platforms-benchmark.md` is available as the benchmarking fixture input
