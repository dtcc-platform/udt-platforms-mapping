## ADDED Requirements

### Requirement: Discovery benchmarking workflow uses a canonical benchmark fixture

The repository SHALL contain a file at `reflect/discovery/benchmarking/benchmark.md`. This file is the canonical recall benchmark for discovery sessions — it lists platforms that are expected to appear in discovery responses but are at risk of being missed.

The file SHALL contain a single flat table with columns: `Name`, `Link`, `Layer`, `Aliases`, `Tags`. Rows are ordered by tag (baseline first, then government-led, niche-commercial, no-dt-framing, niche-oss). There SHALL NOT be per-tag section headings.

The file SHALL NOT define scoring rubrics, discovery instructions, or Layer criteria — those belong in `plan/discovery/scope.md`.

#### Scenario: Researcher adds a newly discovered missed platform

- **WHEN** a researcher notices that a known in-scope platform did not appear in any model's discovery response
- **THEN** they add a row to `reflect/discovery/benchmarking/benchmark.md`

#### Scenario: Eval prompt reads the fixture

- **WHEN** the eval prompt runs
- **THEN** it reads `reflect/discovery/benchmarking/benchmark.md` and extracts all expected platforms with their Tags, expected Layer, and Aliases

### Requirement: Discovery benchmarking workflow defines alias semantics in the benchmark fixture

Each benchmark row SHALL use the `Aliases` column as the optional list of known variant names for that platform.

For each platform row, the `Aliases` cell SHALL contain either:
- a comma-separated list of one or more alternative names by which the platform may appear in a discovery response summary table, or
- an empty cell, indicating no known aliases

Aliases SHALL be specific enough to identify the platform unambiguously. Generic terms SHALL NOT be used as aliases.

The `Aliases` column is maintained by researchers: when a model is found to use a variant name that caused a false negative, the researcher adds that variant as an alias in the corresponding benchmark row.

#### Scenario: Researcher records a variant name discovered during eval review

- **WHEN** a researcher reviews a coverage report and notices a model used `CityEnergyAnalyst` while the benchmark has `City Energy Analyst`, causing a false negative
- **THEN** the researcher adds `CityEnergyAnalyst` to the `Aliases` cell for that platform row in `reflect/discovery/benchmarking/benchmark.md`

#### Scenario: Platform has no known aliases

- **WHEN** a platform has no observed name variants
- **THEN** its `Aliases` cell is empty and the eval matches only against the canonical `Name`

#### Scenario: Platform has multiple aliases

- **WHEN** a platform's `Aliases` cell contains `CityEnergyAnalyst, CEA`
- **THEN** the eval treats both `CityEnergyAnalyst` and `CEA` as valid match targets in addition to the canonical name

### Requirement: Discovery benchmarking workflow provides a CLI eval prompt

The repository SHALL contain a file at `reflect/discovery/benchmarking/prompt.md`. This file is a Claude Code CLI prompt that performs a recall check against all discovery response files. It is NOT a web chat paste prompt.

The prompt SHALL instruct Claude Code to:

1. Read `reflect/discovery/benchmarking/benchmark.md` and extract all expected platforms with their Tags, expected Layer, and Aliases
2. Glob all files matching `observe/discovery/*.md`
3. For each response file, extract the model name from the YAML metadata block (`model:` field) and parse the summary table to find discovered platform names
4. For each expected platform in the benchmark, check per response file whether the platform name appears in the response summary table using this match rule: build a match set containing the canonical `Name` plus all entries from the `Aliases` cell (split on `,`, trimmed); the platform is found if any member of the match set appears as a case-insensitive substring in the response `Name` column value
5. Record: found (with Layer match/mismatch noted if Layer differs from expected) or missing
6. Write a coverage report to `reflect/discovery/benchmarking/coverage.md`, overwriting if it exists

The prompt SHALL instruct Claude Code to use the model name from the response YAML metadata as the column header in the report, not the filename.

The prompt SHALL be runnable by a researcher telling Claude Code: `run the discovery eval` or `run reflect/discovery/benchmarking/prompt.md`.

#### Scenario: Researcher runs the eval against model responses

- **WHEN** a researcher tells Claude Code to run `reflect/discovery/benchmarking/prompt.md`
- **THEN** Claude Code reads the benchmark and all discovery response files from `observe/discovery/`, produces a coverage report, and saves it to `reflect/discovery/benchmarking/coverage.md`

#### Scenario: Alias eliminates a false negative

- **WHEN** the benchmark has `City Energy Analyst` with alias `CityEnergyAnalyst`, and a model's response summary table contains `CityEnergyAnalyst`
- **THEN** the eval records the platform as found, not missing

#### Scenario: A new discovery response is added

- **WHEN** a researcher adds a new file to `observe/discovery/`
- **THEN** the next eval run automatically includes it without any changes to the eval prompt

### Requirement: Discovery benchmarking workflow writes a structured coverage report

The coverage report saved to `reflect/discovery/benchmarking/coverage.md` SHALL contain:

1. A header block with: report date, benchmark file path, number of response files tested
2. A single flat recall table with columns: `Platform`, `Layer`, `Tags`, and one column per model using the model name from the response YAML metadata. Rows are ordered as in the benchmark. Each result cell SHALL contain `✓ found`, `✗ missing`, or `✓ found (Layer: <actual>)` when the Layer in the response differs from the benchmark Layer. There SHALL NOT be per-tag section headings separating the recall rows.
3. A Novel Finds section grouped by model (`###` heading per model) listing platforms found in responses but absent from the benchmark, in a table matching the benchmark column order: `Name`, `Link`, `Layer`, `Aliases`, `Tags`
4. A summary table at the end: `Model`, `Found`, `Missing`, `Wrong layer`, `Novel Finds` — one row per model

The report SHALL be a valid Markdown file readable in any standard viewer.

#### Scenario: Researcher reads the recall table

- **WHEN** a researcher opens the coverage report
- **THEN** they see a single table listing all benchmark platforms with their Layer, Tags, and per-model recall result

#### Scenario: All models miss the same platform

- **WHEN** a platform appears as `✗ missing` in every model column
- **THEN** the summary row for each model reflects one additional missing count

#### Scenario: A model finds a platform but assigns the wrong Layer

- **WHEN** a model's response includes a platform from the benchmark but with a different Layer than expected
- **THEN** the report cell shows `✓ found (Layer: <actual>)` and the summary counts it as found but also increments the wrong-layer count
