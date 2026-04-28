# Spec Delta: act-udt-platform-comparison-prompt

## Change Type

Modify capability

## Requirements

### Requirement: Comparison prompt is web-canonical

The prompt SHALL instruct the user to use the resolved prompt in a web interface rather than treat CLI execution as the canonical path.

### Requirement: Comparison prompt writes web-prefixed outputs

The prompt SHALL instruct the user to save the web response to:

- `observe/udt-platform-comparison/web-<model-short>.md`
