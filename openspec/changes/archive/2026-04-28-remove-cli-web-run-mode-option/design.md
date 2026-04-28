# Design: remove-cli-web-run-mode-option

## Summary

Retire the shared run-modes capability and make act prompts execute through one governed path only.

## Current Problem

The current design treats interface choice as a reusable prompt capability:

- prompts declare required inputs
- prompts ask the user `Run as CLI or Web?`
- prompts define two execution paths
- outputs are saved with either `cli-` or `web-` prefixes

That has three costs:

1. it adds repeated boilerplate to every act prompt
2. it governs interaction style rather than research behavior
3. it splits saved observations by interface rather than by prompt/model alone

## Proposed Model

Act prompts remain self-contained prompt templates with declared required inputs, but they no longer branch by interface.

The governed behavior becomes:

- read the required input files
- execute the prompt body directly
- save the response to one canonical observe-path pattern

This change retires the `prompt-run-modes` capability entirely instead of replacing it with another shared interface spec.

## Scope

The proposal changes:

- `openspec/specs/prompt-run-modes/spec.md` by retiring it
- `openspec/specs/act-udt-platforms-prompt/spec.md`
- `openspec/specs/act-udt-platform-comparison-prompt/spec.md`

It also implies live prompt changes under `act/` and verification updates in prompt-status materials.

## Save Convention

The follow-up implementation should use one canonical observe filename pattern for act prompts:

- `observe/<thread>/<model-short>.md`

That keeps the saved artifact tied to the prompt/thread and model, without encoding interface mode.

## Verification Consequences

Prompt verification should stop expecting:

- a CLI-or-Web question
- a two-mode behavior section
- `cli-` / `web-` filename prefixes

It should still expect:

- a `## Required Inputs` section where applicable
- alignment with the governing act-prompt spec
