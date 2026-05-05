## MODIFIED Requirements

### Requirement: Repository is organised as action research phases at top level

The repository SHALL use four top-level folders matching the action research phases: `plan/`, `act/`, `observe/`, and `reflect/`.

The `plan/`, `act/`, `observe/`, and `reflect/` folders SHALL expose canonical artifacts as direct files. Direct filenames SHALL begin with the research-thread name when the artifact belongs to a thread.

The canonical research threads are:

- `udt-platforms`
- `udt-initiatives`
- `udt-platform-comparison`

The repository SHALL NOT use a top-level `calibration/` folder for live workflow state.

#### Scenario: Researcher navigates the repository

- **WHEN** a researcher opens the repository root
- **THEN** they see the four phase folders
- **THEN** the researcher can find canonical planning inputs directly under `plan/`
- **THEN** the researcher can find canonical prompts directly under `act/`
- **THEN** the researcher can find observed outputs directly under `observe/`
- **THEN** the researcher can find reflection artifacts directly under `reflect/`

### Requirement: observe/ holds canonical saved outputs per thread

`observe/udt-platforms-web-chatgpt.md`, `observe/udt-platforms-web-claude.md`, and `observe/udt-platforms-web-gemini.md` SHALL contain saved web responses for `udt-platforms`.
`observe/udt-platform-comparison-web-chatgpt.md`, `observe/udt-platform-comparison-web-claude.md`, and `observe/udt-platform-comparison-web-gemini.md` SHALL contain saved web responses for `udt-platform-comparison`.
Observed workflow outputs, such as benchmarking coverage, SHALL also live as direct files under `observe/`.

#### Scenario: Researcher saves a web response

- **WHEN** a researcher saves a canonical web response
- **THEN** the response is saved as a direct file under `observe/`
- **THEN** the filename begins with the matching research-thread name

### Requirement: reflect/ holds synthesized reflection artifacts as direct files

`reflect/` SHALL contain synthesized reflection, reporting, and benchmark-analysis outputs as direct files whose names begin with the research-thread name.

#### Scenario: Researcher finds reflection artifacts

- **WHEN** a researcher opens `reflect/`
- **THEN** reflection artifacts are direct files
- **THEN** the filename identifies the thread and function
