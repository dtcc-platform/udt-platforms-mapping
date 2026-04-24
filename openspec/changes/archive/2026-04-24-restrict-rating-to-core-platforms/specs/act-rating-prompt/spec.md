## MODIFIED Requirements

### Requirement: Comparison prompt Part 1 scoring table includes functional category columns

The Part 1 scoring table SHALL include the six dimension columns and six functional category columns. It SHALL NOT include a `Layer` column. It SHALL NOT include a `Relevance` column — Relevance is retired.

Each score column SHALL use the same 1–5 integer scoring format — bare integer, `?` for unknown, no `/5` suffix in table cells.

The prompt SHALL include a legend immediately below the Part 1 table instruction listing each abbreviated column header with its full name and one-line description.

#### Scenario: Researcher reads the Part 1 table

- **WHEN** an AI responds to the comparison prompt
- **THEN** the Part 1 table header contains exactly: `Name`, `Link`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`

#### Scenario: Researcher compares functional strengths across platforms

- **WHEN** an AI responds to the comparison prompt
- **THEN** every platform row contains a numeric 1–5 score (or `?`) in every dimension and category column, with no `Layer` field in the Part 1 table

### Requirement: Comparison prompt uses a core-platform-only comparison scope

The rating prompt SHALL treat `plan/rating/platforms.md` as a curated list of canonical `core-platform` entries only.

The prompt SHALL instruct the model not to broaden the comparison to backbones or domain modules, even if those appear elsewhere in discovery outputs.

#### Scenario: Researcher runs rating on the selected set

- **WHEN** the AI reads `plan/rating/platforms.md`
- **THEN** it treats every listed row as part of a core-platform-only comparison scope

#### Scenario: Broader ecosystem entries exist in discovery outputs

- **WHEN** discovery responses include backbones or domain modules
- **THEN** the rating prompt ignores them unless the researcher explicitly changes the rating workflow contract
