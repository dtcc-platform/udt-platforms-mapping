# Design: add-workflow-naming-conventions

## Summary

This change introduces one baseline naming capability for cross-cutting workflow names.

The goal is not to move all structural path rules into a naming spec. The goal is to give the repo one explicit contract for naming formats that affect traceability across branches, commits, OpenSpec changes, and calibration cycles.

## Boundary

`workflow-naming-conventions` should own:

- branch naming formats
- commit naming formats
- OpenSpec change naming expectations
- calibration cycle token format such as `c01`
- naming-token expectations for calibration segments like `<spec-name>` and `<agent>`

It should not own:

- the existence of `plan/`, `act/`, `observe/`, `reflect/`
- which folders/files are canonical
- the calibration path contract itself

Those remain structural concerns owned by `repository-structure` and `calibration-archive`.

## Motivation

The calibration redesign made naming more important than before.

Examples:

- `calibration/<spec-name>/c01/<agent>/prompt.md`
- isolated agent branches prior to merge
- follow-up OpenSpec changes that encode scope in their names

These names are not just convenience. They are part of how the workflow is read and trusted later through git history.

## Likely baseline requirements

The naming spec should likely require:

- commit messages to use one of the repo's governed patterns
- agent-isolation branches to use the agent name as the branch name
- calibration cycles to use zero-padded `c01`, `c02`, and so on
- OpenSpec change names to be descriptive, lowercase, and hyphen-separated

The spec may also retain examples currently present in the README naming table, but governed as requirements rather than soft guidance.

## Risks

The main risk is duplication with structural specs.

This change should avoid repeating structural path meaning and instead focus only on the naming formats that those structural specs rely on.
