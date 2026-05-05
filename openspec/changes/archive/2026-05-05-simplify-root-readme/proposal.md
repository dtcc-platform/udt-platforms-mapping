## Why

The root README has accumulated methodology, operating instructions, naming policy, diagrams, and future-direction notes now that phase README files and repo-wide specs carry more of the detailed documentation load.

Simplifying it will make the repository easier for researchers to enter while preserving OpenSpec as the formal source of truth.

## What Changes

- Reframe the root README around collaborating with AI agents on Urban Digital Twin platform research.
- Keep the root README as a concise orientation page rather than a detailed contract document.
- Retain the two current diagrams because they communicate the research execution loop and prompt interpretation review clearly.
- Keep future directions, but shorten them to brief notes.
- Keep only a tiny pointer to `openspec/specs/` and the most relevant repo-wide specs.
- Leave phase README files as tactical local folder guides, with only consistency edits if needed.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `repo-readme`: Clarify that the root README should be concise, researcher-facing, diagram-supported, and defer formal contracts to specs and local phase READMEs.

## Impact

- Affects `README.md`.
- May require small wording consistency updates in `plan/README.md`, `act/README.md`, `observe/README.md`, or `reflect/README.md`.
- Updates the `repo-readme` spec to govern the simplified root README shape.
