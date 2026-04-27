# Spec: prompt-run-modes

## Purpose

Defines the shared run-modes contract for prompt files — the `## Required Inputs` declaration section, the CLI-or-Web mode ask, the per-mode behaviors, and the response filename prefix convention.

## Requirements

### Requirement: Run-modes prompts declare a Required Inputs section

Each run-modes-compliant prompt file SHALL include a `## Required Inputs` section naming the complete set of input files it needs.

This contract applies to:

- `act/udt-platforms/prompt.md`
- `act/udt-platform-comparison/prompt.md`

### Requirement: Run-modes prompts instruct the AI to ask the user which mode to run

Each run-modes-compliant prompt SHALL instruct the AI to ask:

> Run as CLI or Web?

In CLI mode the AI reads all declared input files and saves the response to `observe/<cycle>/cli-<model-short>.md`.
In Web mode the AI emits a fully resolved prompt and the researcher saves the response to `observe/<cycle>/web-<model-short>.md`.

### Requirement: Response filenames carry an interface prefix

Response files saved under `observe/<cycle>/` SHALL be named with either:

- `cli-<model-short>.md`
- `web-<model-short>.md`

### Requirement: Run-modes contract applies only to act/ prompts

Reflect-phase prompts do not declare run modes and execute directly in CLI mode.
