# Spec Delta: act-udt-platform-comparison-prompt

## Change Type

Modify capability

## Requirements

### Requirement: Comparison prompt declares required inputs

The prompt SHALL include a `## Required Inputs` section listing:

- `plan/udt-platform-comparison/rubrics.md`
- `plan/udt-platform-comparison/platforms.md`
- `plan/udt-platform-comparison/source-policy.md`

### Requirement: Comparison prompt executes through one governed path

The prompt SHALL not ask the user to choose between CLI and Web modes.
The prompt SHALL execute through one direct path and save the response to:

- `observe/udt-platform-comparison/<model-short>.md`
