## Context

The `restructure-research-docs` change migrated the inventory CSV schema: it added a `Relevance` column (position 4, after `Phase`), replaced the `-1` "not assessed" sentinel with `0` throughout, and updated the discovery prompt to score all 12 dimensions. The `platform-inventory-csv` spec was updated at that time, but `prompts/platform-inventory.md` and its spec (`platform-inventory-prompt`) were not. The prompt is now out of sync on three points.

## Goals / Non-Goals

**Goals:**
- Bring `prompts/platform-inventory.md` into sync with the current CSV schema
- Bring `openspec/specs/platform-inventory-prompt/spec.md` into sync with the same

**Non-Goals:**
- Changing the inventory CSV format itself (already correct)
- Changing how comparison responses are extracted (unaffected)
- Adding new extraction logic beyond the three schema fixes

## Decisions

**D1 — Extract functional category scores from discovery tables rather than forcing a fixed value**

The old behaviour forced `Viz/DM/Sim/IoT/Std/Infra` to `-1` for discovery rows on the assumption that discovery did not score those dimensions. Since the discovery prompt was updated to score all 12 dimensions, the correct behaviour is to read those columns from the summary table the same way as the research dimension columns. If a column is absent or contains `0`, that value is used as-is.

**D2 — No special handling for Relevance 1–2 rows**

Relevance 1–2 platforms may have `0` in all dimension columns (if the model did not score them). This is valid and requires no special-casing — `0` in score columns already means "not assessed at this phase."

## Migration Plan

1. Update `openspec/specs/platform-inventory-prompt/spec.md` — three MODIFIED requirements
2. Update `prompts/platform-inventory.md` — matching changes to Step 2A, Step 4, and Step 5
