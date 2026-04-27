# UDT Platforms Reporting Prompt

Use this prompt to produce `reflect/udt-platforms/reporting/ecosystem.md` from qualifying `udt-platforms` response files in `observe/udt-platforms/`.

**Requires:** An AI CLI with filesystem access. This prompt is CLI-only.

1. Run this prompt in your AI CLI session with no extra input
2. The model will scan `observe/udt-platforms/` automatically
3. Save the generated output to `reflect/udt-platforms/reporting/ecosystem.md`

---

> Paste into your AI CLI session from this line onwards.

## Prompt

You are a research assistant maintaining the `udt-platforms` ecosystem summary for this project.

Your task is to scan `observe/udt-platforms/`, extract the summary-table rows from qualifying `udt-platforms` responses only, and write one consolidated Markdown table to `reflect/udt-platforms/reporting/ecosystem.md`.

**Do not ask for file paths or user input.** Read `observe/udt-platforms/` directly using your file tools.

### Step 1 — Identify qualifying files

Read all files in `observe/udt-platforms/`.

For each file:

- Check whether it begins with a fenced YAML block (` ```yaml `) containing a `prompt:` field
- If `prompt: udt-platforms` → it is a qualifying response
- Any other `prompt` value, or no YAML block: skip the file silently

If no qualifying responses exist, report that no qualifying files were found and do not write an output file.

### Step 2 — Extract the summary rows

For each qualifying response:

1. Locate the summary table immediately after the metadata block
2. Extract every data row from that table, excluding the header row and separator row
3. Preserve exactly these columns:
   - `Name`
   - `Link`
   - `Type`
   - `Reason`

Rules:

- Preserve the `Link` cell as a Markdown link
- Keep blank `Reason` cells blank
- If a qualifying file does not contain the expected summary table, skip it silently

### Step 3 — Build the consolidated Markdown table

Gather all extracted rows from all qualifying responses into one combined row set, then build one Markdown table only from that full aggregated set.

Use exactly this column order:

`Name`, `Link`, `Type`, `Reason`

Do not add any headings, prose, notes, per-file sections, source lists, or extra columns.

### Step 4 — Order the rows deterministically

After all qualifying rows have been gathered, sort the final combined row set once before writing the table.

Sort first by `Type`, then by `Name`, then by the URL target extracted from the `Link` cell, then by `Reason`.

### Step 5 — Write the output file

Write the final single-table Markdown document to:

`reflect/udt-platforms/reporting/ecosystem.md`

Overwrite the file if it already exists.

After writing the file, give a short confirmation stating:

- the saved path
- how many qualifying files were used
- how many rows were written
