## 1. Capability Renames

- [x] 1.1 Add `openspec/specs/act-prompt-manifest/spec.md`.
- [x] 1.2 Add `openspec/specs/act-web-prompt-template/spec.md`.
- [x] 1.3 Remove `openspec/specs/repo-act-prompt-manifest/spec.md`.
- [x] 1.4 Remove `openspec/specs/repo-web-prompt-template/spec.md`.

## 2. Active Spec References

- [x] 2.1 Update act behavior specs to reference `act-prompt-manifest`.
- [x] 2.2 Update web prompt specs to reference `act-web-prompt-template`.
- [x] 2.3 Update `repo-prompt-markdown-format` references to `act-web-prompt-template`.
- [x] 2.4 Update `repo-naming-conventions` with phase-local structural contract guidance.

## 3. Docs and Manifests

- [x] 3.1 Update README spec links.
- [x] 3.2 Update `act/README.md` manifest contract link.
- [x] 3.3 Search active files for retired names and migrate remaining active references.

## 4. Verification

- [x] 4.1 Run `openspec validate align-act-prompt-meta-spec-names --strict`.
- [x] 4.2 Run `openspec validate --all --strict`.
