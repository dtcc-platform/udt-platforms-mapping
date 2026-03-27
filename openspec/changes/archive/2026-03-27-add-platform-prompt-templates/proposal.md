## Why

The `prompts/` directory exists but is empty, leaving researchers without standardized AI prompts for the three core research activities: discovering platforms, comparing them, and analyzing their licenses. Without shared templates, each session risks inconsistent depth, missed criteria, and non-comparable outputs.

## What Changes

- Add a prompt template for **platform discovery** — structured to elicit comprehensive UDT platform candidates using defined inclusion criteria
- Add a prompt template for **platform comparison** — structured to produce side-by-side analysis across key dimensions (architecture, openness, maturity, city-scale capability, integration, governance)
- Add a prompt template for **license analysis** — structured to assess a platform's license type, restrictions, commercial use, and compatibility with DTCC's needs

## Capabilities

### New Capabilities

- `platform-discovery-prompt`: A reusable prompt template that guides an AI model through systematic discovery of UDT platforms using primary sources and defined inclusion criteria
- `platform-comparison-prompt`: A reusable prompt template that produces structured comparisons of two or more UDT platforms across the dimensions defined in the research methodology
- `license-analysis-prompt`: A reusable prompt template that guides an AI model through license evaluation using the criteria defined in `docs/license-review.md`

### Modified Capabilities

<!-- No existing capabilities have changing requirements -->

## Impact

- Populates `prompts/` with three Markdown template files
- No changes to existing `docs/`, `search_logs/`, or `responses/` structure
- Prompts reference criteria defined in `docs/methodology.md` and `docs/license-review.md` — those documents should be stable before finalizing templates
