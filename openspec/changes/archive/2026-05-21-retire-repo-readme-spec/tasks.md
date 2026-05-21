## 1. Spec Retirement

- [x] 1.1 Remove `openspec/specs/repo-readme/spec.md`.
- [x] 1.2 Update `research-workflow-structure` to state phase README files are documentation aids and not canonical research artifacts.
- [x] 1.3 Update `repo-prompt-review` to remove dependency on `repo-readme`.

## 2. Active References

- [x] 2.1 Remove `repo-readme` from the root README specs list.
- [x] 2.2 Update phase README references that point to `repo-readme`.
- [x] 2.3 Search active files for `repo-readme` references and migrate or remove remaining active references.

## 3. Verification

- [x] 3.1 Run `openspec validate retire-repo-readme-spec --strict`.
- [x] 3.2 Run `openspec validate --all --strict`.
