## Why

Comparison sessions do deep primary-source research and may produce a more accurate Relevance assessment than the first-pass discovery survey. Currently the comparison prompt's Part 1 table has no Relevance column, so revised scores are lost. Adding Relevance to the comparison output lets researchers see when deep research changes a platform's scope classification, and gives the inventory a higher-confidence score to work with.

## What Changes

- **`prompts/platform-comparison.md`**: Add a `Relevance` column to the Part 1 scoring table. Instruct the model to reassess the Relevance score using the rubric from the pasted scope, treating the discovery row's score as a starting point that may be revised upward or downward based on primary-source evidence.
- **`prompts/platform-inventory.md`**: Update Step 3 (comparison extraction) to include `Relevance` in the extracted columns.

## Capabilities

### New Capabilities

_(none)_

### Modified Capabilities

- `platform-comparison-prompt`: Part 1 table gains a `Relevance` column; model reassesses Relevance during deep research
- `platform-inventory-prompt`: comparison row extraction includes `Relevance`

## Impact

- `prompts/platform-comparison.md`
- `prompts/platform-inventory.md`
- `openspec/specs/platform-comparison-prompt/spec.md`
- `openspec/specs/platform-inventory-prompt/spec.md`
