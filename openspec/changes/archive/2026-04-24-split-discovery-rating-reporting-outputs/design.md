## Context

Discovery and rating reporting are currently blurred. The live discovery reporting prompt tries to produce `ecosystem.csv` and `ecosystem-map.html`, even though those outputs are a better fit for the evaluated comparison data in the rating phase. The user intent is to make discovery reporting produce a single Markdown table extracted from related responses, and to move CSV/HTML ownership to rating reporting.

This is not only a file-location cleanup. It clarifies the semantic split:
- discovery reporting: summarize what was found
- rating reporting: export structured evaluated data

## Goals / Non-Goals

**Goals:**
- Make discovery reporting output a single Markdown file with one table
- Sort that table by the URL portion of the `Link` column
- Move CSV/HTML output responsibility to rating reporting
- Add baseline specs for the currently stubbed rating reporting prompt

**Non-Goals:**
- Implement the full rating reporting workflow in this proposal
- Redesign the discovery or rating act-phase prompts
- Change the comparison scoring schema itself

## Decisions

### 1. Discovery reporting becomes Markdown-first

Discovery reporting will output a Markdown file rather than a CSV file.

Proposed output:
- `reflect/discovery/reporting/ecosystem.md`

Rationale:
- Discovery results are still exploratory and classification-oriented
- A Markdown table is easier to inspect in context than a partial CSV export
- This keeps discovery reporting aligned with the repository's emphasis on readable intermediate artifacts

Alternative considered:
- Keep discovery reporting as CSV and add a Markdown summary later
Why not chosen:
- It keeps the current semantic confusion and duplicates the export role that properly belongs to rating reporting

### 2. Sort the discovery report by URL

The discovery table will be ordered by the URL portion of the `Link` column, not by source-file order.

Rationale:
- URL ordering is deterministic
- It groups related domains naturally
- It makes cross-run and cross-model inspection more stable

### 3. Retire the discovery CSV capability instead of repurposing it silently

The existing discovery-owned ecosystem CSV capability will be removed from the discovery phase rather than silently redefined.

Rationale:
- The current capability explicitly names a CSV contract
- Reusing it for Markdown would hide a real contract change

### 4. Rating reporting becomes the owner of CSV and HTML outputs

Rating reporting will own:
- `reflect/rating/reporting/ecosystem.csv`
- `reflect/rating/reporting/ecosystem-map.html`

Rationale:
- Rating data is already normalized around a selected comparison set
- CSV/HTML are better suited to evaluated, downstream-consumable data

## Risks / Trade-offs

- [Discovery users may expect machine-friendly export immediately] → Mitigation: document that machine-friendly export begins in rating reporting
- [URL ordering may feel less intuitive than chronology] → Mitigation: specify it clearly as a deterministic ordering rule
- [This change leaves rating reporting more defined than implemented] → Mitigation: include explicit tasking to create the new baseline prompt and output contracts before implementation
