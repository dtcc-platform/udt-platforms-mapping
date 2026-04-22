## MODIFIED Requirements

### Requirement: reflect/discovery/benchmarking/prompt.md exists as a Claude Code CLI eval prompt

The repository SHALL contain a file at `reflect/discovery/benchmarking/prompt.md`. This file is a Claude Code CLI prompt — it contains instructions for Claude Code to execute a recall check against all discovery response files. It is NOT a web chat paste prompt.

The prompt SHALL instruct Claude Code to:

1. Read `reflect/discovery/benchmarking/benchmark.md` and extract all expected platforms with their Tags, expected Layer, and Aliases
2. Glob all files matching `observe/discovery/*.md`
3. For each response file, extract the model name from the YAML metadata block (`model:` field) and parse the summary table to find discovered platform names
4. For each expected platform in the fixture, check — per response file — whether the platform name appears in the response summary table using the following match rule: build a match set containing the canonical `Name` plus all entries from the `Aliases` cell (split on `,`, trimmed); the platform is found if any member of the match set appears as a case-insensitive substring in the response `Name` column value
5. Record: found (with Layer match/mismatch noted if Layer differs from expected) or missing
6. Write a coverage report to `reflect/discovery/benchmarking/coverage.md`, overwriting if it exists

The report recall section SHALL be a single flat table with columns: `Platform`, `Layer`, `Tags`, and one column per model. Rows are ordered as in the benchmark. There SHALL NOT be per-tag section headings in the recall section.

The prompt SHALL instruct Claude Code to use the model name from the response YAML metadata as the column header in the report, not the filename.

The prompt SHALL be runnable by a researcher telling Claude Code: "run the discovery eval" or "run reflect/discovery/benchmarking/prompt.md".

#### Scenario: Researcher runs the eval against model responses

- **WHEN** a researcher tells Claude Code to run `reflect/discovery/benchmarking/prompt.md`
- **THEN** Claude Code reads the fixture and all discovery response files from `observe/discovery/`, produces a coverage report with a single flat recall table, and saves it to `reflect/discovery/benchmarking/coverage.md`

#### Scenario: Alias eliminates a false negative

- **WHEN** the fixture has "City Energy Analyst" with alias `CityEnergyAnalyst`, and a model's response summary table contains "CityEnergyAnalyst"
- **THEN** the eval records the platform as found, not missing

#### Scenario: A new discovery response is added

- **WHEN** a researcher adds a new file to `observe/discovery/`
- **THEN** the next eval run automatically includes it without any changes to the eval prompt
