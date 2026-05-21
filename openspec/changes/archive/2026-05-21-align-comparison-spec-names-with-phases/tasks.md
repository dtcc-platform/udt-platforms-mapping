## 1. Action Spec Renames

- [x] 1.1 Add `openspec/specs/act-platform-comparison/spec.md`.
- [x] 1.2 Add `openspec/specs/act-platform-discovery-benchmark/spec.md`.
- [x] 1.3 Remove `openspec/specs/act-compare-platforms-prompt/spec.md`.
- [x] 1.4 Remove `openspec/specs/act-benchmark-platform-discovery-prompt/spec.md`.

## 2. Plan Spec Renames

- [x] 2.1 Add `openspec/specs/plan-platform-comparison-rubric/spec.md`.
- [x] 2.2 Add `openspec/specs/plan-platform-source-policy/spec.md`.
- [x] 2.3 Remove `openspec/specs/platform-comparison-rubric/spec.md`.
- [x] 2.4 Remove `openspec/specs/platform-source-policy/spec.md`.

## 3. Run Input Spec Merge

- [x] 3.1 Merge `plan-platform-comparison-set` behavior into `act-platform-comparison`.
- [x] 3.2 Merge `plan-platform-discovery-benchmark` behavior into `act-platform-discovery-benchmark`.
- [x] 3.3 Remove `openspec/specs/plan-platform-comparison-set/spec.md`.
- [x] 3.4 Remove `openspec/specs/plan-platform-discovery-benchmark/spec.md`.

## 4. References and Docs

- [x] 4.1 Update `act/compare-platforms.md` required contracts.
- [x] 4.2 Update `act/benchmark-platform-discovery.md` required contracts.
- [x] 4.3 Update README links and naming examples.
- [x] 4.4 Update `repo-naming-conventions`, `repo-readme`, and `research-workflow-structure` references.

## 5. Verification

- [x] 5.1 Search active files for retired names and migrate remaining active references.
- [x] 5.2 Run `openspec validate align-comparison-spec-names-with-phases --strict`.
- [x] 5.3 Run `openspec validate --all --strict`.
