## Why

The discovery prompt requires researchers to manually replace a `[SEARCH_SCOPE]` placeholder before use, but the fallback when no replacement is made already defaults to a global scope — making the placeholder redundant.
Removing it simplifies the workflow to paste-and-run with no user preparation.

## What Changes

- Remove the `[SEARCH_SCOPE]` placeholder and its guard instruction from the discovery prompt
- Replace with a hardcoded global scope description that also calls out non-English-speaking markets and government-led initiatives
- Simplify the usage header from three steps to two (no replacement step)
- Hardcode the save-as filename to `responses/global-platforms-discovery.md`
- Update the docs reference from `docs/methodology.md` to `docs/02-methodology.md`

## Capabilities

### New Capabilities

_(none)_

### Modified Capabilities

- `platform-discovery-prompt`: remove the parameterised scope token requirement; update the usage header requirement to reflect the simplified flow and fixed filename

## Impact

- Modified file: `prompts/platform-discovery.md`
- No changes to response file format, summary table schema, or downstream workflow
