## Context

Prompt files in `prompts/` are fill-in templates. Some require the user to replace a placeholder with real data before the prompt can be used. When referenced via `@file` without filling in the placeholder, models silently proceed with incomplete input and produce useless output. The fix is a guard instruction block inserted immediately before each placeholder.

## Goals / Non-Goals

**Goals:**
- Define a canonical guard instruction wording usable across any prompt file
- Apply the guard to `platform-comparison.md` (`[PASTE_SELECTED_PLATFORMS_HERE]`) and `license-analysis.md` (`[PASTE_SELECTED_PLATFORM_HERE]`)
- Ensure consistent wording so the pattern is recognisable and easy to replicate in future prompts

**Non-Goals:**
- Programmatic placeholder detection or tooling
- Changes to prompt logic, scoring rubrics, or output format
- Any prompt files that do not currently have unfilled placeholders

## Decisions

**1. Guard as inline instruction block, not a file-level preamble**

The guard is placed immediately before the placeholder it protects, not at the top of the file. This keeps the check contextually adjacent to the missing data and makes it obvious which placeholder it covers when a prompt has more than one.

Alternatives considered:
- Top-of-file preamble: would work but is easy to miss when a prompt has many preamble paragraphs already.
- Separate `USAGE.md` instruction file: does not travel with the prompt when copy-pasted.

**2. Canonical wording**

```
**Before proceeding:** If the placeholder below still contains the literal text `[PLACEHOLDER_TEXT]`, stop and ask the user to supply the required data before continuing. Do not attempt to generate output without it.
```

The wording uses `[PLACEHOLDER_TEXT]` as a slot; each instance substitutes the exact placeholder string used in that prompt.

Alternatives considered:
- Softer wording ("consider asking"): too weak — models may still proceed.
- Longer explanation: unnecessary; the instruction is self-contained.

## Risks / Trade-offs

- [Risk] A model may still ignore the guard instruction → Mitigation: canonical imperative wording ("stop and ask") minimises this; no purely technical fix exists for model non-compliance.
- [Risk] Guard wording drifts across prompts → Mitigation: spec defines the canonical template; future prompts must copy it verbatim.

## Migration Plan

1. Add guard block to `prompts/platform-comparison.md` before `[PASTE_SELECTED_PLATFORMS_HERE]`
2. Add guard block to `prompts/license-analysis.md` before `[PASTE_SELECTED_PLATFORM_HERE]`
3. No rollback needed — the change is additive text only.
