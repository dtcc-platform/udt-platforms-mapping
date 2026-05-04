## REMOVED Requirements

### Requirement: UDT platforms thread maps technical artifacts through broad discovery

**Reason**: The active repository model no longer treats individual threads as cycles. The output schema, Type values, broad-discovery framing, and platform-only comparison handoff are governed by `act-udt-platforms-prompt`.

**Migration**: Use `act-udt-platforms-prompt` for prompt/output behavior and `plan-udt-platforms-scope` for the classification input.

### Requirement: UDT platforms thread owns the scope-table contract

**Reason**: The scope-table contract belongs to the file-specific `plan-udt-platforms-scope` capability after flattening `plan/`.

**Migration**: Use `plan-udt-platforms-scope` for `plan/udt-platforms-scope.md`.
