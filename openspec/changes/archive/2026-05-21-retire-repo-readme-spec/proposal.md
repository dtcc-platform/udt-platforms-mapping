## Why

`repo-readme` governs documentation placement and wording rather than research behavior. Retiring it keeps OpenSpec focused on durable research workflow, prompt, output, naming, and review contracts.

## What Changes

- Remove `repo-readme` as a standalone OpenSpec capability.
- Remove active references that present README documentation as governed by `repo-readme`.
- Keep durable phase README/non-canonical documentation expectations in `research-workflow-structure`.
- Keep prompt-review README expectations in `repo-prompt-review`.
- Remove `repo-readme` from the root README specs list.
- **BREAKING**: `repo-readme` is retired after migration.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `research-workflow-structure`: Clarify that phase README files are documentation aids and not canonical research artifacts.
- `repo-prompt-review`: Remove the dependency on `repo-readme` for detailed README placement.

### Removed Capabilities

- `repo-readme`: Retired because README documentation governance is no longer a standalone research contract.

## Impact

- Affects OpenSpec docs/spec references and README links.
- Does not remove root or phase README files.
- Does not change research workflow behavior, prompt contracts, output contracts, or naming rules.
