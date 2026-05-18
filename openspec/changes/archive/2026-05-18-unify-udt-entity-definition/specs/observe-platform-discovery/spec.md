## REMOVED Requirements

### Requirement: Platform discovery observations use the governed response contract

**Reason**: Platform discovery observations are replaced by unified entity discovery observations.

**Migration**: Save unified discovery responses as `observe/entity-discovery-<model-short>.md` using `observe-entity-discovery`.

#### Scenario: Researcher saves unified discovery output instead

- **WHEN** a researcher saves discovery output for platforms or related UDT candidates
- **THEN** the researcher saves it as `observe/entity-discovery-<model-short>.md`
