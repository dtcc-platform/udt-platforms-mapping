## Context

The repository now uses phase-object-role names for OpenSpec capabilities. Entity discovery has been aligned, but comparison and benchmark specs still use prompt-centric and unprefixed names.

Two tiny plan specs currently govern the existence of run-input files. Their meaningful behavior is action-specific: platform comparison consumes `plan/platform-comparison-set.md`, and platform discovery benchmarking consumes `plan/platform-discovery-benchmark.md`.

## Goals / Non-Goals

**Goals:**

- Align platform comparison and benchmark capability names with phase-object-role grammar.
- Move comparison rubric and source policy under the `plan-` phase.
- Fold run-input usage behavior into the consuming `act-` specs.
- Keep the actual `plan/` run-input files.

**Non-Goals:**

- Do not rename live files under `act/` or `plan/`.
- Do not change comparison scoring dimensions or source policy semantics.
- Do not change observed platform comparison or coverage output contracts.
- Do not rename all remaining legacy act specs in this change.

## Decisions

- Use `act-platform-comparison` for the comparison action spec.
  - Rationale: it follows phase-object-role grammar and avoids prompt-centric naming.
  - Alternative considered: `act-compare-platforms`. That matches the live file but not the spec naming convention.

- Use `act-platform-discovery-benchmark` for the benchmark action spec.
  - Rationale: benchmark behavior is an action and consumes a run-input fixture.
  - Alternative considered: keep `act-benchmark-platform-discovery-prompt`. That preserves history but keeps prompt-centric grammar.

- Rename rubric and source policy to `plan-platform-comparison-rubric` and `plan-platform-source-policy`.
  - Rationale: they are planned rules used by comparison actions.
  - Alternative considered: merge them into `act-platform-comparison`. That would make the action spec too large and reduce reuse.

- Remove standalone specs for `plan-platform-comparison-set` and `plan-platform-discovery-benchmark`.
  - Rationale: these specs only assert that run-input files exist; the behavior belongs in the consuming action specs.
  - Alternative considered: keep them as plan input contracts. That is more explicit but creates low-value spec noise.

## Risks / Trade-offs

- Removing standalone plan input specs reduces direct validation of those input file names -> Mitigate by requiring the files in the consuming act specs.
- Renaming specs may break stale references -> Search active files for old names during implementation.
- Some old names remain in archived changes -> Leave archived history unchanged.

## Migration Plan

1. Add the four new capability specs.
2. Remove the six retired capability specs.
3. Update live act manifests and active specs to reference the new names.
4. Update README and naming guidance examples.
5. Validate OpenSpec.
