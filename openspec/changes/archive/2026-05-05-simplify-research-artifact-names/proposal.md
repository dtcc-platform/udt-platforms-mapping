## Why

The live repository names still read like internal thread identifiers (`udt-platforms`, `udt-platform-comparison`) even though the repository context already supplies the UDT domain. After flattening the folders, the remaining `udt-*` and "thread" language makes canonical artifacts harder for researchers to scan and understand.

## What Changes

- Replace live canonical artifact filenames with researcher-facing names that describe the artifact's role.
- Retire "thread" as the main live organizing concept and use research objects, research actions, and artifact roles instead.
- Drop the repeated `udt-` prefix from live filenames and prompt identifiers.
- Update prompt save-as conventions, glob patterns, required inputs, README examples, and specs to use the new names.
- Preserve archived OpenSpec history as-is; old names remain understandable as historical names only.

## Capabilities

### New Capabilities

- `plan-platform-definition`: Governs `plan/platform-definition.md`, replacing `plan/udt-platforms-scope.md`.
- `plan-initiative-definition`: Governs `plan/initiative-definition.md`, replacing `plan/udt-initiatives-scope.md`.
- `plan-platform-comparison-set`: Governs `plan/platform-comparison-set.md`, replacing `plan/udt-platform-comparison-platforms.md`.
- `plan-platform-dimensions-scoring`: Governs `plan/platform-dimensions-scoring.md`, replacing `plan/udt-platform-comparison-rubrics.md`.
- `plan-platform-source-policy`: Governs `plan/platform-source-policy.md`, replacing `plan/udt-platform-comparison-source-policy.md`.
- `plan-platform-discovery-benchmark`: Governs `plan/platform-discovery-benchmark.md`, replacing `plan/udt-platforms-benchmark.md`.
- `act-discover-platforms-prompt`: Governs `act/discover-platforms.md`, replacing `act/udt-platforms.md`.
- `act-discover-initiatives-prompt`: Governs `act/discover-initiatives.md`, replacing `act/udt-initiatives.md`.
- `act-compare-platforms-prompt`: Governs `act/compare-platforms.md`, replacing `act/udt-platform-comparison.md`.
- `act-benchmark-platform-discovery-prompt`: Governs `act/benchmark-platform-discovery.md`, replacing `act/udt-platforms-benchmarking.md`.
- `act-report-platform-discovery-prompt`: Governs `act/report-platform-discovery.md`, replacing `act/udt-platforms-reporting.md`.
- `act-benchmark-platform-comparison-prompt`: Governs `act/benchmark-platform-comparison.md`, replacing `act/udt-platform-comparison-benchmarking.md`.
- `act-report-platform-comparison-prompt`: Governs `act/report-platform-comparison.md`, replacing `act/udt-platform-comparison-reporting.md`.
- `observe-platform-discovery-coverage`: Governs `observe/platform-discovery-coverage.md`, replacing `observe/udt-platforms-benchmarking-coverage.md`.
- `reflect-platform-ecosystem`: Governs `reflect/platform-ecosystem.md`, replacing `reflect/udt-platforms-ecosystem.md`.
- `reflect-platform-comparison-ecosystem`: Governs `reflect/platform-comparison-ecosystem.*`, replacing `reflect/udt-platform-comparison-ecosystem.*`.

### Modified Capabilities

- `repo-structure`: Replace thread-prefixed artifact naming with object/action/role naming and update canonical file locations.
- `repo-readme`: Replace thread-centered documentation requirements with researcher-facing object/action/role language and new file examples.
- `repo-naming-conventions`: Define researcher-facing live artifact naming, including dropping `udt-` from live filenames.
- `repo-prompt-markdown-format`: Update example prompt paths to the new canonical prompt names.

## Impact

- Affected live folders: `plan/`, `act/`, `observe/`, `reflect/`.
- Affected docs: root `README.md` and phase folder READMEs.
- Affected specs: repo-wide naming/structure/readme specs plus all artifact-specific specs whose canonical file path changes.
- Affected prompt behavior: required input paths, save-as instructions, YAML `prompt:` values, and glob patterns.
- No external dependencies or runtime code changes.
