## Why

Two shared act prompt meta-contracts still use `repo-` names even though they govern `act/` prompt manifests and web prompt composition. Renaming them under the `act-` phase keeps OpenSpec capability names consistent with the phase-object-role convention.

## What Changes

- Rename `repo-act-prompt-manifest` to `act-prompt-manifest`.
- Rename `repo-web-prompt-template` to `act-web-prompt-template`.
- Update active specs and docs that reference the old meta-contract names.
- Update naming guidance to state that phase-local structural contracts SHOULD use the phase prefix.
- **BREAKING**: old capability names are retired after migration.

## Capabilities

### New Capabilities

- `act-prompt-manifest`: Defines the shared manifest contract for governed prompt files under `act/`.
- `act-web-prompt-template`: Defines the shared structure for canonical web prompt templates used by act prompts.

### Modified Capabilities

- `act-entity-discovery`: Update required meta-contract references to the new names.
- `act-platform-comparison`: Update required meta-contract references to the new names.
- `act-platform-discovery-benchmark`: Update required meta-contract references to the new names.
- `act-benchmark-platform-comparison-prompt`: Update required meta-contract references to the new names.
- `act-report-platform-comparison-prompt`: Update required meta-contract references to the new names.
- `act-report-platform-discovery-prompt`: Update required meta-contract references to the new names.
- `repo-prompt-markdown-format`: Update references from `repo-web-prompt-template` to `act-web-prompt-template`.
- `repo-readme`: Update README contract references to the new names.
- `repo-naming-conventions`: Add guidance for phase-local structural contracts such as act prompt manifests and act web prompt templates.

### Removed Capabilities

- `repo-act-prompt-manifest`: Replaced by `act-prompt-manifest`.
- `repo-web-prompt-template`: Replaced by `act-web-prompt-template`.

## Impact

- Affects OpenSpec capability names and active Markdown references only.
- Affects README and `act/README.md` links.
- Does not change prompt manifest behavior, web prompt composition behavior, or output contracts.
