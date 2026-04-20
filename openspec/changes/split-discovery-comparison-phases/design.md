## Context

The project currently has one scope file (`docs/01-scope.md`) consumed by both prompts, and both prompts produce overlapping outputs — discovery scores 12 dimensions it shouldn't own, comparison reassesses Layer and Relevance it shouldn't touch. The Relevance rubric (0–5) exists as a separate classification axis alongside the Layer taxonomy, but the two are correlated and redundant: Layer already encodes the architectural role and inclusion boundary via observable criteria. The CSV mixes discovery and comparison rows under a Phase column, making it a hybrid artifact that serves neither phase well.

## Goals / Non-Goals

**Goals:**
- One scope file per phase, each containing only what that phase needs
- Discovery owns: Layer classification (single four-row criteria table), exclusion decision
- Comparison owns: 12 dimension scoring only
- CSV is comparison-only: clean schema, no discovery rows, no Relevance, no Phase
- Retire Relevance as a scored field — Layer + criteria table replaces it
- Drop seed list — it was anchored to Relevance scores

**Non-Goals:**
- Changing any of the 12 dimension rubrics
- Changing the Layer values (`core-platform`, `backbone`, `domain-module`, `excluded`)
- Changing the comparison output structure (3-part format, profiles, landscape observations)
- Migrating existing discovery response markdown files

## Decisions

**Decision: Retire Relevance entirely, not replace it**

Relevance (0–5) was the inclusion rubric. With the Layer criteria table, inclusion is now determined by whether a platform matches any of the three in-scope layer criteria — a binary outcome, not a score. The criteria are observable (checkable against primary sources), not judgment-based. Keeping Relevance alongside Layer would create two competing classification systems. Retired.

**Decision: Discovery scope file contains only the Layer criteria table**

The four-row table (`core-platform`, `backbone`, `domain-module`, `excluded`) with Definition and Criteria columns is the entire discovery scope. No rubrics, no seed list, no target corpus size. The discovery AI needs exactly this to classify platforms — nothing else.

**Decision: Comparison scope file contains only the 12 dimension rubrics**

The comparison AI receives Layer from the discovery row (pasted in) and never reassesses it. It only needs the dimension rubrics. The scope file split enforces this ownership boundary at the paste step.

**Decision: CSV discovery rows are dropped, not migrated**

Existing discovery rows (Phase=discovery) were produced by the old prompt which scored 12 dimensions during discovery — data that the new architecture considers out of place. Keeping them would pollute the comparison-only schema. Discovery outputs live in `responses/` markdown files; the CSV is not their artifact.

**Decision: `docs/01-scope.md` is retired, not repurposed**

The file currently has both roles (discovery framing + all rubrics). Repurposing it to be one of the two new files risks confusion. Retire it cleanly; two new files with unambiguous names replace it.

**Decision: Seed list is dropped**

The seed list existed to calibrate the Relevance rubric. With Relevance gone, there is nothing to calibrate. The Layer criteria table is self-contained and doesn't require calibration examples.

## Risks / Trade-offs

- [Risk: existing discovery responses reference Relevance scores] → Mitigation: those files are historical artefacts in `responses/`; they are not regenerated. New discovery sessions produce the new format.
- [Risk: CSV loses ~50 comparison rows that referenced discovery Relevance as a starting point] → Mitigation: comparison no longer needs a starting Relevance; it scores only dimensions. The loss is acceptable.
- [Risk: Layer criteria table is too terse — AI misclassifies edge cases] → Mitigation: criteria are observable (primary sources checkable); edge cases can be revisited by re-running discovery in deep research mode on a specific platform.
- [Risk: `docs/01-scope.md` still referenced in existing prompt sessions or notes] → Mitigation: both prompts will update their paste instructions to reference the new files; the old file is removed from the repo.
