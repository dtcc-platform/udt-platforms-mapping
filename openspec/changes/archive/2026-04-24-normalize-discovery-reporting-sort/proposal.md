## Why

The current discovery reporting sort rule is too loose. Saying "sort by the URL part of `Link`" allows raw string sorting that separates related rows like `dtcc.chalmers.se`, `www.dtcc.chalmers.se`, and `platform.dtcc.chalmers.se`, even after all rows have been gathered.

## What Changes

- Tighten the discovery reporting sort contract so ordering happens only after all qualifying rows from all discovery responses have been aggregated
- Define sorting in terms of a normalized URL sort key rather than the raw Markdown link target string
- Require host normalization so rows from the same base domain group together before tie-breaking

## Capabilities

### New Capabilities

### Modified Capabilities

- `reflect-discovery-reporting-prompt`: refine the ordering requirement for the consolidated Markdown table

## Impact

- Affects `reflect/discovery/reporting/prompt.md`
- Affects the baseline discovery reporting prompt spec
- Changes the expected ordering of rows in `reflect/discovery/reporting/ecosystem.md`
