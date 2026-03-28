## Why

The comparison prompt requires manually specifying platform names via `[PLATFORM_A]` / `[PLATFORM_B]` tokens and separately pasting inventory rows — three manual steps with no natural selection surface. The discovery prompt already produces a summary table at the end of each response. Using that table as the selection interface (mark rows with `x`, paste into comparison prompt) reduces setup to one step and eliminates the need for any new file.

## What Changes

- **BREAKING** Replace `[PLATFORM_A]`, `[PLATFORM_B]`, and `[PASTE_INVENTORY_ROWS_HERE]` in `prompts/platform-comparison.md` with a single `[PASTE_SELECTED_PLATFORMS_HERE]` token — the prompt derives comparison scope from the pasted table rows
- Make the summary table **required** (not optional) in `prompts/platform-discovery.md` — it is now the selection interface for comparison sessions
- Update `docs/methodology.md` to document the selection workflow

## Capabilities

### New Capabilities

### Modified Capabilities
- `platform-discovery-prompt`: the summary table at the end of discovery responses changes from optional to required
- `platform-comparison-prompt`: the scope input mechanism changes from named platform tokens + separate inventory rows to a single pasted selection table

## Impact

- `prompts/platform-comparison.md` — token replacement (**BREAKING**)
- `prompts/platform-discovery.md` — summary table made required
- `docs/methodology.md` — selection workflow documented
- `openspec/specs/platform-discovery-prompt/spec.md` — summary table requirement added
- `openspec/specs/platform-comparison-prompt/spec.md` — scope input requirement updated
