## MODIFIED Requirements

### Requirement: Report platform discovery prompt synthesizes platform ecosystem

The repository SHALL contain `act/report-platform-discovery.md`.

The prompt SHALL conform to `repo-act-prompt-manifest`.

The prompt SHALL declare `act-report-platform-discovery-prompt` as a required prompt behavior contract.

The prompt SHALL scan `observe/platform-discovery-*.md` files without requiring manual path input.

The prompt SHALL treat as qualifying only files whose YAML block contains `prompt: platform-discovery`.

The prompt SHALL write its output to `reflect/platform-ecosystem.md`.

The prompt SHALL instruct the model to write output conforming to `reflect-platform-ecosystem`.

The live `act/report-platform-discovery.md` prompt body SHALL avoid duplicating behavior supplied by required contracts.

#### Scenario: Researcher runs platform discovery reporting

- **WHEN** a researcher runs `act/report-platform-discovery.md`
- **THEN** the prompt conforms to the shared act manifest contract
- **THEN** the prompt incorporates the reporting prompt behavior contract
- **THEN** the prompt scans platform discovery observations
- **THEN** it writes the ecosystem summary under `reflect/`
- **THEN** the written synthesis follows `reflect-platform-ecosystem`
