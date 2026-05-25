## REMOVED Requirements

### Requirement: Entity discovery benchmark action checks discovery recall

**Reason**: Known candidates are now handled inside the main entity discovery prompt through `plan-entity-discovery-recall-checklist`.

**Migration**: Use `act/entity-discovery.md` with the `plan-entity-discovery-recall-checklist` contract.

### Requirement: Entity discovery benchmark fixture is available

**Reason**: The benchmark fixture is replaced by the OpenSpec recall-checklist contract so each known entity can be tracked as a requirement.

**Migration**: Add known candidates as requirements under `plan-entity-discovery-recall-checklist`.
