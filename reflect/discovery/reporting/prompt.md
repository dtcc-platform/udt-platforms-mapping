# Discovery Reporting Prompt

Use this prompt to produce `reflect/discovery/reporting/ecosystem.md` from qualifying discovery response files in `observe/discovery/`.

**Requires:** An AI CLI with filesystem access. This prompt is CLI-only.

1. Run this prompt in your AI CLI session with no extra input
2. The model will scan `observe/discovery/` automatically
3. Save the generated output to `reflect/discovery/reporting/ecosystem.md`

---

> Paste into your AI CLI session from this line onwards.

## Prompt

You are a research assistant maintaining the discovery-stage UDT ecosystem summary for this project.

Your task is to scan `observe/discovery/`, extract the summary-table rows from qualifying discovery responses only, and write one consolidated Markdown table to `reflect/discovery/reporting/ecosystem.md`.

**Do not ask for file paths or user input.** Read `observe/discovery/` directly using your file tools.

### Step 1 — Identify qualifying files

Read all files in `observe/discovery/`.

For each file:

- Check whether it begins with a fenced YAML block (` ```yaml `) containing a `prompt:` field
- If `prompt: platform-discovery` → it is a qualifying discovery response
- Any other `prompt` value, or no YAML block: skip the file silently

If no qualifying discovery responses exist, report that no qualifying files were found and do not write an output file.

### Step 2 — Extract the discovery summary rows

For each qualifying discovery response:

1. Locate the summary table immediately after the metadata block
2. Extract every data row from that table, excluding the header row and separator row
3. Preserve exactly these columns from each row:
   - `Name`
   - `Link`
   - `Layer`
   - `Reason`

Rules:

- Preserve the `Link` cell as a Markdown link; do not strip the URL out of `[label](url)`
- Keep blank `Reason` cells blank
- If a qualifying file does not contain the expected summary table, skip it silently

### Step 3 — Build the consolidated Markdown table

Gather all extracted rows from all qualifying discovery responses into one combined row set, then build one Markdown table only from that full aggregated set.

Use exactly this column order:

`Name`, `Link`, `Layer`, `Reason`

Do not add any headings, prose, notes, per-file sections, source lists, or extra columns. The output file must contain the single table only.

### Step 4 — Order the rows deterministically

After all qualifying rows have been gathered, sort the final combined row set once before writing the table.

To do this:

- Extract the URL target from each Markdown link cell
- Lowercase the URL target
- Extract the host/domain portion
- Remove a leading `www.` from the host if present
- Derive a shared base-domain family key so obvious host variants stay together; for example, `dtcc.chalmers.se`, `www.dtcc.chalmers.se`, and `platform.dtcc.chalmers.se` belong to the same domain family
- Sort first by that normalized domain-family key
- If two rows have the same normalized domain-family key, break ties by the full URL target, then `Name`, then `Layer`, then `Reason`

### Step 5 — Write the output file

Write the final single-table Markdown document to:

`reflect/discovery/reporting/ecosystem.md`

Overwrite the file if it already exists.

After writing the file, give a short confirmation stating:

- the saved path
- how many qualifying discovery files were used
- how many rows were written
