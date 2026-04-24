## Why

The repository explains its workflow in prose, but it does not yet have a governed presentation artifact that can be used as a short tutorial. A workflow presentation should stay aligned with the repository's method and specs, not drift into a separate slide deck that must be maintained by hand.

## What Changes

- Add a workflow-presentation capability governed by one baseline spec.
- Add a workflow presentation area under `workflow/presentation/`.
- Define a runnable CLI prompt that generates a short tutorial deck at `workflow/presentation/deck.md`.
- Define the deck as a Pandoc-ready Markdown presentation source that explains the repository workflow and stays aligned with the current specs.

## Capabilities

### New Capabilities

- `workflow-presentation`: governs the workflow presentation generator prompt, the generated deck, and the presentation's required tutorial arc.

### Modified Capabilities

- `ar-folder-layout`: extend the workflow-level folder contract to include `workflow/presentation/` alongside `workflow/prompts-status/`.

## Impact

- New workflow-level folder: `workflow/presentation/`
- New baseline spec: `openspec/specs/workflow-presentation/spec.md`
- Updated folder-layout contract in `openspec/specs/ar-folder-layout/spec.md`
- New generated artifact intended for Pandoc conversion, without changing the research-cycle prompts or outputs
