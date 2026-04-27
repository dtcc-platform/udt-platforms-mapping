## MODIFIED Requirements

### Requirement: Repository is organised as action research phases at top level

The repository SHALL use four top-level folders matching the action research phases: `plan/`, `act/`, `observe/`, and `reflect/`.

Each phase folder SHALL contain exactly one subfolder per research cycle. The canonical research cycles are:

- `udt-platforms`
- `udt-initiatives`
- `udt-platform-comparison`

The repository MAY also contain a top-level `calibration/` folder for archival prompt/result comparisons across agents.

No files SHALL live at the phase root level for cycle-specific research content — all research-cycle content is inside a cycle subfolder. Each cycle is fully self-contained within its phase folder.

#### Scenario: Researcher navigates the repository

- **WHEN** a researcher opens the repository root
- **THEN** they see four phase folders (`plan/`, `act/`, `observe/`, `reflect/`) containing the `udt-platforms`, `udt-initiatives`, and `udt-platform-comparison` cycles, and MAY also see `calibration/`

#### Scenario: Researcher follows the technical-artifact cycle end-to-end

- **WHEN** a researcher wants to understand the technical-artifact mapping cycle end-to-end
- **THEN** they read `plan/udt-platforms/`, `act/udt-platforms/`, `observe/udt-platforms/`, and `reflect/udt-platforms/` in sequence

### Requirement: README explains the three-cycle model and comparison handoff

`README.md` SHALL explain that the canonical research workflow now uses three cycles:

- `udt-platforms`
- `udt-initiatives`
- `udt-platform-comparison`

It SHALL describe:

- `udt-platforms` as the technical-artifact mapping cycle
- `udt-initiatives` as the initiative/project mapping cycle
- `udt-platform-comparison` as the side-by-side comparison cycle for selected platforms

It SHALL also state that only `Type = platform` rows from `udt-platforms` are eligible for `udt-platform-comparison`.

#### Scenario: New contributor reads the README

- **WHEN** a new contributor opens `README.md`
- **THEN** they understand the three-cycle model and the platform-only handoff into comparison
