## ADDED Requirements

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
