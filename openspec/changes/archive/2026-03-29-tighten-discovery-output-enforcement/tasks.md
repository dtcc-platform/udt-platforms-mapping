## 1. Update Discovery Spec

- [x] 1.1 In `openspec/specs/platform-discovery-prompt/spec.md`, tighten the structured-output requirement to require the exact three-part response order and canonical inclusion-criterion values
- [x] 1.2 In `openspec/specs/platform-discovery-prompt/spec.md`, tighten the agent-agnostic formatting requirement to forbid extra headings or trailing sections beyond the required output structure
- [x] 1.3 In `openspec/specs/platform-discovery-prompt/spec.md`, strengthen the primary-source requirement so factual bullet content must use inline links to primary sources and unknown facts remain `?` or unknown

## 2. Update Discovery Prompt

- [x] 2.1 In `prompts/platform-discovery.md`, rewrite `### Output Format` so it says the response contains exactly the metadata block, summary table, and `##` platform sections in that order
- [x] 2.2 In `prompts/platform-discovery.md`, constrain `Inclusion criterion` to the canonical allowed values in both the table and per-platform template
- [x] 2.3 In `prompts/platform-discovery.md`, strengthen the citation/source rules to require inline primary-source links for factual detail sentences and forbid extra `Sources` or `Notes` sections
