## Context

The research workflow produces two types of response files in `responses/`: discovery responses (quick, judgment-based first-pass scoring of many platforms) and comparison responses (deep, rubric-based scoring of a small selected set). The current inventory only ingests comparison responses and only tracks included platforms, creating two gaps:

1. **Excluded platforms are invisible** — a researcher cannot see what was considered and why it was excluded.
2. **Discovery scores are discarded** — quick first-pass scores never reach the inventory, so model-to-model comparisons at discovery depth are impossible.

The design resolves both gaps by extending the inventory schema and rewriting the curation prompt to pull from both response types.

## Goals / Non-Goals

**Goals:**
- Add `Phase` column to distinguish discovery vs comparison rows
- Add `-1` sentinel to represent "not applicable at this phase" (distinct from `?` = unknown)
- Convert inventory to CSV (URL-only links, no Markdown syntax in cells)
- Extend discovery prompt summary table with a `Criterion` column covering both inclusion and exclusion labels
- Add formal exclusion criteria to `docs/01-scope.md` (three named categories)
- Rewrite inventory prompt to read both discovery and comparison responses

**Non-Goals:**
- Migrating historical discovery responses that predate this change (they will be ignored until re-run or manually updated to include the `Criterion` column)
- Deduplicating rows across phases — the same platform may appear as both a `discovery` row and a `comparison` row
- Changing the comparison prompt or comparison response format

## Decisions

### Decision: CSV over Markdown for the inventory file

**Chosen:** `.csv` at `docs/05-platform-inventory.csv`

**Why:** The inventory is tabular data consumed by researchers who filter, sort, and compare rows. CSV is directly importable into spreadsheet tools, queryable with standard tools, and has no risk of Markdown table rendering quirks. Markdown tables become unwieldy at 17+ columns.

**Alternative considered:** Keep `.md`, widen table — rejected because Markdown link syntax in the `Link` column (`[text](url)`) adds noise when imported into tools, and very wide tables render poorly.

### Decision: -1 as the sentinel for "not applicable"

**Chosen:** `-1` integer in score columns

**Why:** The existing schema uses `?` for "unknown but expected" and integers `1–5` for real scores. A discovery row where functional category scores (Viz, DM, Sim, IoT, Std, Infra) were never collected is not "unknown" — it is "not applicable at this phase". A distinct sentinel preserves the semantics and allows tooling to filter correctly.

**Alternative considered:** Empty cell — rejected because CSV parsers treat empty cells as null, making it hard to distinguish "not yet filled in" from "intentionally absent". `?` was also rejected because it conflates absence with uncertainty.

### Decision: Phase column instead of deduplication

**Chosen:** Keep one row per (platform, response file) with a `Phase` column

**Why:** Discovery and comparison scores for the same platform are different data — different research depth, potentially different model, different date. Merging them into one row would lose the comparison signal. Keeping both allows researchers to see how scores shift from discovery to comparison.

**Alternative considered:** Overwrite discovery row when comparison row is added — rejected because it destroys the discovery signal and makes model-to-model comparisons at discovery depth impossible.

### Decision: Criterion column in discovery summary table covers both inclusion and exclusion

**Chosen:** Single `Criterion` column with values from both inclusion and exclusion label sets

**Why:** Platforms are either included (one of three inclusion labels) or excluded (one of three exclusion labels). A single column with six possible values is simpler than two separate columns (one for included criterion, one for excluded reason). The label set is small enough that a single column is unambiguous.

**Alternative considered:** Separate `Inclusion Criterion` and `Exclusion Reason` columns — rejected as redundant; only one can be populated per row.

### Decision: Excluded platforms do NOT require per-platform sections in discovery responses

**Chosen:** Per-platform `##` sections are optional for excluded platforms

**Why:** Excluded platforms are often dismissed quickly during discovery — requiring a full section with six scored dimensions for platforms the researcher is actively excluding adds friction and provides little value. The summary table row with the exclusion criterion label is sufficient.

**Alternative considered:** Require sections for excluded platforms — rejected as disproportionate research effort for out-of-scope platforms.

## Risks / Trade-offs

- **Historical discovery responses lack a `Criterion` column** → Inventory prompt will silently skip those files or extract rows without criterion data. Mitigation: the prompt preamble should note which files were skipped or had missing columns.
- **CSV link column loses human-readable labels** → Researchers lose the `[text](url)` display name. Mitigation: the platform Name column already provides the human-readable label; the Link column only needs the URL.
- **-1 sentinel requires tooling awareness** → Any script consuming the CSV must treat -1 as "not applicable", not as a score. Mitigation: document the sentinel value in the CSV header comments or methodology doc.

## Migration Plan

1. Rename `docs/05-platform-inventory.md` → `docs/05-platform-inventory.csv`
2. Rewrite CSV header row to match new column order (add `Phase`, remove Markdown from `Link`)
3. Convert existing rows: strip Markdown link syntax from `Link`, set `Phase=comparison` for all existing rows, set `Viz/DM/Sim/IoT/Std/Infra` to existing values (they were already scored at comparison depth)
4. Update `prompts/platform-inventory.md` with full rewrite
5. Update `prompts/platform-discovery.md`: add `Criterion` column to summary table instructions, add excluded platform requirement
6. Update `docs/01-scope.md`: add exclusion criteria section
7. Update `docs/02-methodology.md`: change `.md` → `.csv` in Mermaid diagram

No rollback is needed — git history preserves the previous `.md` file.

## Open Questions

- Should the Mermaid diagram in `docs/02-methodology.md` show a discovery→inventory path (since discovery rows now feed the inventory directly)? Currently the diagram only shows `comparison → inventory`. _Decision deferred to implementation; add the arrow if it clarifies the workflow._
