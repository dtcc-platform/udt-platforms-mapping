## Context

The research workflow currently maintains rubric definitions in two places: inside the prompt files (where they must be for self-contained pasting into AI sessions) and in `docs/02-methodology.md` (as a human reference). When a rubric changes, both must be updated in sync. Additionally, `docs/01-scope.md` uses a binary include/exclude gate with six named criteria, which maps awkwardly to the CSV — excluded platforms receive `-1` sentinel values that pollute the scoring columns and require special-casing in the visualization.

The discovery and comparison prompts have drifted structurally: discovery produces 6 dimension columns while comparison produces 12, meaning a platform's row in the CSV looks different depending on which prompt produced it.

## Goals / Non-Goals

**Goals:**

- Single canonical location for all rubric definitions (`docs/01-scope.md`)
- Prompts remain fully self-contained for pasting via a `[PASTE_SCOPE_HERE]` placeholder filled at run time
- Discovery and comparison produce identical CSV columns; research depth is the only structural difference
- Replace `-1` sentinel with `0` (not assessed), eliminating the need for special-casing
- Replace binary scope gate with a Relevance 0–5 score that lives in the CSV alongside other scores

**Non-Goals:**

- Changing the scoring rubrics themselves (1–5 criteria remain as-is)
- Modifying the visualization (`docs/05-platform-inventory.html`)
- Changing the comparison output format (Part 1/2/3 structure stays)
- Retroactively updating historical response files in `responses/`

## Decisions

**D1 — Rubrics live in `01-scope.md`, supplied to prompts via paste**

Alternatives considered:
- _Inline rubrics in both prompts_ (current state): two maintenance points, drift risk.
- _Prompts reference `01-scope.md` by path_: prompts are pasted verbatim into AI sessions that have no filesystem access; path references are meaningless.
- _Separate `rubrics.md` pasted as preamble_: adds a third file with no clear owner.

Decision: `01-scope.md` becomes the rubric source. Its content is pasted into the `[PASTE_SCOPE_HERE]` slot before running a session. The guard prevents silent failures if the user forgets to paste.

**D2 — `[PASTE_SCOPE_HERE]` guard pattern (same as existing `[PASTE_SELECTED_PLATFORMS_HERE]`)**

The comparison prompt already uses this guard pattern. Extending it to both prompts is consistent and familiar. The guard instruction is: _"If `[PASTE_SCOPE_HERE]` still appears verbatim, stop and ask the user to paste `docs/01-scope.md` before continuing."_

**D3 — Relevance as a 0–5 column, not a binary gate**

Alternatives considered:
- _Keep binary include/exclude, add Relevance separately_: redundant; two signals for the same question.
- _Remove scope signal entirely_: loses the ability to filter marginal platforms in the visualization.

Decision: Relevance replaces the binary gate entirely. Score 0 means "out of scope / not assessed." Scores 1–5 express degree of relevance. This eliminates `-1` and the three named exclusion criteria from the discovery prompt output.

**D4 — `02-methodology.md` retains workflow and file naming only**

The rubrics section in `02-methodology.md` was always a duplicate of what lives in the prompts. Removing it reduces the file to its unique content: the workflow diagram, file naming conventions, and the CSV column legend. No rubric content belongs there.

**D5 — Discovery prompt drops deep-research instruction; comparison retains it**

This is the sole intentional structural difference between the two prompts. Discovery is a first-pass survey with relaxed primary-source requirements; comparison is a deep, evidence-based analysis. All other structural elements (columns, guards, output format) are identical.

## Risks / Trade-offs

- **Paste friction** → Users must paste two items (scope + prompt) instead of one. Mitigation: the guard makes forgetting visible immediately; the methodology doc describes the two-step paste in the workflow.
- **01-scope.md grows large** → If rubric tables become long, pasting scope into every session wastes context tokens. Mitigation: rubric tables are already present in the prompts today; net token cost is unchanged or reduced (one source vs. two).
- **Historical CSV rows have `-1` values** → Existing rows need a one-time migration (replace `-1` with `0`, add empty `Relevance` column). Mitigation: straightforward CSV edit; git history preserves the pre-migration state.
- **Response files in `responses/` use old column set** → Discovery responses currently only have 6 dimension columns. Mitigation: historical responses are not re-processed; the inventory prompt reads them on a best-effort basis and the CSV is the canonical record.

## Migration Plan

1. Update `docs/01-scope.md` — replace binary criteria with Relevance 0–5 rubric table; append all 12 dimension rubrics.
2. Update `docs/02-methodology.md` — remove functional category rubrics section; update workflow description to reference two-step paste.
3. Update `prompts/platform-discovery.md` — add `[PASTE_SCOPE_HERE]` guard and slot; add 6 functional columns to output table; add Relevance column; replace `-1` with `0`; remove deep-research instruction; remove inline rubric definitions.
4. Update `prompts/platform-comparison.md` — add `[PASTE_SCOPE_HERE]` guard and slot; remove inline rubric definitions.
5. Update `docs/05-platform-inventory.csv` — add `Relevance` column (empty for existing rows); replace all `-1` values with `0`.

No rollback strategy required — all changes are to documentation and data files under version control. Reverting via git is sufficient.

## Open Questions

- Should the Relevance column appear before or after the 12 score columns in the CSV? (Proposal assumes it's a metadata-adjacent column, placed near `Phase`.)
- Should `01-scope.md` retain any prose context (e.g., "what is a UDT platform?") or become purely a rubric table? Keeping brief prose preserves the file's usefulness as a standalone onboarding document.
