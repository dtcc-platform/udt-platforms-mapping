## Context

The discovery prompt has a `[SEARCH_SCOPE]` placeholder that requires researcher action before use. Its guard instruction tells the model to default to a global scope if the placeholder is not replaced — meaning the placeholder's only purpose is to allow narrower scopes. Since this project targets a global inventory, the placeholder adds friction with no benefit.

## Goals / Non-Goals

**Goals:**
- Remove `[SEARCH_SCOPE]` and its guard instruction
- Replace with a hardcoded global scope that explicitly names non-English markets and government-led initiatives
- Simplify the usage header to two steps

**Non-Goals:**
- Supporting scoped (non-global) discovery — not a current requirement
- Changing the output format, summary table schema, or any other prompt behaviour

## Decisions

### Hardcode global scope rather than removing the scope line

**Decision:** Keep a `**Search scope:**` line in the prompt body but with a fixed value instead of a placeholder.

**Rationale:** Removing the line entirely would leave the model without an explicit framing of what to search for. The fixed value also adds the non-English/government-led note that was absent from the placeholder's fallback default.

### No design complexity

This change is a targeted text edit — one placeholder removed, one line reworded, one usage step removed, one filename hardcoded. No architectural decisions required beyond what the spec captures.

## Risks / Trade-offs

- **Loss of scoped discovery** — researchers who wanted to target a specific region can no longer do so with this prompt. Low risk: no evidence this has been used in practice; global scope is what all existing responses use.
