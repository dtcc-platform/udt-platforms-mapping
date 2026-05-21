## Why

Comparison and benchmark specs still use older names that do not follow the phase-object-role convention. Some tiny `plan-*` specs only define the existence of run-input files, while the meaningful behavior is in the actions that consume those inputs.

## What Changes

- Rename `act-compare-platforms-prompt` to `act-platform-comparison`.
- Rename `act-benchmark-platform-discovery-prompt` to `act-platform-discovery-benchmark`.
- Rename `platform-comparison-rubric` to `plan-platform-comparison-rubric`.
- Rename `platform-source-policy` to `plan-platform-source-policy`.
- Merge `plan-platform-comparison-set` behavior into `act-platform-comparison`.
- Merge `plan-platform-discovery-benchmark` behavior into `act-platform-discovery-benchmark`.
- Update `act/compare-platforms.md` and `act/benchmark-platform-discovery.md` required contract references.
- Update README spec links and active cross-spec references.
- **BREAKING**: old capability names are retired after migration.

## Capabilities

### New Capabilities

- `act-platform-comparison`: Defines the platform comparison action, including selected comparison set behavior, scoring contract composition, source-policy composition, DTCC reference handling, and output contract conformance.
- `act-platform-discovery-benchmark`: Defines the platform discovery benchmark action, including benchmark fixture consumption and coverage output behavior.
- `plan-platform-comparison-rubric`: Defines planned platform comparison dimensions and scoring behavior.
- `plan-platform-source-policy`: Defines planned acceptable source and citation behavior for platform comparison.

### Modified Capabilities

- `repo-naming-conventions`: Include comparison examples that follow phase-object-role grammar.
- `repo-readme`: Update formal spec links and naming examples where needed.
- `research-workflow-structure`: Update references to renamed act and plan comparison specs if present.

### Removed Capabilities

- `act-compare-platforms-prompt`: Replaced by `act-platform-comparison`.
- `act-benchmark-platform-discovery-prompt`: Replaced by `act-platform-discovery-benchmark`.
- `platform-comparison-rubric`: Replaced by `plan-platform-comparison-rubric`.
- `platform-source-policy`: Replaced by `plan-platform-source-policy`.
- `plan-platform-comparison-set`: Merged into `act-platform-comparison`.
- `plan-platform-discovery-benchmark`: Merged into `act-platform-discovery-benchmark`.

## Impact

- Affects platform comparison and platform discovery benchmark action specs.
- Affects `act/compare-platforms.md` and `act/benchmark-platform-discovery.md`.
- Keeps run-input files `plan/platform-comparison-set.md` and `plan/platform-discovery-benchmark.md`; only their standalone OpenSpec capability specs are removed.
- Does not change observed output contracts or comparison scoring semantics.
