## Context

Discovery responses from three models (Claude, GPT, Gemini) are saved as `responses/global-platforms-discovery-*.md`. Each begins with a YAML metadata block (`model:`, `date:`, `prompt:`) followed by a summary table (`Name | Link | Layer | Reason`) and per-platform sections. There is currently no mechanism to check whether known-expected platforms appear in these responses.

The eval system needs to be runnable inside Claude Code (CLI), where the model has file-read access — not a web chat paste prompt.

## Goals / Non-Goals

**Goals:**
- Define a fixture file format that groups expected platforms by discovery gap category (why a model might miss them), not by Layer
- Define a CLI eval prompt that reads all discovery responses automatically and writes a coverage report
- Define a report format that shows per-model recall per gap category and a summary table

**Non-Goals:**
- Precision testing (penalising models for extra finds)
- Automated CI execution — this is a researcher-run eval, not a pipeline check
- Evaluating comparison responses — discovery only

## Decisions

**Fixture grouped by gap category, not by Layer.**
Gap categories (e.g., "no digital-twin framing", "non-English/government-led") describe the discovery failure mode and are more actionable for prompt improvement than grouping by Layer. A platform's Layer appears as a column within each category group.

**Eval prompt is a Claude Code CLI prompt, not a web chat paste.**
The eval reads files directly using Claude Code's file access tools. This avoids manual paste steps and allows automatic globbing of all discovery response files. The prompt file lives at `tests/eval-discovery.md` and is run by telling Claude Code to execute it.

**Model name sourced from response YAML metadata, not from filename.**
Each response file contains `model: <name>` in its YAML metadata block. Using this as the column header makes reports self-labelling and decoupled from filename conventions.

**Reports saved to `tests/reports/YYYY-MM-DD-coverage.md`.**
Keeping reports in the repo allows tracking recall improvement over time as the fixture grows and prompts are updated. Date-stamped filenames avoid overwrites.

**Platform matching is name-based, case-insensitive.**
The fixture stores the canonical platform name. The eval checks whether that name (case-insensitive) appears in a response's summary table `Name` column or per-platform section heading. This handles minor formatting variation between models.

## Risks / Trade-offs

- **Fixture is manually curated** — it only catches gaps a researcher has already noticed. It will not surface unknown unknowns. Mitigation: treat the fixture as a growing log; add entries whenever a known platform is found to be missing from a response.
- **Name matching can produce false negatives** — if a model uses a different name variant (e.g., "GeoDatalytics Toolkit" vs "GeoDatalytics"), the match fails. Mitigation: fixture entries can include an optional `aliases` note for known variants; the eval prompt handles these.
- **Reports are not machine-parseable** — Markdown output is readable but not easily diffed programmatically. Acceptable for a researcher-run eval; revisit if automation is needed later.
