# Platform Inventory Prompt

Use this prompt to curate `docs/05-platform-inventory.md` from all completed comparison response files.

**Requires:** An AI CLI with filesystem access — Claude Code, Codex CLI, or Gemini CLI.
This prompt cannot be used in a web chat session (the model needs to read local files).

1. Run this prompt in your AI CLI session — no input required
2. The model will scan `responses/` automatically and produce inventory rows
3. Paste the output rows into `docs/05-platform-inventory.md` below the existing header row

> **Save response as:** paste directly into `docs/05-platform-inventory.md` — do not save as a separate response file.

---

> Paste into your AI CLI session from this line onwards.

## Prompt

You are a research assistant maintaining the UDT platform inventory for this project.

Your task is to scan the `responses/` directory, extract scored platform rows from all comparison response files, and produce a consolidated table ready to paste into `docs/05-platform-inventory.md`.

**Do not ask for file paths or user input.** Read `responses/` directly using your file tools.

---

### Step 1 — Identify qualifying files

Read all files in `responses/`. For each file:

- Check whether it begins with a fenced YAML block (` ```yaml `) containing `prompt: platform-comparison`
- If yes: it is a qualifying comparison response — proceed to Step 2
- If the file has no YAML block, or the YAML block does not contain `prompt: platform-comparison`: skip the file silently

---

### Step 2 — Extract metadata and rows

For each qualifying file:

1. Read the YAML block and extract:
   - `model` → value for the `Model` column
   - `date` → value for the `Date` column

2. Locate the **Part 1 scoring table** — the GFM pipe table that appears under the `Part 1` heading and contains columns including `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`.

3. Extract every data row from that table (exclude the header row and separator row).

---

### Step 3 — Reorder columns

The output table must use exactly this column order:

| Name | Link | Arch | Open | City | Mature | Integ | Gov | Viz | DM | Sim | IoT | Std | Infra | Model | Date |

If the source table has columns in a different order, reorder them.
Append `Model` and `Date` as the last two columns using the values from Step 2.

Score cells must contain bare integers (1–5) or `?` for unknown. Do not write `/5` in table cells.

---

### Step 4 — Output

First, output a brief preamble (plain text, not a table row) stating:
- Which files were processed (filenames only)
- How many rows were extracted in total
- Which files were skipped and why (if any)

Then output the data rows only — no header row, no separator row, no surrounding prose.

The rows must be valid GFM pipe table rows that align with the header already present in `docs/05-platform-inventory.md`.
