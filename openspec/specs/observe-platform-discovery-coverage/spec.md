# Spec: observe-platform-discovery-coverage

## Purpose

Defines this researcher-facing canonical artifact.

## Requirements

### Requirement: Platform discovery coverage stores benchmark output

The repository SHALL contain `observe/platform-discovery-coverage.md` as the generated coverage output from `act/benchmark-platform-discovery.md`.

#### Scenario: Benchmark writes coverage

- **WHEN** `act/benchmark-platform-discovery.md` completes
- **THEN** coverage is saved as `observe/platform-discovery-coverage.md`
