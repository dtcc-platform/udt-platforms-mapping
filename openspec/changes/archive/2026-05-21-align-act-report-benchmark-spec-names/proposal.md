## Why

Three action capabilities still carry the old `-prompt` suffix even though the repository naming convention now uses phase-object-role names for OpenSpec capabilities. Renaming them completes the active act-spec cleanup without changing live `act/` manifest filenames.

## What Changes

- Rename `act-benchmark-platform-comparison-prompt` to `act-platform-comparison-benchmark`.
- Rename `act-report-platform-comparison-prompt` to `act-platform-comparison-report`.
- Rename `act-report-platform-discovery-prompt` to `act-platform-discovery-report`.
- Update live act manifests and active specs/docs that reference the old capability names.
- Update naming guidance with reporting and benchmarking examples.
- **BREAKING**: old `-prompt` capability names are retired after migration.

## Capabilities

### New Capabilities

- `act-platform-comparison-benchmark`: Defines the platform comparison benchmarking action stub.
- `act-platform-comparison-report`: Defines the platform comparison reporting action and reflect export behavior.
- `act-platform-discovery-report`: Defines the platform discovery reporting action and reflect synthesis behavior.

### Modified Capabilities

- `repo-naming-conventions`: Add examples for the renamed act reporting and benchmarking capabilities.
- `repo-readme`: Update formal spec links if the old act report or benchmark capability names are listed.

### Removed Capabilities

- `act-benchmark-platform-comparison-prompt`: Replaced by `act-platform-comparison-benchmark`.
- `act-report-platform-comparison-prompt`: Replaced by `act-platform-comparison-report`.
- `act-report-platform-discovery-prompt`: Replaced by `act-platform-discovery-report`.

## Impact

- Affects OpenSpec capability names, required-contract references, and active documentation links.
- Affects `act/benchmark-platform-comparison.md`, `act/report-platform-comparison.md`, and `act/report-platform-discovery.md` contract paths.
- Does not rename live `act/` files.
- Does not change reporting, benchmarking, reflect output, or prompt manifest behavior.
