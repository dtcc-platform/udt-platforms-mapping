## ADDED Requirements

### Requirement: UDT platform comparison is a platform-only side-by-side evaluation cycle

The repository SHALL define a canonical `udt-platform-comparison` cycle for side-by-side evaluation of selected UDT platforms.

This cycle SHALL compare platforms rather than frameworks, modules, or initiatives.

#### Scenario: Researcher wants to benchmark selected UDT systems

- **WHEN** a researcher wants a side-by-side evaluation of selected UDT systems
- **THEN** they use `udt-platform-comparison`

### Requirement: UDT platform comparison consumes the selected platform subset from UDT platforms

`udt-platform-comparison` SHALL consume a researcher-selected subset of `udt-platforms` rows where `Type = platform`.

The cycle SHALL NOT broaden its candidate set to include:

- `framework`
- `module`
- `excluded`

#### Scenario: Researcher sees a useful framework in the mapping output

- **WHEN** a researcher sees a `framework` row in `udt-platforms`
- **THEN** that row remains mapping context and is not included directly in platform comparison

### Requirement: UDT platform comparison remains the repository's benchmarking cycle

The cycle name is `comparison` rather than `rating` because the governed behavior is side-by-side benchmarking of a selected set, not only isolated scoring.

Numeric scoring MAY remain part of the cycle's prompt and reporting workflow, but the cycle's primary identity is comparative evaluation.

#### Scenario: Researcher describes the cycle in README or design docs

- **WHEN** the repository explains the third cycle
- **THEN** it describes it as platform comparison or benchmarking rather than generic rating
