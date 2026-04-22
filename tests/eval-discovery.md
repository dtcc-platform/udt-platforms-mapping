# Discovery Coverage Eval

This is a Claude Code CLI prompt. Run it by telling Claude Code:

> "Run the discovery eval" or "Run tests/eval-discovery.md"

Claude Code will use its file tools to execute the steps below automatically.

---

## Instructions

You are running a recall check on UDT platform discovery responses. Follow these steps exactly:

### Step 1 — Load the fixture

Read `tests/discovery-fixtures.md`. Extract all expected platforms with:
- Gap category name (the `## Gap:` heading text)
- Platform name (from the `Name` column)
- Link (from the `Link` column)
- Expected Layer (from the `Expected Layer` column)

### Step 2 — Find all discovery responses

Glob all files matching `responses/global-platforms-discovery-*.md`. For each file:
- Read the YAML metadata block at the top (between the ` ```yaml ` fences) and extract the `model` field — this is the column header for that model in the report
- Parse the summary table (the pipe table immediately after the metadata block) and collect all platform names from the `Name` column

### Step 3 — Check recall for each expected platform

For each expected platform in the fixture, and for each response file:
- Search for the platform name case-insensitively in the response's summary table `Name` column
- If found: check whether the `Layer` column value matches the expected Layer
  - Match → record `✓ found`
  - Layer differs → record `✓ found (Layer: <actual value>)`
- If not found: record `✗ missing`

This is a recall check only. Do not flag or report platforms that appear in responses but are not in the fixture.

### Step 4 — Write the report

Write the report to `tests/reports/coverage.md`. Overwrite it if it already exists.

Write the report to that path with this structure:

```
# Discovery Coverage Report — YYYY-MM-DD

**Fixture:** tests/discovery-fixtures.md
**Responses tested:** N files

---

## Gap: <gap category name>

| Platform | Expected Layer | <model-1> | <model-2> | <model-3> |
| -------- | -------------- | --------- | --------- | --------- |
| <name>   | <layer>        | ✓ found   | ✗ missing | ✗ missing |

---

## Summary

| Model     | Found | Missing | Wrong layer |
| --------- | ----- | ------- | ----------- |
| <model-1> | X/N   | Y       | Z           |
```

Use the `model` field from each response's YAML metadata as the column/row header — not the filename.

After writing the file, confirm the path where it was saved.
