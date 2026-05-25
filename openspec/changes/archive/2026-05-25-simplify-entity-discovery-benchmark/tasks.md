## 1. Simplify Fixture

- [x] 1.1 Remove the benchmark tag legend and `Tags` column from `plan/entity-discovery-benchmark.md`.
- [x] 1.2 Remove broad baseline entries and keep only accepted benchmark cases that add recall-check value.

## 2. Update Contracts And Report Shape

- [x] 2.1 Update `act-entity-discovery-benchmark` to read `Name`, `Link`, `Type`, and `Aliases`.
- [x] 2.2 Update `observe-entity-discovery-benchmark-report` to omit `Tags` in recall and novel-find tables.
- [x] 2.3 Update the saved benchmark report to match the simplified shape.

## 3. Verify

- [x] 3.1 Search for stale benchmark `Tags` requirements.
- [x] 3.2 Run OpenSpec validation.
- [x] 3.3 Confirm unrelated dirty files remain unstaged.
