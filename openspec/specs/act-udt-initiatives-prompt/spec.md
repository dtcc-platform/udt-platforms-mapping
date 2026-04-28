# Spec: act-udt-initiatives-prompt

## Purpose

Defines the prompt template at `act/udt-initiatives/prompt.md` — structure, required inputs, output contract, and save-as conventions for the `udt-initiatives` thread.

## Requirements

### Requirement: UDT initiatives prompt file exists

The repository SHALL contain a file at `act/udt-initiatives/prompt.md` that provides a self-contained prompt template for AI-assisted initiative and project mapping of UDT-related efforts.

### Requirement: UDT initiatives prompt declares required inputs

The prompt SHALL include a `## Required Inputs` section listing:

- `plan/udt-initiatives/scope.md`

### Requirement: UDT initiatives prompt uses the initiative table contract

The prompt SHALL instruct the model to return a summary table with exactly these columns:

- `Initiative`
- `Link`
- `Uses`
- `Reason`

The prompt SHALL preserve `Uses = ?` when the technical substrate is unclear.

### Requirement: UDT initiatives prompt is web-canonical

The prompt SHALL resolve `plan/udt-initiatives/scope.md` into one copy-ready prompt block.
The prompt SHALL instruct the user to paste the resolved prompt into a web interface and save the response to `observe/udt-initiatives/web-<model-short>.md`.
