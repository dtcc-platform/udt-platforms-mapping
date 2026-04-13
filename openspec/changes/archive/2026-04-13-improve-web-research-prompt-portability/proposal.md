## Why

The current prompt set works well in AI CLIs and generally works in web chats, but modern Research / Deep Research modes on Claude, ChatGPT, and Gemini tend to introduce their own report structure, citation UI, and planning artifacts. That drift makes it harder to get outputs that conform to this repository's strict Markdown, citation, and save-file contracts.

## What Changes

- Add explicit Research / Deep Research compatibility instructions to the discovery, comparison, and license-analysis prompts.
- Tighten prompt-level rules so web research agents suppress generated plans, executive summaries, product-native citation formats, and extra report sections.
- Clarify that secondary sources may be used only to discover candidates, while final factual claims must still be supported by primary sources.
- Add explicit web-chat usage guidance where prompts are portable to browser-based research tools, while preserving the existing CLI-first workflow for repository-local tasks.
- Add stronger uncertainty and stopping rules so research-mode agents prefer `unknown` / `?` over weakly supported claims or speculative completeness.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `platform-discovery-prompt`: extend the prompt contract to support Research / Deep Research mode without violating the existing three-part output structure.
- `platform-comparison-prompt`: add research-mode guardrails so web-based research tools preserve the selection-table scope and emit only the required comparison structure.
- `license-analysis-prompt`: add research-mode guardrails and stronger source-priority rules so browser-based research tools keep the flat output contract and license-evidence requirements.

## Impact

Affected files are `prompts/platform-discovery.md`, `prompts/platform-comparison.md`, `prompts/license-analysis.md`, and the corresponding specs under `openspec/specs/`. No production code, data files, or external dependencies are required.
