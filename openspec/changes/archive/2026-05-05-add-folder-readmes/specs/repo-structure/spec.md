## MODIFIED Requirements

### Requirement: Repository is organised as action research phases at top level

The repository SHALL use four top-level folders matching the action research phases: `plan/`, `act/`, `observe/`, and `reflect/`.

The `plan/`, `act/`, `observe/`, and `reflect/` folders SHALL expose canonical artifacts as direct files. Direct filenames SHALL begin with the research-thread name when the artifact belongs to a thread.

The canonical research threads are:

- `udt-platforms`
- `udt-initiatives`
- `udt-platform-comparison`

The repository SHALL NOT use a top-level `calibration/` folder for live workflow state.

The phase folders MAY contain local `README.md` files for documentation. These README files are not canonical research artifacts.

#### Scenario: Researcher navigates the repository

- **WHEN** a researcher opens the repository root
- **THEN** they see the four phase folders
- **THEN** the researcher can find canonical planning inputs directly under `plan/`
- **THEN** the researcher can find canonical prompts directly under `act/`
- **THEN** the researcher can find observed outputs directly under `observe/`
- **THEN** the researcher can find reflection artifacts directly under `reflect/`

## REMOVED Requirements

### Requirement: README explains the three-thread model and comparison handoff

**Reason**: README documentation requirements move to the dedicated `repo-readme` capability.

**Migration**: Use `repo-readme` requirement `Root README explains the three-thread model and comparison handoff`.

### Requirement: README explains prompt interpretation review

**Reason**: README documentation requirements move to the dedicated `repo-readme` capability, while prompt-review workflow behavior remains in `repo-prompt-review`.

**Migration**: Use `repo-readme` requirement `Root README explains prompt interpretation review`.
