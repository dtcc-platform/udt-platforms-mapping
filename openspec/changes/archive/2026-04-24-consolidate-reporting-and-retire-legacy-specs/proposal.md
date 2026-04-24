## Why

Several baseline specs now carry more structure than the live workflow needs. The clearest cases are a prompt/output split where the output has no independent lifecycle, a no-op spec with no active requirements, and fully retired legacy specs that still sit in the main baseline set.

## What Changes

- Merge `reflect-rating-reporting-prompt` and `reflect-rating-reporting-ecosystem` into one baseline capability.
- Remove `reflect-discovery-reporting-ecosystem` because it no longer defines active requirements.
- Remove the retired baseline specs `relevance-score` and `platform-discovery-scope`.
- Update the workflow prompt-status audit contract and live mapping so it points at the surviving governing specs.

## Capabilities

### New Capabilities

- `reflect-rating-reporting`: governs `reflect/rating/reporting/prompt.md` and its structured CSV/HTML outputs as one workflow contract.

### Modified Capabilities

- `workflow-prompts-status`: update the audit workflow to reference the new merged rating-reporting capability and to stop depending on removed baseline specs.
- `reflect-rating-reporting-prompt`: remove this separate capability and fold its requirements into `reflect-rating-reporting`.
- `reflect-rating-reporting-ecosystem`: remove this separate capability and fold its requirements into `reflect-rating-reporting`.
- `reflect-discovery-reporting-ecosystem`: remove this no-op capability from the baseline set.
- `relevance-score`: remove this retired capability from the baseline set.
- `platform-discovery-scope`: remove this retired legacy capability from the baseline set.

## Impact

- Affected baseline specs under `openspec/specs/`
- Affected live audit prompt at `workflow/prompts-status/prompt.md`
- Expected result: fewer baseline capabilities with no change to the live discovery/rating workflow outputs
