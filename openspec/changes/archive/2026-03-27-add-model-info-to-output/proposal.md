## Why

Saved research response files have no record of which AI model produced them, making it impossible to assess reliability, reproduce results, or compare outputs across models. Adding a model metadata header to each output makes provenance explicit without requiring the researcher to remember to log it manually.

## What Changes

- Each of the three prompt templates will instruct the AI model to begin its response with a metadata block containing: model name and version, the date of the session, and the prompt template used
- The metadata block will use a consistent, portable Markdown format (a fenced code block or a definition list) that renders cleanly in any viewer

## Capabilities

### New Capabilities

<!-- None — this change adds requirements to existing capabilities only -->

### Modified Capabilities

- `platform-discovery-prompt`: add requirement that output begins with a model metadata block
- `platform-comparison-prompt`: add requirement that output begins with a model metadata block
- `license-analysis-prompt`: add requirement that output begins with a model metadata block

## Impact

- `openspec/specs/platform-discovery-prompt/spec.md` — new requirement added
- `openspec/specs/platform-comparison-prompt/spec.md` — new requirement added
- `openspec/specs/license-analysis-prompt/spec.md` — new requirement added
- `prompts/platform-discovery.md` — metadata block instruction added to Output Format section
- `prompts/platform-comparison.md` — metadata block instruction added to Output Format section
- `prompts/license-analysis.md` — metadata block instruction added to Output Format section
