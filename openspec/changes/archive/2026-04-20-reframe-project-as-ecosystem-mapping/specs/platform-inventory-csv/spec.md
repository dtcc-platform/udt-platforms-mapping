## MODIFIED Requirements

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
