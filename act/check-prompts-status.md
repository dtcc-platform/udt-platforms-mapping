# Prompt Status Check

Use this prompt to audit whether live repository prompt files are still valid and up to date relative to their governing specs and related files.

**Requires:** An AI CLI with filesystem and git access.  
This prompt is CLI-only. Do not use it in a web chat session.

Run it by telling your AI CLI:

```text
Run act/check-prompts-status.md
```

Save the generated report to `act/check-prompts-status-report.md`.

---

## Prompt

You are auditing the validity and freshness of live prompt files in this repository.

Your task is to inspect the live prompts under `act/` and `reflect/`, compare them against their governing baseline specs and related files, assign each prompt one status (`valid`, `review-needed`, or `invalid`), and write the full report to `act/check-prompts-status-report.md`.

Do not inspect archived change artifacts under `openspec/changes/` or `openspec/changes/archive/`. Do not inspect archival calibration artifacts under `calibration/`.

### Audit scope

Audit these live prompts only:

- `act/udt-platforms/prompt.md`
- `act/udt-platform-comparison/prompt.md`
- `reflect/udt-platforms/benchmarking/prompt.md`
- `reflect/udt-platforms/reporting/prompt.md`
- `reflect/udt-platform-comparison/benchmarking/prompt.md`
- `reflect/udt-platform-comparison/reporting/prompt.md`

### Prompt mapping

#### 1. `act/udt-platforms/prompt.md`

- Governing spec: `openspec/specs/act-udt-platforms-prompt/spec.md`
- Shared contracts:
  - `openspec/specs/prompt-run-modes/spec.md`
  - `openspec/specs/prompt-markdown-format/spec.md`

#### 2. `act/udt-platform-comparison/prompt.md`

- Governing spec: `openspec/specs/act-udt-platform-comparison-prompt/spec.md`
- Shared contracts:
  - `openspec/specs/prompt-run-modes/spec.md`
  - `openspec/specs/prompt-markdown-format/spec.md`

#### 3. `reflect/udt-platforms/benchmarking/prompt.md`

- Governing spec: `openspec/specs/reflect-udt-platforms-benchmarking/spec.md`
- Shared contracts: none

#### 4. `reflect/udt-platforms/reporting/prompt.md`

- Governing spec: `openspec/specs/reflect-udt-platforms-reporting-prompt/spec.md`
- Shared contracts: none

#### 5. `reflect/udt-platform-comparison/benchmarking/prompt.md`

- Governing spec: none currently present
- Shared contracts: none

#### 6. `reflect/udt-platform-comparison/reporting/prompt.md`

- Governing spec: `openspec/specs/reflect-udt-platform-comparison-reporting/spec.md`
- Shared contracts: none

### Status rules

Assign exactly one status to each prompt:

- `valid`
- `review-needed`
- `invalid`

Use these meanings:

- `valid`: no missing files, no direct contract mismatch, and no newer freshness dependency
- `review-needed`: the prompt is runnable, but a governing spec or shared contract is newer than the prompt, or the prompt has no governing spec yet
- `invalid`: missing dependency, broken `## Required Inputs` declaration, or direct contradiction with the governing contract

### Freshness rules

Distinguish **freshness dependencies** from **runtime inputs**.

- Freshness dependencies:
  - the governing prompt spec
  - any shared contract spec listed in the mapping above
- Runtime inputs:
  - files declared under `## Required Inputs`

If any freshness dependency has a newer git commit than the prompt file, mark the prompt `review-needed`.
A runtime-input file being newer than the prompt does **not** make the prompt stale by itself.

### Required checks for each prompt

For each prompt:

1. Confirm the prompt file exists
2. Identify its governing spec and shared contracts from the mapping above
3. If the prompt has a `## Required Inputs` section, extract the declared input paths
4. Confirm all declared required-input files exist
5. Confirm the prompt does not directly contradict its governing spec
6. Get the latest git commit for the prompt and its freshness dependencies
7. Compare git freshness using the rules above
8. Record findings and assign one final status

### Report format

Write the report to `act/check-prompts-status-report.md` with exactly this structure:

```md
# Prompt Status Report — YYYY-MM-DD

**Prompts checked:** N
**Directories scanned:** act/, reflect/

## Summary

| Prompt | Status | Governing Spec | Shared Contracts | Required Inputs | Reason |
| ------ | ------ | -------------- | ---------------- | --------------- | ------ |
```
