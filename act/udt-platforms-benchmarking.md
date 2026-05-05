# UDT Platforms Coverage Eval

This is a Claude Code CLI prompt. Run it by telling Claude Code:

> "Run the udt-platforms eval" or "Run act/udt-platforms-benchmarking.md"

Claude Code will use its file tools to execute the steps below automatically.

---

## Instructions

You are running a recall check on `udt-platforms` responses. Follow these steps exactly:

### Step 1 — Load the fixture

Read `plan/udt-platforms-benchmark.md`. Extract all expected artifacts from the single table with:

- Name
- Link
- Expected `Type`
- Aliases
- Tags

### Step 2 — Find all `udt-platforms` responses

Glob all files matching `observe/udt-platforms-web-*.md`.

For each file:

- Read the YAML metadata block and extract the `model` field
- Parse the summary table and collect all artifact names from the `Name` column
- Record the `Type` column value for each summary row

### Step 3 — Check recall for each expected artifact

For each expected artifact in the fixture, and for each response file:

- Build a match set from the canonical `Name` plus all `Aliases`
- Search case-insensitively in the response `Name` column
- If found:
  - `Type` matches → record `✓ found`
  - `Type` differs → record `✓ found (Type: <actual value>)`
- If not found → record `✗ missing`

### Step 4 — Collect novel finds

For each response file, identify artifacts in its summary table that do not match any benchmark entry using the same matching logic.

For each novel find, record:

- Name
- Link
- Type
- Aliases: blank
- Tags: blank

### Step 5 — Write the report

Write the report to `observe/udt-platforms-benchmarking-coverage.md`. Overwrite it if it already exists.

Use this structure:

```text
# UDT Platforms Coverage Report — YYYY-MM-DD

**Fixture:** plan/udt-platforms-benchmark.md
**Responses tested:** N files

## Recall

| Artifact | Type | Tags | <model-1> | <model-2> |

## Novel Finds — not in benchmark

### <model-1>

| Name | Link | Type | Aliases | Tags |

## Summary

| Model | Found | Missing | Wrong type | Novel Finds |
```

Rows in the recall table are ordered as in the benchmark. Use the `model` field from YAML metadata as the model header.
