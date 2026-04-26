## Why

The shared Markdown-format spec still describes a generic `prompts/` layout that no longer matches the live repository. The contract is still useful, but its wording is stale and no longer names the governed prompt set clearly.

## What Changes

- Realign `prompt-markdown-format` with the current repository structure.
- Make the spec describe the shared Markdown contract as applying to governed prompt templates in the live repo rather than to a generic `prompts/` directory.
- Clarify that the contract is shared across prompts such as `act/discovery/prompt.md` and `act/rating/prompt.md`.
- Keep the shared portable Markdown behavior itself unchanged unless a current prompt contract requires a wording adjustment.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `prompt-markdown-format`: Update the requirement wording so the shared Markdown contract matches the current governed prompt set and repository paths.

## Impact

- Affects the baseline wording of the shared Markdown-format contract.
- May affect prompt-status interpretation because the shared contract is one of its freshness dependencies.
- Does not require a structural repo redesign by itself.
