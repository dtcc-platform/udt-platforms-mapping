# Spec: calibration-archive

## Purpose

Defines the archival calibration area at `calibration/`, where generated prompts are stored for independent spec-interpretation calibration against the same accepted contract.

## Requirements

### Requirement: Calibration archive exists as a top-level archival area

The repository SHALL contain a top-level `calibration/` area for archival prompt-generation artifacts across agents.

### Requirement: Calibration archive uses spec-name, cycle, and agent path segments

Calibration artifacts SHALL use the path pattern `calibration/<spec-name>/<cycle>/<agent>/`.

`<spec-name>` SHALL identify the governed spec being calibrated, such as:

- `act-udt-platforms-prompt`
- `act-udt-initiatives-prompt`
- `act-udt-platform-comparison-prompt`

`<cycle>` SHALL identify the accepted iteration baseline using the zero-padded form `c01`, `c02`, and so on.
`<agent>` SHALL identify the agent or branch responsible for the calibration run.

### Requirement: Calibration archive stores generated prompts before branching

For a given spec and cycle, generated prompts SHALL be saved first into shared calibration artifacts before per-agent proposal branching begins.

Each calibration leaf folder at `calibration/<spec-name>/<cycle>/<agent>/` SHALL contain:

- `prompt.md`

### Requirement: Calibration proposal context is isolated before merge

After shared prompts are available, each agent may create its own branch and its own OpenSpec change proposal.

Before merge into a dedicated calibration branch, an agent performing proposal work SHALL have access to:

- the governing spec
- the shared generated prompts

Before merge, that agent SHALL NOT depend on:

- other agents' change proposals
- any synthesis artifact

### Requirement: Calibration branch review happens after isolated proposal generation

Independent agent branches SHALL be merged into a dedicated calibration branch before any accepted follow-up change is synthesized.

That calibration branch SHALL be the place where merged OpenSpec proposals are reviewed together before selecting any accepted follow-up OpenSpec change.

### Requirement: Calibration archive is archival rather than canonical

Artifacts under `calibration/` SHALL be treated as archival calibration evidence rather than canonical accepted prompts or accepted reference outputs.
