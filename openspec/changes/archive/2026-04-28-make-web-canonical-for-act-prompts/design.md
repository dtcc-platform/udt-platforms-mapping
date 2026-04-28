# Design: make-web-canonical-for-act-prompts

## Summary

Shift canonical research execution for `act/` prompts from CLI-first to web-first, and complete the act-prompt set by adding a governed `udt-initiatives` prompt.

## Current Problem

The repository currently has:

- `act/udt-platforms/prompt.md`
- `act/udt-platform-comparison/prompt.md`
- no governed `act/udt-initiatives/prompt.md`

And the two existing act prompts currently assume:

- required inputs are read directly by an AI CLI
- the result is saved to `observe/<thread>/<model-short>.md`

That is no longer aligned with actual intended use, which is web-based execution.

## Proposed Model

For `act/` research prompts:

- the canonical interface is the web interface
- each prompt resolves its planning inputs into one copy-ready block
- the user pastes that resolved prompt into a web model
- the response is saved under `observe/<thread>/web-<model-short>.md`

This restores a web-oriented save convention, but without restoring the old CLI/Web branching.
The canonical mode is just web.

## New `udt-initiatives` Prompt

The repository should add `act/udt-initiatives/prompt.md` as a first-class governed prompt.

Its job is to:

- map initiatives, projects, programmes, and deployments
- use `plan/udt-initiatives/scope.md`
- produce the governed initiative table contract
- preserve `Uses = ?` when the technical substrate is unclear

## Scope

This proposal changes:

- `openspec/specs/ar-folder-layout/spec.md`
- `openspec/specs/act-udt-platforms-prompt/spec.md`
- `openspec/specs/act-udt-platform-comparison-prompt/spec.md`
- prompt-status expectations

This proposal adds:

- `openspec/specs/act-udt-initiatives-prompt/spec.md`
- `act/udt-initiatives/prompt.md`

## Save Convention

Canonical act-prompt responses should use:

- `observe/udt-platforms/web-<model-short>.md`
- `observe/udt-initiatives/web-<model-short>.md`
- `observe/udt-platform-comparison/web-<model-short>.md`

## Verification Consequences

Prompt verification should expect:

- a `## Required Inputs` section
- web-oriented execution instructions
- no CLI-first execution requirement for research prompts
