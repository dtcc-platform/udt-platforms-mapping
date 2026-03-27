## Context

`docs/methodology.md` states the inclusion criteria but is intentionally abstract — it defines *what qualifies*, not *what we are looking for*. Before running discovery sessions, researchers need an operational document that translates the criteria into a bounded search, names the platforms already known to qualify, and sets a target corpus size. This is `docs/scope.md`.

## Goals / Non-Goals

**Goals:**
- Provide a single reference document a researcher reads before starting any discovery session
- Translate the three inclusion criteria from `docs/methodology.md` into concrete yes/no guidance
- Name explicit exclusion examples so the inclusion boundary is calibrated, not just stated
- Seed the platform list with known qualifiers so discovery sessions extend an existing corpus rather than starting from zero
- Set a target range (15–30 platforms) to frame the scope of the review

**Non-Goals:**
- Replacing or duplicating `docs/methodology.md` — scope.md is operational, methodology.md is normative
- Providing full platform profiles — those go in `docs/platform-inventory.md` and `responses/`
- Being exhaustive — the seed list is illustrative, not a pre-approved final list

## Decisions

### Decision: Separate file (`docs/scope.md`) rather than extending `docs/methodology.md`

**Rationale:** Methodology documents should be stable; scope documents evolve as research progresses. Keeping them separate allows the inclusion criteria to remain fixed while the seed list and target count are updated as platforms are confirmed or excluded.

### Decision: Seed list includes platforms across the full spectrum of inclusion criteria

The seed list covers all three criteria:
- **Explicit UDT:** DTCC, Virtual Singapore
- **City-scale capabilities:** Cesium, 3D City DB
- **Adjacent architecture:** iTwin, Eclipse Ditto, FIWARE

**Rationale:** Including seeds from each criterion calibrates the boundary for discovery sessions — researchers can compare new candidates against known qualifiers from the appropriate category.

### Decision: Explicit exclusion examples paired with rationale

Each exclusion example includes a one-line reason why it falls outside the moderate boundary.

**Rationale:** "Excluded" without rationale is ambiguous. Knowing *why* a platform is excluded helps researchers apply the same reasoning to borderline cases.

## Risks / Trade-offs

- **Seed list becomes stale** → Some seeded platforms may be superseded or discontinued. Mitigation: scope.md is a living document; update it as research reveals changes.
- **Target range feels arbitrary** → 15–30 is a reasonable working corpus for a landscape review, but the actual count will be driven by what exists. Mitigation: treat the range as a planning heuristic, not a hard constraint.
