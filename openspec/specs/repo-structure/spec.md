# Spec: repo-structure

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

The repository SHALL NOT use a top-level `calibration/` folder for live workflow state.

#### Scenario: Researcher navigates the repository

- **WHEN** a researcher opens the repository root
- **THEN** they see the four phase folders
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

#### Scenario: Researcher saves a web response

- **WHEN** a researcher saves a canonical web response
- **THEN** the response is saved under the matching `observe/<thread>/` folder

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

### Requirement: README explains prompt interpretation review

`README.md` SHALL explain that prompt interpretation review uses agents sequentially to check whether prompts faithfully interpret governing specs.

It SHALL explain that accepted improvements are captured as OpenSpec deltas rather than calibration artifacts.

#### Scenario: Researcher reviews prompt improvement guidance

- **WHEN** a researcher reads the prompt interpretation review guidance in `README.md`
- **THEN** the README explains sequential agent review
- **THEN** the README explains that OpenSpec changes preserve accepted review decisions
