## Why

The `Select` column and `x`-marking workflow adds unnecessary friction: researchers must edit a generated response file to add marks, then clear them afterwards, and the `x` values end up as noise in the pasted table. The same goal — choosing which platforms to compare — is achieved simply by copying the desired rows directly.

## What Changes

- Remove the `Select` column from the discovery summary table output format
- Remove the instruction to leave the `Select` column empty from the discovery prompt
- Remove step 2 ("Place `x` in the Select column") from the comparison prompt usage header
- Simplify step 3 to "Copy the rows you want to compare (including the header row)"
- Remove the `x`-marked rows language from the comparison prompt body token description
- Remove step 6 ("Clear the `x` marks") from the methodology workflow
- Update specs to reflect the simplified selection model

## Capabilities

### New Capabilities

_None._

### Modified Capabilities

- `platform-discovery-prompt`: summary table schema changes — `Select` column removed
- `platform-comparison-prompt`: usage header and token description updated to remove `x`-marking language

## Impact

- `prompts/platform-discovery.md` — summary table column list and trailing instruction
- `prompts/platform-comparison.md` — usage header steps and `[PASTE_SELECTED_PLATFORMS_HERE]` context sentence
- `docs/methodology.md` — discovery-to-comparison workflow steps 2 and 6
- `openspec/specs/platform-discovery-prompt/spec.md` — summary table schema requirement
- `openspec/specs/platform-comparison-prompt/spec.md` — selection token requirement
