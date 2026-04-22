## MODIFIED Requirements

### Requirement: Platform inventory prompt file exists

The repository SHALL contain a file at `reflect/discovery/reporting/prompt.md` that provides a self-contained prompt for producing the consolidated ecosystem CSV and HTML from all qualifying response files in `observe/discovery/`.

#### Scenario: File is present and non-empty

- **WHEN** a researcher navigates to `reflect/discovery/reporting/prompt.md`
- **THEN** the file exists and contains a complete, copy-pasteable prompt with no required user input

### Requirement: Prompt auto-scans the observe/discovery directory

The prompt SHALL instruct the model to read all files in `observe/discovery/` without requiring the researcher to specify file paths or names.

#### Scenario: Researcher runs the prompt without specifying files

- **WHEN** a researcher pastes the prompt into an AI CLI session
- **THEN** the model reads all files in `observe/discovery/` automatically, without asking for file paths

#### Scenario: No qualifying response files exist

- **WHEN** the model scans `observe/discovery/` and finds no files with `prompt: platform-discovery` in their YAML block
- **THEN** the model reports that no qualifying response files were found and produces no output

### Requirement: Prompt usage header identifies the target files

The prompt usage header SHALL state that the outputs are `reflect/discovery/reporting/ecosystem.csv` and `reflect/discovery/reporting/ecosystem-map.html` and instruct the researcher to save them in that folder.

#### Scenario: Researcher reads usage instructions

- **WHEN** a researcher opens `reflect/discovery/reporting/prompt.md`
- **THEN** the usage header tells them the output files are `ecosystem.csv` and `ecosystem-map.html` in `reflect/discovery/reporting/`
