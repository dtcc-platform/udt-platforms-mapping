## MODIFIED Requirements

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

### Requirement: observe/ holds canonical saved outputs per thread

`observe/udt-platforms/` SHALL contain saved web responses for `udt-platforms`.
`observe/udt-initiatives/` SHALL contain saved web responses for `udt-initiatives`.
`observe/udt-platform-comparison/` SHALL contain saved web responses for `udt-platform-comparison`.

#### Scenario: Researcher saves a web response

- **WHEN** a researcher saves a canonical web response
- **THEN** the response is saved under the matching `observe/<thread>/` folder

### Requirement: README explains prompt interpretation review

`README.md` SHALL explain that prompt interpretation review uses agents sequentially to check whether prompts faithfully interpret governing specs.

It SHALL explain that accepted improvements are captured as OpenSpec deltas rather than calibration artifacts.

#### Scenario: Researcher reviews prompt improvement guidance

- **WHEN** a researcher reads the prompt interpretation review guidance in `README.md`
- **THEN** the README explains sequential agent review
- **THEN** the README explains that OpenSpec changes preserve accepted review decisions

## REMOVED Requirements

### Requirement: README explains the isolation rule for calibration

**Reason**: The isolated calibration workflow is retired.

**Migration**: Use the `README explains prompt interpretation review` requirement.
