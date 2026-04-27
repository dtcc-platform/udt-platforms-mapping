# Spec: calibration-archive

## Purpose

Defines the archival calibration area at `calibration/`, where prompt and result pairs from different agents are stored for comparison against the same accepted contract.

## Requirements

### Requirement: Calibration archive exists as a top-level archival area

The repository SHALL contain a top-level `calibration/` area for archival prompt/result comparisons across agents.

### Requirement: Calibration archive uses research, cycle, and agent path segments

Calibration artifacts SHALL use the path pattern `calibration/<research>/<cycle>/<agent>/`.

`<research>` SHALL identify one of the canonical research cycles:

- `udt-platforms`
- `udt-initiatives`
- `udt-platform-comparison`

`<cycle>` SHALL identify the accepted iteration baseline, such as `c1` or `c2`.
`<agent>` SHALL identify the agent or branch responsible for the calibration run.

### Requirement: Calibration archive stores one prompt and one result per agent run

Each calibration leaf folder at `calibration/<research>/<cycle>/<agent>/` SHALL contain exactly:

- `prompt.md`
- `result.md`

### Requirement: Calibration archive is archival rather than canonical

Artifacts under `calibration/` SHALL be treated as archival calibration evidence rather than canonical accepted prompts or accepted reference outputs.
