## 1. Replace the discovery benchmarking baseline set

- [x] 1.1 Add the baseline spec `openspec/specs/reflect-discovery-benchmarking/spec.md`
- [x] 1.2 Remove the baseline specs `openspec/specs/reflect-discovery-benchmarking-prompt/spec.md`, `openspec/specs/reflect-discovery-benchmarking-coverage/spec.md`, `openspec/specs/reflect-discovery-benchmarking-benchmark/spec.md`, and `openspec/specs/fixture-alias-column/spec.md`

## 2. Align workflow prompt-status audit

- [x] 2.1 Update `openspec/specs/workflow-prompts-status/spec.md` to reference the unified benchmarking spec
- [x] 2.2 Update `workflow/prompts-status/prompt.md` mapping to use the unified benchmarking spec
- [x] 2.3 Refresh `workflow/prompts-status/report.md` so it no longer points at removed benchmarking spec names

## 3. Verify and archive

- [x] 3.1 Verify there are no live references to the removed benchmarking spec names outside archived change history
- [x] 3.2 Archive the completed change after baseline cleanup
