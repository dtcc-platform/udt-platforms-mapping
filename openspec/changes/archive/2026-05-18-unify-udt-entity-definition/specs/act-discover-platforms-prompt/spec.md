## REMOVED Requirements

### Requirement: Discover platforms prompt is the canonical platform discovery prompt

**Reason**: Platform discovery is replaced by unified entity discovery so technical artifacts, initiatives, and excluded boundary candidates are discovered through one prompt.

**Migration**: Use `act-discover-entities-prompt` and `act/discover-entities.md`.

#### Scenario: Researcher runs unified discovery instead

- **WHEN** a researcher needs to discover UDT platforms or related candidates
- **THEN** the researcher uses `act/discover-entities.md`
