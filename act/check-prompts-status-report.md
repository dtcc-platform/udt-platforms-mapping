# Prompt Status Report — 2026-04-28

**Prompts checked:** 7
**Directories scanned:** act/, reflect/

## Summary

| Prompt | Status | Governing Spec | Shared Contracts | Required Inputs | Reason |
| ------ | ------ | -------------- | ---------------- | --------------- | ------ |
| `act/udt-initiatives/prompt.md` | `valid` | `openspec/specs/act-udt-initiatives-prompt/spec.md` | `openspec/specs/prompt-markdown-format/spec.md` | `plan/udt-initiatives/scope.md` | Prompt and contract are aligned |
| `act/udt-platform-comparison/prompt.md` | `valid` | `openspec/specs/act-udt-platform-comparison-prompt/spec.md` | `openspec/specs/prompt-markdown-format/spec.md` | `plan/udt-platform-comparison/rubrics.md`, `plan/udt-platform-comparison/platforms.md`, `plan/udt-platform-comparison/source-policy.md` | Prompt and contract are aligned |
| `act/udt-platforms/prompt.md` | `valid` | `openspec/specs/act-udt-platforms-prompt/spec.md` | `openspec/specs/prompt-markdown-format/spec.md` | `plan/udt-platforms/scope.md` | Prompt and contract are aligned |
| `reflect/udt-platform-comparison/benchmarking/prompt.md` | `review-needed` | `none` | `none` | `none` | Stub prompt has no governing spec yet |
| `reflect/udt-platform-comparison/reporting/prompt.md` | `valid` | `openspec/specs/reflect-udt-platform-comparison-reporting/spec.md` | `none` | `observe/udt-platform-comparison/*.md` | Prompt and contract are aligned |
| `reflect/udt-platforms/benchmarking/prompt.md` | `valid` | `openspec/specs/reflect-udt-platforms-benchmarking/spec.md` | `none` | `reflect/udt-platforms/benchmarking/benchmark.md`, `observe/udt-platforms/*.md` | Prompt and contract are aligned |
| `reflect/udt-platforms/reporting/prompt.md` | `valid` | `openspec/specs/reflect-udt-platforms-reporting-prompt/spec.md` | `none` | `observe/udt-platforms/*.md` | Prompt and contract are aligned |

## act/udt-initiatives/prompt.md

- **Status:** `valid`
- **Governing spec:** `openspec/specs/act-udt-initiatives-prompt/spec.md`
- **Shared contracts:** `openspec/specs/prompt-markdown-format/spec.md`
- **Required inputs:** `plan/udt-initiatives/scope.md`
- **Freshness dependencies checked:** `openspec/specs/act-udt-initiatives-prompt/spec.md`, `openspec/specs/prompt-markdown-format/spec.md`
- **Prompt git reference:** `working tree modified`
- **Newer dependency references:** none
- **Findings:**
  - Required inputs exist at the `udt-initiatives` path.
  - Prompt uses the governed initiative table contract.
  - Prompt is web-canonical and writes to the `observe/udt-initiatives/web-<model-short>.md` pattern.

## act/udt-platform-comparison/prompt.md

- **Status:** `valid`
- **Governing spec:** `openspec/specs/act-udt-platform-comparison-prompt/spec.md`
- **Shared contracts:** `openspec/specs/prompt-markdown-format/spec.md`
- **Required inputs:** `plan/udt-platform-comparison/rubrics.md`, `plan/udt-platform-comparison/platforms.md`, `plan/udt-platform-comparison/source-policy.md`
- **Freshness dependencies checked:** `openspec/specs/act-udt-platform-comparison-prompt/spec.md`, `openspec/specs/prompt-markdown-format/spec.md`
- **Prompt git reference:** `67e1cf7`
- **Newer dependency references:** none
- **Findings:**
  - Required-input files exist at the renamed comparison paths.
  - Prompt behavior matches the platform-only comparison contract.
  - Prompt is web-canonical and writes to the `observe/udt-platform-comparison/web-<model-short>.md` pattern.

## act/udt-platforms/prompt.md

- **Status:** `valid`
- **Governing spec:** `openspec/specs/act-udt-platforms-prompt/spec.md`
- **Shared contracts:** `openspec/specs/prompt-markdown-format/spec.md`
- **Required inputs:** `plan/udt-platforms/scope.md`
- **Freshness dependencies checked:** `openspec/specs/act-udt-platforms-prompt/spec.md`, `openspec/specs/prompt-markdown-format/spec.md`
- **Prompt git reference:** `working tree modified after 67e1cf7`
- **Newer dependency references:** none
- **Findings:**
  - Required inputs exist at the renamed `udt-platforms` paths.
  - Prompt uses the new `Type`-based artifact contract.
  - Prompt now frames `udt-platforms` as a broad global discovery thread rather than a strict source-policy workflow.
  - Prompt is web-canonical and writes to the `observe/udt-platforms/web-<model-short>.md` pattern.

## reflect/udt-platform-comparison/benchmarking/prompt.md

- **Status:** `review-needed`
- **Governing spec:** `none`
- **Shared contracts:** `none`
- **Required inputs:** `none`
- **Freshness dependencies checked:** `none`
- **Prompt git reference:** `67e1cf7`
- **Newer dependency references:** none
- **Findings:**
  - Stub prompt exists at the renamed path.
  - No governing spec exists yet for the benchmarking workflow.

## reflect/udt-platform-comparison/reporting/prompt.md

- **Status:** `valid`
- **Governing spec:** `openspec/specs/reflect-udt-platform-comparison-reporting/spec.md`
- **Shared contracts:** `none`
- **Required inputs:** `observe/udt-platform-comparison/*.md`
- **Freshness dependencies checked:** `openspec/specs/reflect-udt-platform-comparison-reporting/spec.md`
- **Prompt git reference:** `67e1cf7`
- **Newer dependency references:** none
- **Findings:**
  - Prompt scans the renamed comparison observe path.
  - Prompt metadata filter and output paths match the current baseline spec.

## reflect/udt-platforms/benchmarking/prompt.md

- **Status:** `valid`
- **Governing spec:** `openspec/specs/reflect-udt-platforms-benchmarking/spec.md`
- **Shared contracts:** `none`
- **Required inputs:** `reflect/udt-platforms/benchmarking/benchmark.md`, `observe/udt-platforms/*.md`
- **Freshness dependencies checked:** `openspec/specs/reflect-udt-platforms-benchmarking/spec.md`
- **Prompt git reference:** `67e1cf7`
- **Newer dependency references:** none
- **Findings:**
  - Benchmark fixture exists with the new `Type` column.
  - Prompt scans the renamed `udt-platforms` observe path.

## reflect/udt-platforms/reporting/prompt.md

- **Status:** `valid`
- **Governing spec:** `openspec/specs/reflect-udt-platforms-reporting-prompt/spec.md`
- **Shared contracts:** `none`
- **Required inputs:** `observe/udt-platforms/*.md`
- **Freshness dependencies checked:** `openspec/specs/reflect-udt-platforms-reporting-prompt/spec.md`
- **Prompt git reference:** `67e1cf7`
- **Newer dependency references:** none
- **Findings:**
  - Prompt scans the renamed `udt-platforms` observe path.
  - Prompt extracts the `Name`, `Link`, `Type`, `Reason` table contract expected by the current baseline spec.
