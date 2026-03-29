## Why

The license analysis prompt body is missing two instructions that its spec requires and that the other two prompts already include: an explicit primary-sources instruction and an explicit uncertainty-handling instruction. It also lacks a concrete output example, making it harder for models to produce consistently structured responses.

## What Changes

- Add a primary-sources instruction to `prompts/license-analysis.md` (use primary sources only; cite each claim)
- Add an uncertainty-handling instruction to `prompts/license-analysis.md` (state "unknown"/"unclear"; never fabricate)
- Add a concrete fictional example to the Output Format section of `prompts/license-analysis.md`

No spec changes are needed — the requirements already exist in `openspec/specs/license-analysis-prompt/spec.md`. This change brings the prompt into conformance with its existing spec.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

None. The spec already covers these requirements; this is a prompt-only conformance fix.

## Impact

- `prompts/license-analysis.md` — body additions only
