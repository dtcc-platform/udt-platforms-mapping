## REMOVED Requirements

### Requirement: Platform definition is the canonical platform discovery planning contract

**Reason**: Platform discovery classification behavior now belongs in the `platform-definition` behavior spec. `plan/` is reserved for run inputs, not stable behavior contracts.

**Migration**: Use `openspec/specs/platform-definition/spec.md` for platform classification behavior. Use `plan/` only for run-specific platform discovery inputs if needed.
