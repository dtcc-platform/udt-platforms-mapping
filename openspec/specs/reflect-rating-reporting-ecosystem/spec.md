# Spec: rating-reporting-ecosystem

## Purpose

Defines the structured rating-reporting export ownership for `reflect/rating/reporting/ecosystem.csv` and `reflect/rating/reporting/ecosystem-map.html`.

## Requirements

### Requirement: Rating reporting owns ecosystem CSV and HTML outputs

The structured ecosystem export files SHALL belong to the rating reporting phase, not the discovery reporting phase.

The repository SHALL treat these as the canonical rating reporting outputs:
- `reflect/rating/reporting/ecosystem.csv`
- `reflect/rating/reporting/ecosystem-map.html`

#### Scenario: Researcher looks for structured export outputs

- **WHEN** a researcher wants CSV or HTML ecosystem outputs
- **THEN** they use the rating reporting workflow under `reflect/rating/reporting/`

### Requirement: Rating ecosystem CSV is comparison-oriented

`reflect/rating/reporting/ecosystem.csv` SHALL contain rows derived from rating/comparison responses rather than raw discovery reporting summaries.

#### Scenario: Researcher opens the rating ecosystem CSV

- **WHEN** a researcher opens `reflect/rating/reporting/ecosystem.csv`
- **THEN** the file reflects structured rating output rather than discovery-only extraction

### Requirement: Rating ecosystem CSV omits Layer

`reflect/rating/reporting/ecosystem.csv` SHALL use the rating Part 1 schema without a `Layer` column.

The CSV SHALL use exactly this column order:

`Name`, `Link`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`, `Model`, `Date`

#### Scenario: Researcher opens the rating ecosystem CSV

- **WHEN** a researcher opens `reflect/rating/reporting/ecosystem.csv`
- **THEN** the file contains only the layer-free comparison columns plus `Model` and `Date`

### Requirement: Rating ecosystem export reflects the core-platform-only rating scope

The rating ecosystem export SHALL reflect the repository's core-platform-only rating workflow and SHALL NOT rely on `Layer` as a downstream filter or grouping field.

#### Scenario: Researcher explores the HTML export

- **WHEN** a researcher uses `reflect/rating/reporting/ecosystem-map.html`
- **THEN** the interface does not require a `Layer` field to browse the exported rating data
