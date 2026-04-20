## Why

The project is scoped as a "UDT platform review" but the real goal is mapping the full UDT ecosystem — platforms, infrastructure backbones, and domain-specific analytics/simulation tools all participate in real deployments. Without an explicit layer taxonomy, domain modules like analytics toolkits get silently excluded from discovery, and comparison results cannot be grouped or visualised by architectural role.

## What Changes

- Reframe the project goal in `docs/01-scope.md` from "platform review" to "ecosystem mapping"
- Define three ecosystem layers: **Core Platform**, **Infrastructure/Backbone**, **Domain Module**
- Add a `Layer` column to the inventory CSV so every platform carries its layer assignment
- Update the discovery prompt to explicitly instruct the AI to search across all three layers
- Update the comparison prompt to assess and revise the `Layer` assignment during deep research (layer classification can improve with deeper evidence)

## Capabilities

### New Capabilities

_(none)_

### Modified Capabilities

- `platform-discovery-scope`: Goal statement reframed from "platform review" to "ecosystem mapping"; definition updated to enumerate the three layers and instruct broad search across all of them
- `platform-inventory-csv`: Add `Layer` column (values: `core-platform` | `backbone` | `domain-module`) with `0` / blank for unassessed rows
- `platform-discovery-prompt`: Add explicit instruction to search all three ecosystem layers and assign a `Layer` value for each discovered platform
- `platform-comparison-prompt`: Add instruction to assess and revise the `Layer` assignment during deep research, with rationale required when reclassifying

## Impact

- `docs/01-scope.md` — goal statement + layer taxonomy definition + layer column documentation
- `data/platform-inventory.csv` — new `Layer` column (existing rows need backfill)
- `prompts/platform-discovery.md` — layer search instruction
- `prompts/platform-comparison.md` — layer revision instruction
- No rubric changes; no breaking changes to scoring dimensions
