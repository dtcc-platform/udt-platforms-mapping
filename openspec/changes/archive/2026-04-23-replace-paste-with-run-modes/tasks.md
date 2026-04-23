## 1. Create plan/rating/platforms.md

- [x] 1.1 Create `plan/rating/platforms.md` with a short header paragraph explaining the file's purpose (per-run platform selection, comparison-scope boundary, must include DTCC)
- [x] 1.2 Add the three-column GFM table header (`Name`, `Link`, `Layer`) below the paragraph
- [x] 1.3 Seed with the DTCC row plus any platforms currently in-scope for the active rating cycle (lift from the most recent discovery response's summary table)

## 2. Rewrite act/discovery/prompt.md

- [x] 2.1 Remove the cut-line blockquote (`> Paste into your AI session from this line onwards.`) and the four-step numbered paste instructions from the usage header
- [x] 2.2 Add a `## Required Inputs` section listing `plan/discovery/scope.md` with a short description of what it provides
- [x] 2.3 Add a `## Run Modes` section instructing the AI to ask the user "Run as CLI or Web?" and defining each mode's behavior, including the save-as path (`observe/discovery/cli-<model-short>.md` or `observe/discovery/web-<model-short>.md`)
- [x] 2.4 Remove the `[PASTE_SCOPE_HERE]` token and the canonical placeholder-guard block immediately preceding it
- [x] 2.5 Rewrite prompt-body references to "pasted scope content" as "the Layer criteria from the required inputs" (single edit, consistent phrasing)
- [x] 2.6 Keep the existing requirements around Layer classification output, summary table, DTCC required entry, Markdown rules, uncertainty handling, and primary sources — these do not change

## 3. Rewrite act/rating/prompt.md

- [x] 3.1 Remove the cut-line blockquote and numbered paste instructions from the usage header
- [x] 3.2 Add a `## Required Inputs` section listing `plan/rating/rubrics.md`, `plan/rating/platforms.md`, and `plan/rating/source-policy.md` with short descriptions of each
- [x] 3.3 Add a `## Run Modes` section (same shape as the discovery prompt)
- [x] 3.4 Remove the `[PASTE_SCOPE_HERE]` token, the `[PASTE_SELECTED_PLATFORMS_HERE]` token, and their preceding guard and scope-boundary instruction blocks
- [x] 3.5 Remove the inline source-policy-like text from the Research Instructions section — `plan/rating/source-policy.md` is now the single source of truth and is inlined by the resolver
- [x] 3.6 Update the DTCC reference wording to point at `plan/rating/platforms.md` instead of the pasted table row
- [x] 3.7 Rewrite body references to "pasted scope/rubrics" as "the rubrics from the required inputs"
- [x] 3.8 Update the save-as filename note to match the `cli-` / `web-` prefix convention

## 4. Rename existing observe/ response files with web- prefix

- [x] 4.1 `observe/discovery/claude.md` → `observe/discovery/web-claude.md`
- [x] 4.2 `observe/discovery/chatgpt.md` → `observe/discovery/web-chatgpt.md`
- [x] 4.3 `observe/discovery/gemini.md` → `observe/discovery/web-gemini.md`
- [x] 4.4 `observe/rating/claude.md` → `observe/rating/web-claude.md`
- [x] 4.5 `observe/rating/chatgpt.md` → `observe/rating/web-chatgpt.md`
- [x] 4.6 `observe/rating/gemini.md` → `observe/rating/web-gemini.md`

## 5. Update reflect/ prompts to reflect the new filename convention

- [x] 5.1 Update `reflect/discovery/benchmarking/prompt.md` — note that `observe/discovery/*.md` filenames carry `cli-` / `web-` prefixes; the `model` field in the YAML metadata remains the authoritative column header (no change to report structure needed)
- [x] 5.2 Update `reflect/discovery/reporting/prompt.md` — same note about the new filename convention
- [x] 5.3 Regenerate `reflect/discovery/benchmarking/coverage.md` after renaming to confirm the report still builds cleanly

## 6. Add Design section to README.md

- [x] 6.1 Add a new `## Design` section to `README.md` covering:
  - The run-modes model — how the AI CLI asks CLI-or-Web, and what each mode does
  - Why `plan/rating/platforms.md` is a file, not a CLI argument — per-run selections become git-diffable and reviewable across cycle runs, making "what did we compare in cycle 2 vs cycle 1?" a simple git log
  - The distinction between `plan/` definitions (scope, rubrics, source-policy — slow-moving) and `plan/` per-run data (platforms.md — changes each run)
  - The response filename convention: `cli-<model>.md` or `web-<model>.md` in `observe/*/`, with the prefix as the single authority on interface

## 7. Validate

- [x] 7.1 Run `openspec validate --strict` and resolve any surfaced deltas — `openspec validate replace-paste-with-run-modes --strict` passes; the 7 pre-existing baseline spec validation failures are unrelated to this change
- [x] 7.2 Confirm `openspec/specs/prompt-paste-boundary/` and `openspec/specs/prompt-placeholder-guard/` are removed from the baseline when this change archives — both delta files use `## REMOVED Requirements` for every requirement in the baseline specs; archive will drop the spec folders
- [x] 7.3 Confirm `openspec/specs/prompt-run-modes/` and `openspec/specs/plan-rating-platforms/` appear in the baseline when this change archives — both delta files use `## ADDED Requirements` declaring new capabilities; archive will create the spec folders
