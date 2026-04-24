## 1. Move live prompt-status artifacts

- [x] 1.1 Move `reflect-workflow/prompt-validity/` to `workflow/prompts-status/`
- [x] 1.2 Update the live prompt-validity prompt and report contents to use the new `workflow/prompts-status/` paths

## 2. Update governed contracts

- [x] 2.1 Sync the prompt-validity baseline specs to the new `workflow/prompts-status/` paths
- [x] 2.2 Update the folder-layout baseline spec to allow `workflow/` and to name `workflow/prompts-status/` as the prompt-status location

## 3. Verify path consistency

- [x] 3.1 Search live repository files for stale `reflect-workflow/prompt-validity` references and update any remaining live paths
- [x] 3.2 Run the prompt-status audit from its new location and verify it still writes `workflow/prompts-status/report.md`
