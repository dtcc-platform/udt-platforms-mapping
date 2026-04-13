## MODIFIED Requirements

### Requirement: Prompt auto-scans the responses directory

The prompt SHALL instruct the model to read all files in `responses/` without requiring the researcher to specify file paths or names.

#### Scenario: Researcher runs the prompt without specifying files

- **WHEN** a researcher pastes the prompt into an AI CLI session
- **THEN** the model reads all files in `responses/` automatically, without asking for file paths

#### Scenario: No qualifying response files exist

- **WHEN** the model scans `responses/` and finds no files with `prompt: platform-discovery` or `prompt: platform-comparison` in their YAML block
- **THEN** the model reports that no qualifying response files were found and produces no output

### Requirement: Prompt identifies qualifying files by YAML metadata

The prompt SHALL instruct the model to identify two classes of qualifying files:

- **Discovery responses**: files whose YAML block contains `prompt: platform-discovery`
- **Comparison responses**: files whose YAML block contains `prompt: platform-comparison`

Files that do not contain either field SHALL be ignored silently.

#### Scenario: Directory contains mixed response types

- **WHEN** `responses/` contains discovery, comparison, and license response files
- **THEN** only discovery and comparison files contribute rows to the output

#### Scenario: File has no YAML block

- **WHEN** a file in `responses/` has no fenced YAML block at the top
- **THEN** the model skips that file without error

### Requirement: Prompt extracts rows from discovery responses

For discovery responses, the prompt SHALL instruct the model to locate the summary table (the GFM pipe table immediately after the metadata block) and extract every row — including excluded platforms (those with `-1` scores).

Each extracted row SHALL be output as a CSV row with `Phase` set to `discovery`.

The six functional category columns (`Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`) SHALL be set to `-1` for all discovery rows, because those scores are only produced at comparison phase.

#### Scenario: Discovery response contains included and excluded platforms

- **WHEN** the model reads a discovery response whose summary table includes rows with -1 scores (excluded platforms)
- **THEN** the output includes CSV rows for both included and excluded platforms, all with Phase=`discovery`

#### Scenario: Discovery row functional categories

- **WHEN** a discovery row is output
- **THEN** the Viz, DM, Sim, IoT, Std, and Infra columns contain `-1`

### Requirement: Prompt extracts Part 1 scoring table rows from comparison responses

For comparison responses, the prompt SHALL instruct the model to locate the Part 1 scoring table and extract every data row (excluding the header row).

Each extracted row SHALL be output as a CSV row with `Phase` set to `comparison`.

#### Scenario: Response contains a Part 1 table

- **WHEN** a qualifying comparison response file contains a Part 1 scoring table with platform rows
- **THEN** the model extracts all data rows from that table with Phase=`comparison`

#### Scenario: Part 1 table is missing from a qualifying comparison file

- **WHEN** a qualifying comparison response file does not contain a Part 1 scoring table
- **THEN** the model skips that file and notes the omission in its preamble output

### Requirement: Output table includes Model and Date columns from YAML metadata

Each output row SHALL include a `Model` column and a `Date` column populated from the `model` and `date` fields of the source file's YAML metadata block.

#### Scenario: Researcher identifies which model produced a score

- **WHEN** a researcher reads the inventory CSV
- **THEN** every row contains the model name and research date from the response file it was extracted from

#### Scenario: Same platform appears in multiple response files

- **WHEN** the same platform name appears in two or more qualifying response files
- **THEN** the output contains one row per occurrence, each with its own Phase, Model, and Date values

### Requirement: Output CSV schema matches the platform inventory

The output SHALL use exactly the following column order:

`Name`, `Link`, `Phase`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`, `Model`, `Date`

Score cells SHALL contain bare integers (1–5), `-1` (excluded/not-applicable), or `?` for unknown. No `/5` suffix. The `Link` column SHALL contain raw URLs only — no Markdown link syntax.

#### Scenario: Researcher pastes output into the inventory CSV

- **WHEN** a researcher copies the output and appends it to `docs/05-platform-inventory.csv`
- **THEN** the columns align with the existing header without modification

### Requirement: Prompt output is ready to append to the inventory CSV

The prompt SHALL instruct the model to output only CSV data rows (no header row, no surrounding prose after the preamble) so the researcher can paste them directly under the header row in `docs/05-platform-inventory.csv`.

#### Scenario: Researcher pastes output without editing

- **WHEN** a researcher copies the model's output and appends it to `docs/05-platform-inventory.csv` below the header row
- **THEN** the resulting file parses correctly as a CSV with no extra formatting

### Requirement: Prompt usage header identifies the target file

The prompt usage header SHALL state that the output is intended for `docs/05-platform-inventory.csv` and instruct the researcher to paste the output below the existing header row.

#### Scenario: Researcher reads usage instructions

- **WHEN** a researcher opens `prompts/platform-inventory.md`
- **THEN** the usage header tells them the output file is `docs/05-platform-inventory.csv` and how to append the rows
