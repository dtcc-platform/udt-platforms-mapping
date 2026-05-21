# Spec: act-platform-discovery-report

## Purpose

Defines the prompt execution contract and required output-contract conformance.

## Requirements

### Requirement: Report platform discovery prompt synthesizes platform ecosystem

The repository SHALL contain `act/report-platform-discovery.md`.

The prompt SHALL conform to `act-prompt-manifest`.

The prompt SHALL declare `act-platform-discovery-report` as a required prompt behavior contract.

The prompt SHALL scan `observe/entity-discovery-*.md` files without requiring manual path input.

The prompt SHALL treat as qualifying only files whose YAML block contains `prompt: entity-discovery`.

The prompt SHALL skip files silently when they do not contain a qualifying YAML metadata block.

The prompt SHALL extract summary table rows from each qualifying response.

The prompt SHALL preserve exactly the `Name`, `Type`, and `Link` columns.

The prompt SHALL preserve Markdown links from qualifying response rows.

The prompt SHALL combine all extracted rows into one Markdown table.

The prompt SHALL sort the combined rows deterministically by `Type`, then `Name`, then URL target.

The prompt SHALL write its output to `reflect/platform-ecosystem.md`.

The prompt SHALL instruct the model to write output conforming to `reflect-platform-ecosystem`.

The prompt SHALL overwrite `reflect/platform-ecosystem.md` if it already exists.

The live `act/report-platform-discovery.md` prompt body SHALL avoid duplicating behavior supplied by required contracts.

#### Scenario: Researcher runs platform discovery reporting

- **WHEN** a researcher runs `act/report-platform-discovery.md`
- **THEN** the prompt conforms to the shared act manifest contract
- **THEN** the prompt incorporates the reporting prompt behavior contract
- **THEN** the prompt scans entity discovery observations
- **THEN** it writes the ecosystem summary under `reflect/`
- **THEN** the written synthesis follows `reflect-platform-ecosystem`
