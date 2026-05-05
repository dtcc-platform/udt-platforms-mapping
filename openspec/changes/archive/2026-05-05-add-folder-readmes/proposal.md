## Why

The flattened phase folders make local navigation simpler, but each folder now needs a short local guide so researchers can understand its contents without relying only on the root README. README requirements are also currently mixed into `repo-structure`, which makes the structure spec responsible for both filesystem layout and documentation behavior.

## What Changes

- Add a dedicated `repo-readme` capability for root and folder-level README contracts.
- Require `README.md` to remain the repository-wide workflow and navigation entrypoint.
- Require `plan/README.md`, `act/README.md`, `observe/README.md`, and `reflect/README.md` to explain the local purpose, artifact types, and naming expectations of each phase folder.
- Move README-specific requirements out of `repo-structure` where they describe documentation rather than physical layout.
- Keep prompt-review workflow behavior in `repo-prompt-review`, while letting `repo-readme` govern where documentation entrypoints explain it.

## Capabilities

### New Capabilities

- `repo-readme`: Governs root and folder-level README documentation entrypoints for the repository workflow.

### Modified Capabilities

- `repo-structure`: Remove README explanation requirements so this capability only governs repository layout and canonical artifact locations.
- `repo-prompt-review`: Clarify that prompt review owns workflow behavior, while README placement is governed by `repo-readme`.

## Impact

- Affected documentation: `README.md`, `plan/README.md`, `act/README.md`, `observe/README.md`, and `reflect/README.md`.
- Affected specs: `repo-structure`, `repo-prompt-review`, and new `repo-readme`.
- No code or dependency changes.
