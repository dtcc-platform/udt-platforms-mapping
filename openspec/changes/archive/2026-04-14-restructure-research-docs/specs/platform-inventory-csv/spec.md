## REMOVED Requirements

### Requirement: Inventory CSV uses -1 as sentinel for excluded or unresearched scores
**Reason:** The `-1` sentinel is replaced by `0`. Score `0` means "not assessed at this phase." This eliminates the need for special-casing negative values in tooling and visualization.
**Migration:** Replace all `-1` values in `docs/05-platform-inventory.csv` with `0`. Update any tooling or visualization code that treats `-1` as "not assessed" to treat `0` instead.

## MODIFIED Requirements

### Requirement: Inventory CSV column order is fixed
The CSV SHALL use exactly this column order:

`Name`, `Link`, `Phase`, `Relevance`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`, `Model`, `Date`

The `Relevance` column SHALL appear immediately after `Phase` and before the twelve score columns. Its values SHALL be integers 0–5. Existing rows that predate this change SHALL have `Relevance` set to `0` (not assessed) until manually updated.

Score columns (Arch through Infra) SHALL use integers 0–5, where `0` means not assessed at this phase, or `?` for unknown. The `-1` sentinel is no longer used.

#### Scenario: Researcher pastes new rows into the CSV
- **WHEN** a researcher appends rows produced by `prompts/platform-inventory.md`
- **THEN** the columns align with the header, including the new Relevance column in position 4

#### Scenario: Discovery row in the inventory
- **WHEN** a researcher reads a row with Phase=`discovery`
- **THEN** functional category columns (Viz, DM, Sim, IoT, Std, Infra) contain `0` (not assessed at this phase) rather than `-1`

#### Scenario: Out-of-scope platform row in the inventory
- **WHEN** a researcher reads a row for an out-of-scope platform
- **THEN** the Relevance column contains `0` or `1`, and score columns contain `0`; there is no `-1` value anywhere in the row

### Requirement: Inventory CSV header includes a Phase column
The CSV header row SHALL include a `Phase` column that distinguishes the prompt type at which a platform row was produced: `discovery` for rows extracted from discovery responses, `comparison` for rows extracted from comparison responses. The value reflects which prompt produced the row, not a research quality level.

#### Scenario: Researcher filters by prompt type
- **WHEN** a researcher filters the CSV by Phase
- **THEN** they can separately view first-pass discovery scores and deep comparison scores for the same platform

#### Scenario: Same platform appears at both phases
- **WHEN** both a discovery response and a comparison response exist for the same platform
- **THEN** the inventory contains two rows for that platform — one with Phase=`discovery` and one with Phase=`comparison`
