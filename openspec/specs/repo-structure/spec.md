# Spec: repo-structure

## Purpose

Defines the live repository phase structure and canonical researcher-facing artifact locations.

## Requirements

### Requirement: Repository is organised as action research phases at top level

The repository SHALL use four top-level folders matching the action research phases: `plan/`, `act/`, `observe/`, and `reflect/`.

The `plan/`, `act/`, `observe/`, and `reflect/` folders SHALL expose canonical artifacts as direct files. Direct filenames SHALL identify the artifact's research object, research action, or artifact role.

The canonical live research objects are:

- platforms
- initiatives

The canonical live research actions are:

- discover platforms
- discover initiatives
- compare platforms
- benchmark platform discovery
- report platform discovery
- benchmark platform comparison
- report platform comparison

The repository SHALL NOT use a top-level `calibration/` folder for live workflow state.

The phase folders MAY contain local `README.md` files for documentation. These README files are not canonical research artifacts.

#### Scenario: Researcher navigates the repository

- **WHEN** a researcher opens the repository root
- **THEN** they see the four phase folders
- **THEN** the researcher can find canonical planning inputs directly under `plan/`
- **THEN** the researcher can find canonical prompts directly under `act/`
- **THEN** the researcher can find observed outputs directly under `observe/`
- **THEN** the researcher can find reflection artifacts directly under `reflect/`

### Requirement: plan/ holds research definitions and run inputs

`plan/platform-definition.md` SHALL contain the platform discovery definition and classification contract.
`plan/initiative-definition.md` SHALL contain the initiative discovery definition.
`plan/platform-dimensions-scoring.md` SHALL contain platform comparison dimensions and scoring rubrics.
`plan/platform-source-policy.md` SHALL contain platform comparison source-policy input.
`plan/platform-comparison-set.md` SHALL contain the selected platform comparison set.
`plan/platform-discovery-benchmark.md` SHALL contain the platform discovery benchmark fixture.

#### Scenario: Researcher starts from planning inputs

- **WHEN** a researcher opens `plan/`
- **THEN** they see definitions, scoring, source policy, comparison set, and benchmark fixture files as direct files
- **THEN** no canonical planning input uses the old `udt-` thread-prefixed filename pattern

### Requirement: act/ holds canonical research action prompts

`act/discover-platforms.md` SHALL be the canonical platform discovery prompt template.
`act/discover-initiatives.md` SHALL be the canonical initiative discovery prompt template.
`act/compare-platforms.md` SHALL be the canonical platform comparison prompt template.
`act/benchmark-platform-discovery.md` SHALL be the canonical platform discovery benchmark prompt.
`act/report-platform-discovery.md` SHALL be the canonical platform discovery reporting prompt.
`act/benchmark-platform-comparison.md` SHALL be the platform comparison benchmarking prompt stub.
`act/report-platform-comparison.md` SHALL be the canonical platform comparison reporting prompt.

#### Scenario: Researcher finds canonical prompts

- **WHEN** a researcher opens `act/`
- **THEN** they see research action prompts as direct files
- **THEN** no canonical prompt uses the old `udt-` thread-prefixed filename pattern

### Requirement: observe/ holds canonical saved outputs by action and model

`observe/platform-discovery-chatgpt.md`, `observe/platform-discovery-claude.md`, and `observe/platform-discovery-gemini.md` SHALL contain saved web responses for platform discovery.
`observe/platform-comparison-chatgpt.md`, `observe/platform-comparison-claude.md`, and `observe/platform-comparison-gemini.md` SHALL contain saved web responses for platform comparison.
Observed workflow outputs, such as `observe/platform-discovery-coverage.md`, SHALL also live as direct files under `observe/`.

#### Scenario: Researcher saves a web response

- **WHEN** a researcher saves a canonical web response
- **THEN** the response is saved as a direct file under `observe/`
- **THEN** the filename identifies the research action and model

### Requirement: reflect/ holds synthesized reflection artifacts as direct files

`reflect/` SHALL contain synthesized reflection, reporting, and benchmark-analysis outputs as direct files whose names identify the research object and artifact function.

`reflect/platform-ecosystem.md` SHALL contain the platform discovery ecosystem synthesis.
`reflect/platform-comparison-ecosystem.csv` and `reflect/platform-comparison-ecosystem-map.html` SHALL contain platform comparison structured reflection outputs.

#### Scenario: Researcher finds reflection artifacts

- **WHEN** a researcher opens `reflect/`
- **THEN** reflection artifacts are direct files
- **THEN** filenames identify research object and function without the old `udt-` prefix
