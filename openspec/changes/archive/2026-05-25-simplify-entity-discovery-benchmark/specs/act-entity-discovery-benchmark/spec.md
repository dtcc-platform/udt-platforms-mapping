## MODIFIED Requirements

### Requirement: Entity discovery benchmark action checks discovery recall

The repository SHALL contain `act/entity-discovery-benchmark.md`.

The prompt SHALL conform to `act-prompt-manifest`.

The prompt SHALL declare `act-entity-discovery-benchmark` as a required prompt behavior contract.

The prompt SHALL scan `observe/entity-discovery-*.md` files and write `observe/entity-discovery-benchmark-report.md`.

The prompt SHALL require `plan/entity-discovery-benchmark.md` as the expected entity fixture.

The prompt SHALL extract expected entities from the benchmark fixture table using `Name`, `Link`, expected `Type`, and `Aliases`.

The prompt SHALL parse each entity discovery response's YAML metadata block and use the `model` field as the response label.

The prompt SHALL parse each entity discovery response summary table and collect entity names and `Type` values from summary rows.

The prompt SHALL match expected entities case-insensitively against response entity names using the canonical `Name` and all `Aliases`.

The prompt SHALL record `✓ found` when a matched response row has the expected `Type`.

The prompt SHALL record `✓ found (Type: <actual value>)` when a matched response row has a different `Type`.

The prompt SHALL record `✗ missing` when no response row matches the expected entity.

The prompt SHALL collect novel finds from each response file by identifying summary rows that do not match any benchmark entry.

The prompt SHALL instruct the model to write benchmark output conforming to `observe-entity-discovery-benchmark-report`.

The prompt SHALL overwrite `observe/entity-discovery-benchmark-report.md` if it already exists.

The live `act/entity-discovery-benchmark.md` prompt body SHALL avoid duplicating behavior supplied by required contracts.

#### Scenario: Researcher runs entity discovery benchmark

- **WHEN** a researcher runs `act/entity-discovery-benchmark.md`
- **THEN** the prompt conforms to the shared act manifest contract
- **THEN** the prompt incorporates the benchmark prompt behavior contract
- **THEN** the prompt reads entity discovery observations and benchmark fixture
- **THEN** it writes a benchmark report to `observe/entity-discovery-benchmark-report.md`
- **THEN** the written report follows `observe-entity-discovery-benchmark-report`

### Requirement: Entity discovery benchmark fixture is available

The repository SHALL contain `plan/entity-discovery-benchmark.md` as the benchmark fixture input for entity discovery.

The file SHALL contain the expected entity table used by `act/entity-discovery-benchmark.md`.

The expected entity table SHALL use the columns `Name`, `Link`, `Type`, and `Aliases`.

#### Scenario: Researcher opens entity discovery benchmark

- **WHEN** a researcher opens `plan/entity-discovery-benchmark.md`
- **THEN** the entity discovery benchmark fixture is available
- **THEN** the fixture table exposes `Name`, `Link`, `Type`, and `Aliases`
