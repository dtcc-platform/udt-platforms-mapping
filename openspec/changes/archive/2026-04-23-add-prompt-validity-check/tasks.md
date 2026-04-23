## 1. Define the audit contract

- [x] 1.1 Add `prompt-validity-audit-prompt` spec for the CLI maintenance prompt, target scope, status model, and output path
- [x] 1.2 Add `prompt-validity-audit-report` spec for the report structure and prompt-level findings

## 2. Implement the tooling prompt

- [x] 2.1 Create `tools/prompt-validity/prompt.md` as a CLI-only audit prompt
- [x] 2.2 Encode the prompt-to-governing-spec mapping and shared-contract checks for live prompts under `act/` and `reflect/`
- [x] 2.3 Implement freshness rules that distinguish governing-contract changes from routine runtime-input changes

## 3. Generate and validate the report

- [x] 3.1 Run the audit prompt and write `tools/prompt-validity/report.md`
- [x] 3.2 Verify the report statuses and findings for the current live prompts
- [x] 3.3 Fix any surfaced prompt/spec inconsistencies or document them before archiving the change
