## Context

Prompt generation now starts from behavior and output specs. That improves contract fidelity, but the generated platform discovery prompt was less ergonomic than the maintained canonical prompt because the specs did not define reusable web prompt shape.

The missing behavior is shared across the three main research prompts: platform discovery, initiative discovery, and platform comparison.

## Goals / Non-Goals

**Goals:**

- Define reusable web prompt structure once.
- Improve generated prompt quality for the three canonical research prompts.
- Keep action-specific behavior in action-specific prompt specs.
- Reuse `repo-prompt-markdown-format` instead of duplicating formatting rules.

**Non-Goals:**

- Do not include benchmark prompts.
- Do not include report prompts.
- Do not change output contracts.
- Do not make generated comparison artifacts canonical.

## Decisions

- Add `repo-web-prompt-template` as a cross spec.
  - Rationale: resolver sections, copy-ready output, metadata handling, and paste/save guidance are common prompt-template behavior.
  - Alternative considered: duplicate requirements directly in each prompt spec. That would work but create drift.

- Keep action-specific requirements in each `act-*` prompt spec.
  - Rationale: platform Type classification, initiative `Uses = ?`, and platform comparison scoring/scope are not generic prompt-template behavior.
  - Alternative considered: make the cross spec too broad. That would blur shared shape and research behavior.

- Keep benchmark and report prompts out of scope.
  - Rationale: the user explicitly excluded benchmark prompts, and report prompts may have different ergonomics.

## Risks / Trade-offs

- Cross spec may become too generic to be useful -> Keep it focused on reusable web prompt structure.
- Prompt specs may become layered -> Use explicit references: conform to `repo-web-prompt-template`, conform to `repo-prompt-markdown-format`, then define action-specific behavior.
- Existing prompts may need small updates during apply -> Update only the three in-scope prompts.
