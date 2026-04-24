# Spec: reflect-rating-reporting

## Purpose

Defines the rating reporting workflow at `reflect/rating/reporting/`, including the CLI prompt and the structured CSV/HTML outputs it generates from rating responses.

## Requirements

### Requirement: Rating reporting workflow exists

The repository SHALL contain a file at `reflect/rating/reporting/prompt.md` that provides a self-contained AI CLI prompt for generating the structured rating reporting outputs from files in `observe/rating/`.

#### Scenario: File is present and non-empty

- **WHEN** a researcher navigates to `reflect/rating/reporting/prompt.md`
- **THEN** the file exists and contains a complete CLI prompt

### Requirement: Rating reporting workflow scans observe/rating automatically

The prompt SHALL instruct the model to read all relevant files in `observe/rating/` without requiring manual path input.

#### Scenario: Researcher runs the prompt

- **WHEN** a researcher runs `reflect/rating/reporting/prompt.md`
- **THEN** the model scans `observe/rating/` automatically

### Requirement: Rating reporting workflow owns structured CSV and HTML outputs

The structured ecosystem export files SHALL belong to the rating reporting workflow.

The prompt SHALL instruct the model to generate:
- `reflect/rating/reporting/ecosystem.csv`
- `reflect/rating/reporting/ecosystem-map.html`

#### Scenario: Researcher looks for structured export outputs

- **WHEN** a researcher wants CSV or HTML ecosystem outputs
- **THEN** they use the rating reporting workflow under `reflect/rating/reporting/`

### Requirement: Rating reporting workflow uses a layer-free comparison export schema

The prompt SHALL instruct the model to extract the Part 1 scoring table from qualifying rating responses using a layer-free schema:
- `Name`
- `Link`
- `Arch`
- `Open`
- `City`
- `Mature`
- `Integ`
- `Gov`
- `Viz`
- `DM`
- `Sim`
- `IoT`
- `Std`
- `Infra`

The generated CSV SHALL append `Model` and `Date` after those columns.

`reflect/rating/reporting/ecosystem.csv` SHALL use exactly this column order:

`Name`, `Link`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`, `Model`, `Date`

#### Scenario: Researcher completes rating reporting

- **WHEN** the model finishes the rating reporting prompt
- **THEN** it writes `ecosystem.csv` and `ecosystem-map.html` under `reflect/rating/reporting/` using the layer-free Part 1 schema

#### Scenario: Researcher opens the rating ecosystem CSV

- **WHEN** a researcher opens `reflect/rating/reporting/ecosystem.csv`
- **THEN** the file contains only the layer-free comparison columns plus `Model` and `Date`

### Requirement: Rating reporting workflow reflects the core-platform-only rating scope

The rating ecosystem export SHALL reflect the repository's core-platform-only rating workflow and SHALL NOT rely on `Layer` as a downstream filter or grouping field.

#### Scenario: Researcher explores the HTML export

- **WHEN** a researcher uses `reflect/rating/reporting/ecosystem-map.html`
- **THEN** the interface does not require a `Layer` field to browse the exported rating data
