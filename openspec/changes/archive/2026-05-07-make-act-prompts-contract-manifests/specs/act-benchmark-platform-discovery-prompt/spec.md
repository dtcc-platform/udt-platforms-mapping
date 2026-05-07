## MODIFIED Requirements

### Requirement: Benchmark platform discovery prompt checks discovery recall

The repository SHALL contain `act/benchmark-platform-discovery.md`.

The prompt SHALL conform to `repo-act-prompt-manifest`.

The prompt SHALL declare `act-benchmark-platform-discovery-prompt` as a required prompt behavior contract.

The prompt SHALL scan `observe/platform-discovery-*.md` files and write `observe/platform-discovery-coverage.md`.

The prompt SHALL read expected artifacts from `plan/platform-discovery-benchmark.md`.

The prompt SHALL instruct the model to write coverage output conforming to `observe-platform-discovery-coverage`.

The live `act/benchmark-platform-discovery.md` prompt body SHALL avoid duplicating behavior supplied by required contracts.

#### Scenario: Researcher runs platform discovery benchmark

- **WHEN** a researcher runs `act/benchmark-platform-discovery.md`
- **THEN** the prompt conforms to the shared act manifest contract
- **THEN** the prompt incorporates the benchmark prompt behavior contract
- **THEN** the prompt reads platform discovery observations and benchmark fixture
- **THEN** it writes coverage to `observe/platform-discovery-coverage.md`
- **THEN** the written coverage follows `observe-platform-discovery-coverage`
