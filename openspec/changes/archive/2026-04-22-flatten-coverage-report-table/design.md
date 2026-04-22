## Context

The benchmark uses a single flat table (`Name | Link | Layer | Aliases | Tags`). The coverage report currently groups rows under `## Tag:` headings, which is inconsistent — it recreates the multi-section structure that was removed from the benchmark for the same reason.

## Goals / Non-Goals

**Goals:**
- Single recall table in the coverage report: `Platform | Layer | Tags | <model columns>`
- Consistent structure between benchmark and report

**Non-Goals:**
- Changing the Novel Finds section (already per-model headings, which is appropriate)
- Changing the Summary table

## Decisions

### Tags as a column, not a section heading

The `Tags` column value is copied directly from the benchmark row. Rows stay in the same order as the benchmark (baseline first, then government-led, niche-commercial, no-dt-framing, niche-oss) — the Tags column provides the grouping signal without needing section breaks.

**Why:** Consistent with the benchmark design. A researcher scanning the report sees one table, same as the benchmark, and can cross-reference by eye.

## Risks / Trade-offs

- **Less visual separation by tag** — a long table is harder to skim by failure mode than sectioned tables. Mitigation: the Tags column is still there; a researcher can filter or sort if viewing in a tool that supports it.
