# Discovery Coverage Eval

This is a Claude Code CLI prompt. Run it by telling Claude Code:

> "Run the discovery eval" or "Run evals/discovery/run.md"

Claude Code will use its file tools to execute the steps below automatically.

---

## Instructions

You are running a recall check on UDT platform discovery responses. Follow these steps exactly:

### Step 1 — Load the fixture

Read `evals/discovery/benchmark.md`. Extract all expected platforms from the single table with:

- Platform name (from the `Name` column)
- Link (from the `Link` column)
- Expected layer (from the `Layer` column)
- Aliases (from the `Aliases` column — split on `,` and trim each entry; may be empty)
- Tags (from the `Tags` column — for grouping in the report)

### Step 2 — Find all discovery responses

Glob all files matching `responses/global-platforms-discovery-*.md`. For each file:

- Read the YAML metadata block at the top (between the `` ```yaml `` fences) and extract the `model` field — this is the column header for that model in the report
- Parse the summary table (the pipe table immediately after the metadata block) and collect all platform names from the `Name` column

### Step 3 — Check recall for each expected platform

For each expected platform in the fixture, and for each response file:

- Build a match set: the canonical `Name` plus all entries from `Aliases`
- Search case-insensitively: the platform is **found** if any member of the match set appears as a substring of any `Name` value in the response's summary table
- If found: check whether the response `Layer` column value matches the benchmark `Layer`
  - Match → record `✓ found`
  - Layer differs → record `✓ found (Layer: <actual value>)`
- If not found: record `✗ missing`

This is a recall check only. Do not flag or report platforms that appear in responses but are not in the fixture in this step.

### Step 4 — Collect novel finds

For each response file, identify platforms in its summary table that do not match any benchmark entry (using the same match logic from Step 3 — canonical Name plus Aliases, case-insensitive substring). These are novel finds for that model.

For each novel find, record:

- Name (from the response summary table `Name` column)
- Link (from the response summary table `Link` column)
- Layer (from the response summary table `Layer` column)
- Aliases: leave blank
- Tags: leave blank

### Step 5 — Write the report

Write the report to `evals/discovery/reports/coverage.md`. Overwrite it if it already exists.

Write the report to that path with this structure:

```
# Discovery Coverage Report — YYYY-MM-DD

**Fixture:** evals/discovery/benchmark.md
**Responses tested:** N files

---

## Recall

| Platform | Layer | Tags | <model-1> | <model-2> | <model-3> |
| -------- | ----- | ---- | --------- | --------- | --------- |
| <name>   | <layer> | <tag> | ✓ found | ✗ missing | ✗ missing |

---

## Novel Finds — not in benchmark

Platforms discovered by models but not in evals/discovery/benchmark.md.
Review and add to the benchmark if in-scope, filling in the Tags column before pasting.

### <model-1>

| Name | Link | Layer | Aliases | Tags |
| ---- | ---- | ----- | ------- | ---- |
| <name> | <link> | <layer> | | |

### <model-2>

| Name | Link | Layer | Aliases | Tags |
| ---- | ---- | ----- | ------- | ---- |
| <name> | <link> | <layer> | | |

---

## Summary

| Model     | Found | Missing | Wrong layer | Novel Finds |
| --------- | ----- | ------- | ----------- | ----------- |
| <model-1> | X/N   | Y       | Z           | W           |
```

Rows in the recall table are ordered as in the benchmark (baseline first, then government-led, niche-commercial, no-dt-framing, niche-oss). Do not add per-tag section headings.

Use the `model` field from each response's YAML metadata as the column/row header — not the filename.

Include all layers in Novel Finds (core-platform, backbone, domain-module, excluded). If a model has no novel finds, omit its `###` section.

After writing the file, confirm the path where it was saved.
