## Why

The three prompt files each contain a Markdown and formatting rules section, but they use different section names, different formats, and slightly different content — making them harder to maintain and inconsistent for AI models reading them.

## What Changes

- Rename `### Markdown Syntax Rules` in `prompts/license-analysis.md` to `### Markdown and Formatting Rules` to match the other two prompts
- Replace the flat bullet-list format in the license prompt's Markdown section with the structured `**Permitted syntax only:**` / `**Prohibited syntax:**` format used by the discovery and comparison prompts
- Add the score notation rule to the license prompt's Markdown section (it is present in discovery and comparison but missing from license)
- Remove the extra blank lines between bullet items inside the Permitted/Prohibited blocks in the comparison prompt, so spacing matches the discovery prompt exactly

## Capabilities

### New Capabilities

_None._

### Modified Capabilities

- `license-analysis-prompt`: Markdown rules section renamed and reformatted to match the standard structure
- `platform-comparison-prompt`: minor whitespace normalisation within the Markdown rules section

## Impact

- `prompts/license-analysis.md` — section rename, format change, score notation addition
- `prompts/platform-comparison.md` — whitespace normalisation only
- `openspec/specs/license-analysis-prompt/spec.md` — portable Markdown syntax requirement updated to reference the standard section structure
