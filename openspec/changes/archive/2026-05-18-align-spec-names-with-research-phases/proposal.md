## Why

Spec names should mirror the repository's research phases so contributors can infer where each contract belongs. Current names mix phase-prefixed specs, unprefixed behavior specs, and prompt-centric act names, which makes the spec set harder to scan and maintain.

## What Changes

- Adopt a phase-object-role naming convention for OpenSpec capability names: `<phase>-<object>-<artifact-role>`.
- Document the convention in the root README and `repo-naming-conventions`.
- Rename `entity-definition` to `plan-entity-definition`.
- Rename `act-discover-entities-prompt` to `act-entity-discovery`.
- Merge `platform-discovery-coverage` behavior into `act-entity-discovery`.
- Remove the standalone `platform-discovery-coverage` spec after its requirements move into the act discovery contract.
- Update prompt manifests and cross-spec references to use the renamed capabilities.
- **BREAKING**: `entity-definition`, `act-discover-entities-prompt`, and `platform-discovery-coverage` are no longer active capability names after migration.

## Capabilities

### New Capabilities

- `plan-entity-definition`: Defines planned UDT entity classification behavior for technical artifacts, initiatives, exclusions, and substrate relationships.
- `act-entity-discovery`: Defines the entity discovery action, including prompt execution, discovery scope, recall coverage, seed-list sampling, and anti-early-stop behavior.

### Modified Capabilities

- `repo-naming-conventions`: Add the phase-object-role naming convention for OpenSpec capability names and distinguish it from live file naming.
- `repo-readme`: Document the OpenSpec naming convention in the README contract.
- `research-workflow-structure`: Update canonical definition references from `entity-definition` to `plan-entity-definition`.

### Removed Capabilities

- `entity-definition`: Replaced by `plan-entity-definition`.
- `act-discover-entities-prompt`: Replaced by `act-entity-discovery`.
- `platform-discovery-coverage`: Merged into `act-entity-discovery`.

## Impact

- Affects `openspec/specs/entity-definition/spec.md`, `openspec/specs/act-discover-entities-prompt/spec.md`, and `openspec/specs/platform-discovery-coverage/spec.md`.
- Affects `act/discover-entities.md` required contract references.
- Affects specs that reference `entity-definition`, especially `research-workflow-structure`.
- Affects README and naming guidance only; it does not change the live `act/discover-entities.md` filename.
