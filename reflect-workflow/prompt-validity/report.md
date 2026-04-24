# Prompt Validity Report — 2026-04-23

**Prompts checked:** 6
**Directories scanned:** act/, reflect/

## Summary

| Prompt                                     | Status          | Governing Spec                                                 | Shared Contracts                                                                           | Required Inputs                                                                      | Reason                                                         |
| ------------------------------------------ | --------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| `act/discovery/prompt.md`                  | `valid`         | `openspec/specs/act-discovery-prompt/spec.md`                  | `openspec/specs/prompt-run-modes/spec.md`, `openspec/specs/prompt-markdown-format/spec.md` | `plan/discovery/scope.md`                                                            | Prompt, spec, and required input declaration are aligned       |
| `act/rating/prompt.md`                     | `valid`         | `openspec/specs/act-rating-prompt/spec.md`                     | `openspec/specs/prompt-run-modes/spec.md`, `openspec/specs/prompt-markdown-format/spec.md` | `plan/rating/rubrics.md`, `plan/rating/platforms.md`, `plan/rating/source-policy.md` | Prompt refreshed to match current governing spec               |
| `reflect/discovery/benchmarking/prompt.md` | `valid`         | `openspec/specs/reflect-discovery-benchmarking-prompt/spec.md` | `openspec/specs/reflect-discovery-benchmarking-coverage/spec.md`                           | `reflect/discovery/benchmarking/benchmark.md`, `observe/discovery/*.md`              | Prompt and governing contracts are aligned                     |
| `reflect/discovery/reporting/prompt.md`    | `invalid`       | `openspec/specs/reflect-discovery-reporting-prompt/spec.md`    | `openspec/specs/reflect-discovery-reporting-ecosystem/spec.md`                             | `observe/discovery/*.md`                                                             | Live prompt contradicts its governing spec and output contract |
| `reflect/rating/benchmarking/prompt.md`    | `review-needed` | `none`                                                         | `none`                                                                                     | `observe/rating/*.md`                                                                | Stub prompt has no governing spec yet                          |
| `reflect/rating/reporting/prompt.md`       | `review-needed` | `none`                                                         | `none`                                                                                     | `observe/rating/*.md`                                                                | Stub prompt has no governing spec yet                          |

## act/discovery/prompt.md

- **Status:** `valid`
- **Governing spec:** `openspec/specs/act-discovery-prompt/spec.md`
- **Shared contracts:** `openspec/specs/prompt-run-modes/spec.md`, `openspec/specs/prompt-markdown-format/spec.md`
- **Required inputs:** `plan/discovery/scope.md`
- **Freshness dependencies checked:** `openspec/specs/act-discovery-prompt/spec.md`, `openspec/specs/prompt-run-modes/spec.md`, `openspec/specs/prompt-markdown-format/spec.md`
- **Prompt git reference:** `07592f5 2026-04-23 feat: replace prompt paste mechanic with CLI/Web run modes`
- **Newer dependency references:** none
- **Findings:**
  - The prompt declares the single required input required by its governing spec.
  - The required input file exists.
  - The prompt follows the current CLI/Web run-modes contract and does not show retired paste workflow language.

## act/rating/prompt.md

- **Status:** `valid`
- **Governing spec:** `openspec/specs/act-rating-prompt/spec.md`
- **Shared contracts:** `openspec/specs/prompt-run-modes/spec.md`, `openspec/specs/prompt-markdown-format/spec.md`
- **Required inputs:** `plan/rating/rubrics.md`, `plan/rating/platforms.md`, `plan/rating/source-policy.md`
- **Freshness dependencies checked:** `openspec/specs/act-rating-prompt/spec.md`, `openspec/specs/prompt-run-modes/spec.md`, `openspec/specs/prompt-markdown-format/spec.md`
- **Prompt git reference:** `working tree updated after 07592f5 2026-04-23 feat: replace prompt paste mechanic with CLI/Web run modes`
- **Newer dependency references:** `0c98d0c 2026-04-23 fix(specs): align rating specs with current inputs`
- **Findings:**
  - The prompt declares all three required input files and they exist.
  - The prompt now explicitly states that the `Layer` value comes from the corresponding row in `plan/rating/platforms.md`, matching the current baseline spec wording.
  - The prompt now explicitly overrides default citation behavior and requires `[Description](https://...)` inline links.
  - The prompt has been refreshed after the governing spec update, so it no longer needs freshness review.
  - A newer `plan/rating/platforms.md` alone would not change this status because per-run data is ignored for freshness.

## reflect/discovery/benchmarking/prompt.md

- **Status:** `valid`
- **Governing spec:** `openspec/specs/reflect-discovery-benchmarking-prompt/spec.md`
- **Shared contracts:** `openspec/specs/reflect-discovery-benchmarking-coverage/spec.md`
- **Required inputs:** `reflect/discovery/benchmarking/benchmark.md`, `observe/discovery/*.md`
- **Freshness dependencies checked:** `openspec/specs/reflect-discovery-benchmarking-prompt/spec.md`, `openspec/specs/reflect-discovery-benchmarking-coverage/spec.md`
- **Prompt git reference:** `07592f5 2026-04-23 feat: replace prompt paste mechanic with CLI/Web run modes`
- **Newer dependency references:** none
- **Findings:**
  - The prompt is CLI-only, which matches its governing spec.
  - The fixture file exists and the prompt scans the current `observe/discovery/` location.
  - The output path and report structure remain compatible with the coverage report contract.

## reflect/discovery/reporting/prompt.md

- **Status:** `invalid`
- **Governing spec:** `openspec/specs/reflect-discovery-reporting-prompt/spec.md`
- **Shared contracts:** `openspec/specs/reflect-discovery-reporting-ecosystem/spec.md`
- **Required inputs:** `observe/discovery/*.md`
- **Freshness dependencies checked:** `openspec/specs/reflect-discovery-reporting-prompt/spec.md`, `openspec/specs/reflect-discovery-reporting-ecosystem/spec.md`
- **Prompt git reference:** `07592f5 2026-04-23 feat: replace prompt paste mechanic with CLI/Web run modes`
- **Newer dependency references:** none
- **Findings:**
  - The governing prompt spec still requires a legacy inventory workflow that extracts `Phase` and `Relevance` rows from discovery and comparison responses.
  - The shared output contract says `reflect/discovery/reporting/ecosystem.csv` is comparison-only and that `Relevance` and `Phase` are retired.
  - The live prompt still instructs the model to extract discovery rows, comparison rows, `Phase`, and `Relevance`, so the prompt contradicts its current output contract.
  - The governing prompt spec and the shared ecosystem spec are themselves inconsistent, and the live prompt currently follows the stale prompt spec rather than the live ecosystem contract.

## reflect/rating/benchmarking/prompt.md

- **Status:** `review-needed`
- **Governing spec:** none
- **Shared contracts:** none
- **Required inputs:** `observe/rating/*.md`
- **Freshness dependencies checked:** none
- **Prompt git reference:** `940878b 2026-04-22 refactor(repo): restructure to action research phase/cycle layout`
- **Newer dependency references:** none
- **Findings:**
  - The file is an explicit stub.
  - No governing baseline prompt spec exists yet for this live prompt.
  - The prompt remains reviewable and intentionally incomplete, so it is not marked `invalid`.

## reflect/rating/reporting/prompt.md

- **Status:** `review-needed`
- **Governing spec:** none
- **Shared contracts:** none
- **Required inputs:** `observe/rating/*.md`
- **Freshness dependencies checked:** none
- **Prompt git reference:** `940878b 2026-04-22 refactor(repo): restructure to action research phase/cycle layout`
- **Newer dependency references:** none
- **Findings:**
  - The file is an explicit stub.
  - No governing baseline prompt spec exists yet for this live prompt.
  - The prompt remains reviewable and intentionally incomplete, so it is not marked `invalid`.
