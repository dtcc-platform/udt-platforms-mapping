## 1. Create the prompt file

- [ ] 1.1 Create `prompts/platform-inventory.md` with a usage header stating: requires an AI CLI with filesystem access (Claude Code, Codex CLI, Gemini CLI); output goes into `docs/05-platform-inventory.md` below the existing header row
- [ ] 1.2 Add the cut-line separator and AI-facing prompt body
- [ ] 1.3 Prompt body instructs the model to scan all files in `responses/`, filter by `prompt: platform-comparison` in the YAML block, and skip files with no YAML block silently
- [ ] 1.4 Prompt body instructs the model to extract Part 1 scoring table rows from each qualifying file and reorder columns to match inventory schema: `Name`, `Link`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`, `Model`, `Date`
- [ ] 1.5 Prompt body instructs the model to populate `Model` and `Date` from the YAML `model` and `date` fields of the source file
- [ ] 1.6 Prompt body instructs the model to output only data rows (no header row, no surrounding prose), preceded by a brief preamble listing files processed and row count

## 2. Verify against spec

- [ ] 2.1 Confirm the prompt file exists at `prompts/platform-inventory.md` and is non-empty
- [ ] 2.2 Run the prompt against the existing `responses/` directory and verify the output table columns match `docs/05-platform-inventory.md` header exactly
- [ ] 2.3 Verify each output row has a non-empty `Model` and `Date` value
- [ ] 2.4 Verify discovery response files (no `prompt: platform-comparison`) produce no rows
- [ ] 2.5 Paste output rows into `docs/05-platform-inventory.md` and confirm the table renders correctly
