## Context

The discovery prompt currently instructs the model to verify Relevance ≥ 3 before including a platform and to only produce full per-platform sections for qualifying platforms. Out-of-scope candidates are silently discarded. The summary table therefore contains only included platforms; there is no record of what was considered and rejected.

The Relevance 0–5 rubric replaced the old binary include/exclude gate precisely to express gradations — but the discovery prompt still behaves like a gate by filtering at output time.

## Goals / Non-Goals

**Goals:**

- All discovered platforms appear in the summary table regardless of Relevance score
- Relevance 1–2 platforms get a brief section (identification fields + Relevance score + one-line reason) rather than a full 12-dimension section
- Relevance 3–5 platforms get the full section as today
- Future sessions can see what was previously assessed and rejected, avoiding duplicate research

**Non-Goals:**

- Changing the Relevance rubric itself
- Changing how the inventory prompt or CSV handle existing rows
- Requiring full 12-dimension scoring for out-of-scope platforms

## Decisions

**D1 — Brief sections for Relevance 1–2, not full sections**

Alternatives considered:
- _No sections for Relevance 1–2_ (table row only): loses the one-line reason that explains why a platform was rejected, which is the primary value of recording it.
- _Full 12-dimension sections for all platforms_: wastes tokens and effort on platforms that won't be compared or inventoried in depth.

Decision: Relevance 1–2 platforms get identification fields only (Organization, Link, License, Type, Relevance) plus a brief **Reason** field explaining the rejection. No dimension scoring required.

**D2 — Remove the "Relevance ≥ 3" filter from Research Instructions**

The instruction "Verify it meets a Relevance score of 3 or higher" implies the model should skip platforms below that threshold entirely. Replacing it with "Score all discovered platforms on the Relevance rubric; include all in the summary table" shifts the prompt from a gate to a survey.

**D3 — Order summary table by Relevance descending**

Relevance 3–5 platforms still appear first in the table and in per-platform sections, keeping the actionable content prominent. Relevance 1–2 rows appear at the bottom of the table; their sections (if any) appear after all Relevance 3–5 sections.

## Risks / Trade-offs

- **Longer responses** → Discovery sessions will be longer when many out-of-scope candidates are found. Mitigation: brief sections for Relevance 1–2 keep the overhead small; the model is instructed to keep reasons to one line.
- **CSV noise** → Relevance 1–2 rows will appear in the inventory when extracted. Mitigation: the Relevance column and visualization filters already handle this; the HTML viz can filter by Relevance ≥ 3.

## Migration Plan

1. Update `prompts/platform-discovery.md` — remove Relevance ≥ 3 filter from Research Instructions; update section description to describe brief vs. full sections; update summary table note; update example if needed.

No CSV migration needed — existing rows are unaffected.
