## Context

The comparison and license prompts both use a 4-step numbered list in their usage header:
1. Open the discovery response / relevant file
2. Copy the relevant rows
3. Replace the placeholder token
4. Paste into AI session

The discovery prompt instead uses two sentences of inline prose followed by two blockquote lines. This is the last remaining header-style inconsistency across the three prompts.

## Goals / Non-Goals

**Goals:**
- Rewrite the discovery prompt usage header as a numbered list matching the comparison/license pattern
- Update the spec requirement to mandate this format

**Non-Goals:**
- Changing the prompt body content
- Changing the `[SEARCH_SCOPE]` token or any other prompt mechanics

## Decisions

**Numbered-step format** — the discovery workflow has fewer mechanical steps than comparison/license (no row-copy step, just replace a scope token), so the list is shorter (3 steps instead of 4). Steps: replace `[SEARCH_SCOPE]`, paste, save response. The save-as instruction moves into the final step rather than a separate blockquote.

**Remove blockquotes** — the `> **Source of truth…**` and `> **Save response as…**` blockquotes are replaced by inline step text and a plain `> **Save response as:**` line consistent with how comparison formats its save-as note.

## Risks / Trade-offs

Minimal. This is a cosmetic change to the usage header only; no prompt logic changes.
