# Design

## Overview

Use first-token effect scope for capability names:

- `repo-*` for repository-wide structure, conventions, and shared contracts
- `plan-*` for planning artifacts
- `act-*` for execution prompt artifacts
- `observe-*` for saved-output artifacts if introduced later
- `reflect-*` for reflection, benchmarking, and reporting artifacts

The current change only renames active repo-wide capabilities. It does not rename phase-scoped capabilities because they already follow the desired pattern.

## Decisions

- Use `repo-naming-conventions` rather than `git-naming-conventions` because the spec governs more than Git; it also covers OpenSpec change names.
- Use `repo-prompt-review` rather than `workflow-prompt-review` because the review workflow is a repository-wide governance contract for prompt/spec fidelity.
- Keep human-facing README phrasing as "Prompt Interpretation Review" where useful; the capability name can be shorter and more systematic.

## Migration

Rename capability directories and update direct links/references in active specs and README. Do not rewrite older archive contents.
