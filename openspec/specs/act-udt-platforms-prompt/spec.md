# Spec: act-udt-platforms-prompt

## Purpose

Defines the prompt template at `act/udt-platforms/prompt.md` — structure, required inputs, output contract, and save-as conventions for the `udt-platforms` thread.

## Requirements

### Requirement: UDT platforms prompt file exists

The repository SHALL contain a file at `act/udt-platforms/prompt.md` that provides a self-contained prompt template for AI-assisted technical-artifact mapping of UDT platforms.

### Requirement: UDT platforms prompt requests Type classification output only

The prompt SHALL instruct the model to return one `##`-level Markdown section per artifact and to assign exactly one `Type` value:

- `platform`
- `framework`
- `module`
- `excluded`

The summary table SHALL use exactly these columns:

- `Name`
- `Link`
- `Type`
- `Reason`

Only `Type = platform` rows are eligible for later platform comparison.
The prompt SHALL describe `udt-platforms` as a broad global discovery thread and instruct the model to prefer stronger evidence when available without turning the thread into a strict source-policy workflow.

### Requirement: UDT platforms prompt declares plan/udt-platforms/scope.md as a required input

The prompt SHALL include a `## Required Inputs` section listing:

- `plan/udt-platforms/scope.md`

### Requirement: UDT platforms prompt executes through one governed path

The prompt SHALL not ask the user to choose between CLI and Web modes.
The prompt SHALL instruct the AI to read the required inputs, including `plan/udt-platforms/scope.md`, and save the response to `observe/udt-platforms/<model-short>.md`.
