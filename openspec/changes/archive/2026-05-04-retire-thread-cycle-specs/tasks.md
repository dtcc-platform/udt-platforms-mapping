## 1. Fold Contracts Into File-Specific Specs

- [x] 1.1 Add `plan-udt-platforms-scope` baseline spec for `plan/udt-platforms-scope.md`.
- [x] 1.2 Add `plan-udt-initiatives-scope` baseline spec for `plan/udt-initiatives-scope.md`.
- [x] 1.3 Update `act-udt-platforms-prompt` so it explicitly owns technical-artifact output, Type, broad-discovery, and platform-only handoff behavior.
- [x] 1.4 Update `act-udt-initiatives-prompt` so it explicitly owns initiative output, `Uses`, broad-discovery, and artifact-vs-initiative boundary behavior.

## 2. Retire Cycle Specs

- [x] 2.1 Remove active `openspec/specs/udt-platforms-cycle/spec.md`.
- [x] 2.2 Remove active `openspec/specs/udt-initiatives-cycle/spec.md`.
- [x] 2.3 Search current non-archive files for active references to the retired cycle spec names.

## 3. Verify

- [x] 3.1 Validate `retire-thread-cycle-specs` with `openspec validate retire-thread-cycle-specs --strict`.
- [x] 3.2 Validate affected active specs with `openspec validate --all --strict`.
- [x] 3.3 Review git diff to confirm archived OpenSpec changes were not rewritten.
