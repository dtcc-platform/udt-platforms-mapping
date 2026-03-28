## 1. Update the discovery prompt output format

- [x] 1.1 Replace the table + paragraph output instructions in `prompts/platform-discovery.md` with the per-platform `##` heading + bullet field structure
- [x] 1.2 Add a concrete example section to the prompt showing the exact field labels and format for one fictional platform
- [x] 1.3 Make the summary table optional — instruct agents to append it after the per-platform sections if useful

## 2. Update the live spec

- [x] 2.1 Apply the delta spec to `openspec/specs/platform-discovery-prompt/spec.md` — replace the existing "structured output aligned with inventory" requirement with the new per-platform section requirement
