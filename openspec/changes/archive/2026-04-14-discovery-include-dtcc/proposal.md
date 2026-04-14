## Why

DTCC is currently added as a hardcoded reference in the comparison prompt — it never appears as a row in the discovery summary table. This means DTCC's profile cannot be pasted into comparison alongside other platforms, and its scores are never updated through normal research sessions. As DTCC's own platform evolves, the hardcoded description in the comparison prompt will drift from reality.

## What Changes

- **`prompts/platform-discovery.md`**: Instruct the model to include DTCC as a required entry in every discovery session, researched from primary sources like any other platform. DTCC SHALL appear as a row in the summary table and have a full per-platform section.
- **`prompts/platform-comparison.md`**: Remove the hardcoded DTCC description and the instruction to add DTCC independently. DTCC enters comparison via the pasted discovery table row, the same as all other platforms. The "include DTCC as a reference entry" instruction is removed; DTCC is just another row.

## Capabilities

### New Capabilities

_(none)_

### Modified Capabilities

- `platform-discovery-prompt`: DTCC added as a required research target in every discovery session
- `platform-comparison-prompt`: Hardcoded DTCC description removed; DTCC enters via the pasted table

## Impact

- `prompts/platform-discovery.md` — DTCC added as required entry
- `prompts/platform-comparison.md` — hardcoded DTCC description and independent-add instruction removed
