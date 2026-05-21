## MODIFIED Requirements

### Requirement: Platform discovery benchmark action checks discovery recall

The repository SHALL contain `act/benchmark-platform-discovery.md`.

The prompt SHALL conform to `act-prompt-manifest`.

The prompt SHALL declare `act-platform-discovery-benchmark` as a required prompt behavior contract.

The prompt SHALL scan `observe/entity-discovery-*.md` files and write `observe/platform-discovery-coverage.md`.

The prompt SHALL require `plan/platform-discovery-benchmark.md` as the expected artifact fixture.

The prompt SHALL extract expected artifacts from the benchmark fixture table using `Name`, `Link`, expected `Type`, `Aliases`, and `Tags`.

The prompt SHALL parse each entity discovery response's YAML metadata block and use the `model` field as the response label.

The prompt SHALL parse each entity discovery response summary table and collect artifact names and `Type` values from summary rows.

The prompt SHALL match expected artifacts case-insensitively against response artifact names using the canonical `Name` and all `Aliases`.

The prompt SHALL record `✓ found` when a matched response row has the expected `Type`.

The prompt SHALL record `✓ found (Type: <actual value>)` when a matched response row has a different `Type`.

The prompt SHALL record `✗ missing` when no response row matches the expected artifact.

The prompt SHALL collect novel finds from each response file by identifying summary rows that do not match any benchmark entry.

The prompt SHALL instruct the model to write coverage output conforming to `observe-platform-discovery-coverage`.

The prompt SHALL overwrite `observe/platform-discovery-coverage.md` if it already exists.

The live `act/benchmark-platform-discovery.md` prompt body SHALL avoid duplicating behavior supplied by required contracts.

#### Scenario: Researcher runs platform discovery benchmark

- **WHEN** a researcher runs `act/benchmark-platform-discovery.md`
- **THEN** the prompt conforms to the shared act manifest contract
- **THEN** the prompt incorporates the benchmark prompt behavior contract
- **THEN** the prompt reads entity discovery observations and benchmark fixture
- **THEN** it writes coverage to `observe/platform-discovery-coverage.md`
- **THEN** the written coverage follows `observe-platform-discovery-coverage`
