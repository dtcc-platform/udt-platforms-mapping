## REMOVED Requirements

### Requirement: Initiative definition is the canonical initiative discovery planning contract

**Reason**: Initiative discovery behavior now belongs in the `initiative-definition` behavior spec. `plan/` is reserved for run inputs, not stable behavior contracts.

**Migration**: Use `openspec/specs/initiative-definition/spec.md` for initiative discovery behavior. Use `plan/` only for run-specific initiative discovery inputs if needed.
