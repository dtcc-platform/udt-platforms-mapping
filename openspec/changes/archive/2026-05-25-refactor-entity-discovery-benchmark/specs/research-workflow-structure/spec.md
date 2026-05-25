## MODIFIED Requirements

### Requirement: observe/ holds canonical saved research outputs

Saved web responses SHALL use filenames that identify the research action and model.

Generated workflow outputs SHALL live as direct files under `observe/` when they are observations of a run.

Generated benchmark reports SHALL use filenames that identify the evaluated research action and `benchmark-report` role.

Prompt review feedback SHALL be stdout/chat by default and SHALL NOT require a saved `observe/` artifact.

Optional saved prompt review evidence SHALL live as a direct file under `observe/` when a researcher explicitly preserves it.

#### Scenario: Researcher saves a web response

- **WHEN** a researcher saves a canonical web response
- **THEN** the response is saved as a direct file under `observe/`
- **THEN** the filename identifies the research action and model

#### Scenario: Researcher receives prompt-review feedback

- **WHEN** a reviewer agent reviews a resolved prompt
- **THEN** the review may happen in stdout/chat without creating an `observe/` file

#### Scenario: Researcher saves prompt-review evidence

- **WHEN** a researcher explicitly saves per-agent prompt review output
- **THEN** the artifact is saved as a direct file under `observe/`
- **THEN** the filename identifies the research action and prompt-review role

#### Scenario: Benchmark report is generated

- **WHEN** a benchmark action generates an observed report
- **THEN** the report is saved as a direct file under `observe/`
- **THEN** the filename identifies the evaluated research action and benchmark-report role
