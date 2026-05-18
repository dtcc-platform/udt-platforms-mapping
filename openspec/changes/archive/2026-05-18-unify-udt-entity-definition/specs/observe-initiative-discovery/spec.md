## REMOVED Requirements

### Requirement: Initiative discovery observations use the governed response contract

**Reason**: Initiative discovery observations are replaced by unified entity discovery observations.

**Migration**: Save unified discovery responses as `observe/entity-discovery-<model-short>.md` using `observe-entity-discovery`.

#### Scenario: Researcher saves unified discovery output instead

- **WHEN** a researcher saves discovery output for initiatives or deployments
- **THEN** the researcher saves it as `observe/entity-discovery-<model-short>.md`
