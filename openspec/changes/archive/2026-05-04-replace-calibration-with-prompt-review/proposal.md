# Replace Calibration With Prompt Review

## Why

The current `calibration/` workflow is an archival, isolated multi-agent process. The repository is moving toward a simpler sequential workflow where agents review whether prompts faithfully interpret OpenSpec contracts, and improvements are captured as OpenSpec deltas rather than loose calibration artifacts.

The existing calibration folder is empty except for `.gitkeep`, while its specs and README guidance still describe a heavier process with calibration branches, cycles, and archived prompt files. That makes the live repository harder to understand and keeps a failing spec around for a workflow that is no longer the preferred path.

## What Changes

- Retire the `calibration/` folder and `calibration-archive` capability.
- Add a `prompt-interpretation-review` capability for sequential agent review of spec-to-prompt fidelity.
- Remove calibration-specific naming requirements.
- Update repository-structure so the canonical top-level model is `plan/`, `act/`, `observe/`, and `reflect/`.
- Rewrite README guidance and diagrams around one coherent workflow that includes OpenSpec review, execution, observation, and reflection.

## Impact

- Prompt improvement evidence moves into OpenSpec changes and archived change history.
- The old `calibration/<spec-name>/<cycle>/<agent>/prompt.md` path contract is removed.
- README becomes shorter and no longer describes isolated calibration branches.
