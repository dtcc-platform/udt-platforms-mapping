## Why

OpenSpec is now scoped to research workflow contracts, but the remaining `repo-*` capabilities still frame research behavior as generic repository governance. Renaming the useful contracts and folding prompt review into the workflow structure removes that mismatch.

## What Changes

- Rename `repo-naming-conventions` to `research-artifact-naming`.
- Rename `repo-prompt-markdown-format` to `observe-markdown-output-format`.
- Fold `repo-prompt-review` requirements into `research-workflow-structure`.
- Remove `repo-prompt-review` as a standalone capability.
- Update active specs, manifests, and README references to the new names.
- **BREAKING**: old `repo-*` capability names are retired after migration.

## Capabilities

### New Capabilities

- `research-artifact-naming`: Defines researcher-facing naming for live research artifacts and phase-aligned OpenSpec capabilities.
- `observe-markdown-output-format`: Defines portable Markdown formatting for governed observed outputs produced by prompts.

### Modified Capabilities

- `act-entity-discovery`: Update required formatting contract references.
- `act-platform-comparison`: Update required formatting contract references.
- `act-web-prompt-template`: Update required formatting contract references.
- `research-workflow-structure`: Add prompt interpretation review requirements that were previously governed by `repo-prompt-review`.

### Removed Capabilities

- `repo-naming-conventions`: Replaced by `research-artifact-naming`.
- `repo-prompt-markdown-format`: Replaced by `observe-markdown-output-format`.
- `repo-prompt-review`: Folded into `research-workflow-structure`.

## Impact

- Affects OpenSpec capability names and active references.
- Affects `act/discover-entities.md`, `act/compare-platforms.md`, README, and `act/README.md`.
- Does not change research workflow behavior, output structure, or Markdown formatting semantics.
