## 1. Fix license prompt usage header

- [x] 1.1 In `prompts/license-analysis.md`, remove the `> **Source of truth for license taxonomy and scoring:**` blockquote from the usage header

## 2. Clarify score notation in license prompt output format

- [x] 2.1 In `prompts/license-analysis.md`, rewrite the `**Score notation:**` line in the Markdown and Formatting Rules section to explicitly state the output field uses a bare number (e.g., `**Score:** 3`) not the `(X/5)` inline form

## 3. Document scoring handoff in methodology

- [x] 3.1 In `docs/methodology.md`, add a sentence after the workflow steps explaining that discovery scores are judgment-based first-pass signals that the comparison prompt deepens with full rubric-based research
