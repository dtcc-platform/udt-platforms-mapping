## MODIFIED Requirements

### Requirement: Platform inventory prompt file exists

The repository SHALL contain a file at `reflect/discovery/reporting/prompt.md` that provides a self-contained prompt for producing a consolidated Markdown table from qualifying discovery response files in `observe/discovery/`.

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
- **THEN** the model reports that no qualifying response files were found and produces no output file

### Requirement: Prompt identifies qualifying files by discovery YAML metadata

The prompt SHALL instruct the model to treat as qualifying only files whose YAML block contains `prompt: platform-discovery`.

Files that do not contain that field SHALL be ignored silently.

#### Scenario: Directory contains mixed response types

- **WHEN** `observe/discovery/` contains discovery and comparison response files
- **THEN** only files with `prompt: platform-discovery` contribute rows to the discovery reporting output

#### Scenario: File has no YAML block

- **WHEN** a file in `observe/discovery/` has no fenced YAML block at the top
- **THEN** the model skips that file without error

### Requirement: Prompt extracts one consolidated Markdown table from discovery responses

The prompt SHALL instruct the model to locate the summary table in each qualifying discovery response and extract the relevant rows into a single consolidated Markdown table.

The output file SHALL contain one table only. The table SHALL use the `Link` column value as a Markdown link, preserving the original URL.

#### Scenario: Multiple discovery responses exist

- **WHEN** the model reads more than one qualifying discovery response
- **THEN** it writes one consolidated Markdown table rather than one table per response

### Requirement: Discovery reporting output is ordered by URL part of Link

The consolidated Markdown table SHALL be ordered by the URL portion of the `Link` column, not by source-file order.

The ordering rule SHALL use the URL target extracted from each Markdown link cell.

#### Scenario: Two rows appear in different source files

- **WHEN** two platform rows come from different discovery responses
- **THEN** their order in the final Markdown table follows the extracted URL ordering rule rather than response-file order

### Requirement: Prompt writes a Markdown file in reflect/discovery/reporting

The discovery reporting prompt SHALL write its output to `reflect/discovery/reporting/ecosystem.md`.

The prompt usage header SHALL identify `ecosystem.md` as the target output file in that folder.

#### Scenario: Researcher reads usage instructions

- **WHEN** a researcher opens `reflect/discovery/reporting/prompt.md`
- **THEN** the usage header tells them to save the output to `reflect/discovery/reporting/ecosystem.md`
