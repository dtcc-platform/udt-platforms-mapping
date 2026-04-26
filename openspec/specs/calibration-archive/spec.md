# Spec: calibration-archive

## Purpose

Defines the archival calibration area at `calibration/`, where prompt and result pairs from different agents are stored for comparison against the same accepted contract.

## Requirements

### Requirement: Calibration archive exists as a top-level archival area

The repository SHALL contain a top-level `calibration/` area for archival prompt/result comparisons across agents.

The purpose of `calibration/` SHALL be prompt calibration rather than canonical research execution.

#### Scenario: Researcher looks for agent comparison artifacts

- **WHEN** a researcher wants to inspect prompt and result differences across agents
- **THEN** they find those artifacts under `calibration/` rather than under the canonical `plan/`, `act/`, `observe/`, or `reflect/` folders

### Requirement: Calibration archive uses research, cycle, and agent path segments

Calibration artifacts SHALL use the path pattern `calibration/<research>/<cycle>/<agent>/`.

`<research>` SHALL identify the research type, such as `discovery` or `rating`.

`<cycle>` SHALL identify the accepted iteration baseline, such as `c1` or `c2`.

`<agent>` SHALL identify the agent or branch responsible for the calibration run.

#### Scenario: Discovery calibration run is archived

- **WHEN** a researcher saves a discovery calibration run for agent `agent-a` from cycle `c1`
- **THEN** the artifacts live under `calibration/discovery/c1/agent-a/`

#### Scenario: Rating calibration run is archived

- **WHEN** a researcher saves a rating calibration run for agent `agent-b` from cycle `c2`
- **THEN** the artifacts live under `calibration/rating/c2/agent-b/`

### Requirement: Calibration archive stores one prompt and one result per agent run

Each calibration leaf folder at `calibration/<research>/<cycle>/<agent>/` SHALL contain exactly these files:
- `prompt.md`
- `result.md`

The archive SHALL remain intentionally minimal in this version of the workflow.

#### Scenario: Agent calibration artifacts are saved

- **WHEN** a researcher saves a completed calibration run
- **THEN** the folder contains `prompt.md` and `result.md`

#### Scenario: Researcher wants to add extra metadata

- **WHEN** a researcher considers adding notes or metadata files to a calibration leaf folder
- **THEN** the current baseline contract does not require or define those files

### Requirement: Calibration archive is archival rather than canonical

Artifacts under `calibration/` SHALL be treated as archival calibration evidence rather than canonical accepted prompts or accepted reference outputs.

The canonical accepted prompt SHALL continue to live under `act/`. Canonical accepted outputs SHALL continue to live under `observe/`.

#### Scenario: Researcher compares canonical and calibration artifacts

- **WHEN** a researcher compares `act/discovery/prompt.md` with `calibration/discovery/c1/agent-a/prompt.md`
- **THEN** the `act/` file is understood as canonical and the `calibration/` file is understood as an archival calibration variant
