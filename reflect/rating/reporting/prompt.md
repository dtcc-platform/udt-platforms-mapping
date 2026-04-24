# Rating Reporting Prompt

Use this prompt to produce `reflect/rating/reporting/ecosystem.csv` and `reflect/rating/reporting/ecosystem-map.html` from qualifying rating response files in `observe/rating/`.

**Requires:** An AI CLI with filesystem access. This prompt is CLI-only.

1. Run this prompt in your AI CLI session with no extra input
2. The model will scan `observe/rating/` automatically
3. Save the generated files to `reflect/rating/reporting/`

---

> Paste into your AI CLI session from this line onwards.

## Prompt

You are a research assistant maintaining the structured rating exports for this project.

Your task is to scan `observe/rating/`, extract the Part 1 scoring-table rows from qualifying rating responses, and write two files:

- `reflect/rating/reporting/ecosystem.csv`
- `reflect/rating/reporting/ecosystem-map.html`

**Do not ask for file paths or user input.** Read `observe/rating/` directly using your file tools.

### Step 1 — Identify qualifying files

Read all files in `observe/rating/`.

For each file:

- Check whether it begins with a fenced YAML block (` ```yaml `) containing a `prompt:` field
- If `prompt: platform-comparison` → it is a qualifying rating response
- Any other `prompt` value, or no YAML block: skip the file silently

If no qualifying rating responses exist, report that no qualifying files were found and do not write output files.

### Step 2 — Extract rating rows

For each qualifying rating response:

1. Read the YAML block and extract:
   - `model`
   - `date`
2. Locate the Part 1 scoring table with these columns:
   - `Name`
   - `Link`
   - `Layer`
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
3. Extract every data row from that table, excluding the header row and separator row

For each extracted row:

- Preserve the `Layer` value as given in the rating response
- Convert the `Link` cell to a raw URL with no Markdown link syntax
- Keep score cells as bare `1`-`5` values or `?`
- Append `model` and `date` from the YAML metadata as the final two columns

If a qualifying file does not contain the expected Part 1 table, skip it silently.

### Step 3 — Build the CSV

Write `reflect/rating/reporting/ecosystem.csv` with exactly this header row:

`Name,Link,Layer,Arch,Open,City,Mature,Integ,Gov,Viz,DM,Sim,IoT,Std,Infra,Model,Date`

Rules:

- Include one CSV row per extracted Part 1 row
- Use standard comma-separated values format
- Keep `Link` as a raw URL only
- Do not include `Relevance` or `Phase`
- Order rows by `Date`, then `Model`, then `Name`, then `Link`

### Step 4 — Build the HTML report

Write `reflect/rating/reporting/ecosystem-map.html` as a self-contained HTML file that visualizes the same row set used in `ecosystem.csv`.

Minimum requirements:

- Show a clear title for the rating ecosystem export
- Include the CSV schema described above
- Provide client-side filtering by `Model` and `Layer`
- Provide a readable comparison table of the exported rows
- Provide at least one visual summary of the score dimensions across the selected rows
- Use plain HTML, CSS, and JavaScript with no build step

The HTML may embed the extracted dataset directly rather than loading the CSV at runtime.

### Step 5 — Write both files

Overwrite these files if they already exist:

- `reflect/rating/reporting/ecosystem.csv`
- `reflect/rating/reporting/ecosystem-map.html`

After writing the files, give a short confirmation stating:

- both saved paths
- how many qualifying rating files were used
- how many CSV rows were written
