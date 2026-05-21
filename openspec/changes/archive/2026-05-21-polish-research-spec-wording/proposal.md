## Why

Recent OpenSpec cleanup removed generic `repo-*` framing, but a few active docs and specs still use repository-centric, prompt-centric, or vendor-specific wording. Polishing those terms makes the active specs match the research-focused structure.

## What Changes

- Update README wording from "Formal repository contracts" to "Formal research contracts".
- Update `act/README.md` from "OpenSpec prompt specs" to research/action-oriented wording.
- Reword `observe-markdown-output-format` so it describes governed Markdown outputs rather than governed prompts.
- Reword `act-web-prompt-template` to remove "repository" framing.
- Reword prompt interpretation review requirements in `research-workflow-structure` to avoid vendor-specific reviewer names.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `observe-markdown-output-format`: Clarify that the contract governs Markdown outputs.
- `act-web-prompt-template`: Remove repository-centric manifest wording.
- `research-workflow-structure`: Make prompt interpretation review wording agent-neutral.

## Impact

- Affects wording in README, `act/README.md`, and active specs.
- Does not change research workflow behavior, prompt contracts, output shapes, or naming contracts.
