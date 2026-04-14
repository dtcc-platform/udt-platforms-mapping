## MODIFIED Requirements

### Requirement: Prompt extracts rows from discovery responses

For discovery responses, the prompt SHALL instruct the model to locate the summary table (the GFM pipe table immediately after the metadata block) and extract every row — including out-of-scope platforms (those with low Relevance scores).

Each extracted row SHALL be output as a CSV row with `Phase` set to `discovery`.

All score columns — including the six functional category columns (`Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`) — SHALL be extracted from the summary table. If a column is absent or contains `0`, that value is used as-is. No column SHALL be forced to a fixed sentinel value.

The `Relevance` column SHALL be extracted from the summary table and included in the output row.

#### Scenario: Discovery response contains in-scope and out-of-scope platforms

- **WHEN** the model reads a discovery response whose summary table includes Relevance 1–2 rows with `0` dimension scores
- **THEN** the output includes CSV rows for all platforms with Phase=`discovery`; out-of-scope rows have `0` in score columns, not `-1`

#### Scenario: Discovery row functional categories

- **WHEN** a discovery row is output
- **THEN** the Viz, DM, Sim, IoT, Std, and Infra columns contain the values from the summary table (typically `0`–`5` or `?`), not a forced `-1`

#### Scenario: Discovery response includes Relevance scores

- **WHEN** the model reads a discovery response summary table
- **THEN** each output row includes the platform's Relevance score in the `Relevance` column

### Requirement: Output CSV schema matches the platform inventory

The output SHALL use exactly the following column order:

`Name`, `Link`, `Phase`, `Relevance`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`, `Model`, `Date`

Score cells SHALL contain bare integers `0`–`5` or `?` for unknown. The `-1` sentinel is no longer used. No `/5` suffix. The `Link` column SHALL contain raw URLs only — no Markdown link syntax.

#### Scenario: Researcher pastes output into the inventory CSV

- **WHEN** a researcher copies the output and appends it to `docs/05-platform-inventory.csv`
- **THEN** the columns align with the existing header, including `Relevance` in position 4, without modification

#### Scenario: Source table uses a different column order

- **WHEN** a Part 1 table in a response file has columns in a different order than the inventory schema
- **THEN** the model reorders columns to match the inventory schema before outputting

#### Scenario: Out-of-scope platform row in output

- **WHEN** the model extracts a row for a platform with Relevance 1 or 2
- **THEN** the row contains `0` (not `-1`) in unscored dimension columns
