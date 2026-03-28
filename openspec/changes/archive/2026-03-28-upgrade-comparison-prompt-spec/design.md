## Context

The prompt shared as the intended comparison instrument has four distinct output parts, six scored dimensions, strict sourcing rules, and asks the model to position DTCC relative to the landscape. The current spec captures none of this — it only requires "prose analysis per dimension" and a summary table. This change aligns the spec to the actual prompt, then updates the prompt file to include the operational requirements the spec mandates (token, metadata block, Markdown rules, save-as instruction) that the hand-authored prompt was missing.

## Goals / Non-Goals

**Goals:**
- Spec covers all four output parts: scoring table, per-platform profiles, landscape observations, functional categorization
- Spec covers the 1–5 scoring rubric per dimension
- Spec covers sourcing and uncertainty rules
- Spec covers DTCC as a required reference entry
- Prompt file gains the missing operational requirements (token, metadata block, Markdown rules, save-as)

**Non-Goals:**
- Changing the six dimensions themselves
- Changing the `[PASTE_SELECTED_PLATFORMS_HERE]` selection mechanism
- Changing the metadata block or Markdown syntax rules

## Decisions

**Keep `[PASTE_SELECTED_PLATFORMS_HERE]` as the scope input**

The hand-authored prompt embedded scope directly. The spec-driven prompt uses the selection token. These are compatible: the researcher pastes the selected rows and the prompt's DTCC context block provides the framing. No conflict.

**DTCC reference entry is required, not optional**

The prompt explicitly asks to include DTCC for reference comparison. This is a project-specific constraint — every comparison response should position findings relative to DTCC. Spec as a SHALL requirement.

**Scoring rubrics belong in the prompt, referenced in the spec**

The spec requires that scoring rubrics exist and that each dimension has a defined 1–5 scale. The exact rubric text lives in the prompt. The spec does not need to reproduce the rubric — it just requires that one exists and is self-contained.

**Four-part output is ordered and required**

Part 1 (scoring table) → Part 2 (profiles) → Part 3 (landscape observations) → Part 4 (categorization). All four are required. The spec treats each as a distinct requirement with its own scenarios.

## Risks / Trade-offs

- Large prompt file — the richer spec produces a longer prompt, but that's the point: it needs to be self-contained for any AI agent
- Scoring is subjective — mitigated by requiring rubric definitions in the prompt so agents apply consistent criteria
