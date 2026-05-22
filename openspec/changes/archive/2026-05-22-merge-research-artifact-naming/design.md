## Context

`research-artifact-naming` and `research-workflow-structure` are both cross-phase research governance specs. After the recent cleanup, the naming spec is small and only supports the workflow structure contract.

## Goals / Non-Goals

**Goals:**

- Keep one cross-phase research workflow spec.
- Preserve current artifact and capability naming requirements.
- Remove the standalone naming capability and update documentation references.

**Non-Goals:**

- Change the phase-specific naming convention.
- Rename existing active phase-specific specs.
- Change prompt, output, rubric, source-policy, or entity-classification behavior.

## Decisions

1. Fold naming requirements into `research-workflow-structure`.

   Rationale: naming is part of the workflow structure contract, and keeping it in the same spec reduces cross-phase spec count without weakening coverage.

2. Remove `research-artifact-naming` rather than leaving it as an empty or pointer spec.

   Rationale: an empty or redirect-only spec would keep an unnecessary active capability.

## Risks / Trade-offs

- Existing links to `research-artifact-naming` could become stale -> update live documentation references and search for remaining live references before validation.
- A larger workflow structure spec is slightly less narrowly scoped -> keep naming requirements as their own requirement blocks within the merged spec.
