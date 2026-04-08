## 1. Add Shared Markdown Contract Spec

- [x] 1.1 Add `openspec/changes/extract-shared-markdown-contract/specs/prompt-markdown-format/spec.md` defining the common Markdown portability contract

## 2. Update Prompt Spec Deltas

- [x] 2.1 Update the discovery prompt spec delta to reference the shared contract and keep only discovery-specific formatting rules
- [x] 2.2 Update the comparison prompt spec delta to reference the shared contract and keep only comparison-specific formatting rules
- [x] 2.3 Update the license analysis prompt spec delta to reference the shared contract and keep only license-specific formatting rules

## 3. Prepare Implementation Follow-Through

- [x] 3.1 Update `prompts/platform-discovery.md` as needed so its Markdown rules section still matches the shared contract plus discovery-specific deltas
- [x] 3.2 Update `prompts/platform-comparison.md` as needed so its Markdown rules section still matches the shared contract plus comparison-specific deltas
- [x] 3.3 Update `prompts/license-analysis.md` as needed so its Markdown rules section still matches the shared contract plus license-specific deltas

## 4. Merge After Acceptance

- [x] 4.1 Fold the new `prompt-markdown-format` spec into `openspec/specs/` after approval
- [x] 4.2 Merge the three modified prompt-spec deltas into the baseline specs after approval
