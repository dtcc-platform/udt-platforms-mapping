# Proposal: remove-cli-web-run-mode-option

## Why

The current act-prompt contract asks the user to choose between CLI and Web execution for every run.
That adds branching to the prompt workflow, duplicates save-path conventions, and keeps a shared spec alive for interface handling rather than research behavior.

The repository is already organized around governed prompts and CLI-centered execution.
Removing the CLI/Web mode option simplifies prompt use, reduces prompt boilerplate, and keeps the act prompts focused on one operational path.

## What Changes

- retire the shared `prompt-run-modes` capability
- remove CLI/Web mode branching from:
  - `act/udt-platforms/prompt.md`
  - `act/udt-platform-comparison/prompt.md`
- replace the current dual save-path convention with one canonical save-path convention for act prompts
- update prompt-status expectations so act prompts are no longer expected to implement a run-modes contract

## Impact

- act prompts become simpler and CLI-first
- web-only resolved-prompt generation is no longer part of the governed prompt contract
- `observe/` save naming for act prompts becomes simpler and no longer needs interface prefixes
- prompt verification becomes narrower because one shared contract is removed
