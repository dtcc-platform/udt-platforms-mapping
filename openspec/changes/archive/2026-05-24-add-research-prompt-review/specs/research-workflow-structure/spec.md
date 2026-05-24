## MODIFIED Requirements

### Requirement: observe/ holds canonical saved research outputs

Saved web responses SHALL use filenames that identify the research action and model.

Generated workflow outputs SHALL live as direct files under `observe/` when they are observations of a run.

Resolved prompt snapshots and per-agent prompt review outputs SHALL live as direct files under `observe/` when they are generated for prompt review.

#### Scenario: Researcher saves a web response

- **WHEN** a researcher saves a canonical web response
- **THEN** the response is saved as a direct file under `observe/`
- **THEN** the filename identifies the research action and model

#### Scenario: Researcher saves prompt-review evidence

- **WHEN** a researcher saves a resolved prompt snapshot or per-agent prompt review output
- **THEN** the artifact is saved as a direct file under `observe/`
- **THEN** the filename identifies the research action and prompt-review role

### Requirement: reflect/ holds synthesized research artifacts

`reflect/` SHALL contain synthesized reflection, reporting, and benchmark-analysis outputs as direct files whose names identify the research object and artifact function.

Prompt-review synthesis outputs SHALL live under `reflect/` when they consolidate resolved-prompt review findings across agents.

#### Scenario: Researcher finds reflection artifacts

- **WHEN** a researcher opens `reflect/`
- **THEN** reflection artifacts are direct files
- **THEN** filenames identify object and function

#### Scenario: Researcher saves prompt-review synthesis

- **WHEN** prompt-review findings are consolidated across agents
- **THEN** the synthesis is saved as a direct file under `reflect/`
- **THEN** the synthesis identifies the reviewed action and prompt-review function
