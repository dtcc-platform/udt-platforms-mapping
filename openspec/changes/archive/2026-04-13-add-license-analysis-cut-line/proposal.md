## Why

`prompts/license-analysis.md` is missing the `> Paste into your AI session from this line onwards.` cut-line blockquote that separates the human-facing usage header from the AI-facing prompt body. Both `platform-discovery.md` and `platform-comparison.md` have this separator; its absence in the license-analysis prompt means a researcher following the same workflow convention may accidentally paste the usage instructions into their AI session. The gap was flagged during verification of the `improve-web-research-prompt-portability` change.

## What Changes

- Add a `---` horizontal rule and `> Paste into your AI session from this line onwards.` blockquote between the usage header and the `## Prompt` section in `prompts/license-analysis.md`, matching the structure of the other two prompts.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `license-analysis-prompt`: usage header gains a cut-line separator — a spec-level requirement that the prompt SHALL include this separator to mark the boundary between the human-facing header and the AI-facing body.

## Impact

Only `prompts/license-analysis.md` and its governing spec `openspec/specs/license-analysis-prompt/spec.md` are affected. No output schemas, response filenames, or downstream workflows change.
