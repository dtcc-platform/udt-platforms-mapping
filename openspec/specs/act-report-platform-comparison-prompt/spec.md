# Spec: act-report-platform-comparison-prompt

## Purpose

Defines this researcher-facing canonical artifact.

## Requirements

### Requirement: Report platform comparison prompt exports comparison ecosystem

The repository SHALL contain `act/report-platform-comparison.md`.

The prompt SHALL scan `observe/platform-comparison-*.md` files without requiring manual path input.

The prompt SHALL treat as qualifying only files whose YAML block contains `prompt: platform-comparison`.

The prompt SHALL write `reflect/platform-comparison-ecosystem.csv` and `reflect/platform-comparison-ecosystem-map.html`.

#### Scenario: Researcher runs platform comparison reporting

- **WHEN** a researcher runs `act/report-platform-comparison.md`
- **THEN** the prompt scans platform comparison observations
- **THEN** it writes comparison ecosystem outputs under `reflect/`
