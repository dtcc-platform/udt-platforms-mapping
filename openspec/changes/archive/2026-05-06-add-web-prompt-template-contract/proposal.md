## Why

The current prompt specs govern action-specific behavior, but they do not share a reusable contract for web prompt ergonomics. This makes generated prompts faithful to behavior specs but weaker than maintained prompts for repeated web use.

A cross-spec for canonical web prompt structure will make generated prompts more usable and reduce duplicated requirements across discovery and comparison prompts.

## What Changes

- Add a repo-wide web prompt template contract for canonical research prompts.
- Require the three canonical research prompts to conform to that template:
  - `act/discover-platforms.md`
  - `act/discover-initiatives.md`
  - `act/compare-platforms.md`
- Keep benchmark and report prompts out of scope.
- Keep action-specific behavior in the individual prompt specs.
- Keep shared Markdown formatting in `repo-prompt-markdown-format`.

## Capabilities

### New Capabilities

- `repo-web-prompt-template`: Defines shared structure for canonical web prompt templates, including resolver sections, required contracts, run inputs, copy-ready output, rendered output contracts, metadata blocks, and paste/save guidance.

### Modified Capabilities

- `act-discover-platforms-prompt`: Require conformance to `repo-web-prompt-template` for the canonical platform discovery prompt.
- `act-discover-initiatives-prompt`: Require conformance to `repo-web-prompt-template` for the canonical initiative discovery prompt.
- `act-compare-platforms-prompt`: Require conformance to `repo-web-prompt-template` for the canonical platform comparison prompt.
- `repo-prompt-markdown-format`: Clarify that the web prompt template contract reuses this shared Markdown formatting contract rather than duplicating it.

## Impact

- Affects prompt specs for platform discovery, initiative discovery, and platform comparison.
- May later affect `act/discover-platforms.md`, `act/discover-initiatives.md`, and `act/compare-platforms.md` during apply.
- Does not affect benchmark or report prompt specs.
- Does not change observe output contracts.
