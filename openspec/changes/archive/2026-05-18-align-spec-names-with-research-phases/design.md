## Context

The repository has phase folders (`plan/`, `act/`, `observe/`, `reflect/`) and several phase-prefixed specs, but not all specs follow the same grammar. `entity-definition` has no phase prefix, while `platform-discovery-coverage` describes behavior that now belongs to the unified entity discovery action.

The user wants spec names to be consistent with the phases while preserving live prompt filenames such as `act/discover-entities.md`.

## Goals / Non-Goals

**Goals:**

- Establish a consistent OpenSpec capability naming grammar: `<phase>-<object>-<artifact-role>`.
- Rename entity definition to `plan-entity-definition`.
- Rename entity discovery act behavior to `act-entity-discovery`.
- Fold recall coverage behavior into `act-entity-discovery`.
- Document the convention in README and `repo-naming-conventions`.

**Non-Goals:**

- Do not rename live files under `act/`, `plan/`, `observe/`, or `reflect/`.
- Do not rename every existing spec in this change.
- Do not change entity discovery output shape.
- Do not change platform comparison behavior.

## Decisions

- Use phase-object-role naming for OpenSpec capabilities.
  - Rationale: specs are contracts, so phase-first names make contract ownership clear in the same way the workflow folders do.
  - Alternative considered: verb-first act names such as `act-discover-entities`. That matches live prompt files but is less consistent across spec phases.

- Keep live `act/` filenames verb-first.
  - Rationale: live act files are executable prompt manifests, so verb phrases such as `discover-entities.md` remain natural for users.
  - Alternative considered: rename live act files to object-role grammar. That would be more uniform but less action-oriented.

- Merge coverage into `act-entity-discovery`.
  - Rationale: recall targets, seed-list sampling, and anti-early-stop rules govern how the discovery action is performed.
  - Alternative considered: rename coverage to `act-entity-discovery-coverage`. That preserves separation but keeps an extra capability for behavior that is inseparable from discovery execution.

- Leave broader spec cleanup for later.
  - Rationale: this change targets the entity discovery path and the naming convention. Renaming all legacy specs would increase blast radius.
  - Alternative considered: rename every spec to phase-object-role at once. That is cleaner eventually but riskier in one step.

## Risks / Trade-offs

- Mixed old and new names will remain temporarily -> Mitigate by documenting the convention as the forward rule and keeping this change scoped.
- Merging coverage into action behavior makes `act-entity-discovery` larger -> Mitigate by grouping requirements clearly inside the spec.
- Existing references may break if not updated -> Search active files for old capability names during implementation.

## Migration Plan

1. Add `plan-entity-definition` from the current `entity-definition` requirements.
2. Add `act-entity-discovery` from the current act discovery prompt requirements plus coverage requirements.
3. Remove `entity-definition`, `act-discover-entities-prompt`, and `platform-discovery-coverage`.
4. Update `act/discover-entities.md` and active spec references.
5. Update README and `repo-naming-conventions` with the naming convention.
6. Validate OpenSpec.
