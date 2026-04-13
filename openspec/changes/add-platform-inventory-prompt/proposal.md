## Why

There is no structured path from completed comparison responses to `docs/05-platform-inventory.md` — researchers must manually extract rows, reformat columns, and add metadata by hand.
A dedicated prompt that auto-scans `responses/` closes this gap and makes the inventory a reliable, reproducible output of the research workflow.

## What Changes

- Add `prompts/platform-inventory.md` — a prompt that scans all files in `responses/`, identifies comparison responses by their YAML metadata block (`prompt: platform-comparison`), extracts the Part 1 scoring table rows, and outputs a GFM table ready to paste into `docs/05-platform-inventory.md`
- Each response file contributes one row per platform, with `Model` and `Date` columns populated from the YAML block

## Capabilities

### New Capabilities

- `platform-inventory-prompt`: Prompt that reads comparison response files, extracts scored platform rows, appends model and date metadata, and produces a consolidated GFM inventory table

### Modified Capabilities

_(none)_

## Impact

- New file: `prompts/platform-inventory.md`
- No changes to existing prompts, docs, or response files
- `docs/05-platform-inventory.md` is the target paste destination — its schema was already updated to match the comparison table format
