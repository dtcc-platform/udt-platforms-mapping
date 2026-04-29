# Design: replace-ar-folder-layout-with-repository-structure

## Summary

This change replaces the baseline structural capability `ar-folder-layout` with `repository-structure`.

The replacement keeps the current structural contract intact while correcting the capability name so it reflects what the spec actually governs.

## Motivation

The old name implies a narrow concern with folder layout in an action-research framing.

That is no longer accurate. The baseline contract now governs:

- repository phases
- research-thread organization
- canonical prompt locations
- canonical observe/reflect locations
- README explanation requirements for active workflow structure and calibration

This makes the spec a repository-structure contract, not just a folder-layout one.

## Scope

`repository-structure` should own:

- top-level phase folders
- canonical research-thread subfolders
- canonical plan/act/observe/reflect locations
- README requirements about thread roles and calibration explanation

It should not absorb naming rules that are cross-cutting rather than structural.

## Transition

The baseline requirements can move almost directly.

The transition should:

1. create `openspec/specs/repository-structure/spec.md`
2. move the current `ar-folder-layout` requirements into it
3. retire `openspec/specs/ar-folder-layout/spec.md`
4. update any references in active specs or change deltas that still name `ar-folder-layout`

## Risks

The main risk is leaving stale references behind in delta specs or archived change rationale. Baseline references should be updated where they affect active workflow understanding, but archived history should remain archival.
