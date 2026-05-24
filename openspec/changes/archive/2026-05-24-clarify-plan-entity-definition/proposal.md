## Why

The `plan-entity-definition` spec currently introduces `EntityKind` and `Type` before clearly explaining their relationship, which makes the first requirement hard to understand. It also contains at least one overly specific exclusion scenario, making the baseline spec feel tied to a past example instead of a durable classification rule.

This change clarifies the entity definition contract while preserving the current output `Type` values and the reason `artifact` exists as an internal parent concept.

## What Changes

- Clarify that `artifact` is an internal parent concept for technical UDT artifacts, not a discovery-table output `Type`.
- Center the classification contract on the visible output `Type` values: `platform`, `framework`, `module`, `initiative`, and `excluded`.
- Keep `platform`, `framework`, and `module` grouped under the internal artifact concept to avoid repeated technical-artifact wording.
- Replace product- or example-specific exclusion language with principle-based boundary language for communication, presentation, and narrative mapping tools.
- Clarify that initiatives and technical artifacts should be separated when both are present, with initiative substrate captured separately when known.
- Clarify uncertainty handling so weak evidence is explained in reasons, substrate, or artifact details without adding ad hoc output types.
- Tighten repeated wording in the `plan-entity-definition` requirements and scenarios without changing the intended classification behavior.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `plan-entity-definition`: Clarify entity classification terminology, artifact grouping, exclusion boundaries, initiative/artifact separation, and uncertainty handling while preserving the existing output `Type` values.

## Impact

- Affects `openspec/specs/plan-entity-definition/spec.md`.
- May affect future prompt wording or generated prompt manifests that read this spec, but does not introduce new output columns or allowed `Type` values.
- No code, dependency, or API changes are expected.
