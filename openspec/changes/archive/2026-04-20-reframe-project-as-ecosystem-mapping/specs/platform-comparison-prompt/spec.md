## MODIFIED Requirements

### Requirement: Comparison prompt Part 1 scoring table includes functional category columns

The Part 1 scoring table SHALL include a `Layer` column and a `Relevance` column in addition to the six dimension columns and six functional category columns.

The `Layer` column SHALL appear immediately after `Link` and before `Relevance`. It SHALL contain the layer assignment for each platform: `core-platform`, `backbone`, or `domain-module`.

The `Relevance` column SHALL appear immediately after `Layer` and before `Arch`, consistent with the discovery summary table and inventory CSV column order.

The `Relevance` column SHALL contain a bare integer 1–5. The model SHALL reassess the platform's Relevance score using the rubric from the pasted scope content, treating the score from the discovery row as a starting point that may be revised upward or downward based on primary-source evidence found during deep research. Rationale for any revision SHALL appear in the per-platform profile, not in the table cell.

The model SHALL also reassess the `Layer` assignment during deep research, using the layer taxonomy from the pasted scope content. If deep research reveals that a platform's primary architectural role differs from the discovery-assigned layer, the model SHALL revise the `Layer` value. Rationale for any layer reclassification SHALL appear in the per-platform profile alongside any Relevance revision rationale.

Each category column SHALL use the same 1–5 integer scoring format as dimension columns — bare integer, `?` for unknown, no `/5` suffix in table cells.

The prompt SHALL include a legend immediately below the Part 1 table instruction listing each abbreviated column header with its full name and one-line description, for both dimension abbreviations and category abbreviations.

#### Scenario: Researcher reads the Part 1 table

- **WHEN** an AI responds to the comparison prompt
- **THEN** the Part 1 table header contains exactly: `Name`, `Link`, `Layer`, `Relevance`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`

#### Scenario: Researcher needs to interpret an abbreviated column

- **WHEN** a researcher reads the Part 1 table instruction in the prompt
- **THEN** a legend block immediately below the instruction lists every abbreviated header with its full name and a one-line description

#### Scenario: Researcher compares functional strengths across platforms

- **WHEN** an AI responds to the comparison prompt
- **THEN** every platform row contains a numeric 1–5 score (or `?`) in every category column and a `Layer` value

#### Scenario: Deep research reveals a different Relevance than discovery

- **WHEN** an AI finds primary-source evidence that changes a platform's Relevance assessment
- **THEN** the Part 1 table contains the revised score, and the per-platform profile explains the revision

#### Scenario: Deep research reveals a different Layer than discovery

- **WHEN** an AI finds primary-source evidence that a platform's primary architectural role differs from its discovery-assigned layer (e.g., initially tagged `core-platform` but is actually an analytics module)
- **THEN** the Part 1 table contains the revised `Layer` value, and the per-platform profile explains the reclassification
