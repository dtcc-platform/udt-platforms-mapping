## REMOVED Requirements

### Requirement: Discover entities prompt is the canonical discovery prompt

**Reason**: Replaced by `act-entity-discovery`, which names the research action contract using phase-object-role grammar and incorporates recall coverage behavior.

**Migration**: Use `openspec/specs/act-entity-discovery/spec.md`.

#### Scenario: Researcher runs entity discovery

- **WHEN** a researcher resolves `act/discover-entities.md`
- **THEN** the act behavior is governed by `act-entity-discovery`
