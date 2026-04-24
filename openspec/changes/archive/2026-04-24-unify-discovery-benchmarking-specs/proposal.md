## Why

The `reflect/discovery/benchmarking/` folder is currently governed by four separate baseline specs even though it functions as one tightly related benchmarking workflow. That split makes the spec set harder to understand than the folder structure itself.

## What Changes

- Introduce one baseline capability for the whole `reflect/discovery/benchmarking/` folder.
- Fold the benchmark fixture schema, alias semantics, eval prompt behavior, and coverage report structure into that one capability.
- Remove the separate baseline capabilities `reflect-discovery-benchmarking-prompt`, `reflect-discovery-benchmarking-coverage`, `reflect-discovery-benchmarking-benchmark`, and `fixture-alias-column`.
- Update the workflow prompt-status audit to point at the single new benchmarking spec.

## Capabilities

### New Capabilities

- `reflect-discovery-benchmarking`: governs `reflect/discovery/benchmarking/benchmark.md`, `prompt.md`, and `coverage.md` as one folder-level benchmarking workflow contract.

### Modified Capabilities

- `workflow-prompts-status`: update the audit workflow to use the new unified benchmarking capability.
- `reflect-discovery-benchmarking-prompt`: remove this separate capability and fold its requirements into `reflect-discovery-benchmarking`.
- `reflect-discovery-benchmarking-coverage`: remove this separate capability and fold its requirements into `reflect-discovery-benchmarking`.
- `reflect-discovery-benchmarking-benchmark`: remove this separate capability and fold its requirements into `reflect-discovery-benchmarking`.
- `fixture-alias-column`: remove this separate capability and fold its requirements into `reflect-discovery-benchmarking`.

## Impact

- Affected baseline specs under `openspec/specs/`
- Affected live audit prompt and report under `workflow/prompts-status/`
- No change to the runnable eval prompt path or its output path
