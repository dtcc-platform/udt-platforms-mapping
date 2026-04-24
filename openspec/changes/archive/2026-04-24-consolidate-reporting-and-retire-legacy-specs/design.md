## Context

The baseline spec set currently contains four cleanup targets:

- a split rating-reporting contract where one prompt always produces one tightly coupled CSV/HTML output pair
- a discovery-reporting ecosystem spec with no active requirements
- two legacy retired specs (`relevance-score`, `platform-discovery-scope`) that no longer govern live repository behavior

The prompt-status audit also still maps some live prompts to those older baseline names. If the baseline is cleaned up, the audit workflow should reflect that.

## Goals / Non-Goals

**Goals:**
- Replace the rating-reporting prompt/output pair with one baseline capability.
- Remove baseline specs that are purely retired or no-op.
- Keep the live rating and discovery workflows unchanged.
- Update the prompt-status audit so its mapping follows the cleaned baseline set.

**Non-Goals:**
- Change the live output paths for discovery or rating reporting.
- Redesign the semantics of discovery reporting or rating reporting.
- Rewrite archived OpenSpec history.

## Decisions

### Decision: Merge rating reporting into one capability

The new baseline capability will own the prompt path, automatic scan behavior, CSV schema, HTML output ownership, and core-platform-only export framing.

Why:
- The outputs are produced only by the rating-reporting prompt.
- The CSV/HTML contract has no meaningful independent lifecycle from the prompt workflow.

Alternative considered:
- Keep separate prompt and ecosystem specs.
- Rejected because this split mirrors the prompt-status case that was just simplified.

### Decision: Remove no-op and legacy retired baseline specs outright

`reflect-discovery-reporting-ecosystem`, `relevance-score`, and `platform-discovery-scope` will be removed from the main baseline set.

Why:
- They do not define live behavior the repository currently relies on.
- Keeping retired baseline specs in the active spec set increases noise during audits and exploration.

Alternative considered:
- Keep them as permanently retired baseline records.
- Rejected because archived changes already preserve the historical reasoning.

### Decision: Update the prompt-status audit mapping as part of the same change

The live audit prompt and its governing spec will be updated so the audit:
- no longer treats discovery reporting as relying on a removed no-op shared contract
- no longer treats rating reporting as lacking governing specs
- points to the merged `reflect-rating-reporting` baseline capability

Why:
- Otherwise the baseline cleanup would immediately make the audit mapping stale.

## Risks / Trade-offs

- [Removing retired baseline specs may make some older archive references look disconnected] → Keep archives unchanged; they remain the historical record.
- [A future rating-reporting redesign may want separate output specs again] → Split later only if prompt behavior and output contract begin evolving independently.
- [Audit results may shift after the mapping update] → That is expected and desirable because the baseline set is being corrected.
