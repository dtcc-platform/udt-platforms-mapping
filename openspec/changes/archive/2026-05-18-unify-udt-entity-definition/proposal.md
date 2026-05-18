## Why

Platform and initiative discovery currently maintain separate definition specs even though both are deciding how Urban Digital Twin entities should be represented. This duplicates boundary language and makes maintenance harder when a project, programme, deployment, or technical artifact sits near the platform/initiative boundary.

## What Changes

- Introduce one unified entity definition contract that covers technical artifacts, initiatives, excluded candidates, and the relationship between initiatives and the technical artifacts they use.
- Introduce one canonical entity discovery prompt that replaces separate platform and initiative discovery prompts.
- Introduce one entity discovery output contract with a compact summary table containing only `Name`, `Type`, and `Link`, with `Link` as the last column.
- Move substrate details such as `Uses` and boundary details such as `Reason` into per-entity paragraphs or sections rather than table columns.
- Retire direct use of separate `platform-definition` and `initiative-definition` contracts in favor of the unified definition.
- **BREAKING**: Separate platform and initiative discovery prompts are replaced by one entity discovery prompt.
- **BREAKING**: Discovery output uses the unified entity discovery shape instead of separate platform and initiative discovery table shapes.
- Update repository structure and naming guidance so the unified definition is the canonical behavior contract.

## Capabilities

### New Capabilities

- `entity-definition`: Defines UDT entity kinds, technical artifact type classification, initiative inclusion, excluded boundary behavior, and initiative-to-artifact substrate links.
- `act-discover-entities-prompt`: Defines the canonical unified discovery prompt for UDT entities.
- `observe-entity-discovery`: Defines the saved output contract for unified entity discovery responses.

### Modified Capabilities

- `act-discover-platforms-prompt`: Retire in favor of `act-discover-entities-prompt`.
- `act-discover-initiatives-prompt`: Retire in favor of `act-discover-entities-prompt`.
- `observe-platform-discovery`: Retire in favor of `observe-entity-discovery`.
- `observe-initiative-discovery`: Retire in favor of `observe-entity-discovery`.
- `platform-discovery-coverage`: Use `entity-definition` instead of the retired `platform-definition` for candidate fit and seed-list classification references.
- `act-benchmark-platform-discovery-prompt`: Read unified entity discovery observations for platform recall benchmarking.
- `act-report-platform-discovery-prompt`: Read unified entity discovery observations for platform ecosystem reporting.
- `reflect-platform-ecosystem`: Align synthesized platform ecosystem table shape with unified entity discovery summary columns.
- `repo-structure`: Document `entity-definition` as the canonical entity-definition contract and retire the separate definition specs from active use.
- `repo-naming-conventions`: Prefer the unified definition name for entity-boundary behavior.

## Impact

- Affects `openspec/specs/platform-definition/spec.md` and `openspec/specs/initiative-definition/spec.md`, which will be retired or replaced during implementation.
- Affects `act/discover-platforms.md` and `act/discover-initiatives.md`, which will be replaced or retired by `act/discover-entities.md`.
- Affects saved observation contracts for platform and initiative discovery, which will be replaced by `observe/entity-discovery-<model-short>.md`.
- Does not change comparison, reporting, or benchmark behavior except where they depend on platform discovery Type values.
