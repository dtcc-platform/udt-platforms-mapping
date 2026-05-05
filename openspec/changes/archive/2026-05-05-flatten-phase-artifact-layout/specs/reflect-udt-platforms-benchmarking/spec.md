## REMOVED Requirements

### Requirement: UDT platforms benchmarking workflow uses a canonical benchmark fixture

**Reason**: The benchmarking fixture belongs to `plan/` after phase flattening.

**Migration**: Use `plan-udt-platforms-benchmark`.

### Requirement: UDT platforms benchmarking workflow provides a CLI eval prompt

**Reason**: The benchmarking prompt belongs to `act/`, and coverage belongs to `observe/`, after phase flattening.

**Migration**: Use `act-udt-platforms-benchmarking-prompt` and `observe-udt-platforms-benchmarking-coverage`.
