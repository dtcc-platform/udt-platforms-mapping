## Context

All three researcher-facing prompt files follow the same two-zone structure: a human-facing usage header above, and an AI-facing prompt body below. The boundary between zones is marked by a horizontal rule and a `> Paste into your AI session from this line onwards.` blockquote. This convention allows researchers to paste only the AI-facing body into their session without accidentally including usage instructions.

`platform-discovery.md` and `platform-comparison.md` both implement this convention correctly. `prompts/license-analysis.md` has the horizontal rule but is missing the cut-line blockquote, so the zone boundary is unmarked. The omission was introduced when the file was originally structured and was not caught until the `improve-web-research-prompt-portability` verification.

## Goals / Non-Goals

**Goals:**
- Add the missing cut-line blockquote to `prompts/license-analysis.md` so all three prompts follow the same two-zone convention.
- Update the governing spec to require the cut-line.

**Non-Goals:**
- Do not change any prompt instructions, output schemas, or usage steps.
- Do not restructure or reformat any other section of the file.

## Decisions

### Decision: Add the blockquote in the same position as the other two prompts

The cut-line should appear immediately after the `---` horizontal rule that closes the usage header, and immediately before `## Prompt`. This matches the exact position in `platform-discovery.md:12` and `platform-comparison.md:16` and requires no other structural changes.

Alternatives considered:
- Remove the cut-line from discovery and comparison instead. Rejected — the cut-line is a useful operational convention worth preserving.

## Risks / Trade-offs

- [Change is cosmetic] → No functional risk; any researcher already pasting from `## Prompt` downward is unaffected.
