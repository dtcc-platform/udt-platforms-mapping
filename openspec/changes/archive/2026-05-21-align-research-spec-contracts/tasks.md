## 1. Capability Renames and Retirement

- [x] 1.1 Add `openspec/specs/research-artifact-naming/spec.md`.
- [x] 1.2 Add `openspec/specs/observe-markdown-output-format/spec.md`.
- [x] 1.3 Remove `openspec/specs/repo-naming-conventions/spec.md`.
- [x] 1.4 Remove `openspec/specs/repo-prompt-markdown-format/spec.md`.
- [x] 1.5 Remove `openspec/specs/repo-prompt-review/spec.md`.
- [x] 1.6 Fold prompt interpretation review requirements into `openspec/specs/research-workflow-structure/spec.md`.

## 2. Active References

- [x] 2.1 Update act prompt manifests to reference `observe-markdown-output-format`.
- [x] 2.2 Update act behavior specs to reference `observe-markdown-output-format`.
- [x] 2.3 Update `act-web-prompt-template` formatting references.
- [x] 2.4 Update README and phase README references from old `repo-*` names.
- [x] 2.5 Search active files for retired `repo-*` capability names and migrate remaining active references.

## 3. Verification

- [x] 3.1 Run `openspec validate align-research-spec-contracts --strict`.
- [x] 3.2 Run `openspec validate --all --strict`.
