# Spec Delta: act-udt-platforms-prompt

## Change Type

Modify capability

## Requirements

### Requirement: UDT platforms prompt declares required inputs only

The prompt SHALL include a `## Required Inputs` section listing:

- `plan/udt-platforms/scope.md`

### Requirement: UDT platforms prompt executes through one governed path

The prompt SHALL not ask the user to choose between CLI and Web modes.
The prompt SHALL execute through one direct path and save the response to:

- `observe/udt-platforms/<model-short>.md`
