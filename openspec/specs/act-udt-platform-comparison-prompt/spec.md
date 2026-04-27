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

### Requirement: Comparison prompt supports CLI and Web run modes

In CLI mode the AI reads all three required inputs and saves the response to `observe/udt-platform-comparison/cli-<model-short>.md`.
In Web mode the AI inlines the required inputs and the researcher saves the response to `observe/udt-platform-comparison/web-<model-short>.md`.
