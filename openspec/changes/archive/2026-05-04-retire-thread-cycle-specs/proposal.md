## Why

The repository now uses flattened `plan/` and `act/` entrypoints, and README defines the cycle as the repeated `PLAN -> ACT -> OBSERVE -> REFLECT` loop rather than a per-thread object. The remaining `udt-platforms-cycle` and `udt-initiatives-cycle` specs preserve useful contracts, but their names now conflict with the repository model and duplicate file-specific prompt/scope governance.

## What Changes

- Retire `udt-platforms-cycle` as an active capability.
- Retire `udt-initiatives-cycle` as an active capability.
- Introduce `plan-udt-platforms-scope` to govern `plan/udt-platforms-scope.md`.
- Introduce `plan-udt-initiatives-scope` to govern `plan/udt-initiatives-scope.md`.
- Keep output-format and save-path behavior under the existing act prompt specs.
- Preserve the broad-discovery semantics and platform/initiative boundary by moving them into the relevant file-specific specs.

## Capabilities

### New Capabilities

- `plan-udt-platforms-scope`: Governs the flattened `plan/udt-platforms-scope.md` classification input.
- `plan-udt-initiatives-scope`: Governs the flattened `plan/udt-initiatives-scope.md` initiative mapping input.

### Modified Capabilities

- `act-udt-platforms-prompt`: Keep prompt-level output, Type, and comparison-handoff requirements as the canonical output contract for `udt-platforms`.
- `act-udt-initiatives-prompt`: Keep prompt-level initiative table and `Uses = ?` requirements as the canonical output contract for `udt-initiatives`.
- `udt-platforms-cycle`: Retire because the thread contract is now split across file-specific scope and act prompt specs.
- `udt-initiatives-cycle`: Retire because the thread contract is now split across file-specific scope and act prompt specs.

## Impact

- Affected specs only; no prompt behavior or research output schema changes are intended.
- Active specs become aligned with the flattened entrypoint model.
- `openspec validate --all --strict` should have fewer failures because `udt-initiatives-cycle` is removed and the new scope specs include scenarios.
