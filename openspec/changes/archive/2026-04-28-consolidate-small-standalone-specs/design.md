# Design: consolidate-small-standalone-specs

## Summary

Consolidate the smallest low-value standalone specs into adjacent capabilities that already own the same behavior.

## Consolidation Principles

A small spec should remain standalone when it has at least one of these properties:

- it is a genuinely shared contract across multiple prompts or workflows
- it governs top-level repository structure
- it defines a concept that can evolve independently
- it provides a stable reference point that would otherwise be duplicated

A small spec should be merged when most of the following are true:

- it only governs one file or one narrow rule
- that rule is already semantically owned by another nearby capability
- it does not create a meaningful reuse boundary
- its future evolution is likely to stay coupled to the neighboring spec

## Keep As Standalone

### `prompt-markdown-format`

Small, but still a real shared contract across multiple live prompts.

### `ar-folder-layout`

Structural root for the repository layout and phase/thread semantics.

### `calibration-archive`

Distinct archival model that can evolve separately from top-level folder layout.

### `act-check-prompts-status`

Operational maintenance capability rather than a narrow sub-rule of another spec.

### `plan-udt-platform-comparison-platforms`

Owns the selected-platform boundary and DTCC inclusion rule, which are more than a trivial file-existence check.

## Retire And Merge

### `plan-udt-platform-comparison-rubrics`

This spec currently says only that the file exists and contains the 12 rubrics used by the comparison prompt.
That is better owned by `act-udt-platform-comparison-prompt`, because the prompt is the thing that consumes and operationalizes those rubrics.

### `udt-platform-comparison-cycle`

This spec currently adds one short platform-only handoff rule that already belongs with the comparison prompt contract.
That rule should live in `act-udt-platform-comparison-prompt`.

### `plan-udt-platforms-scope`

This spec currently restates the scope-table contract for the same thread already governed by `udt-platforms-cycle`.
The `Type` table and the “initiatives are separate” note belong naturally in `udt-platforms-cycle`.

## Outcome

After consolidation, the baseline spec set becomes smaller without losing important boundaries.
The surviving capability boundaries reflect:

- shared prompt contracts
- thread-level workflow contracts
- structural repository contracts
- maintenance and archival contracts
