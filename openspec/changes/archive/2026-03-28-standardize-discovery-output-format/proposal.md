## Why

Discovery prompt responses vary in structure across AI agents — some write long prose paragraphs, others use flat bullet lists, making it hard to compare results or transfer data to the inventory. A consistent, scannable format (heading per platform, bullet fields) reduces friction for researchers working across multiple agents.

## What Changes

- Add an explicit per-platform section structure to the discovery prompt output format: one `##` heading per platform, followed by a fixed set of bullet-point fields
- Replace the current open-ended "structured output" instruction with a concrete template showing the exact fields and their format
- Ensure the format requirement is agent-agnostic — stated in terms of output structure, not prose style, so it holds across ChatGPT, Claude, Gemini, etc.

## Capabilities

### New Capabilities
<!-- none -->

### Modified Capabilities
- `platform-discovery-prompt`: the requirement for structured output aligned with inventory (currently requires "clearly labelled fields") must be tightened to require a per-platform heading and bullet-point field list, so the format is unambiguous and consistent across agents

## Impact

- `prompts/platform-discovery.md` — output format instruction updated
- `openspec/specs/platform-discovery-prompt/spec.md` — structured output requirement tightened
