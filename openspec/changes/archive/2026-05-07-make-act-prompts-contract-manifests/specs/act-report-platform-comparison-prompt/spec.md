## MODIFIED Requirements

### Requirement: Report platform comparison prompt exports comparison ecosystem

The repository SHALL contain `act/report-platform-comparison.md`.

The prompt SHALL conform to `repo-act-prompt-manifest`.

The prompt SHALL declare `act-report-platform-comparison-prompt` as a required prompt behavior contract.

The prompt SHALL scan `observe/platform-comparison-*.md` files without requiring manual path input.

The prompt SHALL treat as qualifying only files whose YAML block contains `prompt: platform-comparison`.

The prompt SHALL write `reflect/platform-comparison-ecosystem.csv` and `reflect/platform-comparison-ecosystem-map.html`.

The prompt SHALL instruct the model to write outputs conforming to `reflect-platform-comparison-ecosystem`.

The live `act/report-platform-comparison.md` prompt body SHALL avoid duplicating behavior supplied by required contracts.

#### Scenario: Researcher runs platform comparison reporting

- **WHEN** a researcher runs `act/report-platform-comparison.md`
- **THEN** the prompt conforms to the shared act manifest contract
- **THEN** the prompt incorporates the reporting prompt behavior contract
- **THEN** the prompt scans platform comparison observations
- **THEN** it writes comparison ecosystem outputs under `reflect/`
- **THEN** the written exports follow `reflect-platform-comparison-ecosystem`
