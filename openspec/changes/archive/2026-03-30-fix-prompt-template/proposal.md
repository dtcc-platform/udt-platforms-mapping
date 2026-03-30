## Why

The `prompts/platform-comparison.md` file mixes human-facing usage instructions with the AI prompt body. When a researcher pastes the entire file into a fresh AI session, the model receives the usage instructions (including references to the placeholder token and workflow steps) as part of its context, causing it to misinterpret the prompt as a document to summarise rather than instructions to execute — producing an empty or confused response instead of the comparison report.

## What Changes

- Add a clear cut-line separator between the human-facing usage section and the AI prompt body in `prompts/platform-comparison.md`, so it is unambiguous what should be pasted into an AI session
- Update the usage header instruction to tell researchers to paste only from the cut-line onwards (not the whole file)
- Apply the same separator pattern to `prompts/platform-discovery.md` for consistency

## Capabilities

### New Capabilities

- `prompt-paste-boundary`: A standardised cut-line convention that separates human operator instructions from the AI-facing prompt body within a prompt template file

### Modified Capabilities

- `platform-comparison-prompt`: The usage header instruction is updated to reference the cut-line and direct researchers to paste only the AI prompt section

## Impact

- `prompts/platform-comparison.md` — structural edit to add separator and update usage instruction
- `prompts/platform-discovery.md` — structural edit to add separator and update usage instruction
- `openspec/specs/platform-comparison-prompt/spec.md` — requirement update for the usage header
- `openspec/specs/prompt-paste-boundary/spec.md` — new spec for the cut-line convention
