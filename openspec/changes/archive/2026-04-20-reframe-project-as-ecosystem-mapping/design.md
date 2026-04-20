## Context

The project currently presents itself as a "UDT platform review" — a survey of platforms that qualify as urban digital twins. In practice, real UDT deployments compose three types of components: full twin platforms (e.g. DTCC, Virtual Singapore), infrastructure backbones (e.g. FIWARE, 3DCityDB, iTwin), and domain-specific analytics/simulation tools (e.g. climate risk toolkits, traffic simulators). All three types surface during discovery and all three are relevant to anyone building or evaluating a UDT stack.

Without an explicit layer taxonomy, discovery sessions silently drop domain modules as "not quite a platform", and comparison results cannot be grouped by architectural role for visualisation. Adding a `Layer` field makes the ecosystem structure queryable and ensures discovery casts a full net.

## Goals / Non-Goals

**Goals:**
- Reframe the project goal as ecosystem mapping rather than platform review
- Define three canonical layer values (`core-platform`, `backbone`, `domain-module`) and document them in the scope file
- Surface all three layer types during discovery by explicit prompt instruction
- Allow comparison sessions to revise the layer assignment with deeper evidence
- Make the inventory filterable and visualisable by layer

**Non-Goals:**
- Changing any scoring rubric (Relevance, Arch, Open, etc.)
- Changing the comparison prompt's research dimensions or scoring logic
- Automated layer inference — layer is always human/AI assigned per row, not computed
- Backfilling layer values for archived discovery sessions (only the live CSV needs backfill)

## Decisions

**Decision: Three layers, not a flat tag**

Alternatives considered: free-text `Type` field; boolean `is-platform` flag; four layers (adding "standards body"). Three named layers cover the real structure without over-engineering. Standards bodies (OGC, ISO) score Relevance 1–3 and fit as `backbone` or `domain-module`; no fourth layer needed.

**Decision: Controlled vocabulary — `core-platform` | `backbone` | `domain-module`**

Kebab-case, lowercase, no spaces — consistent with existing CSV conventions (Phase values are also lowercase). A blank/`0` value means unassessed, matching the rubric convention for unscored dimensions.

**Decision: Layer is assigned during discovery, revisable during comparison**

Discovery assigns a provisional layer based on surface-level evidence. Comparison, which does deep research, may reclassify — e.g. a tool initially tagged `core-platform` that on deeper inspection is an analytics module gets revised to `domain-module`. Rationale is required in the comparison output when reclassifying, so the change is traceable.

**Decision: Layer definition lives in `docs/01-scope.md`, not a separate file**

The scope file is already pasted into every session. Putting the layer taxonomy there means both discovery and comparison AI have the definitions in context automatically via the existing `[PASTE_SCOPE_HERE]` mechanism. No new file or paste step needed.

**Decision: Backfill existing CSV rows with best-guess layer values**

Existing rows should be backfilled so the column is queryable from day one. Values can be revised in future comparison sessions — the layer column is never locked.

## Risks / Trade-offs

- [Risk: layer boundaries are fuzzy — some platforms span two layers] → Mitigation: assign the primary role; comparison can refine. Document that `backbone` means "primary role is infrastructure/enabling layer", not exclusive.
- [Risk: discovery AI over-includes domain modules, bloating the corpus] → Mitigation: Relevance rubric still filters; a domain module with Relevance 1 is still out of scope. Layer and Relevance are orthogonal.
- [Risk: existing inventory rows have no Layer value on first read] → Mitigation: backfill as part of implementation tasks before the change is archived.
