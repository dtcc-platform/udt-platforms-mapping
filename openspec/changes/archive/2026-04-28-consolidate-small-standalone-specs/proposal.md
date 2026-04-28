# Proposal: consolidate-small-standalone-specs

## Why

The current baseline spec set has a few capabilities that are very small and add little value as standalone specs.
Some of them only restate one file-existence rule or one handoff rule that is already owned more naturally by a neighboring capability.

This makes the spec surface larger than necessary:

- more capability names to scan
- more places to check when changing one workflow area
- weaker separation between meaningful shared contracts and thin wrapper specs

The goal is not to collapse the spec model aggressively.
It is to merge only the standalone specs that are too small to justify their own capability boundary.

## What Changes

Retire these standalone capabilities and merge their requirements into nearby owning specs:

- `plan-udt-platform-comparison-rubrics`
  - merge into `act-udt-platform-comparison-prompt`
- `udt-platform-comparison-cycle`
  - merge into `act-udt-platform-comparison-prompt`
- `plan-udt-platforms-scope`
  - merge into `udt-platforms-cycle`

Keep these standalone capabilities even if they are small:

- `prompt-markdown-format`
- `ar-folder-layout`
- `calibration-archive`
- `act-check-prompts-status`
- `plan-udt-platform-comparison-platforms`

## Impact

- fewer low-value capability files in `openspec/specs/`
- clearer ownership of comparison and mapping rules
- smaller mental surface for future prompt and workflow edits
- no intended behavior change in the live repository, only spec consolidation
