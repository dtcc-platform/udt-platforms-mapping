## Context

Discovery responses already end with a summary table (introduced in the previous change, currently optional). The comparison prompt currently uses three separate tokens. This change wires the two prompts together by making the discovery summary table the natural handoff point: researcher marks `x` on rows they want to compare, copies those rows, pastes into the comparison prompt.

## Goals / Non-Goals

**Goals:**
- Make the discovery → comparison handoff a single paste operation
- Remove the three-token complexity from the comparison prompt
- Make the summary table a required output of discovery sessions

**Non-Goals:**
- Any new files or tooling
- Changing the six research dimensions or the comparison output structure
- Changing the discovery prompt's per-platform section format

## Decisions

**Summary table becomes required in discovery responses**

It was made optional in the previous change to keep flexibility. Now that it's the selection interface, it must always be present. The per-platform sections remain the primary output; the table follows at the end as a summary and selection surface.

**Single `[PASTE_SELECTED_PLATFORMS_HERE]` token**

The researcher pastes only `x`-marked rows — a clean table of 2–N platforms. The prompt instructs the agent to treat every row in the pasted table as a comparison target, so the number of platforms is implicit. No need for `[PLATFORM_A]` / `[PLATFORM_B]` naming.

**`[PASTE_INVENTORY_ROWS_HERE]` removed**

The selection table rows already carry the key context fields from the discovery summary (Platform, Type, License, Maturity). Pasting a separate inventory excerpt is redundant.

## Risks / Trade-offs

- Breaking change to comparison prompt tokens — acceptable, project is pre-data and no saved workflows yet
- Discovery responses without a summary table (pre-change) can't be used as selection input — acceptable, those are historical records

## Open Questions

- None.
