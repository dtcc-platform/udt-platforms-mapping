## MODIFIED Requirements

### Requirement: platforms.md uses a three-column GFM table

The file SHALL contain a Markdown pipe table with exactly two columns in this order: **Name**, **Link**. Each data row SHALL represent one canonical `core-platform` entry to include in the current rating cycle. The table SHALL sit below a short header paragraph explaining the file's purpose.

Inclusion in `plan/rating/platforms.md` SHALL imply that the researcher has already selected that row as a `core-platform` from discovery. The rating model SHALL NOT reassess `Layer`, because `Layer` no longer appears in the file or in rating output.

The file header SHALL also state that aliases do not belong in this table, because rating compares exact selected canonical rows rather than fuzzy-matched names across responses.

#### Scenario: Researcher curates the comparison set

- **WHEN** a researcher selects platforms from a discovery response for a rating cycle run
- **THEN** they copy only the canonical `Name` and `Link` cells for `core-platform` rows into `plan/rating/platforms.md`

#### Scenario: Researcher considers adding a backbone row

- **WHEN** a researcher is choosing rows for `plan/rating/platforms.md`
- **THEN** they exclude backbones and domain modules because the rating workflow is restricted to core platforms

### Requirement: platforms.md must include the DTCC row

The file SHALL include a row for DTCC (Digital Twin Cities Centre) so the rating prompt's Part 3 landscape observations can orient around DTCC. The DTCC row SHALL use the same two-column shape as every other row.

#### Scenario: Researcher assembles a rating selection

- **WHEN** a researcher fills `plan/rating/platforms.md` for a cycle run
- **THEN** the DTCC row is present alongside the other selected core platforms
