## Context

Each prompt spec currently embeds a block of common Markdown rules:

- permitted syntax
- inline Markdown citation format
- prohibited syntax
- whitespace rules

Those rules are semantically identical across the three prompt capabilities, but they are maintained three times. The repo already has precedent for extracting truly shared prompt conventions into independent platform-level specs such as `prompt-paste-boundary` and `prompt-placeholder-guard`.

At the same time, not all formatting rules are shared. Prompt-specific output constraints differ in ways that matter:

- discovery requires `##` platform headings and a specific table/section score format
- comparison requires `###` profile headings, profile score placement, and table score rules
- license analysis uses a flat score field with bare integers and no `X/5` notation

The design therefore needs to extract only the genuinely common Markdown contract and leave the prompt-specific output contract where it belongs.

## Goals / Non-Goals

**Goals:**
- Define one shared spec for the identical Markdown portability rules used by prompt templates
- Remove duplicated common-rule text from the three prompt specs
- Preserve prompt-specific formatting constraints in their existing prompt specs
- Keep the resulting spec set easy to read and maintain

**Non-Goals:**
- Changing prompt behavior or scoring logic
- Converting prompt files into includes or templated composition
- Moving prompt-specific heading or score notation rules into the shared spec
- Reorganizing unrelated prompt requirements

## Decisions

**1. Extract only the truly identical Markdown rules**

The shared `prompt-markdown-format` spec will own:
- permitted syntax
- citation format
- prohibited syntax
- whitespace rules

These are the cross-cutting portability rules that are identical across prompt types.

Alternatives considered:
- Extract all formatting rules into one spec: rejected because heading levels, score notation, and score placement differ meaningfully by prompt
- Keep all formatting local: rejected because it preserves unnecessary duplication and drift risk

**2. Keep prompt-specific deltas local**

Each prompt spec will continue to define only its own unique formatting requirements:

- discovery: `##` heading level, inline `**Dimension (X/5):**` notation, bare numbers in table cells, explicit citation override note
- comparison: `###` profile headings, `X/5` score notation, inline score placement in profile labels, bare numeric table cells
- license analysis: bare numeric `**Score:**` field with no `/5`

This keeps the shared spec small and the prompt specs concrete.

**3. Shared contract remains normative, prompt files remain standalone**

The shared spec is a governance artifact, not a runtime include mechanism. Prompt files stay self-contained copy-paste files. During implementation, the prompt bodies may still contain the shared Markdown text verbatim; the refactor is about how the requirements are governed, not about introducing file composition.

## Risks / Trade-offs

- [Risk] Contributors may move too much into the shared spec later and blur prompt-specific requirements
  - Mitigation: the shared spec explicitly scopes itself to common Markdown portability rules only
- [Risk] Prompt files and specs may temporarily diverge during transition
  - Mitigation: tasks include updating prompt files after the spec refactor is accepted
- [Trade-off] The spec graph gains one more capability
  - Acceptable because it removes repeated normative text and matches the repo's existing pattern for shared prompt contracts

## Migration Plan

1. Add the new `prompt-markdown-format` spec under the change
2. Update the three prompt spec deltas to reference the shared Markdown contract and keep only prompt-specific formatting rules
3. If the change is implemented, update the corresponding prompt files so their Markdown sections still satisfy the shared contract plus each prompt's local deltas
4. Fold the new shared spec and modified prompt specs into the baseline only after the change is accepted
