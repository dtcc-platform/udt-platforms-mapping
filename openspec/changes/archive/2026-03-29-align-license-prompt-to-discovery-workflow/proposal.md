## Why

The license analysis prompt uses its own `[PLATFORM_NAME]` + `[LICENSE_URL_OR_TEXT]` tokens, requiring the researcher to manually transcribe platform details they already have in the discovery summary table. Aligning it to the same row-paste pattern as the comparison prompt makes the entire post-discovery workflow consistent: copy row(s), paste, run.

## What Changes

- **BREAKING**: Replace the `[PLATFORM_NAME]` and `[LICENSE_URL_OR_TEXT]` placeholder tokens with a single `[PASTE_SELECTED_PLATFORM_HERE]` token that accepts a pasted row (plus header) from the discovery summary table
- Update the usage header instructions to match the discovery-to-prompt pattern (open response file, copy row including header, replace token, paste prompt)
- Update the prompt body to instruct the model to derive the platform name and starting license signal from the pasted row, and to locate the full license text using the Link field
- Update the `docs/methodology.md` workflow to include license analysis as a third post-discovery path alongside comparison
- Update the spec to reflect the new token contract

## Capabilities

### New Capabilities

_None._

### Modified Capabilities

- `license-analysis-prompt`: token contract changes from two freeform tokens to a single structured table row token; usage header and prompt body updated accordingly

## Impact

- `prompts/license-analysis.md` — token replacement, usage header, prompt body phrasing
- `docs/methodology.md` — optional license analysis step added to the workflow
- `openspec/specs/license-analysis-prompt/spec.md` — token requirement updated
