# Prompt Validity Report — 2026-04-24

**Prompts checked:** 6
**Directories scanned:** act/, reflect/

## Summary

| Prompt                                     | Status          | Governing Spec                                                 | Shared Contracts                                                                           | Required Inputs                                                                      | Reason                                                   |
| ------------------------------------------ | --------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| `act/discovery/prompt.md`                  | `valid`         | `openspec/specs/act-discovery-prompt/spec.md`                  | `openspec/specs/prompt-run-modes/spec.md`, `openspec/specs/prompt-markdown-format/spec.md` | `plan/discovery/scope.md`                                                            | Prompt, spec, and required input declaration are aligned |
| `act/rating/prompt.md`                     | `review-needed` | `openspec/specs/act-rating-prompt/spec.md`                     | `openspec/specs/prompt-run-modes/spec.md`, `openspec/specs/prompt-markdown-format/spec.md` | `plan/rating/rubrics.md`, `plan/rating/platforms.md`, `plan/rating/source-policy.md` | Governing spec still contains stale Layer wording        |
| `reflect/discovery/benchmarking/prompt.md` | `review-needed` | `openspec/specs/reflect-discovery-benchmarking/spec.md`        | `none`                                                                                     | `reflect/discovery/benchmarking/benchmark.md`, `observe/discovery/*.md`              | Governing spec is newer than the live prompt             |
| `reflect/discovery/reporting/prompt.md`    | `invalid`       | `openspec/specs/reflect-discovery-reporting-prompt/spec.md`    | `none`                                                                                     | `observe/discovery/*.md`                                                             | Live sort rule exceeds governing spec                    |
| `reflect/rating/benchmarking/prompt.md`    | `review-needed` | `none`                                                         | `none`                                                                                     | `observe/rating/*.md`                                                                | Stub prompt has no governing spec yet                    |
| `reflect/rating/reporting/prompt.md`       | `review-needed` | `openspec/specs/reflect-rating-reporting/spec.md`              | `none`                                                                                     | `observe/rating/*.md`                                                                | Governing spec is newer than the live prompt             |

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
  - The prompt follows the current CLI/Web run-modes contract and the shared Markdown contract.

## act/rating/prompt.md

- **Status:** `review-needed`
- **Governing spec:** `openspec/specs/act-rating-prompt/spec.md`
- **Shared contracts:** `openspec/specs/prompt-run-modes/spec.md`, `openspec/specs/prompt-markdown-format/spec.md`
- **Required inputs:** `plan/rating/rubrics.md`, `plan/rating/platforms.md`, `plan/rating/source-policy.md`
- **Freshness dependencies checked:** `openspec/specs/act-rating-prompt/spec.md`, `openspec/specs/prompt-run-modes/spec.md`, `openspec/specs/prompt-markdown-format/spec.md`
- **Prompt git reference:** `2c32b95 2026-04-24 refactor: restrict rating workflow to core platforms`
- **Newer dependency references:** none
- **Findings:**
  - The prompt declares all three required input files and they exist.
  - The live prompt is aligned with the current two-column `plan/rating/platforms.md` file and the core-platform-only scope.
  - The governing spec still contains stale wording in its Required Inputs section describing `plan/rating/platforms.md` as `rows of Name, Link, Layer`.
  - I am inferring `review-needed` from that internal spec drift signal rather than from a freshness mismatch.

## reflect/discovery/benchmarking/prompt.md

- **Status:** `valid`
- **Governing spec:** `openspec/specs/reflect-discovery-benchmarking/spec.md`
- **Shared contracts:** `none`
- **Required inputs:** `reflect/discovery/benchmarking/benchmark.md`, `observe/discovery/*.md`
- **Freshness dependencies checked:** `openspec/specs/reflect-discovery-benchmarking/spec.md`
- **Prompt git reference:** `07592f5 2026-04-23 feat: replace prompt paste mechanic with CLI/Web run modes`
- **Newer dependency references:** `uncommitted baseline change: openspec/specs/reflect-discovery-benchmarking/spec.md`
- **Findings:**
  - The prompt is now governed by the unified baseline spec at `openspec/specs/reflect-discovery-benchmarking/spec.md`.
  - The fixture file exists and the prompt scans the current `observe/discovery/` location.
  - The governing baseline spec is newer than the live prompt, so the prompt is currently `review-needed`.

## reflect/discovery/reporting/prompt.md

- **Status:** `invalid`
- **Governing spec:** `openspec/specs/reflect-discovery-reporting-prompt/spec.md`
- **Shared contracts:** `none`
- **Required inputs:** `observe/discovery/*.md`
- **Freshness dependencies checked:** `openspec/specs/reflect-discovery-reporting-prompt/spec.md`
- **Prompt git reference:** `e750370 2026-04-24 fix: normalize discovery reporting sort order`
- **Newer dependency references:** none
- **Findings:**
  - The prompt and governing spec agree on discovery-only extraction and `ecosystem.md` output.
  - The live prompt now sorts by a shared base-domain family key so `dtcc.chalmers.se`, `www.dtcc.chalmers.se`, and `platform.dtcc.chalmers.se` stay together.
  - The governing spec still defines the ordering rule only in terms of normalized host/domain plus `www.` stripping.
  - That is a direct contract mismatch, so the prompt is marked `invalid` until the governing spec is updated to match the live sort rule.

## reflect/rating/benchmarking/prompt.md

- **Status:** `review-needed`
- **Governing spec:** `none`
- **Shared contracts:** `none`
- **Required inputs:** `observe/rating/*.md`
- **Freshness dependencies checked:** none
- **Prompt git reference:** `940878b 2026-04-22 refactor(repo): restructure to action research phase/cycle layout`
- **Newer dependency references:** none
- **Findings:**
  - The file is an explicit stub.
  - No governing baseline prompt spec exists for this live prompt.
  - The runtime input path exists as a pattern target, but the prompt remains intentionally incomplete.

## reflect/rating/reporting/prompt.md

- **Status:** `review-needed`
- **Governing spec:** `openspec/specs/reflect-rating-reporting/spec.md`
- **Shared contracts:** `none`
- **Required inputs:** `observe/rating/*.md`
- **Freshness dependencies checked:** `openspec/specs/reflect-rating-reporting/spec.md`
- **Prompt git reference:** `2c32b95 2026-04-24 refactor: restrict rating workflow to core platforms`
- **Newer dependency references:** `uncommitted baseline change: openspec/specs/reflect-rating-reporting/spec.md`
- **Findings:**
  - The live prompt is now governed by the merged baseline spec at `openspec/specs/reflect-rating-reporting/spec.md`.
  - The prompt-status audit mapping has been updated to use that merged capability.
  - The governing baseline spec is newer than the live prompt, so the prompt remains `review-needed`.
  - This is a freshness issue rather than evidence that the live rating reporting prompt itself is broken.
