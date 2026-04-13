# Spec: platform-inventory-csv

## Purpose

Defines the requirements for `docs/05-platform-inventory.csv` — the canonical inventory of UDT platforms, stored in CSV format with one row per platform per research session.

## Requirements

### Requirement: Inventory file is a CSV at docs/05-platform-inventory.csv

The repository SHALL contain a CSV file at `docs/05-platform-inventory.csv` instead of `docs/05-platform-inventory.md`. The file SHALL use standard comma-separated values format with a header row.

#### Scenario: Researcher opens the inventory

- **WHEN** a researcher opens `docs/05-platform-inventory.csv`
- **THEN** the file opens as a table in any CSV viewer, spreadsheet tool, or plain text editor

#### Scenario: Old .md inventory no longer exists

- **WHEN** a researcher navigates to `docs/05-platform-inventory.md`
- **THEN** the file does not exist; the canonical inventory is at `docs/05-platform-inventory.csv`

### Requirement: Inventory CSV header includes a Phase column

The CSV header row SHALL include a `Phase` column that distinguishes the research depth at which a platform row was produced: `discovery` for rows extracted from discovery responses, `comparison` for rows extracted from comparison responses.

#### Scenario: Researcher filters by research depth

- **WHEN** a researcher filters the CSV by Phase
- **THEN** they can separately view quick discovery-pass scores and deep comparison scores for the same platform

#### Scenario: Same platform appears at both phases

- **WHEN** both a discovery response and a comparison response exist for the same platform
- **THEN** the inventory contains two rows for that platform — one with Phase=`discovery` and one with Phase=`comparison`

### Requirement: Inventory CSV Link column contains URLs only

The `Link` column in the inventory CSV SHALL contain raw URLs (e.g., `https://cesium.com`) with no Markdown link syntax. The column header SHALL remain `Link`.

#### Scenario: Researcher imports CSV into a spreadsheet

- **WHEN** a researcher imports `docs/05-platform-inventory.csv` into Excel or Google Sheets
- **THEN** the Link column contains clickable or plain URLs, not Markdown `[text](url)` syntax

### Requirement: Inventory CSV uses -1 as sentinel for excluded or unresearched scores

Score columns for a platform row SHALL use `-1` to mean "not applicable or not researched at this phase", distinct from `?` (unknown but expected) and `1` (lowest real score). In particular:

- Discovery rows SHALL use `-1` for all six functional category columns (`Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`) because those are only scored at comparison phase.
- Excluded platform rows (from discovery) SHALL use `-1` for all twelve score columns.

#### Scenario: Discovery row in the inventory

- **WHEN** a researcher reads a row with Phase=`discovery`
- **THEN** the six functional category columns (`Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`) contain `-1`, not `?` or blank

#### Scenario: Excluded platform row in the inventory

- **WHEN** a researcher reads a row for an excluded platform
- **THEN** all twelve score columns contain `-1`

### Requirement: Inventory CSV column order is fixed

The CSV SHALL use exactly this column order:

`Name`, `Link`, `Phase`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`, `Model`, `Date`

#### Scenario: Researcher pastes new rows into the CSV

- **WHEN** a researcher appends rows produced by `prompts/platform-inventory.md`
- **THEN** the columns align with the header without reordering
