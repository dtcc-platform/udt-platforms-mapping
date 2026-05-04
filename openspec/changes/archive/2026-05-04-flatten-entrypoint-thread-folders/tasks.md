## 1. Move Entrypoint Files

- [x] 1.1 Move `plan/udt-platforms/scope.md` to `plan/udt-platforms-scope.md`.
- [x] 1.2 Move `plan/udt-initiatives/scope.md` to `plan/udt-initiatives-scope.md`.
- [x] 1.3 Move `plan/udt-platform-comparison/rubrics.md`, `source-policy.md`, and `platforms.md` to flattened `plan/udt-platform-comparison-*.md` filenames.
- [x] 1.4 Move `act/udt-platforms/prompt.md`, `act/udt-initiatives/prompt.md`, and `act/udt-platform-comparison/prompt.md` to flattened `act/*.md` prompt filenames.
- [x] 1.5 Remove now-empty canonical thread folders under `plan/` and `act/` while preserving unrelated direct files such as `act/check-prompts-status.md`.

## 2. Update Current Workflow References

- [x] 2.1 Update README repository model and how-to guidance to describe flattened `plan/` and `act/` entrypoints.
- [x] 2.2 Update canonical act prompt content so required inputs and run instructions reference flattened `plan/*.md` paths.
- [x] 2.3 Update prompt-status maintenance artifacts to reference flattened canonical prompt paths where applicable.
- [x] 2.4 Update active baseline specs for repository structure and the three canonical act prompts to match the accepted flattened paths.

## 3. Verify Migration

- [x] 3.1 Search current non-archive files for retired canonical paths under `plan/<thread>/` and `act/<thread>/prompt.md`.
- [x] 3.2 Confirm `observe/<thread>/` and `reflect/<thread>/` structures remain unchanged.
- [x] 3.3 Run OpenSpec validation for `flatten-entrypoint-thread-folders`.
- [x] 3.4 Review git diff to ensure archived OpenSpec changes were not rewritten.
