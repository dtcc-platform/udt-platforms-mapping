# Spec: repo-readme

## Purpose

Governs the root README and phase README documentation entrypoints.

## Requirements

### Requirement: Root README explains repository workflow and navigation

`README.md` SHALL be the repository-wide documentation entrypoint.

It SHALL present the repository as a spec-first research repository for collaborating with AI agents on Urban Digital Twin platform research.

It SHALL explain that expected model behavior is separated from prompt wording.

It SHALL explain that OpenSpec specs are behavior contracts, `plan/` contains run inputs, `act/` contains contract manifests, `observe/` stores raw outputs, and `reflect/` stores synthesis.

It SHALL explain that resolving an `act/` manifest combines required specs and run inputs into a concrete prompt for a model or agent.

It SHALL explain that repository-local skills can provide shortcuts for resolving governed manifests, while OpenSpec specs and act manifests remain the source of truth.

It SHALL document `udt:discover` as a shortcut for resolving `act/discover-entities.md` for web use and explain the `/copy` fallback when automatic copy is unavailable.

It SHALL explain that resolving the same manifest with different agents can reveal ambiguous spec interpretation and support contract improvement.

It SHALL explain the action research workflow, the roles of `plan/`, `act/`, `observe/`, and `reflect/`, the canonical research objects and actions, and the relationship between OpenSpec, manifests, resolved prompts, outputs, reflection, and git history.

It SHALL do this as a concise researcher-facing orientation page, using phase README files for local folder detail and `openspec/specs/` for formal repository contracts.

It SHALL retain separate diagrams for the research execution flow and prompt interpretation improvement workflow.

It SHALL keep future-direction notes concise when they are included.

It SHALL include a small pointer to the governing repo-wide specs for structure, naming, prompt review, act prompt manifests, web prompt templates, agent skills, and README documentation.

It SHALL explain that live artifact names use researcher-facing object/action/role language and do not repeat the `udt-` prefix.

#### Scenario: Contributor opens the repository

- **WHEN** a contributor reads `README.md`
- **THEN** they understand the repository workflow at a high level
- **THEN** they understand that specs define behavior and `plan/` contains run inputs
- **THEN** they understand that `act/` files are manifests that must be resolved into prompts
- **THEN** they understand that repository-local skills can shortcut common manifest resolution tasks
- **THEN** they can find the phase folders and their local README files
- **THEN** they can find the formal governing specs without the README duplicating their full contract text

### Requirement: Root README explains research objects and platform comparison handoff

`README.md` SHALL explain:

- entity discovery as broad technical-artifact, initiative, project, programme, deployment, and boundary-candidate discovery
- platform comparison as stricter side-by-side evaluation

It SHALL state that only rows classified as `Type = platform` by entity discovery are eligible for platform comparison.

#### Scenario: Researcher reads research object roles

- **WHEN** a researcher reads `README.md`
- **THEN** the README explains entity discovery and platform comparison
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

`plan/README.md` SHALL explain that `plan/` contains run inputs used by governed prompts.

It SHALL explain that stable behavior definitions, source policies, scoring rules, and output contracts live in `openspec/specs/`.

It SHALL explain the live run-input filenames, including `platform-comparison-set.md` and `platform-discovery-benchmark.md`.

#### Scenario: Researcher opens plan/

- **WHEN** a researcher reads `plan/README.md`
- **THEN** they understand which files are planning inputs
- **THEN** they understand how object/role filenames identify purpose

### Requirement: Act README explains prompt manifests

`act/README.md` SHALL explain that `act/` contains contract manifests used to resolve or run governed research, benchmarking, and reporting workflows.

It SHALL explain the live manifest filenames, including `discover-entities.md`, `compare-platforms.md`, `benchmark-platform-discovery.md`, `report-platform-discovery.md`, `benchmark-platform-comparison.md`, and `report-platform-comparison.md`.

It SHALL explain that manifest behavior is governed by OpenSpec prompt specs and `repo-act-prompt-manifest`.

It SHALL explain that manifest and prompt behavior changes should go through OpenSpec.

#### Scenario: Researcher opens act/

- **WHEN** a researcher reads `act/README.md`
- **THEN** they understand which files are action manifests
- **THEN** they understand that prompt contracts and manifest structure are governed by OpenSpec

### Requirement: Observe README explains saved outputs

`observe/README.md` SHALL explain that `observe/` contains saved model outputs and generated coverage artifacts.

It SHALL explain that saved web outputs identify the research action and model in the filename, such as `entity-discovery-claude.md` and `platform-comparison-gemini.md`.

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
