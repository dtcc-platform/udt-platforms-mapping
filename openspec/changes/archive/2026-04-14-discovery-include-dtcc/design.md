## Context

The comparison prompt currently adds DTCC as a fixed reference via a hardcoded description block:

> "DTCC (Digital Twin Cities Centre) is a Swedish research centre developing an open-source, city-scale urban digital twin platform..."

This description was written at a point in time and will drift as DTCC evolves. More importantly, DTCC never appears as a row in the discovery summary table — it cannot be pasted into comparison alongside other platforms, breaking the "copy rows from discovery into comparison" workflow for DTCC itself.

## Goals / Non-Goals

**Goals:**

- DTCC appears as a researched row in every discovery summary table
- DTCC flows into comparison the same way as any other platform (via the pasted table)
- DTCC's scores are updated through normal research sessions rather than by editing the prompt
- The comparison prompt no longer needs to hardcode DTCC's description

**Non-Goals:**

- Changing DTCC's Relevance score (it remains 5 per the seed list in `01-scope.md`)
- Making DTCC optional in discovery — it is always required
- Removing the concept of a "reference platform" from comparison — DTCC's role as reference platform is preserved, just not hardcoded

## Decisions

**D1 — DTCC is a required entry in discovery, not optional**

Alternatives considered:
- _Optional: researcher adds DTCC manually_: inconsistent; easy to forget; DTCC scores drift.
- _Required: prompt always instructs the model to include DTCC_: consistent, always up to date, flows naturally into comparison.

Decision: The discovery prompt SHALL instruct the model to include DTCC as a required research target in addition to all other discovered platforms. It appears in the summary table with a full per-platform section.

**D2 — Hardcoded DTCC description removed from comparison prompt**

The comparison prompt currently supplies DTCC's description itself. Once DTCC appears as a row in the discovery table, that row is pasted into comparison along with all other platforms. The hardcoded block becomes redundant and potentially contradictory.

The instruction "include DTCC as a reference entry" is replaced with: "treat the DTCC row from the pasted table as the reference platform for landscape observations in Part 3."

**D3 — DTCC's role as reference platform preserved in Part 3**

The Part 3 landscape observations (DTCC's Position, Comparable Platforms, Complementary Platforms) still orient around DTCC. The change is only in how DTCC's profile data enters the prompt — via the table, not hardcoded.

## Risks / Trade-offs

- **DTCC research quality varies by model** → A model may have more or less current knowledge of DTCC than the hardcoded description. Mitigation: DTCC's primary source (dtcc.chalmers.se, GitHub repo) is well-indexed; the prompt's primary-source instruction applies equally to DTCC.
- **Discovery responses become DTCC-anchored** → Every discovery session now includes DTCC research overhead. Mitigation: DTCC is a small, well-documented platform; the overhead is minimal.
- **Pasting DTCC row into comparison is now required** → Previously the researcher could paste any subset of discovery rows; now they must include the DTCC row for Part 3 to work correctly. Mitigation: the comparison prompt instructions should note that the DTCC row must be included.

## Migration Plan

1. Update `prompts/platform-discovery.md` — add explicit instruction to include DTCC as a required research entry; add DTCC to the example or a note about required platforms.
2. Update `prompts/platform-comparison.md` — remove the hardcoded DTCC description block; update the "About DTCC" instruction to say DTCC enters via the pasted table; add a note that the DTCC row must be included when selecting platforms to compare.
