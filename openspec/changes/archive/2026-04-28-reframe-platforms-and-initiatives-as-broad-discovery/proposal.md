## Why

`udt-platforms` and `udt-initiatives` are being used more as broad global discovery threads than as high-confidence characterization stages. The current governed source-policy files make those threads too restrictive for recall-oriented ecosystem scouting, while `udt-platform-comparison` is the place where stricter evidence discipline actually needs to hold.

## What Changes

- Reframe `udt-platforms` as a broad technical-artifact discovery thread optimized for global recall rather than strict evidence filtering.
- Reframe `udt-initiatives` as a broad initiative and deployment discovery thread optimized for recall rather than strict evidence filtering.
- Remove the governed source-policy requirement from `udt-platforms` and `udt-initiatives`.
- Keep the stricter evidence policy for `udt-platform-comparison`.
- Update the affected prompt, folder-layout, and cycle contracts so the first two threads are explicitly broad discovery threads rather than source-policy-governed mapping stages.

## Capabilities

### New Capabilities

### Modified Capabilities
- `act-udt-platforms-prompt`: Remove the governed source-policy input requirement and realign the prompt with broad discovery semantics.
- `ar-folder-layout`: Remove the canonical requirement that `plan/udt-platforms/` and `plan/udt-initiatives/` contain `source-policy.md`.
- `udt-platforms-cycle`: Reframe the cycle as broad technical-artifact discovery and remove the governed source-policy requirement.
- `udt-initiatives-cycle`: Reframe the cycle as broad initiative/deployment discovery and remove the governed source-policy requirement.
- `plan-udt-platforms-source-policy`: Retire this capability because the thread no longer requires a governed source-policy input.
- `plan-udt-initiatives-source-policy`: Retire this capability because the thread no longer requires a governed source-policy input.

## Impact

- Affected live plan files and canonical prompt inputs
- Affected baseline specs for thread and folder-layout behavior
- Affected README wording about discovery breadth versus comparison confidence
