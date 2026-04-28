# Spec Delta: act-udt-platforms-prompt

## Change Type

Modify capability

## Requirements

### Requirement: UDT platforms prompt is web-canonical

The prompt SHALL instruct the user to use the resolved prompt in a web interface rather than treat CLI execution as the canonical path.

### Requirement: UDT platforms prompt writes web-prefixed outputs

The prompt SHALL instruct the user to save the web response to:

- `observe/udt-platforms/web-<model-short>.md`
