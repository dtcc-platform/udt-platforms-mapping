## Why

The `restructure-research-docs` change updated the inventory CSV schema (adding `Relevance`, replacing `-1` with `0`) but did not update the inventory prompt or its spec. The prompt still instructs the model to use `-1`, omits the `Relevance` column, and forces functional category scores to `-1` for discovery rows even though discovery now scores all 12 dimensions.

## What Changes

- **`prompts/platform-inventory.md`**: Add `Relevance` to the extraction and column order; replace all `-1` sentinels with `0`; remove the instruction that forces `Viz/DM/Sim/IoT/Std/Infra` to `-1` for discovery rows — extract them from the table instead.
- **`openspec/specs/platform-inventory-prompt/spec.md`**: Update the same three requirements to match the current CSV schema.

## Capabilities

### New Capabilities

_(none)_

### Modified Capabilities

- `platform-inventory-prompt`: column order adds `Relevance`; sentinel changes from `-1` to `0`; discovery functional categories extracted from table rather than forced to a fixed value

## Impact

- `prompts/platform-inventory.md`
- `openspec/specs/platform-inventory-prompt/spec.md`
