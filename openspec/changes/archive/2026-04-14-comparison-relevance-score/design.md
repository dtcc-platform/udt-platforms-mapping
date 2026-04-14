## Context

Discovery produces a first-pass Relevance score based on lightweight research and judgment. Comparison does primary-source deep research on the same platforms. The Relevance rubric is already present in the session via `[PASTE_SCOPE_HERE]`, so the model has everything it needs to reassess. The only gap is that the Part 1 table has no column for it.

## Goals / Non-Goals

**Goals:**
- Comparison Part 1 table includes a `Relevance` column with a score that may differ from the discovery row
- The model is instructed to treat the discovery Relevance as a starting point, not a fixed value
- Inventory CSV comparison rows carry a Relevance value

**Non-Goals:**
- Changing the Relevance rubric itself
- Requiring the model to justify Relevance changes in the Part 1 table (rationale belongs in the per-platform profile)
- Changing how discovery rows handle Relevance

## Decisions

**D1 — Relevance goes in the Part 1 table, not a separate section**

The Part 1 table is the compact scoring summary. Relevance is a score (0–5) that fits naturally alongside the 12 dimension scores. Adding it to the table keeps all scores in one place for copy-paste into the inventory.

**D2 — Model may revise Relevance upward or downward**

The instruction should say "reassess using the rubric; the discovery score is a starting point." This is more honest than "confirm the discovery score" — deep research sometimes reveals a platform is less relevant than it appeared (e.g., no city-scale deployments found) or more relevant (explicit UDT framing found in primary sources).

**D3 — Column position: after Name/Link, before Arch**

Consistent with the discovery summary table column order: `Name, Link, Relevance, Arch, Open, ...`. This also matches the inventory CSV column order, making inventory extraction straightforward.

**D4 — Inventory prompt Step 3 updated to extract Relevance**

The inventory prompt extracts comparison rows from the Part 1 table. Once the table has a Relevance column, Step 3 just needs to name it alongside the other score columns.

## Migration Plan

1. Update `prompts/platform-comparison.md` — add `Relevance` column to Part 1 table spec and example; add reassessment instruction
2. Update `prompts/platform-inventory.md` — add `Relevance` to Step 3 extraction list
3. Update specs for both capabilities
