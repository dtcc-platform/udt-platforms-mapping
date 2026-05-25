## 1. Add Recall Checklist Contract

- [x] 1.1 Add `openspec/specs/plan-entity-discovery-recall-checklist/spec.md` with GeoDatalytics as the first known recall-check entity.
- [x] 1.2 Add the recall checklist contract to `act/entity-discovery.md`.
- [x] 1.3 Document the completeness-versus-blind-benchmark tradeoff in the discovery manifest.

## 2. Update Discovery Output Contract

- [x] 2.1 Update `act-entity-discovery` to require the recall checklist and miss categorization.
- [x] 2.2 Update `observe-entity-discovery` to require `## Known Candidate Recall Check`.
- [x] 2.3 Regenerate `act/entity-discovery-resolved-codex.md` so it includes the new contract.

## 3. Remove Standalone Benchmark Workflow

- [x] 3.1 Delete `plan/entity-discovery-benchmark.md`.
- [x] 3.2 Delete `act/entity-discovery-benchmark.md`.
- [x] 3.3 Delete `observe/entity-discovery-benchmark-report.md`.
- [x] 3.4 Delete `act-entity-discovery-benchmark` and `observe-entity-discovery-benchmark-report` specs.
- [x] 3.5 Update README and phase README references.
- [x] 3.6 Update research workflow structure to remove standalone benchmark action/report assumptions.

## 4. Verify

- [x] 4.1 Search for stale entity discovery benchmark references.
- [x] 4.2 Run OpenSpec validation.
- [x] 4.3 Confirm unrelated dirty files remain unstaged.
