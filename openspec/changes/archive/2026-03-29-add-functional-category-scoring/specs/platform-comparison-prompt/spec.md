## MODIFIED Requirements

### Requirement: Comparison prompt requests a four-part structured output

The prompt template SHALL instruct the model to produce output in exactly three parts, in this order:

1. **Scoring table** — one row per platform, six dimension score columns, six functional category score columns, plus a link column
2. **Per-platform profiles** — one structured profile per platform with all six dimension analyses, sources, and scores
3. **Landscape observations** — gaps in the landscape, where DTCC sits relative to others, which platforms are directly comparable, which are complementary

#### Scenario: Researcher extracts summary data

- **WHEN** an AI responds to the comparison prompt
- **THEN** Part 1 contains a Markdown table with one row per platform, numeric dimension scores per dimension column, and numeric category scores per category column

#### Scenario: Researcher reads a platform profile

- **WHEN** a researcher reads Part 2 of the response
- **THEN** each platform has a self-contained profile with organization, link, license, type, dimension analyses with scores, and a sources section

#### Scenario: Researcher understands DTCC's position

- **WHEN** a researcher reads Part 3
- **THEN** the response explicitly positions DTCC relative to comparable and complementary platforms in the landscape

## ADDED Requirements

### Requirement: Comparison prompt Part 1 scoring table includes functional category columns

The Part 1 scoring table SHALL include one column per functional category in addition to the six dimension columns. The six functional categories are: `visualization` (abbreviated `Viz`), `data-management` (`DM`), `simulation` (`Sim`), `iot-sensing` (`IoT`), `standards` (`Std`), and `infrastructure` (`Infra`).

Each category column SHALL use the same 1–5 integer scoring format as dimension columns — bare integer, `?` for unknown, no `/5` suffix in table cells.

The prompt SHALL include a legend immediately below the Part 1 table instruction listing each abbreviated column header with its full name and one-line description, for both dimension abbreviations and category abbreviations.

#### Scenario: Researcher reads the Part 1 table

- **WHEN** an AI responds to the comparison prompt
- **THEN** the Part 1 table header contains exactly: `Name`, `Link`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`

#### Scenario: Researcher needs to interpret an abbreviated column

- **WHEN** a researcher reads the Part 1 table instruction in the prompt
- **THEN** a legend block immediately below the instruction lists every abbreviated header with its full name and a one-line description

#### Scenario: Researcher compares functional strengths across platforms

- **WHEN** an AI responds to the comparison prompt
- **THEN** every platform row contains a numeric 1–5 score (or `?`) in every category column

### Requirement: Comparison prompt defines functional category rubrics

The prompt template SHALL define a 1–5 scoring rubric for each of the six functional categories. Each rubric SHALL be self-contained in the prompt and SHALL provide anchor descriptions for scores 1, 3, and 5 at minimum.

The same rubrics SHALL appear in `docs/methodology.md` in a dedicated section alongside the existing workflow prose, so researchers have a stable reference without reading the full prompt.

#### Scenario: AI scores a platform's visualization capability

- **WHEN** an AI assigns a `Viz` score to a platform
- **THEN** the score reflects the rubric anchors defined in the prompt — 5 for purpose-built primary visualization, 3 for moderate capability not the primary strength, 1 for absent or negligible

#### Scenario: Researcher consults methodology for category definitions

- **WHEN** a researcher opens `docs/methodology.md`
- **THEN** a section lists all six functional category rubrics with their 1–5 anchor descriptions

#### Scenario: Two agents score the same platform's functional category

- **WHEN** a researcher runs the comparison prompt on two different AI agents
- **THEN** both agents apply the same rubric anchors, producing comparable category scores
