## Why

The repository now needs a clearer home for prompt-status artifacts than `reflect-workflow/`. That folder name reflects a previous narrower framing, while the agreed direction is to introduce a broader `workflow/` root and start with a concrete `workflow/prompts-status/` area for prompt freshness and validity reporting.

## What Changes

- Rename the live prompt-status area from `reflect-workflow/prompt-validity/` to `workflow/prompts-status/`.
- Update the prompt-validity audit prompt and report paths to use the new `workflow/prompts-status/` location.
- Update the governed folder-layout contract so the repository can contain a top-level `workflow/` root alongside the action-research phase folders.
- Keep the change narrow: prepare the workflow root through `workflow/prompts-status/` only, without adding presentation or docs artifacts yet.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `ar-folder-layout`: allow a top-level `workflow/` root and replace `reflect-workflow/prompt-validity/` with `workflow/prompts-status/` in the folder contract.
- `prompt-validity-audit-prompt`: change the governed live prompt path and report path from `reflect-workflow/prompt-validity/` to `workflow/prompts-status/`.
- `prompt-validity-audit-report`: change the governed report path from `reflect-workflow/prompt-validity/report.md` to `workflow/prompts-status/report.md`.

## Impact

- Affected live paths: `reflect-workflow/prompt-validity/` to `workflow/prompts-status/`
- Affected baseline specs: `openspec/specs/ar-folder-layout/spec.md`, `openspec/specs/prompt-validity-audit-prompt/spec.md`, `openspec/specs/prompt-validity-audit-report/spec.md`
- Affected audit workflow references in prompts and generated reports
