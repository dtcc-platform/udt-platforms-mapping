# Spec: observe-udt-platforms-benchmarking-coverage

## Purpose

Defines the flattened benchmarking coverage output for the `udt-platforms` thread.

## Requirements

### Requirement: UDT platforms benchmarking coverage lives in observe

The repository SHALL contain `observe/udt-platforms-benchmarking-coverage.md` as the generated coverage output from the benchmarking prompt.

#### Scenario: Benchmarking coverage is generated

- **WHEN** the benchmarking prompt completes
- **THEN** coverage is saved as `observe/udt-platforms-benchmarking-coverage.md`
