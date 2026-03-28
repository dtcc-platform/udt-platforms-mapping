## 1. Update the live spec

- [x] 1.1 Apply the delta spec to `openspec/specs/platform-comparison-prompt/spec.md` — replace the structured table and dimension requirements with the new four-part output, scoring, DTCC reference, uncertainty, and sources requirements

## 2. Rewrite the comparison prompt

- [x] 2.1 Add the DTCC context block to `prompts/platform-comparison.md` — describe DTCC as the reference platform (open-source, city-scale, CityGML/IFC, Swedish research centre)
- [x] 2.2 Replace the six dimension descriptions with the full scoring rubrics (1–5 scale per dimension with defined criteria)
- [x] 2.3 Replace the output format section with the four-part structure (scoring table → profiles → landscape observations → functional categorization), including the profile template and categorization tag vocabulary
- [x] 2.4 Add explicit uncertainty and sourcing rules (distinguish inference, no fabrication, primary sources only, per-platform sources section)
- [x] 2.5 Add an agent-agnostic output constraints section to the prompt: permitted syntax, prohibited syntax, citation format, whitespace rules, profile heading level (`###`), score notation rules (`X/5` inline in profiles as `**Dimension (X/5):**`, bare number in table cells), and a concrete example profile for one fictional platform showing all of the above
- [x] 2.6 Verify the prompt retains: `[PASTE_SELECTED_PLATFORMS_HERE]` token, metadata block, save-as filename instruction
