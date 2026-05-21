## MODIFIED Requirements

### Requirement: Report platform comparison prompt exports comparison ecosystem

The repository SHALL contain `act/report-platform-comparison.md`.

The prompt SHALL conform to `act-prompt-manifest`.

The prompt SHALL declare `act-report-platform-comparison-prompt` as a required prompt behavior contract.

The prompt SHALL scan `observe/platform-comparison-*.md` files without requiring manual path input.

The prompt SHALL treat as qualifying only files whose YAML block contains `prompt: platform-comparison`.

The prompt SHALL skip files silently when they do not contain a qualifying YAML metadata block.

The prompt SHALL extract each qualifying response's `model` and `date` values from the YAML metadata block.

The prompt SHALL extract the Part 1 scoring table rows from each qualifying response.

The prompt SHALL preserve the governed scoring columns from `observe-platform-comparison`.

The prompt SHALL convert Markdown links to raw URLs in the CSV output.

The prompt SHALL append `Model` and `Date` as final CSV columns.

The prompt SHALL order CSV rows by `Date`, then `Model`, then `Name`, then `Link`.

The prompt SHALL produce a self-contained HTML report that visualizes the same row set used in the CSV.

The prompt SHALL write `reflect/platform-comparison-ecosystem.csv` and `reflect/platform-comparison-ecosystem-map.html`.

The prompt SHALL instruct the model to write outputs conforming to `reflect-platform-comparison-ecosystem`.

The prompt SHALL overwrite both reflect outputs if they already exist.

The live `act/report-platform-comparison.md` prompt body SHALL avoid duplicating behavior supplied by required contracts.

#### Scenario: Researcher runs platform comparison reporting

- **WHEN** a researcher runs `act/report-platform-comparison.md`
- **THEN** the prompt conforms to the shared act manifest contract
- **THEN** the prompt incorporates the reporting prompt behavior contract
- **THEN** the prompt scans platform comparison observations
- **THEN** it writes comparison ecosystem outputs under `reflect/`
- **THEN** the written exports follow `reflect-platform-comparison-ecosystem`
