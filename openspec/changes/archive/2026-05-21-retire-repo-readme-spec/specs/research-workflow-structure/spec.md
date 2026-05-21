## MODIFIED Requirements

### Requirement: Research workflow is organised as action research phases

The repository SHALL use four top-level folders matching the action research phases: `plan/`, `act/`, `observe/`, and `reflect/`.

The `plan/`, `act/`, `observe/`, and `reflect/` folders SHALL expose canonical research artifacts as direct files. Direct filenames SHALL identify the artifact's research object, research action, or artifact role.

The canonical live research objects are:

- entities
- platforms
- initiatives

The canonical live research actions are:

- discover entities
- compare platforms
- benchmark platform discovery
- report platform discovery
- benchmark platform comparison
- report platform comparison

The phase folders MAY contain local `README.md` files for documentation. These README files are documentation aids and SHALL NOT be treated as canonical research artifacts or standalone OpenSpec-governed contracts.

#### Scenario: Researcher navigates the workflow

- **WHEN** a researcher opens the repository root
- **THEN** they see the four research phase folders
- **THEN** the researcher can find canonical planning inputs directly under `plan/`
- **THEN** the researcher can find canonical prompts directly under `act/`
- **THEN** the researcher can find observed outputs directly under `observe/`
- **THEN** the researcher can find reflection artifacts directly under `reflect/`
