# Spec: reflect-udt-platforms-reporting-prompt

## Purpose

Defines the requirements for `reflect/udt-platforms/reporting/prompt.md`.

## Requirements

### Requirement: Prompt auto-scans observe/udt-platforms

The prompt SHALL instruct the model to read all files in `observe/udt-platforms/` without requiring manual path input.

### Requirement: Prompt identifies qualifying files by udt-platforms YAML metadata

The prompt SHALL treat as qualifying only files whose YAML block contains `prompt: udt-platforms`.

### Requirement: Prompt extracts one consolidated Markdown table

The output file SHALL contain one table only using exactly these columns:

- `Name`
- `Link`
- `Type`
- `Reason`

The prompt SHALL write its output to `reflect/udt-platforms/reporting/ecosystem.md`.
