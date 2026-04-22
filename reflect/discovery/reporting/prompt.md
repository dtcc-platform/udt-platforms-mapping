# Platform Inventory Prompt

Use this prompt to produce `reflect/discovery/reporting/ecosystem.csv` and `reflect/discovery/reporting/ecosystem-map.html` from all discovery response files in `observe/discovery/`.

**Requires:** An AI CLI with filesystem access — Claude Code, Codex CLI, or Gemini CLI.
This prompt cannot be used in a web chat session (the model needs to read local files).

1. Run this prompt in your AI CLI session — no input required
2. The model will scan `observe/discovery/` automatically and produce ecosystem data
3. Save outputs to `reflect/discovery/reporting/ecosystem.csv` and `reflect/discovery/reporting/ecosystem-map.html`

---

> Paste into your AI CLI session from this line onwards.

## Prompt

You are a research assistant maintaining the UDT platform inventory for this project.

Your task is to scan the `observe/discovery/` directory, extract platform rows from all discovery response files, and produce `ecosystem.csv` and `ecosystem-map.html` in `reflect/discovery/reporting/`.

**Do not ask for file paths or user input.** Read `observe/discovery/` directly using your file tools.

---

### Step 1 — Identify qualifying files

Read all files in `observe/discovery/`. For each file:

- Check whether it begins with a fenced YAML block (` ```yaml `) containing a `prompt:` field
- If `prompt: platform-discovery` → it is a **discovery response** — proceed to Step 2A
- If `prompt: platform-comparison` → it is a **comparison response** — proceed to Step 2B
- Any other value or no YAML block: skip the file silently

---

### Step 2A — Extract rows from discovery responses

For each discovery response:

1. Read the YAML block and extract:
   - `model` → value for the `Model` column
   - `date` → value for the `Date` column

2. Locate the **summary table** — the GFM pipe table that appears immediately after the metadata block.

3. Extract every data row from that table (exclude the header row and separator row).

4. For each row, output a CSV row with:
   - `Phase` = `discovery`
   - `Name` = platform name from the table
   - `Link` = URL from the Link column — strip any Markdown link syntax `[text](url)` and keep the URL only
   - `Relevance` = Relevance score from the table
   - `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra` = all 12 score columns from the summary table; use the value as-is (`0` if absent or unscored)
   - `Model`, `Date` = from YAML metadata

---

### Step 3 — Extract rows from comparison responses

For each comparison response:

1. Read the YAML block and extract:
   - `model` → value for the `Model` column
   - `date` → value for the `Date` column

2. Locate the **Part 1 scoring table** — the GFM pipe table that appears under the `Part 1` heading and contains columns including `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`.

3. Extract every data row from that table (exclude the header row and separator row).

4. For each row, output a CSV row with:
   - `Phase` = `comparison`
   - `Name`, `Link`, `Relevance`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra` = from the Part 1 table
   - `Link` = URL only — strip any Markdown link syntax
   - `Model`, `Date` = from YAML metadata

---

### Step 4 — Reorder columns

Every output row must use exactly this column order:

`Name`, `Link`, `Phase`, `Relevance`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`, `Model`, `Date`

Score cells must contain bare integers (`0`–`5`) or `?` for unknown. `0` means not assessed at this phase. Do not write `/5`. The `-1` sentinel is no longer used.

---

### Step 5 — Output

First, output a brief preamble (plain text, not a CSV row) stating:
- Which files were processed (filenames only), separated into discovery and comparison
- How many rows were extracted in total
- Which files were skipped and why (if any), including files with missing or unrecognised columns

Then output the CSV data rows only — no header row, no surrounding prose.

The rows must be valid CSV that aligns with the header in `reflect/discovery/reporting/ecosystem.csv`:

```
Name,Link,Phase,Relevance,Arch,Open,City,Mature,Integ,Gov,Viz,DM,Sim,IoT,Std,Infra,Model,Date
```
