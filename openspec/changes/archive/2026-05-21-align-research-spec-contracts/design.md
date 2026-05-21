## Context

The active OpenSpec set has been narrowed toward research workflow. The remaining generic `repo-*` capabilities either define research-facing contracts under generic names or govern prompt review as a separate process spec.

This change keeps naming and Markdown output formatting as first-class research contracts, while folding prompt review into the research workflow structure where it belongs.

## Goals / Non-Goals

**Goals:**

- Remove remaining generic `repo-*` capability names from active specs.
- Keep artifact naming and Markdown output formatting behavior intact under research-oriented names.
- Fold prompt interpretation review into `research-workflow-structure`.
- Update active manifest and spec references.

**Non-Goals:**

- Do not change output format rules.
- Do not change prompt behavior, discovery behavior, comparison behavior, or reporting behavior.
- Do not rename live phase files solely because a spec name changes.

## Decisions

- Use `research-artifact-naming` for naming conventions.
  - Rationale: naming applies across `plan/`, `act/`, `observe/`, `reflect/`, and OpenSpec capabilities.
  - Alternative considered: `plan-research-artifact-naming`. That over-anchors a cross-phase naming contract in `plan`.

- Use `observe-markdown-output-format` for Markdown formatting.
  - Rationale: the contract governs observed Markdown outputs produced by prompts.
  - Alternative considered: `research-markdown-format`. That is broader but less tied to the output phase.

- Fold `repo-prompt-review` into `research-workflow-structure`.
  - Rationale: prompt interpretation review is part of maintaining research workflow fidelity, not a standalone repo contract.
  - Alternative considered: rename to `reflect-prompt-fidelity-review`. That keeps a separate capability but preserves process overhead.

## Risks / Trade-offs

- Renaming formatting specs touches several prompt contracts -> Mitigate with active reference scans.
- Folding prompt review makes `research-workflow-structure` broader -> Accept because it centralizes workflow-level governance.
- Archived changes will still contain old `repo-*` names -> Leave archived history unchanged.
