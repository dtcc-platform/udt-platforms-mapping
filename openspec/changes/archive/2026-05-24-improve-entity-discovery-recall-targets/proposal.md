## Why

The entity discovery recall target still says "candidate artifacts" even though the current entity model includes technical artifacts, initiatives, and excluded boundary candidates. The quota also omits an initiative target, which can cause discovery to under-sample real-world UDT projects and deployments.

This change aligns recall coverage with the unified entity definition while keeping quotas as quality floors rather than stopping conditions.

## What Changes

- Rename the recall floor from "candidate artifacts" to "candidate entities".
- Increase the minimum recall floor from 40 to 50 candidate entities when enough evidence is available.
- Add an explicit initiative target so discovery samples projects, deployments, programmes, and pilots.
- Keep platform, framework, module, and excluded targets as minimum quality gates.
- Add a flexible remainder so discovery can include additional high-relevance entities from any allowed `Type`.
- Preserve the rule that quotas are not stopping conditions and unsupported candidates must not be fabricated.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `act-entity-discovery`: Update broad recall behavior to use candidate entities, include initiative coverage, and raise the minimum recall floor.

## Impact

- Affects `openspec/specs/act-entity-discovery/spec.md`.
- May affect generated entity discovery prompts that inline the act discovery contract.
- No output column, filename, code, dependency, or API changes are expected.
