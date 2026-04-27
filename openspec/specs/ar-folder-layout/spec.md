# Spec: ar-folder-layout

## Purpose

Defines the top-level folder structure for the repository, organised as action research phases plus a separate archival calibration area.

## Requirements

### Requirement: Repository is organised as action research phases at top level

The repository SHALL use four top-level folders matching the action research phases: `plan/`, `act/`, `observe/`, and `reflect/`.

Each phase folder SHALL contain exactly one subfolder per research cycle. The canonical research cycles are:

- `udt-platforms`
- `udt-initiatives`
- `udt-platform-comparison`

The repository MAY also contain a top-level `calibration/` folder for archival prompt/result comparisons across agents.

#### Scenario: Researcher navigates the repository

- **WHEN** a researcher opens the repository root
- **THEN** they see the four phase folders, the three cycle names, and may also see `calibration/`

### Requirement: plan/ holds cycle inputs

`plan/udt-platforms/` SHALL contain `scope.md`.
`plan/udt-initiatives/` SHALL contain `scope.md`.
`plan/udt-platform-comparison/` SHALL contain `rubrics.md`, `source-policy.md`, and `platforms.md`.

### Requirement: act/ holds canonical prompts and maintenance prompts

`act/udt-platforms/prompt.md` SHALL be the canonical `udt-platforms` prompt template.
`act/udt-platform-comparison/prompt.md` SHALL be the canonical `udt-platform-comparison` prompt template.
`act/check-prompts-status.md` SHALL be the prompt-status maintenance prompt.

### Requirement: observe/ holds canonical saved outputs per cycle

`observe/udt-platforms/` SHALL contain saved `udt-platforms` responses.
`observe/udt-platform-comparison/` SHALL contain saved comparison responses.
Artifacts under `calibration/` SHALL NOT be treated as canonical outputs.

### Requirement: reflect/ holds benchmarking and reporting per cycle

`reflect/udt-platforms/` SHALL contain `benchmarking/` and `reporting/`.
`reflect/udt-platform-comparison/` SHALL contain `reporting/` and MAY contain `benchmarking/`.
`reflect/udt-initiatives/` MAY contain reporting or synthesis artifacts.

### Requirement: README explains the three-cycle model and comparison handoff

`README.md` SHALL explain:

- `udt-platforms` as the technical-artifact mapping cycle
- `udt-initiatives` as the initiative/project mapping cycle
- `udt-platform-comparison` as the side-by-side comparison cycle

It SHALL also state that only `Type = platform` rows from `udt-platforms` are eligible for `udt-platform-comparison`.
