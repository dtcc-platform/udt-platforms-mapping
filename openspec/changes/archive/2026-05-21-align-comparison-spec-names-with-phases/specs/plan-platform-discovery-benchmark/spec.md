## REMOVED Requirements

### Requirement: Platform discovery benchmark contains recall fixture

**Reason**: Benchmark fixture behavior is consumed by and governed in `act-platform-discovery-benchmark`.

**Migration**: Keep `plan/platform-discovery-benchmark.md` as the run input. Use `openspec/specs/act-platform-discovery-benchmark/spec.md` for behavior.

#### Scenario: Researcher opens platform discovery benchmark

- **WHEN** a researcher opens `plan/platform-discovery-benchmark.md`
- **THEN** benchmark fixture behavior is governed by `act-platform-discovery-benchmark`
