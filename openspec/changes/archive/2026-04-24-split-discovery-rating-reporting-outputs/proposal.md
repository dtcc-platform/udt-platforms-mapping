## Why

The current reporting split is wrong for the kind of knowledge each phase produces. Discovery reporting should summarize discovered platforms from related responses in a readable Markdown table, while CSV and HTML outputs belong to rating reporting, where the data is already evaluated and structured for downstream analysis.

## What Changes

- Change `reflect/discovery/reporting/prompt.md` so it produces a single Markdown file containing one consolidated table extracted from related discovery responses
- Order the discovery reporting table by the URL part of the `Link` column rather than by prompt-order appearance
- Retire discovery ownership of `reflect/discovery/reporting/ecosystem.csv`
- Introduce rating reporting as the owner of `ecosystem.csv` and `ecosystem-map.html`
- Define a proper baseline spec for `reflect/rating/reporting/prompt.md`

## Capabilities

### New Capabilities
- `reflect-rating-reporting-prompt`: rating reporting prompt that generates structured ecosystem outputs from rating responses
- `reflect-rating-reporting-ecosystem`: rating reporting output contract for `ecosystem.csv` and `ecosystem-map.html`

### Modified Capabilities
- `reflect-discovery-reporting-prompt`: discovery reporting prompt changes from CSV/HTML generation to Markdown-table extraction and URL-based ordering

## Impact

- Affects `reflect/discovery/reporting/prompt.md`
- Retires the discovery-owned ecosystem CSV contract
- Adds baseline requirements for `reflect/rating/reporting/prompt.md` and its outputs
- Clarifies the semantic split between discovery summarization and rating export
