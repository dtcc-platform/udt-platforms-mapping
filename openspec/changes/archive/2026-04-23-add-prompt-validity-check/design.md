## Context

The repository uses prompt files as governed artifacts rather than ad hoc text. Live prompts in `act/` and `reflect/` are expected to remain aligned with their governing baseline specs under `openspec/specs/` and, where applicable, with the files they declare under `## Required Inputs`.

Today, prompt drift is found manually. This is error-prone because not every related file change should invalidate a prompt. For example, `plan/rating/platforms.md` is per-run data and is expected to change frequently without requiring regeneration of `act/rating/prompt.md`. By contrast, a newer governing spec or a broken required-input path is a meaningful signal that the prompt needs review.

## Goals / Non-Goals

**Goals:**
- Provide one CLI-only prompt that audits all live prompt files in the repository
- Distinguish contract freshness from routine runtime-input churn
- Produce a durable Markdown report with explicit prompt-level findings
- Make it easy for a researcher to rerun the audit after changing prompts, specs, or planning files

**Non-Goals:**
- Automatically regenerate prompts
- Prove semantic equivalence between a prompt and its governing spec
- Audit archived changes under `openspec/changes/archive/`
- Treat every related file modification as prompt staleness

## Decisions

### 1. Use a dedicated tooling prompt outside the action-research phase folders

The audit prompt will live at `tools/prompt-validity/prompt.md`, with output written to `tools/prompt-validity/report.md`.

Rationale:
- The audit is maintenance tooling, not a research-cycle artifact
- It checks multiple prompt families across the repository
- It should not be conflated with discovery or rating research outputs

Alternative considered:
- Put the audit under `reflect/`
Why not chosen:
- `reflect/` is cycle-oriented research work, while the audit is cross-cutting repo maintenance

### 2. Audit only live prompt files

The audit will inspect live prompt files only:
- `act/**/prompt.md`
- `reflect/**/prompt.md`

It will exclude:
- archived change artifacts
- delta specs under `openspec/changes/`
- generated reports other than its own target output

Rationale:
- The goal is to validate the prompts a researcher would actually run now

### 3. Separate freshness dependencies from runtime inputs

The audit will classify related files into two groups:

- **Freshness dependencies**: governing prompt spec and any shared contract spec the prompt explicitly relies on
- **Runtime inputs**: files named in the prompt's `## Required Inputs` section

Freshness rule:
- If a freshness dependency has a newer git modification than the prompt, the prompt becomes `review-needed`

Runtime-input rule:
- Runtime-input files must exist and remain structurally compatible with the prompt contract
- A newer runtime-input file alone does not make the prompt stale

Rationale:
- This avoids false positives for files such as `plan/rating/platforms.md`, which are expected to change per run

Alternative considered:
- Mark any related-file change as staleness
Why not chosen:
- It would produce noisy reports and undermine trust in the audit

### 4. Use three audit statuses

Each audited prompt will receive one of:
- `valid`
- `review-needed`
- `invalid`

Definitions:
- `valid`: no missing files, no contract contradictions found, and no newer freshness dependencies
- `review-needed`: prompt is still runnable, but a freshness dependency is newer or a likely drift signal exists
- `invalid`: missing referenced files, broken required-input declarations, or direct contradiction with governing contract

Rationale:
- A binary pass/fail would collapse meaningful maintenance cases into one bucket

### 5. Require a structured Markdown report

The audit will always overwrite `tools/prompt-validity/report.md` with:
- a header block summarizing audit date and scope
- a summary table with one row per prompt
- a findings section with one subsection per prompt

Rationale:
- The audit needs to be inspectable and git-diffable like other repository artifacts

## Risks / Trade-offs

- [Git freshness is only a proxy for semantic drift] → Mitigation: use `review-needed` rather than `invalid` when the signal is chronological rather than structural
- [Prompt-to-spec mapping may require maintenance as new prompts are added] → Mitigation: require the audit to report unmapped prompts explicitly
- [Tooling prompt introduces another governed artifact] → Mitigation: keep it CLI-only and scoped to one maintenance purpose
