## 1. Update discovery prompt contract

- [x] 1.1 Update `openspec/specs/platform-discovery-prompt/spec.md` with research-mode compatibility, web-chat usage guidance, primary-source discovery/support distinction, and stronger uncertainty rules
- [x] 1.2 Revise `prompts/platform-discovery.md` to add a research-mode preamble, anti-drift output constraints, and explicit web-chat save guidance

## 2. Update comparison prompt contract

- [x] 2.1 Update `openspec/specs/platform-comparison-prompt/spec.md` with research-mode suppression rules, pasted-scope boundary protection, primary-source discovery/support distinction, and web-chat usage guidance
- [x] 2.2 Revise `prompts/platform-comparison.md` to add a research-mode preamble, explicit scope-boundary wording, anti-drift output constraints, and manual-save guidance for web chat sessions. Note: the current file has the `[PASTE_SELECTED_PLATFORMS_HERE]` literal token on its own line immediately above a pre-filled default platform table — the guard instruction would halt on the literal token even though a table is present. Resolve this dual-state as part of this revision by replacing both the bare token line and the default table with a single clean placeholder.

## 3. Update license prompt contract

- [x] 3.1 Update `openspec/specs/license-analysis-prompt/spec.md` with research-mode suppression rules, stronger source-priority wording, and web-chat usage guidance
- [x] 3.2 Revise `prompts/license-analysis.md` to add a research-mode preamble, stronger software-license versus tier-evidence instructions, anti-drift output constraints, and manual-save guidance for web chat sessions

## 4. Validate prompt consistency

- [x] 4.1 Review all three prompt files to ensure the new research-mode wording preserves existing output schemas, heading levels, and save-file conventions
- [x] 4.2 Verify `platform-inventory.md` remains CLI-only and is not accidentally broadened to web-chat usage
