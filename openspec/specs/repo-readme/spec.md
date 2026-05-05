# Spec: repo-readme

## Purpose

Governs the root README and phase README documentation entrypoints.

## Requirements

### Requirement: Root README explains repository workflow and navigation

`README.md` SHALL be the repository-wide documentation entrypoint.

It SHALL explain the action research workflow, the roles of `plan/`, `act/`, `observe/`, and `reflect/`, the canonical research objects and actions, and the relationship between OpenSpec, prompts, outputs, reflection, and git history.

It SHALL link to the governing repo-wide specs for structure, naming, prompt review, and README documentation.

It SHALL explain that live artifact names use researcher-facing object/action/role language and do not repeat the `udt-` prefix.

#### Scenario: Contributor opens the repository

- **WHEN** a contributor reads `README.md`
- **THEN** they understand the repository workflow at a high level
- **THEN** they can find the phase folders and their local README files
- **THEN** they can find the governing repo-wide specs

### Requirement: Root README explains research objects and platform comparison handoff

`README.md` SHALL explain:

- platform discovery as broad technical-artifact discovery
- initiative discovery as broad project, programme, and deployment discovery
- platform comparison as stricter side-by-side evaluation

It SHALL state that only rows classified as `Type = platform` by platform discovery are eligible for platform comparison.

#### Scenario: Researcher reads research object roles

- **WHEN** a researcher reads `README.md`
- **THEN** the README explains platform discovery, initiative discovery, and platform comparison
- **THEN** the README states that only `Type = platform` rows are eligible for platform comparison

### Requirement: Phase folders include local README files

The repository SHALL contain `plan/README.md`, `act/README.md`, `observe/README.md`, and `reflect/README.md`.

Each phase README SHALL explain the local folder purpose, the artifact types stored there, and the naming expectations for direct files in that folder.

Each phase README SHALL point readers back to `README.md` and the governing specs instead of duplicating the full repository workflow.

Each phase README SHALL use object/action/role language rather than thread-centered language for live artifacts.

#### Scenario: Researcher opens a phase folder

- **WHEN** a researcher opens `plan/`, `act/`, `observe/`, or `reflect/`
- **THEN** the folder contains a local `README.md`
- **THEN** the local README explains the folder contents and naming expectations
- **THEN** the local README points to the root README or governing specs for full workflow context

### Requirement: Plan README explains planning inputs

`plan/README.md` SHALL explain that `plan/` contains definitions, source policy, scoring dimensions, comparison set, and benchmark fixture inputs used by governed prompts.

It SHALL explain the live planning filenames, including `platform-definition.md`, `initiative-definition.md`, `platform-dimensions-scoring.md`, `platform-source-policy.md`, `platform-comparison-set.md`, and `platform-discovery-benchmark.md`.

#### Scenario: Researcher opens plan/

- **WHEN** a researcher reads `plan/README.md`
- **THEN** they understand which files are planning inputs
- **THEN** they understand how object/role filenames identify purpose

### Requirement: Act README explains prompt templates

`act/README.md` SHALL explain that `act/` contains canonical prompt templates used to run research, benchmarking, and reporting workflows.

It SHALL explain the live prompt filenames, including `discover-platforms.md`, `discover-initiatives.md`, `compare-platforms.md`, `benchmark-platform-discovery.md`, `report-platform-discovery.md`, `benchmark-platform-comparison.md`, and `report-platform-comparison.md`.

It SHALL explain that prompt behavior is governed by OpenSpec prompt specs and that prompt changes should go through OpenSpec.

#### Scenario: Researcher opens act/

- **WHEN** a researcher reads `act/README.md`
- **THEN** they understand which files are prompts
- **THEN** they understand that prompt contracts are governed by OpenSpec

### Requirement: Observe README explains saved outputs

`observe/README.md` SHALL explain that `observe/` contains saved model outputs and generated coverage artifacts.

It SHALL explain that saved web outputs identify the research action and model in the filename, such as `platform-discovery-claude.md` and `platform-comparison-gemini.md`.

#### Scenario: Researcher opens observe/

- **WHEN** a researcher reads `observe/README.md`
- **THEN** they understand which files are observed outputs
- **THEN** they understand how action and model identifiers appear in filenames

### Requirement: Reflect README explains synthesis artifacts

`reflect/README.md` SHALL explain that `reflect/` contains synthesized ecosystem summaries, reporting artifacts, and benchmark analysis outputs.

It SHALL explain that reflection artifacts use filenames that identify the research object and artifact function, such as `platform-ecosystem.md` and `platform-comparison-ecosystem.csv`.

#### Scenario: Researcher opens reflect/

- **WHEN** a researcher reads `reflect/README.md`
- **THEN** they understand which files are reflection artifacts
- **THEN** they understand how filenames identify object and function
