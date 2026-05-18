## 1. Phase-Aligned Spec Renames

- [x] 1.1 Add `openspec/specs/plan-entity-definition/spec.md` from the current entity definition requirements.
- [x] 1.2 Add `openspec/specs/act-entity-discovery/spec.md` from the current entity discovery action requirements and coverage requirements.
- [x] 1.3 Remove `openspec/specs/entity-definition/spec.md`.
- [x] 1.4 Remove `openspec/specs/act-discover-entities-prompt/spec.md`.
- [x] 1.5 Remove `openspec/specs/platform-discovery-coverage/spec.md` after coverage behavior is merged.

## 2. References

- [x] 2.1 Update `act/discover-entities.md` required contracts to use `act-entity-discovery` and `plan-entity-definition`.
- [x] 2.2 Update active specs that reference `entity-definition`, `act-discover-entities-prompt`, or `platform-discovery-coverage`.
- [x] 2.3 Update README and workflow docs to list phase-object-role spec names.

## 3. Naming Convention

- [x] 3.1 Update `openspec/specs/repo-naming-conventions/spec.md` with `<phase>-<object>-<artifact-role>` grammar.
- [x] 3.2 Update `openspec/specs/repo-readme/spec.md` to require the README to document the convention.
- [x] 3.3 Clarify that live `act/` filenames may remain verb-first while OpenSpec capability names use phase-object-role grammar.

## 4. Verification

- [x] 4.1 Search active files for retired names and migrate remaining active references.
- [x] 4.2 Run `openspec validate align-spec-names-with-research-phases --strict`.
- [x] 4.3 Run `openspec validate --all --strict`.
