## Why

The repository now has one small naming-only cross-phase research spec beside the workflow structure spec. Merging naming into workflow structure keeps the research governance surface minimal while preserving the same naming requirements.

## What Changes

- Move live artifact and OpenSpec capability naming requirements into `research-workflow-structure`.
- **BREAKING**: Remove the standalone `research-artifact-naming` capability.
- Update documentation references so the workflow structure spec is the single cross-phase research governance spec.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `research-workflow-structure`: add the research artifact and capability naming requirements.
- `research-artifact-naming`: remove this standalone capability after its requirements are folded into `research-workflow-structure`.

## Impact

- Updates active OpenSpec specs under `openspec/specs/`.
- Updates README references to remove the retired standalone naming spec.
- Does not change phase-specific research action, output, rubric, or source-policy behavior.
