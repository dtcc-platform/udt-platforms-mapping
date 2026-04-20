## Context

`docs/01-scope.md` opens with a "What Is a UDT Platform?" section that currently contains explicit exclusion language ("generic IoT platforms, general-purpose GIS tools without urban twin framing are out of scope"). This prose runs before the Relevance rubric, which already handles exclusion via score 1 ("Out of scope — general purpose or spec/standard only"). The two mechanisms are redundant but contradictory in effect: the definition pre-filters discovery search queries while the rubric post-filters scored candidates.

The existing `platform-discovery-scope` spec requires the file to contain "brief prose context explaining what a UDT platform is" but does not specify what posture that prose should take. This change tightens that requirement.

## Goals / Non-Goals

**Goals:**
- Rewrite the definition so it describes what to search for (search boundary), not what to reject
- Ensure the definition stays permissive enough that borderline platforms (e.g., Eclipse Ditto, iTwin — both Relevance 3) surface during discovery and reach the rubric
- Update the `platform-discovery-scope` spec to require search-boundary framing explicitly

**Non-Goals:**
- Changing any scoring rubric criteria
- Changing how prompts consume `docs/01-scope.md` (paste mechanism unchanged)
- Altering the seed list or target corpus size

## Decisions

**Decision: Keep the definition short and anchor it to search queries, not exclusions**

The definition should tell the discovery AI what space to scan — not pre-judge candidates. Framing: "what would a researcher type into a search engine to find these platforms?" rather than "what would disqualify a platform?" Exclusion is the rubric's job (score 1).

Alternative considered: remove the definition entirely and rely solely on the rubric. Rejected because the rubric assumes a candidate is already in hand; the definition is needed to frame the initial search, especially for AI-assisted discovery sessions that need a starting query.

**Decision: Remove the word "moderate" from the inclusion boundary description**

"Moderate inclusion boundary" is ambiguous and could be read as pre-permissive filtering. The rewrite omits it; the rubric's score 2 ("marginal — could contribute but not designed for it") implicitly defines where the soft boundary sits.

**Decision: No change to the spec's existing scenarios**

All existing `platform-discovery-scope` scenarios remain valid. Only the prose requirement for the definition section changes.

## Risks / Trade-offs

- [Risk: broader search surfaces more out-of-scope platforms] → Mitigation: score 1 in the rubric explicitly handles this; the researcher simply scores and moves on. Wider net is preferable to missing valid candidates.
- [Risk: definition becomes too vague without the exclusion examples] → Mitigation: the rewritten prose names enabling-layer and infrastructure-twin platforms as in-scope examples, giving the AI positive anchors instead of negative ones.
