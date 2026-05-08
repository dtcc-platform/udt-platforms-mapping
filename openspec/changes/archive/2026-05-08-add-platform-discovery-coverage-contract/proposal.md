## Why

Recent platform discovery runs can satisfy the current contract with a small representative set because the prompt asks for breadth and recall without defining minimum coverage. This change adds explicit coverage pressure so discovery runs do not stop after examples when more relevant artifacts are discoverable.

## What Changes

- Add a reusable platform discovery coverage contract for candidate count, category quotas, seed-list sampling, and continuation behavior.
- Require the canonical platform discovery prompt to declare and use the new coverage contract.
- Require saved platform discovery outputs to report whether the coverage targets were met or why they were not met.
- Clarify that platform discovery is candidate discovery across `platform`, `framework`, `module`, and useful `excluded` boundary cases, not platform-only filtering.

## Capabilities

### New Capabilities

- `platform-discovery-coverage`: Defines recall coverage targets, category quotas, seed-list sampling requirements, and non-exhaustive stopping rules for platform discovery.

### Modified Capabilities

- `act-discover-platforms-prompt`: Requires the canonical discovery prompt to include the platform discovery coverage contract and render it into executable model instructions.
- `observe-platform-discovery`: Requires saved discovery outputs to include a compact coverage statement before the summary table.

## Impact

- Affects `act/discover-platforms.md` resolution through its required contract manifest.
- Affects `openspec/specs/act-discover-platforms-prompt/spec.md`, `openspec/specs/observe-platform-discovery/spec.md`, and the new `openspec/specs/platform-discovery-coverage/spec.md`.
- No dependency or runtime code changes.
