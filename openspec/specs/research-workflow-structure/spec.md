# Spec: research-workflow-structure

## Purpose

Defines the live research workflow phase structure and artifact ownership boundaries.

## Requirements

### Requirement: Research workflow is organised as action research phases

The repository SHALL use four top-level folders matching the action research phases: `plan/`, `act/`, `observe/`, and `reflect/`.

The `plan/`, `act/`, `observe/`, and `reflect/` folders SHALL expose canonical research artifacts as direct files.

Direct filenames SHALL identify the artifact's research object, research action, or artifact role.

The phase folders MAY contain local `README.md` files for documentation.

These README files SHALL NOT be treated as canonical research artifacts or standalone OpenSpec-governed contracts.

#### Scenario: Researcher navigates the workflow

- **WHEN** a researcher opens the repository root
- **THEN** they see the four research phase folders
- **THEN** the researcher can find planning inputs directly under `plan/`
- **THEN** the researcher can find research action prompts directly under `act/`
- **THEN** the researcher can find observed outputs directly under `observe/`
- **THEN** the researcher can find reflection artifacts directly under `reflect/`

### Requirement: plan/ holds research run inputs

`plan/` SHALL contain researcher-facing run inputs used by governed prompts.

`plan/` SHALL NOT be the canonical home for stable behavior definitions, source policies, scoring rubrics, output contracts, or prompt behavior contracts.

Stable behavior definitions, source policies, and scoring rubrics SHALL be governed in `openspec/specs/`.

Additional `plan/` files MAY contain run-specific scope notes, seed inputs, selected candidates, or temporary input material used by canonical prompts.

#### Scenario: Researcher starts from planning inputs

- **WHEN** a researcher opens `plan/`
- **THEN** they see run inputs as direct files
- **THEN** stable behavior definitions, policies, and rubrics are not treated as canonical plan artifacts

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

### Requirement: reflect/ holds synthesized research artifacts

`reflect/` SHALL contain synthesized reflection and reporting outputs as direct files whose names identify the research object and artifact function.

Prompt-review synthesis outputs SHALL live under `reflect/` when they consolidate resolved-prompt review findings across agents.

#### Scenario: Researcher finds reflection artifacts

- **WHEN** a researcher opens `reflect/`
- **THEN** reflection artifacts are direct files
- **THEN** filenames identify object and function

#### Scenario: Researcher saves prompt-review synthesis

- **WHEN** prompt-review findings are consolidated across agents
- **THEN** the synthesis is saved as a direct file under `reflect/`
- **THEN** the synthesis identifies the reviewed action and prompt-review function

### Requirement: Static publication output is separate from research phase folders

The repository SHALL support a top-level `docs/` folder for static publication output generated from research artifacts.

The `docs/` folder SHALL NOT be treated as a fifth action research phase.

The `docs/` folder SHALL NOT become the canonical source location for `plan/`, `act/`, `observe/`, or `reflect/` research artifacts.

Published observation pages SHALL live under the `docs/observations/` category folder.

Published reflection pages SHALL live under the `docs/reflections/` category folder.

The public `docs/index.html` home page SHALL include an `observations` category section linking to generated pages under `docs/observations/`.

The public `docs/index.html` home page SHALL include a `reflections` category section linking to generated pages under `docs/reflections/`.

Phase-local `README.md` files SHALL NOT be treated as publishable research artifact pages.

#### Scenario: Researcher distinguishes source artifacts from publication output

- **WHEN** a researcher opens the repository
- **THEN** canonical research source artifacts remain under the four phase folders
- **THEN** generated public pages may be found under `docs/`

#### Scenario: Observation artifacts are published under docs observe

- **WHEN** `observe/platform-discovery-chatgpt.md` is published
- **THEN** the generated page lives at `docs/observations/platform-discovery-chatgpt.html`
- **THEN** `docs/index.html` links to `./observations/platform-discovery-chatgpt.html` from the `observations` category section

#### Scenario: Reflection artifacts are published under docs reflect

- **WHEN** `reflect/platform-ecosystem.md` is published
- **THEN** the generated page lives at `docs/reflections/platform-ecosystem.html`
- **THEN** `docs/index.html` links to `./reflections/platform-ecosystem.html` from the `reflections` category section

#### Scenario: Phase README files are not published as artifacts

- **WHEN** `observe/README.md` or `reflect/README.md` exists
- **THEN** it is not listed as a research artifact page in `docs/index.html`

### Requirement: Repository scripts hold operational automation

The repository SHALL support a top-level `scripts/` folder for operational automation.

Scripts SHALL NOT be treated as canonical research artifacts.

Scripts SHALL NOT be placed in `act/` unless they are themselves governed research action prompts or prompt artifacts.

The repository SHALL provide `scripts/publish.sh` as the canonical command for publishing observation and reflection Markdown artifacts to `docs/`.

The publish command SHALL fail with a clear error when `pandoc` is unavailable.

#### Scenario: Contributor adds publication automation

- **WHEN** a contributor adds a script that publishes research artifacts to static pages
- **THEN** the script may live under `scripts/`
- **THEN** the script is not treated as an `act/` prompt

#### Scenario: Contributor publishes observation and reflection pages

- **WHEN** a contributor runs `scripts/publish.sh` from the repository
- **THEN** eligible direct Markdown files under `observe/` are published to `docs/observations/`
- **THEN** eligible direct Markdown files under `reflect/` are published to `docs/reflections/`
- **THEN** `docs/index.html` is updated with grouped publication links

#### Scenario: Pandoc is missing

- **WHEN** a contributor runs `scripts/publish.sh` without `pandoc` available
- **THEN** the command exits with an error explaining that `pandoc` is required

### Requirement: Published artifact tables support shared interactions

Published observation and reflection artifact pages SHALL load shared client-side behavior for table interaction when generated by the repository publication command.

Published artifact tables with header cells and body rows SHALL support text filtering across row content.

Published artifact tables with header cells and body rows SHALL support sorting by column.

The table interaction behavior SHALL be implemented as shared static documentation assets rather than source Markdown changes.

#### Scenario: Published table can be filtered

- **WHEN** a published observation or reflection artifact page contains a table with header cells and body rows
- **THEN** the generated page loads shared behavior that provides a filter control for the table
- **THEN** entering filter text narrows visible rows by matching row content

#### Scenario: Published table can be sorted

- **WHEN** a published observation or reflection artifact page contains a table with header cells and body rows
- **THEN** the generated page loads shared behavior that makes table columns sortable
- **THEN** selecting a sortable column reorders body rows by that column

#### Scenario: Source Markdown remains unchanged

- **WHEN** table interaction behavior is added to published artifact pages
- **THEN** source Markdown artifacts under `observe/` and `reflect/` are not modified to encode sorting or filtering controls

### Requirement: Live artifact names use researcher-facing object/action/role language

Live research artifact filenames SHALL use researcher-facing names that describe the artifact's research object, action, or role.

Live filenames SHALL NOT repeat the `udt-` prefix because the repository context supplies the Urban Digital Twin domain.

#### Scenario: Contributor names a live artifact

- **WHEN** a contributor creates or renames a live research artifact
- **THEN** the filename uses object/action/role language
- **THEN** the filename does not begin with `udt-`

### Requirement: Phase folders use phase-specific naming grammar

Plan artifacts SHALL use noun phrases for run inputs, definitions, rubrics, policies, or fixtures.

Act artifacts SHALL use object/action/role names for executable research actions and reporting actions.

Observe artifacts SHALL identify the research action and model or generated output.

Reflect artifacts SHALL identify the research object and synthesis or export product.

OpenSpec capability names SHALL use phase-object-role grammar:

- `plan-<object>-<artifact-role>` for planned definitions, inputs, rubrics, source policies, and checklist contracts
- `act-<object>-<artifact-role>` for research actions, prompt execution contracts, and reporting actions
- `observe-<object>-<artifact-role>` for saved outputs and generated observations
- `reflect-<object>-<artifact-role>` for synthesis, reporting, and reflection outputs

Live artifact filenames SHALL use the same object/action/role naming convention as the governed capability without repeating the phase prefix supplied by the folder.

Phase-local structural contracts SHALL use the phase prefix when the contract governs artifacts in one phase folder.

Cross-phase research governance contracts SHALL use the `research-` prefix.

#### Scenario: Researcher scans phase folders

- **WHEN** a researcher opens `plan/`, `act/`, `observe/`, or `reflect/`
- **THEN** filenames communicate the artifact role using the phase naming grammar

#### Scenario: Contributor names a phase-aligned spec

- **WHEN** a contributor creates or renames an OpenSpec capability for one workflow phase
- **THEN** the capability name follows `<phase>-<object>-<artifact-role>`
- **THEN** the matching live artifact filename uses the object/action/role portion without the phase prefix

#### Scenario: Contributor names a cross-phase research spec

- **WHEN** a contributor creates or renames an OpenSpec capability governing the research workflow across phases
- **THEN** the capability name uses the `research-` prefix
