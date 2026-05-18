## 1. Definition Migration

- [x] 1.1 Add `openspec/specs/entity-definition/spec.md` with unified entity kind, Type, initiative, artifact, exclusion, tie-break, and uncertainty requirements.
- [x] 1.2 Remove or retire active `openspec/specs/platform-definition/spec.md` and `openspec/specs/initiative-definition/spec.md` after their consumers are migrated.

## 2. Prompt Contract Updates

- [x] 2.1 Add `openspec/specs/act-discover-entities-prompt/spec.md` as the canonical unified discovery prompt contract.
- [x] 2.2 Add `act/discover-entities.md` to inline `entity-definition`, `act-discover-entities-prompt`, `observe-entity-discovery`, and formatting contracts.
- [x] 2.3 Retire `openspec/specs/act-discover-platforms-prompt/spec.md` and `openspec/specs/act-discover-initiatives-prompt/spec.md`.
- [x] 2.4 Retire or remove `act/discover-platforms.md` and `act/discover-initiatives.md` after `act/discover-entities.md` is active.

## 3. Output Contract Updates

- [x] 3.1 Add `openspec/specs/observe-entity-discovery/spec.md` with a summary table ordered as `Name`, `Type`, `Link`.
- [x] 3.2 Ensure `Uses`, `Reason`, descriptions, and uncertainty details are reported in per-entity sections instead of table columns.
- [x] 3.3 Retire `openspec/specs/observe-platform-discovery/spec.md` and `openspec/specs/observe-initiative-discovery/spec.md`.
- [x] 3.4 Review platform discovery coverage and reporting specs for assumptions that `Type` only has four values, and update if needed.

## 4. Repository Guidance

- [x] 4.1 Update `openspec/specs/repo-structure/spec.md` and related README guidance so `entity-definition`, `act/discover-entities.md`, and `observe/entity-discovery-<model-short>.md` are canonical.
- [x] 4.2 Update `openspec/specs/repo-naming-conventions/spec.md` to document the merged definition name.
- [x] 4.3 Search the repository for `platform-definition`, `initiative-definition`, `discover-platforms`, and `discover-initiatives` references and migrate active discovery references to the unified entity workflow.

## 5. Verification

- [x] 5.1 Run OpenSpec validation for `unify-udt-entity-definition`.
- [x] 5.2 Confirm no active prompt contract still requires the retired definition specs or retired discovery prompts.
- [x] 5.3 Review generated diffs for unrelated changes before archiving or applying.
