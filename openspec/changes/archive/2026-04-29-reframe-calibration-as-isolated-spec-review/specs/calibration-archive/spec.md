# Spec Delta: calibration-archive

## Change Type

Modify capability

## Requirements

### Requirement: Calibration archive stores prompt-interpretation calibration artifacts

Calibration artifacts SHALL support prompt-interpretation calibration, not only prompt/result execution pairs.

The archive SHALL support storing generated prompt artifacts for the calibration round.

The actual candidate changes for that round SHALL be captured as isolated OpenSpec proposals on the agent branches.

### Requirement: Shared prompt artifacts precede isolated proposal work

For a given calibration target and cycle, generated prompts SHALL be saved first into shared calibration artifacts.

Only after those prompts are available may per-agent branches produce isolated OpenSpec proposals.

### Requirement: Review and proposal context is isolated before merge

Before merge into a calibration branch, an agent performing review or proposal work SHALL have access to:

- the governing spec
- the shared generated prompts

Before merge, that agent SHALL NOT depend on:

- other agents' change proposals
- any synthesis artifact

### Requirement: Calibration branch review happens after isolated proposal generation

Independent agent branches SHALL be merged into a dedicated calibration branch before the accepted follow-up change is synthesized.

That calibration branch SHALL be the place where merged OpenSpec proposals are reviewed together prior to selecting any accepted follow-up OpenSpec change.

### Requirement: Calibration archive remains non-canonical

Artifacts under `calibration/` SHALL remain calibration evidence rather than accepted canonical workflow state.
