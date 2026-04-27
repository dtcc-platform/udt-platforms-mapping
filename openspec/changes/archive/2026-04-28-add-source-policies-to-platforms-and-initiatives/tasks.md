## 1. Canonical Inputs

- [x] 1.1 Create `plan/udt-platforms/source-policy.md` with ranked evidence, unacceptable sources, and contradiction-handling rules for technical-artifact mapping.
- [x] 1.2 Create `plan/udt-initiatives/source-policy.md` with ranked evidence, unacceptable sources, contradiction-handling rules, and explicit handling for unresolved `Uses` values.

## 2. Prompt And Cycle Alignment

- [x] 2.1 Update `act/udt-platforms/prompt.md` so `plan/udt-platforms/source-policy.md` is a required input and the prompt instructs the model to follow it.
- [x] 2.2 Update any live documentation or cycle-level notes that describe `udt-platforms` or `udt-initiatives` inputs so the new source-policy files are part of the canonical workflow.

## 3. Verification

- [x] 3.1 Verify that active baseline specs, plan files, and prompt files all agree on the new `source-policy.md` paths for `udt-platforms` and `udt-initiatives`.
- [x] 3.2 Refresh prompt-status or equivalent verification output if the `udt-platforms` prompt changes as part of implementation.
