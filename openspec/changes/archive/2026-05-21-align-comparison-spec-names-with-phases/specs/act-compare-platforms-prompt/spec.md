## REMOVED Requirements

### Requirement: Compare platforms prompt is the canonical platform comparison prompt

**Reason**: Replaced by `act-platform-comparison`, which follows phase-object-role naming and includes selected comparison set behavior.

**Migration**: Use `openspec/specs/act-platform-comparison/spec.md`.

#### Scenario: Researcher runs platform comparison

- **WHEN** a researcher resolves `act/compare-platforms.md`
- **THEN** platform comparison action behavior is governed by `act-platform-comparison`
