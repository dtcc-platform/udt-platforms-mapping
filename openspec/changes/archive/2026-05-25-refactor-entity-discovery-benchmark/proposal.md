## Why

The discovery benchmark workflow still uses old `platform-discovery` and `coverage` names even though the repository now treats discovery as broader entity discovery. This makes it unclear whether `observe/platform-discovery-coverage.md` is a process-coverage artifact or the saved result of a benchmark run.

## What Changes

- Rename the benchmark workflow from platform-specific wording to entity-discovery wording.
- Rename the observed benchmark output from `coverage` to `benchmark-report`.
- Keep coverage as a section/concept inside the benchmark report rather than as the artifact name.
- Remove the old platform-discovery benchmark and coverage contracts after migration.
- Update phase files, specs, and README references to the new names.

## Capabilities

### New Capabilities

- `act-entity-discovery-benchmark`: Defines the action that evaluates saved entity discovery outputs against the benchmark fixture.
- `observe-entity-discovery-benchmark-report`: Defines the saved observed benchmark report shape.

### Modified Capabilities

- `act-platform-discovery-benchmark`: Retires the old platform-specific benchmark action contract.
- `observe-platform-discovery-coverage`: Retires the old platform-specific coverage output contract.
- `research-workflow-structure`: Aligns workflow documentation with the renamed entity discovery benchmark artifacts.

## Impact

- Affected files under `plan/`, `act/`, `observe/`, `openspec/specs/`, and README documentation.
- The old platform benchmark filenames become obsolete and are replaced by entity benchmark names.
