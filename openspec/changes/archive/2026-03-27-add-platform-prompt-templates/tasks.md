## 1. Platform Discovery Prompt

- [x] 1.1 Create `prompts/platform-discovery.md` with header, usage instructions, and `[SEARCH_SCOPE]` placeholder
- [x] 1.2 Embed all three inclusion criteria from `docs/methodology.md` in the prompt body
- [x] 1.3 Add structured output section instructing the model to return fields matching `docs/platform-inventory.md` columns
- [x] 1.4 Add a note in the file header pointing to `docs/methodology.md` as the authoritative source for inclusion criteria

## 2. Platform Comparison Prompt

- [x] 2.1 Create `prompts/platform-comparison.md` with header, usage instructions, and `[PLATFORM_A]` / `[PLATFORM_B]` placeholders
- [x] 2.2 Embed the six research dimensions (technical architecture, openness/licensing, city-scale capability, maturity, integration posture, governance) in the prompt body
- [x] 2.3 Add output section instructing the model to return a Markdown summary table plus per-dimension prose
- [x] 2.4 Add instruction in the prompt requiring primary-source citations for each claim
- [x] 2.5 Add a note in the file header pointing to `docs/methodology.md` as the source for research dimensions

## 3. License Analysis Prompt

- [x] 3.1 Create `prompts/license-analysis.md` with header, usage instructions, and `[PLATFORM_NAME]` / `[LICENSE_URL_OR_TEXT]` placeholders
- [x] 3.2 Embed license family taxonomy (permissive, copyleft strong/weak, open-core, proprietary) from `docs/license-review.md`
- [x] 3.3 Embed the 1–5 Openness & Licensing scoring rubric and instruct the model to assign a score with rationale
- [x] 3.4 Add a section instructing the model to assess data licensing separately (open standards, format lock-in)
- [x] 3.5 Add a section mapping to the five-item review checklist from `docs/license-review.md`
- [x] 3.6 Add a note in the file header pointing to `docs/license-review.md` as the authoritative source

## 4. Cleanup

- [x] 4.1 Remove `prompts/.gitkeep` now that the directory contains real files
