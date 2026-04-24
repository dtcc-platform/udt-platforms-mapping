## 1. Rename the workflow-audit root

- [x] 1.1 Move `tools/prompt-validity/` to `reflect-workflow/prompt-validity/`
- [x] 1.2 Update the live prompt-validity audit prompt to use the new run path and report path
- [x] 1.3 Update any live references that still mention `tools/prompt-validity/`

## 2. Sync the governed contracts

- [x] 2.1 Update the prompt-validity baseline specs to use `reflect-workflow/prompt-validity/`
- [x] 2.2 Update folder-layout documentation/specs to describe `reflect-workflow/`

## 3. Validate the rename

- [x] 3.1 Confirm the audit prompt is runnable from `reflect-workflow/prompt-validity/prompt.md`
- [x] 3.2 Confirm the report target is `reflect-workflow/prompt-validity/report.md`
- [x] 3.3 Re-run any relevant consistency checks after implementation
