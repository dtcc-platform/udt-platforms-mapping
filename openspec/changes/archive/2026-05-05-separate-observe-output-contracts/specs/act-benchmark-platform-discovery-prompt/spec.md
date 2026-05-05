## MODIFIED Requirements

### Requirement: Benchmark platform discovery prompt checks discovery recall

The repository SHALL contain `act/benchmark-platform-discovery.md`.

The prompt SHALL scan `observe/platform-discovery-*.md` files and write `observe/platform-discovery-coverage.md`.

The prompt SHALL read expected artifacts from `plan/platform-discovery-benchmark.md`.

The prompt SHALL instruct the model to write coverage output conforming to `observe-platform-discovery-coverage`.

#### Scenario: Researcher runs platform discovery benchmark

- **WHEN** a researcher runs `act/benchmark-platform-discovery.md`
- **THEN** the prompt reads platform discovery observations and benchmark fixture
- **THEN** it writes coverage to `observe/platform-discovery-coverage.md`
- **THEN** the written coverage follows `observe-platform-discovery-coverage`
