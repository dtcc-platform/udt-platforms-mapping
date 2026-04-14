## Context

Two files exist solely to support license assessment: `docs/04-license-review.md` (a human reference covering license family taxonomy, evidence locations, and a review checklist) and `prompts/license-analysis.md` (an AI prompt producing a structured 5-section citation report per platform). Both are optional additions to the main discovery/comparison flow.

The `Open` rubric in `docs/01-scope.md` already scores license openness 0–5 but leaves two terms undefined: "open data formats" (at level 5) and "restrictive data formats" (at level 3), and does not distinguish strong from weak copyleft (both currently at level 4).

## Goals / Non-Goals

**Goals:**

- Make the `Open` rubric self-sufficient by defining the undefined terms
- Remove the two now-redundant files cleanly
- Remove the `docs/02-methodology.md` reference to the deleted prompt

**Non-Goals:**

- Changing the 0–5 scale or the meaning of any existing score level
- Modifying the comparison or discovery prompts
- Retroactively re-scoring existing CSV rows

## Decisions

**D1 — Annotate, don't restructure the rubric**

The three changes are additive clarifications within existing level descriptions. No new levels, no reordering. The rubric stays a simple 6-row table.

**D2 — Delete both files, not archive**

Neither file has unique content that isn't either absorbed into the rubric or already present in the comparison prompt's Open dimension analysis. Git history preserves them if needed.

**D3 — Copyleft distinction stays within level 4**

Strong copyleft (GPL) and weak copyleft (LGPL/MPL) both remain at score 4. The distinction is noted as a parenthetical so scorers can weight integration risk in their rationale, but the numeric score doesn't split them — that would add complexity without meaningful signal for a landscape survey.

## Risks / Trade-offs

- **Loss of audit-grade license reports** → Anyone needing a citation-rich per-platform license analysis will have to write their own prompt or reconstruct from the comparison response. Acceptable trade-off for a landscape study.
- **Copyleft distinction is informational only** → If a researcher needs to differentiate GPL from LGPL in scoring, they have no rubric support beyond the parenthetical note. Mitigated by the comparison prompt's Open dimension paragraph which can capture this nuance in prose.

## Migration Plan

1. Update `docs/01-scope.md` — annotate levels 3, 4, 5 of the `Open` rubric
2. Delete `docs/04-license-review.md`
3. Delete `prompts/license-analysis.md`
4. Update `docs/02-methodology.md` — remove license-analysis reference from workflow prose and the mermaid diagram
