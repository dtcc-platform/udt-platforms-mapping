## Why

Resolved prompts are now generated from `act/` manifests plus OpenSpec contracts, so prompt quality depends on whether agents interpret those contracts consistently. A governed prompt-review workflow is needed to define where resolved prompts and review outputs are stored and how different-agent reviews feed accepted clarifications back into OpenSpec.

## What Changes

- Add a new cross-phase research capability, `research-prompt-review`, for reviewing resolved prompts against their manifests, required contracts, and run inputs.
- Define resolved prompts and prompt-review outputs as `observe/` artifacts, because they are generated snapshots and review observations rather than source manifests.
- Define optional prompt-review synthesis as a `reflect/` artifact.
- Document that `research-*` specs govern cross-phase research workflow/governance, while `plan-*`, `act-*`, `observe-*`, and `reflect-*` specs govern one phase.
- Update root and phase README documentation, including Mermaid diagrams, so the prompt-review loop and storage locations are clear.

## Capabilities

### New Capabilities

- `research-prompt-review`: governs multi-agent review of resolved prompts, storage of resolved prompts and review outputs, and escalation of accepted findings into OpenSpec changes.

### Modified Capabilities

- `research-workflow-structure`: clarify that resolved prompts and prompt-review outputs are observed generated artifacts under `observe/`, and prompt-review synthesis belongs under `reflect/`.

## Impact

- Adds one active spec under `openspec/specs/`.
- Updates root, `act/`, `observe/`, and `reflect/` README documentation.
- Updates the root Mermaid diagrams to show resolved-prompt snapshots, reviewer outputs, optional synthesis, and accepted OpenSpec changes.
- Does not change existing research action prompts, output contracts, scoring, source policy, or saved model response formats.
