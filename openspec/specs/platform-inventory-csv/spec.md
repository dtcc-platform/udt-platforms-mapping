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

The CSV header row SHALL include a `Phase` column that distinguishes the prompt type at which a platform row was produced: `discovery` for rows extracted from discovery responses, `comparison` for rows extracted from comparison responses. The value reflects which prompt produced the row, not a research quality level.

#### Scenario: Researcher filters by prompt type

- **WHEN** a researcher filters the CSV by Phase
- **THEN** they can separately view first-pass discovery scores and deep comparison scores for the same platform

#### Scenario: Same platform appears at both phases

- **WHEN** both a discovery response and a comparison response exist for the same platform
- **THEN** the inventory contains two rows for that platform — one with Phase=`discovery` and one with Phase=`comparison`

### Requirement: Inventory CSV Link column contains URLs only

The `Link` column in the inventory CSV SHALL contain raw URLs (e.g., `https://cesium.com`) with no Markdown link syntax. The column header SHALL remain `Link`.

#### Scenario: Researcher imports CSV into a spreadsheet

- **WHEN** a researcher imports `docs/05-platform-inventory.csv` into Excel or Google Sheets
- **THEN** the Link column contains clickable or plain URLs, not Markdown `[text](url)` syntax

### Requirement: Inventory CSV column order is fixed

The CSV SHALL use exactly this column order:

`Name`, `Link`, `Phase`, `Layer`, `Relevance`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`, `Model`, `Date`

The `Layer` column SHALL appear immediately after `Phase` and before `Relevance`. Its values SHALL be one of: `core-platform`, `backbone`, `domain-module`, or blank/`0` for unassessed.

The `Relevance` column SHALL appear immediately after `Layer` and before the twelve score columns. Its values SHALL be integers 0–5. Existing rows that predate this change SHALL have `Relevance` set to `0` (not assessed) until manually updated.

Score columns (Arch through Infra) SHALL use integers 0–5, where `0` means not assessed at this phase, or `?` for unknown. The `-1` sentinel is no longer used.

#### Scenario: Researcher pastes new rows into the CSV

- **WHEN** a researcher appends rows produced by `prompts/platform-inventory.md`
- **THEN** the columns align with the header, including the `Layer` column in position 4 and `Relevance` column in position 5

#### Scenario: Discovery row in the inventory

- **WHEN** a researcher reads a row with Phase=`discovery`
- **THEN** the `Layer` column contains a provisional layer assignment and functional category columns (Viz, DM, Sim, IoT, Std, Infra) contain `0` (not assessed at this phase)

#### Scenario: Out-of-scope platform row in the inventory

- **WHEN** a researcher reads a row for an out-of-scope platform
- **THEN** the `Relevance` column contains `0` or `1`, the `Layer` column contains the assigned layer or blank, and score columns contain `0`; there is no `-1` value anywhere in the row

#### Scenario: Researcher filters inventory by layer

- **WHEN** a researcher filters the CSV by the `Layer` column
- **THEN** they can view only `core-platform` rows, only `backbone` rows, or only `domain-module` rows independently

#### Scenario: Comparison session revises a layer assignment

- **WHEN** a researcher adds a comparison row for a platform with a revised `Layer` value
- **THEN** the comparison row contains the updated layer value; the discovery row retains the original provisional assignment
