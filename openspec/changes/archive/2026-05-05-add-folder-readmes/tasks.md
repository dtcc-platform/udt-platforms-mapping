## 1. Specs

- [x] 1.1 Add baseline `repo-readme` spec from the accepted delta.
- [x] 1.2 Remove README explanation requirements from baseline `repo-structure`.
- [x] 1.3 Update baseline `repo-prompt-review` to reference `repo-readme` for README placement.

## 2. Documentation

- [x] 2.1 Update root `README.md` to identify `repo-readme` as the documentation-entrypoint spec.
- [x] 2.2 Add `plan/README.md` explaining planning inputs and thread-prefixed naming.
- [x] 2.3 Add `act/README.md` explaining canonical prompt templates and OpenSpec governance.
- [x] 2.4 Add `observe/README.md` explaining saved outputs, coverage artifacts, and thread/model filename identifiers.
- [x] 2.5 Add `reflect/README.md` explaining synthesis, reporting, and benchmark-analysis artifacts.

## 3. Verification

- [x] 3.1 Validate the change with `openspec validate add-folder-readmes --strict`.
- [x] 3.2 Validate all specs with `openspec validate --all --strict`.
