## Why

Platform discovery currently points to `plan/platform-definition.md` as the authoritative `Type` contract, but the contract does not define enough interpretation rules for borderline artifacts.

Clarifying how to apply the platform definition will make repeated discovery runs more consistent and make prompt review easier across agents.

## What Changes

- Add explicit classification interpretation requirements to the platform definition contract.
- Define how discovery should handle borderline artifacts, ambiguous evidence, and artifacts that resemble more than one `Type`.
- Require the discover-platforms prompt to render those interpretation rules into executable instructions.
- Keep the source of truth in `plan/platform-definition.md`; the prompt remains the operational rendering of that contract.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `plan-platform-definition`: Add requirements for interpreting and applying the platform `Type` classification criteria.
- `act-discover-platforms-prompt`: Require the prompt to operationalize the platform definition interpretation rules when guiding model classification.

## Impact

- Affects `plan/platform-definition.md`.
- Affects `act/discover-platforms.md`.
- Updates baseline specs for `plan-platform-definition` and `act-discover-platforms-prompt` after archive/sync.
- Does not change output file locations or the `observe-platform-discovery` output contract.
