## Why

The repository currently governs source quality explicitly only for `udt-platform-comparison`, even though `udt-platforms` and `udt-initiatives` also rely on mixed evidence where weak or promotional sources can distort classification. The paper this repo is starting to mimic uses stricter literature/database rules for review work and broader documentation-plus-validation rules for platform characterization, so the mapping cycles need explicit source policies too.

## What Changes

- Add a governed source-policy input at `plan/udt-platforms/source-policy.md` for technical-artifact mapping.
- Add a governed source-policy input at `plan/udt-initiatives/source-policy.md` for initiative/project mapping.
- Update the `udt-platforms` cycle contract so source-priority rules are part of the canonical workflow rather than implicit prompt judgment.
- Update the `udt-platforms` prompt contract so the source policy becomes a required input.
- Update the `udt-initiatives` cycle contract so initiative mapping is governed by a separate, broader source policy suited to project and deployment evidence.

## Capabilities

### New Capabilities
- `plan-udt-platforms-source-policy`: Defines acceptable evidence types and source-priority rules for the `udt-platforms` mapping cycle.
- `plan-udt-initiatives-source-policy`: Defines acceptable evidence types and source-priority rules for the `udt-initiatives` mapping cycle.

### Modified Capabilities
- `act-udt-platforms-prompt`: The prompt contract will require `plan/udt-platforms/source-policy.md` as a governed input and must instruct the model to follow it.
- `udt-platforms-cycle`: The cycle requirements will explicitly govern source prioritization for technical-artifact mapping.
- `udt-initiatives-cycle`: The cycle requirements will explicitly govern source prioritization for initiative and deployment mapping.
- `ar-folder-layout`: The canonical `plan/` layout will include source-policy files for `udt-platforms` and `udt-initiatives`.

## Impact

- Affected live inputs under `plan/`
- Affected baseline specs for cycle and prompt contracts
- Affected README/workflow expectations only if the active documentation needs to mention the new governed inputs
