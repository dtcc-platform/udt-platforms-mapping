## Why

`tools/` is too generic for what this repository is actually storing there. The current contents are not developer utilities; they are workflow-reflection artifacts that audit whether the repository's governed prompts are still valid and up to date.

## What Changes

- Rename the root folder `tools/` to `reflect-workflow/` for workflow-audit artifacts
- Move the prompt-validity audit from `tools/prompt-validity/` to `reflect-workflow/prompt-validity/`
- Update the live audit prompt, output report path, and governing specs to use the new root path
- Update any folder-layout documentation/specs that describe where workflow-reflection artifacts live

## Capabilities

### New Capabilities

### Modified Capabilities

- `prompt-validity-audit-prompt`: rename the governed prompt path from `tools/prompt-validity/prompt.md` to `reflect-workflow/prompt-validity/prompt.md`
- `prompt-validity-audit-report`: rename the governed report path from `tools/prompt-validity/report.md` to `reflect-workflow/prompt-validity/report.md`
- `ar-folder-layout`: describe `reflect-workflow/` as the root folder for workflow-reflection artifacts instead of leaving them under a generic `tools/` root

## Impact

- Affects the live prompt-validity audit files and their paths
- Affects any prompt/run instructions that tell researchers where to run or save the audit
- Affects baseline specs and folder-structure documentation
