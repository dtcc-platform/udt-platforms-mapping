# Spec: reflect-udt-platform-comparison-reporting

## Purpose

Defines the comparison reporting workflow at `reflect/udt-platform-comparison/reporting/`.

## Requirements

### Requirement: Comparison reporting prompt exists

The repository SHALL contain `reflect/udt-platform-comparison/reporting/prompt.md`.

### Requirement: Comparison reporting workflow scans observe/udt-platform-comparison automatically

The prompt SHALL instruct the model to read all relevant files in `observe/udt-platform-comparison/`.

### Requirement: Comparison reporting identifies qualifying files by prompt metadata

The prompt SHALL treat as qualifying only files whose YAML block contains `prompt: udt-platform-comparison`.

### Requirement: Comparison reporting writes ecosystem.csv and ecosystem-map.html

The reporting workflow SHALL write:

- `reflect/udt-platform-comparison/reporting/ecosystem.csv`
- `reflect/udt-platform-comparison/reporting/ecosystem-map.html`
