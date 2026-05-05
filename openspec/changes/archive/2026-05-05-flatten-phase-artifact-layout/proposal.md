# Flatten Phase Artifact Layout

## Why

The repository has already flattened `plan/` and `act/`, but `observe/` and `reflect/` still use nested thread/function folders. That creates a mixed model: some phase folders expose direct artifacts, while others hide artifacts behind thread subtrees.

Flattening the remaining phase folders makes the workflow consistent: the top-level folder identifies the action-research phase, and the filename carries the thread/function/artifact identity.

## What Changes

- Flatten observed web outputs from `observe/<thread>/web-<agent>.md` to `observe/<thread>-web-<agent>.md`.
- Move benchmarking inputs from `reflect/` to `plan/`.
- Move benchmarking and reporting prompts from `reflect/` to `act/`.
- Move benchmarking coverage from `reflect/` to `observe/`.
- Keep synthesized reporting outputs in `reflect/` as direct files.
- Replace nested reflect specs with phase-scoped specs that match the new file locations.
- Update README and repository-structure guidance to describe direct phase artifacts.

## Impact

- `observe/` and `reflect/` become direct artifact folders like `plan/` and `act/`.
- Existing nested `.gitkeep` placeholders become unnecessary.
- Reflect specs are split by effect scope so prompt contracts live under `act-*`, observed artifacts under `observe-*`, planning fixtures under `plan-*`, and synthesized outputs under `reflect-*`.
