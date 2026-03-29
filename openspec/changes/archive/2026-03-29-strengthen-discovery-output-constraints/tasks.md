## 1. Update Discovery Spec

- [x] 1.1 In `openspec/specs/platform-discovery-prompt/spec.md`, update "Discovery prompt enforces agent-agnostic output structure" — add citation override sentence to the citation format bullet
- [x] 1.2 In `openspec/specs/platform-discovery-prompt/spec.md`, rename "Discovery prompt response ends with a required summary table" → "begins with" and update body and scenarios accordingly
- [x] 1.3 In `openspec/specs/platform-discovery-prompt/spec.md`, update "Discovery prompt uses a parameterized search scope token" — add default scope fallback sentence and scenario

## 2. Update Discovery Prompt

- [x] 2.1 In `prompts/platform-discovery.md`, strengthen the citation format rule in `### Markdown and Formatting Rules` — add the override instruction sentence
- [x] 2.2 In `prompts/platform-discovery.md`, move the summary table instruction to the top of `### Output Format` (before per-platform sections) and update the example output order
- [x] 2.3 In `prompts/platform-discovery.md`, add default scope fallback sentence to the `[SEARCH_SCOPE]` instruction in the prompt body
