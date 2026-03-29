## Why

The discovery prompt's usage header uses inline prose and a blockquote, while the comparison and license prompts both use a numbered-step list. This inconsistency makes the toolset feel unfinished and forces researchers to context-switch mentally when moving between prompts.

## What Changes

- Convert the usage header in `prompts/platform-discovery.md` from inline prose + blockquote to a numbered-step list matching the comparison and license prompt format
- Update the `platform-discovery-prompt` spec's save-as filename requirement to reflect the numbered-step format

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `platform-discovery-prompt`: "Discovery prompt usage header includes save-as filename instruction" — update to require numbered step-by-step instructions (matching the format now mandated for comparison and license prompts)

## Impact

- `prompts/platform-discovery.md` — usage header rewritten
- `openspec/specs/platform-discovery-prompt/spec.md` — save-as requirement updated
