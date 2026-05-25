## MODIFIED Requirements

### Requirement: Entity discovery benchmark report stores benchmark output

The repository SHALL contain `observe/entity-discovery-benchmark-report.md` as the generated benchmark output from `act/entity-discovery-benchmark.md`.

The benchmark report SHALL identify the benchmark fixture path and number of tested response files.

The benchmark report SHALL include a recall table with entity, expected type, and one result column per tested model.

The benchmark report SHALL include novel finds grouped by model, using the columns `Name`, `Link`, `Type`, and `Aliases`.

The benchmark report SHALL include a summary table with model-level found, missing, wrong-type, and novel-find counts.

#### Scenario: Benchmark writes report

- **WHEN** `act/entity-discovery-benchmark.md` completes
- **THEN** the benchmark report is saved as `observe/entity-discovery-benchmark-report.md`
- **THEN** the benchmark report includes recall, novel-find, and summary sections
- **THEN** recall and novel-find tables do not require a `Tags` column
