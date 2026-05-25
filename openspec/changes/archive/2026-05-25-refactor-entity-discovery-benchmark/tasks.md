## 1. Rename Live Artifacts

- [x] 1.1 Rename the plan benchmark fixture to `plan/entity-discovery-benchmark.md` and update its text.
- [x] 1.2 Rename the act benchmark prompt to `act/entity-discovery-benchmark.md` and update its required contracts and inputs.
- [x] 1.3 Rename the observed benchmark output to `observe/entity-discovery-benchmark-report.md` and update its headings and fixture references.

## 2. Update Contracts And Documentation

- [x] 2.1 Add the new entity benchmark specs and retire the old platform/coverage specs.
- [x] 2.2 Update README and phase README references to the new benchmark names.
- [x] 2.3 Search for stale `platform-discovery-benchmark` and `platform-discovery-coverage` references and update or remove them.

## 3. Verify

- [x] 3.1 Run OpenSpec validation for the change and all specs.
- [x] 3.2 Confirm refactor changes are separated from existing unrelated working-tree files.
