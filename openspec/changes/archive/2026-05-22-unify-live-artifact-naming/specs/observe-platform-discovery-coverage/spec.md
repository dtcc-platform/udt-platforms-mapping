## MODIFIED Requirements

### Requirement: Platform discovery coverage stores benchmark output

The repository SHALL contain `observe/platform-discovery-coverage.md` as the generated coverage output from `act/platform-discovery-benchmark.md`.

The coverage output SHALL identify the benchmark fixture path and number of tested response files.

The coverage output SHALL include a recall table with artifact, expected type, tags, and one result column per tested model.

The coverage output SHALL include novel finds grouped by model, using the columns `Name`, `Link`, `Type`, `Aliases`, and `Tags`.

The coverage output SHALL include a summary table with model-level found, missing, wrong-type, and novel-find counts.

#### Scenario: Benchmark writes coverage

- **WHEN** `act/platform-discovery-benchmark.md` completes
- **THEN** coverage is saved as `observe/platform-discovery-coverage.md`
- **THEN** the coverage file includes recall, novel-find, and summary sections
