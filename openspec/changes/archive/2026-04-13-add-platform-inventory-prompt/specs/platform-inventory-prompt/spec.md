## ADDED Requirements

### Requirement: Platform inventory prompt file exists

The repository SHALL contain a file at `prompts/platform-inventory.md` that provides a self-contained prompt for producing a consolidated GFM inventory table from all comparison response files in `responses/`.

#### Scenario: File is present and non-empty

- **WHEN** a researcher navigates to `prompts/platform-inventory.md`
- **THEN** the file exists and contains a complete, copy-pasteable prompt with no required user input

### Requirement: Prompt auto-scans the responses directory

The prompt SHALL instruct the model to read all files in `responses/` without requiring the researcher to specify file paths or names.

#### Scenario: Researcher runs the prompt without specifying files

- **WHEN** a researcher pastes the prompt into an AI session
- **THEN** the model reads all files in `responses/` automatically, without asking for file paths

#### Scenario: No comparison response files exist

- **WHEN** the model scans `responses/` and finds no files with `prompt: platform-comparison` in their YAML block
- **THEN** the model reports that no qualifying response files were found and produces no table

### Requirement: Prompt identifies comparison responses by YAML metadata

The prompt SHALL instruct the model to identify qualifying files by the presence of a fenced YAML block at the top of the file containing `prompt: platform-comparison`. Files that do not contain this field SHALL be ignored.

#### Scenario: Directory contains mixed response types

- **WHEN** `responses/` contains both discovery and comparison response files
- **THEN** only files with `prompt: platform-comparison` in their YAML block contribute rows to the output table

#### Scenario: File has no YAML block

- **WHEN** a file in `responses/` has no fenced YAML block at the top
- **THEN** the model skips that file without error

### Requirement: Prompt extracts Part 1 scoring table rows

The prompt SHALL instruct the model to locate the Part 1 scoring table in each qualifying response file and extract every data row (excluding the header row).

#### Scenario: Response contains a Part 1 table

- **WHEN** a qualifying response file contains a Part 1 scoring table with platform rows
- **THEN** the model extracts all data rows from that table

#### Scenario: Part 1 table is missing from a qualifying file

- **WHEN** a qualifying response file does not contain a Part 1 scoring table
- **THEN** the model skips that file and notes the omission in its output

### Requirement: Output table includes Model and Date columns from YAML metadata

Each output row SHALL include a `Model` column and a `Date` column populated from the `model` and `date` fields of the source file's YAML metadata block.

#### Scenario: Researcher identifies which model produced a score

- **WHEN** a researcher reads the inventory table
- **THEN** every row contains the model name and research date from the response file it was extracted from

#### Scenario: Same platform appears in multiple response files

- **WHEN** the same platform name appears in two or more qualifying response files
- **THEN** the output table contains one row per occurrence, each with its own Model and Date values

### Requirement: Output table schema matches the platform inventory

The output table SHALL use exactly the following column order:

`Name`, `Link`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`, `Model`, `Date`

Score cells SHALL contain bare integers (1–5) or `?` for unknown. No `/5` suffix in table cells.

#### Scenario: Researcher pastes output into the inventory

- **WHEN** a researcher copies the output table and pastes it into `docs/05-platform-inventory.md`
- **THEN** the columns align with the existing inventory table header without modification

#### Scenario: Source table uses a different column order

- **WHEN** a Part 1 table in a response file has columns in a different order than the inventory schema
- **THEN** the model reorders columns to match the inventory schema before outputting

### Requirement: Prompt output is ready to paste into the inventory

The prompt SHALL instruct the model to output only the GFM table rows (no header, no surrounding prose) so the researcher can paste them directly under the header row in `docs/05-platform-inventory.md`.

#### Scenario: Researcher pastes output without editing

- **WHEN** a researcher copies the model's output and pastes it into `docs/05-platform-inventory.md` below the header row
- **THEN** the resulting table renders correctly with no extra formatting or blank rows

### Requirement: Prompt usage header identifies the target file

The prompt usage header SHALL state that the output is intended for `docs/05-platform-inventory.md` and instruct the researcher to paste the output below the existing header row.

#### Scenario: Researcher reads usage instructions

- **WHEN** a researcher opens `prompts/platform-inventory.md`
- **THEN** the usage header tells them which file to paste into and how
