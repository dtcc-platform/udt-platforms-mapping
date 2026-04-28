# Spec: act-udt-platform-comparison-prompt

## Purpose

Defines the prompt template at `act/udt-platform-comparison/prompt.md` — structure, required inputs, scoring contract, and save-as conventions for comparison sessions.

## Requirements

### Requirement: UDT platform comparison prompt file exists

The repository SHALL contain a file at `act/udt-platform-comparison/prompt.md` that provides a self-contained prompt template for AI-assisted side-by-side comparison of selected UDT platforms.

### Requirement: Comparison prompt is platform-only

The prompt SHALL treat `plan/udt-platform-comparison/platforms.md` as the selected `Type = platform` subset from `udt-platforms`.
The prompt SHALL instruct the model not to broaden the comparison to frameworks or modules.

### Requirement: Comparison prompt declares required inputs

The prompt SHALL include a `## Required Inputs` section listing:

- `plan/udt-platform-comparison/rubrics.md`
- `plan/udt-platform-comparison/platforms.md`
- `plan/udt-platform-comparison/source-policy.md`

The repository SHALL contain a file at `plan/udt-platform-comparison/rubrics.md`.
That file SHALL contain the 12 dimension and functional-category rubrics used by `act/udt-platform-comparison/prompt.md`.

### Requirement: Comparison prompt executes through one governed path

The prompt SHALL instruct the user to use the resolved prompt in a web interface rather than treat CLI execution as the canonical path.
The prompt SHALL resolve all three required inputs into one copy-ready prompt block.
The prompt SHALL instruct the user to save the web response to `observe/udt-platform-comparison/web-<model-short>.md`.

### Requirement: Comparison prompt owns the platform-only handoff rule

Only rows from `udt-platforms` where `Type = platform` SHALL be eligible for `udt-platform-comparison`.
