## REMOVED Requirements

### Requirement: Benchmark platform discovery prompt checks discovery recall

**Reason**: Replaced by `act-platform-discovery-benchmark`, which follows phase-object-role naming and includes benchmark fixture behavior.

**Migration**: Use `openspec/specs/act-platform-discovery-benchmark/spec.md`.

#### Scenario: Researcher runs platform discovery benchmark

- **WHEN** a researcher runs `act/benchmark-platform-discovery.md`
- **THEN** benchmark action behavior is governed by `act-platform-discovery-benchmark`
