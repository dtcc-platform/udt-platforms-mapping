## 1. Rename specs governing AR-path files

- [x] 1.1 `git mv openspec/specs/platform-discovery-prompt openspec/specs/act-discovery-prompt`
- [x] 1.2 `git mv openspec/specs/platform-inventory-prompt openspec/specs/reflect-discovery-reporting-prompt`
- [x] 1.3 `git mv openspec/specs/discovery-eval-prompt openspec/specs/reflect-discovery-benchmarking-prompt`
- [x] 1.4 `git mv openspec/specs/discovery-fixtures-file openspec/specs/reflect-discovery-benchmarking-benchmark`
- [x] 1.5 `git mv openspec/specs/discovery-coverage-report openspec/specs/reflect-discovery-benchmarking-coverage`
- [x] 1.6 `git mv openspec/specs/platform-discovery-scope-file openspec/specs/plan-discovery-scope`
- [x] 1.7 `git mv openspec/specs/platform-inventory-csv openspec/specs/reflect-discovery-reporting-ecosystem`
- [x] 1.8 `git mv openspec/specs/platform-comparison-prompt openspec/specs/act-rating-prompt`
- [x] 1.9 `git mv openspec/specs/platform-comparison-scope-file openspec/specs/plan-rating-scope`

## 2. Fix stale paths in the two rating specs

- [x] 2.1 Update `openspec/specs/act-rating-prompt/spec.md` — replace `prompts/platform-comparison.md` with `act/rating/prompt.md`; replace `responses/` with `observe/rating/`; replace `docs/01-comparison-scope.md` with `plan/rating/scope.md`; remove `docs/02-methodology.md` reference
- [x] 2.2 Update `openspec/specs/plan-rating-scope/spec.md` — replace `docs/01-comparison-scope.md` with `plan/rating/scope.md`; replace any `docs/01-scope.md` retirement references with the AR equivalent
