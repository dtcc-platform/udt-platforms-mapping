## Why

`plan/udt-platforms/scope.md` currently contains both Type classification criteria and an output contract reminder. This blurs the boundary between operational scope input and the governed prompt/output contract, creating avoidable duplication with the OpenSpec specs and the prompt template.

## What Changes

- Remove the output-format reminder from `plan/udt-platforms/scope.md` so the scope file contains only classification guidance and separation from initiatives.
- Keep the normative output contract in OpenSpec, with the prompt spec responsible for the exact prompt-produced format.
- Preserve the existing `udt-platforms` output schema: `Name`, `Link`, `Type`, `Reason`.
- Preserve the existing comparison handoff rule: only `Type = platform` rows are eligible for `udt-platform-comparison`.
- Clarify that `act/udt-platforms/prompt.md` owns the copy-ready output-format instructions for web-model execution.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `udt-platforms-cycle`: clarify that `plan/udt-platforms/scope.md` owns Type classification criteria only and must not carry the output-format reminder.
- `act-udt-platforms-prompt`: clarify that the prompt template owns the concrete output-format instructions used to produce `udt-platforms` web responses.

## Impact

- Affected files:
  - `plan/udt-platforms/scope.md`
  - `act/udt-platforms/prompt.md`
  - `openspec/specs/udt-platforms-cycle/spec.md`
  - `openspec/specs/act-udt-platforms-prompt/spec.md`
- No dependency, runtime, or API changes.
- Existing saved observation files do not need migration.
