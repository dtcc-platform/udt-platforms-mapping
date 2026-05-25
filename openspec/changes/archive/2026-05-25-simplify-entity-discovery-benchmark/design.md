## Context

`plan/entity-discovery-benchmark.md` is an input fixture, not a taxonomy. Its current `Tags` column duplicates diagnostic intent that can be handled through issue discussion or later analysis. The benchmark only needs enough structure to test whether known candidates are found and classified.

## Goals / Non-Goals

**Goals:**

- Keep the benchmark fixture small and easy to maintain.
- Use `Type` as the only classification column.
- Keep aliases for matching.
- Preserve the ability to detect found, missing, wrong-type, and novel candidates.

**Non-Goals:**

- Add benchmark automation.
- Redesign issue triage labels.
- Re-run discovery or regenerate model outputs.

## Decisions

- Remove `Tags` from fixture and report contracts because it is optional diagnostic metadata, not necessary for recall evaluation.
- Keep `Aliases` because matching canonical names alone is brittle.
- Keep only accepted benchmark cases that represent real misses or known at-risk recall checks. Broad baseline candidates can be discovered through the prompt and do not need to inflate the fixture.

## Risks / Trade-offs

- Removing tags reduces stratified analysis by category. Mitigation: reintroduce a clearer diagnostic field later only if reports need it.
- A smaller fixture gives less broad recall coverage. Mitigation: add future accepted missing candidates incrementally.
