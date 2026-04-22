## MODIFIED Requirements

### Requirement: reflect/discovery/benchmarking/benchmark.md exists as the recall benchmark

The repository SHALL contain a file at `reflect/discovery/benchmarking/benchmark.md`. This file is the canonical recall benchmark for discovery sessions — it lists platforms that are expected to appear in discovery responses but are at risk of being missed.

The file SHALL contain a single flat table with columns: `Name`, `Link`, `Layer`, `Aliases`, `Tags`. Rows are ordered by tag (baseline first, then government-led, niche-commercial, no-dt-framing, niche-oss). There SHALL NOT be per-tag section headings.

The file SHALL NOT define scoring rubrics, discovery instructions, or Layer criteria — those belong in `plan/discovery/scope.md`.

#### Scenario: Researcher adds a newly discovered missed platform

- **WHEN** a researcher notices that a known in-scope platform did not appear in any model's discovery response
- **THEN** they add a row to `reflect/discovery/benchmarking/benchmark.md`

#### Scenario: Eval prompt reads the fixture

- **WHEN** the eval prompt runs
- **THEN** it reads `reflect/discovery/benchmarking/benchmark.md` and extracts all expected platforms with their Tags, expected Layer, and Aliases

## REMOVED Requirements

### Requirement: evals/discovery/reports/ directory exists for generated coverage reports

**Reason:** The AR restructure eliminates the `evals/` folder and the nested `reports/` subdirectory. Coverage reports now live directly at `reflect/discovery/benchmarking/coverage.md`.

**Migration:** Coverage report is now at `reflect/discovery/benchmarking/coverage.md`. No subdirectory is used.
