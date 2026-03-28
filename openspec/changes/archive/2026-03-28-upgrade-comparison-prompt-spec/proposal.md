## Why

The current `platform-comparison-prompt` spec describes a lightweight side-by-side comparison with prose analysis and a summary table. The prompt actually used in research is far richer: it scores each platform 1–5 across six dimensions, produces per-platform structured profiles with sources, generates landscape observations positioning DTCC relative to others, and assigns functional categorization tags. The spec needs to describe a prompt that generates this output — otherwise the spec is not the source of truth for what the prompt does.

## What Changes

- Replace the comparison prompt spec requirements to describe the full four-part output structure: scoring table, per-platform profiles with dimension scores, landscape observations, and functional categorization
- Add requirements for 1–5 dimension scoring with defined rubrics
- Add requirement for explicit uncertainty and source citation rules (distinguish inference from fact, no fabrication, prefer primary sources)
- Add requirement for DTCC as a reference entry in every comparison response
- Add requirement for a per-platform sources section
- Retain: `[PASTE_SELECTED_PLATFORMS_HERE]` token, metadata block, portable Markdown rules, save-as instruction

## Capabilities

### New Capabilities

### Modified Capabilities
- `platform-comparison-prompt`: output structure, scoring, profiling, landscape analysis, and citation rules all change significantly

## Impact

- `prompts/platform-comparison.md` — full rewrite to match the richer spec
- `openspec/specs/platform-comparison-prompt/spec.md` — requirements replaced
