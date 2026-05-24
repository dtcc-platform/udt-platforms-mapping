## MODIFIED Requirements

### Requirement: act/ holds canonical research action prompts

`act/` SHALL contain governed research action prompts and prompt manifests.

Each governed `act/` prompt SHALL identify its required OpenSpec contracts and run inputs according to `act-prompt-manifest`.

Resolved prompt artifacts generated from governed `act/` manifests SHALL live as direct files under `act/` using filenames that identify the action, resolved role, and resolver agent.

`act/` SHALL NOT contain placeholder prompts for undesigned research actions.

#### Scenario: Researcher finds canonical prompts

- **WHEN** a researcher opens `act/`
- **THEN** they see governed research action prompts as direct files
- **THEN** placeholder prompts for undesigned actions are absent

#### Scenario: Researcher saves resolved prompt artifact

- **WHEN** Codex resolves the entity discovery prompt from its governed manifest and contracts
- **THEN** the resolved prompt artifact is saved as a direct file under `act/`
- **THEN** the filename identifies entity discovery, resolved role, and Codex as resolver

### Requirement: observe/ holds canonical saved research outputs

Saved web responses SHALL use filenames that identify the research action and model.

Generated workflow outputs SHALL live as direct files under `observe/` when they are observations of a run.

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
