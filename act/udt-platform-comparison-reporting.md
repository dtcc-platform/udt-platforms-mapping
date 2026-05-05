# UDT Platform Comparison Reporting Prompt

Use this prompt to produce `reflect/udt-platform-comparison-ecosystem.csv` and `reflect/udt-platform-comparison-ecosystem-map.html` from qualifying comparison response files matching `observe/udt-platform-comparison-web-*.md`.

**Requires:** An AI CLI with filesystem access. This prompt is CLI-only.

1. Run this prompt in your AI CLI session with no extra input
2. The model will scan `observe/udt-platform-comparison-web-*.md` automatically
3. Save the generated files to `reflect/`

---

> Paste into your AI CLI session from this line onwards.

## Prompt

You are a research assistant maintaining the structured `udt-platform-comparison` exports for this project.

Your task is to scan `observe/udt-platform-comparison-web-*.md`, extract the Part 1 scoring-table rows from qualifying comparison responses, and write two files:

- `reflect/udt-platform-comparison-ecosystem.csv`
- `reflect/udt-platform-comparison-ecosystem-map.html`

**Do not ask for file paths or user input.** Read files matching `observe/udt-platform-comparison-web-*.md` directly using your file tools.

### Step 1 — Identify qualifying files

Read all files matching `observe/udt-platform-comparison-web-*.md`.

For each file:

- Check whether it begins with a fenced YAML block (` ```yaml `) containing a `prompt:` field
- If `prompt: udt-platform-comparison` → it is a qualifying comparison response
- Any other `prompt` value, or no YAML block: skip the file silently

If no qualifying comparison responses exist, report that no qualifying files were found and do not write output files.

### Step 2 — Extract comparison rows

For each qualifying comparison response:

1. Read the YAML block and extract:
   - `model`
   - `date`
2. Locate the Part 1 scoring table with these columns:
   - `Name`
   - `Link`
   - `Arch`
   - `Open`
   - `City`
   - `Mature`
   - `Integ`
   - `Gov`
   - `Viz`
   - `DM`
   - `Sim`
   - `IoT`
   - `Std`
   - `Infra`
3. Extract every data row from that table

For each extracted row:

- Convert the `Link` cell to a raw URL with no Markdown link syntax
- Keep score cells as bare `1`-`5` values or `?`
- Append `model` and `date` as the final two columns

### Step 3 — Build the CSV

Write `reflect/udt-platform-comparison-ecosystem.csv` with exactly this header row:

`Name,Link,Arch,Open,City,Mature,Integ,Gov,Viz,DM,Sim,IoT,Std,Infra,Model,Date`

Order rows by `Date`, then `Model`, then `Name`, then `Link`.

### Step 4 — Build the HTML report

Write `reflect/udt-platform-comparison-ecosystem-map.html` as a self-contained HTML file that visualizes the same row set used in `ecosystem.csv`.

Minimum requirements:

- Show a clear title for the comparison export
- Provide client-side filtering by `Model`
- Provide a readable comparison table of the exported rows
- Provide at least one visual summary of the score dimensions across the selected rows

### Step 5 — Write both files

Overwrite these files if they already exist:

- `reflect/udt-platform-comparison-ecosystem.csv`
- `reflect/udt-platform-comparison-ecosystem-map.html`

After writing the files, give a short confirmation stating:

- both saved paths
- how many qualifying comparison files were used
- how many CSV rows were written
