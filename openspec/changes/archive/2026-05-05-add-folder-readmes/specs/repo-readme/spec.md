## ADDED Requirements

### Requirement: Root README explains repository workflow and navigation

`README.md` SHALL be the repository-wide documentation entrypoint.

It SHALL explain the action research workflow, the roles of `plan/`, `act/`, `observe/`, and `reflect/`, the canonical research threads, and the relationship between OpenSpec, prompts, outputs, reflection, and git history.

It SHALL link to the governing repo-wide specs for structure, naming, prompt review, and README documentation.

#### Scenario: Contributor opens the repository

- **WHEN** a contributor reads `README.md`
- **THEN** they understand the repository workflow at a high level
- **THEN** they can find the phase folders and their local README files
- **THEN** they can find the governing repo-wide specs

### Requirement: Root README explains the three-thread model and comparison handoff

`README.md` SHALL explain:

- `udt-platforms` as a broad technical-artifact discovery thread
- `udt-initiatives` as a broad initiative/project discovery thread
- `udt-platform-comparison` as the stricter side-by-side comparison thread

It SHALL state that only `Type = platform` rows from `udt-platforms` are eligible for `udt-platform-comparison`.

#### Scenario: Researcher reads thread roles

- **WHEN** a researcher reads `README.md`
- **THEN** the README explains the roles of `udt-platforms`, `udt-initiatives`, and `udt-platform-comparison`
- **THEN** the README states that only `Type = platform` rows are eligible for `udt-platform-comparison`

### Requirement: Root README explains prompt interpretation review

`README.md` SHALL describe prompt interpretation review as the method for using multiple agents to improve prompt/spec fidelity.

It SHALL explain that accepted review feedback is captured through OpenSpec changes rather than calibration artifacts.

#### Scenario: Contributor reads the workflow overview

- **WHEN** a contributor reads `README.md`
- **THEN** they understand that multi-agent prompt review is sequential
- **THEN** they understand that OpenSpec history is the audit trail

### Requirement: Phase folders include local README files

The repository SHALL contain `plan/README.md`, `act/README.md`, `observe/README.md`, and `reflect/README.md`.

Each phase README SHALL explain the local folder purpose, the artifact types stored there, and the naming expectations for direct files in that folder.

Each phase README SHALL point readers back to `README.md` and the governing specs instead of duplicating the full repository workflow.

#### Scenario: Researcher opens a phase folder

- **WHEN** a researcher opens `plan/`, `act/`, `observe/`, or `reflect/`
- **THEN** the folder contains a local `README.md`
- **THEN** the local README explains the folder contents and naming expectations
- **THEN** the local README points to the root README or governing specs for full workflow context

### Requirement: Plan README explains planning inputs

`plan/README.md` SHALL explain that `plan/` contains scope, source-policy, rubric, selected-platform, and benchmark fixture inputs used by governed prompts.

It SHALL explain that thread-specific planning files begin with the research-thread name.

#### Scenario: Researcher opens plan/

- **WHEN** a researcher reads `plan/README.md`
- **THEN** they understand which files are planning inputs
- **THEN** they understand how thread-prefixed filenames identify ownership

### Requirement: Act README explains prompt templates

`act/README.md` SHALL explain that `act/` contains canonical prompt templates used to run research, benchmarking, and reporting workflows.

It SHALL explain that prompt behavior is governed by OpenSpec prompt specs and that prompt changes should go through OpenSpec.

#### Scenario: Researcher opens act/

- **WHEN** a researcher reads `act/README.md`
- **THEN** they understand which files are prompts
- **THEN** they understand that prompt contracts are governed by OpenSpec

### Requirement: Observe README explains saved outputs

`observe/README.md` SHALL explain that `observe/` contains saved model outputs and generated coverage artifacts.

It SHALL explain that saved web outputs should identify the research thread and model in the filename.

#### Scenario: Researcher opens observe/

- **WHEN** a researcher reads `observe/README.md`
- **THEN** they understand which files are observed outputs
- **THEN** they understand how thread and model identifiers appear in filenames

### Requirement: Reflect README explains synthesis artifacts

`reflect/README.md` SHALL explain that `reflect/` contains synthesized ecosystem summaries, reporting artifacts, and benchmark analysis outputs.

It SHALL explain that reflection artifacts should use filenames that identify the research thread and artifact function.

#### Scenario: Researcher opens reflect/

- **WHEN** a researcher reads `reflect/README.md`
- **THEN** they understand which files are reflection artifacts
- **THEN** they understand how filenames identify thread and function
