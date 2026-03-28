## 1. Update the discovery prompt

- [x] 1.1 Make the summary table required in `prompts/platform-discovery.md` — remove the "optional" framing and add a **Select** column (empty, for researcher use)

## 2. Update the comparison prompt

- [x] 2.1 Replace `[PLATFORM_A]`, `[PLATFORM_B]`, and `[PASTE_INVENTORY_ROWS_HERE]` in `prompts/platform-comparison.md` with a single `[PASTE_SELECTED_PLATFORMS_HERE]` token
- [x] 2.2 Update the prompt instructions to tell the agent to treat all pasted rows as comparison targets

## 3. Update methodology docs

- [x] 3.1 Add a section to `docs/methodology.md` documenting the discovery → comparison workflow: mark `x` in summary table, copy marked rows, paste into comparison prompt

## 4. Update live specs

- [x] 4.1 Apply the delta spec to `openspec/specs/platform-discovery-prompt/spec.md` — add the required summary table requirement
- [x] 4.2 Apply the delta spec to `openspec/specs/platform-comparison-prompt/spec.md` — replace the two scope input requirements with the single token requirement
