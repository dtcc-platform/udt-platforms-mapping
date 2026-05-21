## REMOVED Requirements

### Requirement: Platform comparison set contains selected comparison candidates

**Reason**: Selected comparison set behavior is consumed by and governed in `act-platform-comparison`.

**Migration**: Keep `plan/platform-comparison-set.md` as the run input. Use `openspec/specs/act-platform-comparison/spec.md` for behavior.

#### Scenario: Researcher opens platform comparison set

- **WHEN** a researcher opens `plan/platform-comparison-set.md`
- **THEN** platform comparison set behavior is governed by `act-platform-comparison`
