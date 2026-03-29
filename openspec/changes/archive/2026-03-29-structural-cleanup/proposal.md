## Why

Three small structural inconsistencies remain after the batch 1–2 fixes:

1. The license prompt usage header has an extra `> **Source of truth…**` blockquote that the other two prompts don't have, breaking the visual pattern.
2. The license prompt's Output Format section says "bare number only" for the score but doesn't show the placement (`**Openness & Licensing (X/5):**` vs `Score: 5`), making the instruction ambiguous compared to the other prompts.
3. `docs/methodology.md` doesn't explain that discovery scores are judgment-based first-pass signals that the comparison prompt deepens with rubric-based research — a workflow detail documented only in the comparison spec.

## What Changes

- Remove the `> **Source of truth for license taxonomy and scoring:**` blockquote from the license prompt usage header
- Clarify score notation in the license prompt Output Format section to show placement explicitly
- Add a sentence to `docs/methodology.md` explaining the discovery-to-comparison scoring handoff

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `license-analysis-prompt`: "License analysis prompt usage header includes save-as filename instruction" — remove the extra blockquote so the header matches the pattern of the other two prompts

## Impact

- `prompts/license-analysis.md` — usage header and output format section
- `docs/methodology.md` — one sentence addition to the workflow description
