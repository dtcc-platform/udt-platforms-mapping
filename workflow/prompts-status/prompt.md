# Prompt Validity Audit

Use this prompt to audit whether live repository prompt files are still valid and up to date relative to their governing specs and related files.

**Requires:** An AI CLI with filesystem and git access.
This prompt is CLI-only. Do not use it in a web chat session.

Run it by telling your AI CLI:

```text
Run workflow/prompts-status/prompt.md
```

Save the generated report to `workflow/prompts-status/report.md`.

---

## Prompt

You are auditing the validity and freshness of live prompt files in this repository.

Your task is to inspect the live prompts under `act/` and `reflect/`, compare them against their governing baseline specs and related files, assign each prompt one status (`valid`, `review-needed`, or `invalid`), and write the full report to `workflow/prompts-status/report.md`.

Do not inspect archived change artifacts under `openspec/changes/` or `openspec/changes/archive/`.

### Audit scope

Audit these live prompts only:

- `act/discovery/prompt.md`
- `act/rating/prompt.md`
- `reflect/discovery/benchmarking/prompt.md`
- `reflect/discovery/reporting/prompt.md`
- `reflect/rating/benchmarking/prompt.md`
- `reflect/rating/reporting/prompt.md`

### Prompt mapping

Use this mapping table to determine governing files.

#### 1. `act/discovery/prompt.md`

- Governing spec: `openspec/specs/act-discovery-prompt/spec.md`
- Shared contracts:
  - `openspec/specs/prompt-run-modes/spec.md`
  - `openspec/specs/prompt-markdown-format/spec.md`
- Runtime inputs:
  - read from the prompt's `## Required Inputs` section

#### 2. `act/rating/prompt.md`

- Governing spec: `openspec/specs/act-rating-prompt/spec.md`
- Shared contracts:
  - `openspec/specs/prompt-run-modes/spec.md`
  - `openspec/specs/prompt-markdown-format/spec.md`
- Runtime inputs:
  - read from the prompt's `## Required Inputs` section

#### 3. `reflect/discovery/benchmarking/prompt.md`

- Governing spec: `openspec/specs/reflect-discovery-benchmarking-prompt/spec.md`
- Shared contracts:
  - `openspec/specs/reflect-discovery-benchmarking-coverage/spec.md`
- Runtime inputs:
  - `reflect/discovery/benchmarking/benchmark.md`
  - `observe/discovery/*.md`

#### 4. `reflect/discovery/reporting/prompt.md`

- Governing spec: `openspec/specs/reflect-discovery-reporting-prompt/spec.md`
- Shared contracts:
  - `openspec/specs/reflect-discovery-reporting-ecosystem/spec.md`
- Runtime inputs:
  - `observe/discovery/*.md`

#### 5. `reflect/rating/benchmarking/prompt.md`

- Governing spec: none currently present
- Shared contracts: none currently present
- Runtime inputs:
  - `observe/rating/*.md`

#### 6. `reflect/rating/reporting/prompt.md`

- Governing spec: none currently present
- Shared contracts: none currently present
- Runtime inputs:
  - `observe/rating/*.md`

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
  - the runtime input paths listed above for reflect prompts

Freshness rule:

- If any freshness dependency has a newer git commit than the prompt file, mark the prompt `review-needed`

Runtime-input rule:

- A runtime-input file being newer than the prompt does **not** make the prompt stale by itself
- Runtime-input files must still exist and remain compatible with the prompt contract

### Required checks for each prompt

For each prompt:

1. Confirm the prompt file exists
2. Identify its governing spec and shared contracts from the mapping above
3. If the prompt has a `## Required Inputs` section, extract the declared input paths
4. Confirm all declared required-input files exist
5. Confirm the prompt does not directly contradict its governing spec
6. Confirm the prompt's declared inputs are compatible with what the governing spec requires
7. Get the latest git commit for:
   - the prompt file
   - its governing spec
   - each shared contract spec
8. Compare git freshness using the freshness rules above
9. Record findings and assign one final status

### What counts as a direct contradiction

Treat these as direct contradictions:

- prompt references retired workflow language the governing spec forbids
- prompt omits required input declarations required by the governing spec
- prompt asks for run modes where the governing contract says CLI-only
- prompt output contract conflicts with the governing prompt spec
- prompt points to retired output paths where the governing spec defines current paths

Do not treat these alone as contradictions:

- runtime input files changed after the prompt
- wording differences that do not change behavior
- a stub prompt that is explicitly a stub but has no governing spec yet; mark that `review-needed`, not `invalid`

### Report format

Write the report to `workflow/prompts-status/report.md` with exactly this structure:

```md
# Prompt Validity Report — YYYY-MM-DD

**Prompts checked:** N
**Directories scanned:** act/, reflect/

## Summary

| Prompt | Status | Governing Spec | Shared Contracts | Required Inputs | Reason |
| ------ | ------ | -------------- | ---------------- | --------------- | ------ |

## <prompt path>

- **Status:** <valid | review-needed | invalid>
- **Governing spec:** <path or none>
- **Shared contracts:** <comma-separated list or none>
- **Required inputs:** <comma-separated list or none>
- **Freshness dependencies checked:** <comma-separated list or none>
- **Prompt git reference:** `<sha> <date> <subject>` or `untracked`
- **Newer dependency references:** <list or none>
- **Findings:**
  - <finding>
  - <finding>
```

Rules for the report:

- Use one row per prompt in the summary table
- Order prompts by path
- Use one `##` section per prompt after the summary table
- The `Reason` column must be short and high signal
- If a prompt has no governing spec yet, say so explicitly
- If a runtime-input file is newer but ignored by the freshness rule, you may note it in findings but do not change status on that basis alone

### Output behavior

- Write the report to `workflow/prompts-status/report.md`
- Overwrite the file if it already exists
- After writing, give a brief confirmation with the saved path and a one-line summary of how many prompts were `valid`, `review-needed`, and `invalid`
