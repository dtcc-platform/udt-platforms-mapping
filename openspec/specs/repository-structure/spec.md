# Spec: repository-structure

## Purpose

Defines the top-level repository structure for the research workflow, including the phase layout, canonical research-thread locations, canonical prompt/output locations, and README explanation requirements.
## Requirements
### Requirement: Repository is organised as action research phases at top level

The repository SHALL use four top-level folders matching the action research phases: `plan/`, `act/`, `observe/`, and `reflect/`.

The `plan/` and `act/` folders SHALL expose canonical thread entrypoints as direct files whose filenames begin with the research-thread name. The `observe/` and `reflect/` folders SHALL retain one subfolder per research thread.

The canonical research threads are:

- `udt-platforms`
- `udt-initiatives`
- `udt-platform-comparison`

The repository MAY also contain a top-level `calibration/` folder for archival prompt-generation calibration across agents.

#### Scenario: Researcher navigates the repository

- **WHEN** a researcher opens the repository root
- **THEN** they see the four phase folders and may also see `calibration/`
- **THEN** the researcher can find canonical planning inputs directly under `plan/`
- **THEN** the researcher can find canonical thread prompts directly under `act/`
- **THEN** the researcher can find thread-grouped outputs under `observe/`
- **THEN** the researcher can find thread-grouped reflection artifacts under `reflect/`

### Requirement: plan/ holds thread inputs

`plan/udt-platforms-scope.md` SHALL contain the `udt-platforms` scope input.
`plan/udt-initiatives-scope.md` SHALL contain the `udt-initiatives` scope input.
`plan/udt-platform-comparison-rubrics.md` SHALL contain the `udt-platform-comparison` rubrics input.
`plan/udt-platform-comparison-source-policy.md` SHALL contain the `udt-platform-comparison` source-policy input.
`plan/udt-platform-comparison-platforms.md` SHALL contain the `udt-platform-comparison` selected-platform input.

#### Scenario: Researcher starts from planning inputs

- **WHEN** a researcher opens `plan/`
- **THEN** they see the canonical thread planning inputs as direct files
- **THEN** no canonical planning input is hidden behind a per-thread subfolder

### Requirement: act/ holds canonical prompts

`act/udt-platforms.md` SHALL be the canonical `udt-platforms` prompt template.
`act/udt-initiatives.md` SHALL be the canonical `udt-initiatives` prompt template.
`act/udt-platform-comparison.md` SHALL be the canonical `udt-platform-comparison` prompt template.

#### Scenario: Researcher finds canonical prompts

- **WHEN** a researcher opens `act/`
- **THEN** they see the canonical thread prompts as direct files

### Requirement: observe/ holds canonical saved outputs per thread

`observe/udt-platforms/` SHALL contain saved web responses for `udt-platforms`.
`observe/udt-initiatives/` SHALL contain saved web responses for `udt-initiatives`.
`observe/udt-platform-comparison/` SHALL contain saved web responses for `udt-platform-comparison`.
Artifacts under `calibration/` SHALL NOT be treated as canonical outputs.

#### Scenario: Researcher saves a web response

- **WHEN** a researcher saves a canonical web response
- **THEN** the response is saved under the matching `observe/<thread>/` folder
- **THEN** calibration artifacts are not treated as canonical observed outputs

### Requirement: reflect/ holds benchmarking and reporting per thread

`reflect/udt-platforms/` SHALL contain `benchmarking/` and `reporting/`.
`reflect/udt-platform-comparison/` SHALL contain `reporting/` and MAY contain `benchmarking/`.
`reflect/udt-initiatives/` MAY contain reporting or synthesis artifacts.

#### Scenario: Researcher finds reflection artifacts

- **WHEN** a researcher opens `reflect/`
- **THEN** reflection artifacts are grouped by research thread
- **THEN** output-heavy benchmarking and reporting artifacts remain inside thread folders

### Requirement: README explains the three-thread model and comparison handoff

`README.md` SHALL explain:

- `udt-platforms` as a broad technical-artifact discovery thread
- `udt-initiatives` as a broad initiative/project discovery thread
- `udt-platform-comparison` as the stricter side-by-side comparison thread

It SHALL also state that only `Type = platform` rows from `udt-platforms` are eligible for `udt-platform-comparison`.

#### Scenario: Researcher reads thread roles

- **WHEN** a researcher reads `README.md`
- **THEN** the README explains the roles of `udt-platforms`, `udt-initiatives`, and `udt-platform-comparison`
- **THEN** the README states that only `Type = platform` rows are eligible for `udt-platform-comparison`

### Requirement: README explains the isolation rule for calibration

`README.md` SHALL explain that the credibility of calibration depends on isolated proposal context before merge.

It SHALL explain that:

- agents may share the governing spec and generated prompts
- agents do not see other agents' proposals before merge
- synthesis happens on a dedicated calibration branch rather than directly on `main`

#### Scenario: Researcher reviews calibration guidance

- **WHEN** a researcher reads the calibration guidance in `README.md`
- **THEN** the README explains the isolated proposal context rule
- **THEN** the README explains that synthesis happens on a dedicated calibration branch
