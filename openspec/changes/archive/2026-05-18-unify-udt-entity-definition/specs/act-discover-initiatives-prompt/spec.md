## REMOVED Requirements

### Requirement: Discover initiatives prompt is the canonical initiative discovery prompt

**Reason**: Initiative discovery is replaced by unified entity discovery so initiatives and their technical substrates are discovered through one prompt.

**Migration**: Use `act-discover-entities-prompt` and `act/discover-entities.md`.

#### Scenario: Researcher runs unified discovery instead

- **WHEN** a researcher needs to discover UDT initiatives or deployments
- **THEN** the researcher uses `act/discover-entities.md`
