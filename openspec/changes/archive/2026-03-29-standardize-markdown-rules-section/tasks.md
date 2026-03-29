## 1. Update Live Spec

- [x] 1.1 In `openspec/specs/license-analysis-prompt/spec.md`, update "License analysis prompt output uses portable Markdown syntax" — add section heading requirement, structured format requirement, and score notation entry

## 2. Update License Prompt

- [x] 2.1 In `prompts/license-analysis.md`, rename `### Markdown Syntax Rules` to `### Markdown and Formatting Rules`
- [x] 2.2 In `prompts/license-analysis.md`, replace the flat bullet list with the structured `**Permitted syntax only:**` / `**Prohibited syntax:**` format matching the discovery and comparison prompts
- [x] 2.3 In `prompts/license-analysis.md`, add `**Score notation:**` entry: "In the Score field: bare number only (1–5). Do not write `/5`."

## 3. Normalise Comparison Prompt

- [x] 3.1 In `prompts/platform-comparison.md`, remove the extra blank lines between list items inside the `**Permitted syntax only:**` and `**Prohibited syntax:**` blocks so spacing matches the discovery prompt
