## Why

The three prompt templates instruct AI models on what to output but say nothing about how to format it — leaving each model free to use its own Markdown conventions (ChatGPT footnotes, Gemini admonitions, Claude extended syntax). Saved response files will render inconsistently or break in standard Markdown viewers.

## What Changes

- Add a portable Markdown output requirement to each of the three existing prompt specs, covering permitted syntax, prohibited patterns, and citation format
- Update the three prompt template files to include this requirement as a **Markdown Syntax Rules** section, placed immediately before the Output Format section

## Capabilities

### New Capabilities

<!-- None — this change adds requirements to existing capabilities only -->

### Modified Capabilities

- `platform-discovery-prompt`: add requirement that output uses only portable CommonMark/GFM syntax with inline-link citations
- `platform-comparison-prompt`: add requirement that output uses only portable CommonMark/GFM syntax with inline-link citations
- `license-analysis-prompt`: add requirement that output uses only portable CommonMark/GFM syntax with inline-link citations

## Impact

- `openspec/specs/platform-discovery-prompt/spec.md` — new requirement added
- `openspec/specs/platform-comparison-prompt/spec.md` — new requirement added
- `openspec/specs/license-analysis-prompt/spec.md` — new requirement added
- `prompts/platform-discovery.md` — Markdown Syntax Rules section added
- `prompts/platform-comparison.md` — Markdown Syntax Rules section added
- `prompts/license-analysis.md` — Markdown Syntax Rules section added
