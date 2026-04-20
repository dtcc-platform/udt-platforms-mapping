## MODIFIED Requirements

### Requirement: Inventory CSV column order is fixed

The CSV SHALL use exactly this column order:

`Name`, `Link`, `Layer`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`, `Model`, `Date`

The `Relevance` column is retired and SHALL NOT appear in the header or any row. The `Phase` column is retired and SHALL NOT appear — the CSV is comparison-only by definition.

The `Layer` column SHALL appear immediately after `Link`. Its values SHALL be one of: `core-platform`, `backbone`, `domain-module`. It carries the Layer value assigned during discovery and is not reassessed during comparison.

Score columns (Arch through Infra) SHALL use integers 1–5, or `?` for unknown.

#### Scenario: Researcher pastes new rows into the CSV

- **WHEN** a researcher appends rows produced by the comparison prompt
- **THEN** the columns align with the header: Name, Link, Layer, then 12 dimension columns, Model, Date

#### Scenario: Researcher opens the CSV to review comparison results

- **WHEN** a researcher opens `docs/05-platform-inventory.csv`
- **THEN** every row is a comparison result with a Layer value and 12 dimension scores; there are no discovery-only rows and no Relevance column

#### Scenario: Researcher filters by Layer

- **WHEN** a researcher filters the CSV by the `Layer` column
- **THEN** they can view comparison results for `core-platform`, `backbone`, or `domain-module` platforms independently

### Requirement: Inventory CSV contains comparison rows only

The CSV SHALL contain only rows produced by comparison sessions. Discovery outputs live exclusively in `responses/` markdown files. Rows with `Phase=discovery` from the previous schema SHALL be removed during migration.

#### Scenario: Researcher completes a discovery session

- **WHEN** a researcher finishes a discovery session and saves the response
- **THEN** the response is saved as a markdown file in `responses/`; no rows are added to the CSV at this stage

#### Scenario: Researcher completes a comparison session

- **WHEN** a researcher finishes a comparison session
- **THEN** they extract the Part 1 table rows and append them to the CSV with the correct column order

## REMOVED Requirements

### Requirement: Inventory CSV header includes a Phase column
**Reason**: The CSV is now comparison-only. Phase is implicit and no longer needed as a column.
**Migration**: Remove `Phase` column from header and all rows.

### Requirement: Inventory CSV column order is fixed (previous — included Relevance and Phase)
**Reason**: Relevance is retired; Phase is retired. Column order is now: Name, Link, Layer, Arch…Infra, Model, Date.
**Migration**: Remove Relevance and Phase columns; drop all discovery-only rows.
