## Context

The prompt-validity audit marks `act/rating/prompt.md` as `review-needed` because `openspec/specs/act-rating-prompt/spec.md` was updated after the prompt file. The change required by the audit is small: the live prompt should be refreshed so the prompt/spec relationship is explicit again.

## Goals / Non-Goals

**Goals:**
- Bring `act/rating/prompt.md` into clear alignment with the current baseline spec
- Keep the change minimal and wording-focused
- Clear the freshness finding in the prompt-validity audit report

**Non-Goals:**
- Change the behavior contract of the rating workflow
- Modify the governing spec
- Redesign the rating prompt structure

## Decisions

### 1. Use a minimal prompt refresh

Update only the parts of `act/rating/prompt.md` that need to be refreshed for clear conformance with the current spec.

Rationale:
- The prompt is already structurally close to the governing spec
- A small refresh is safer than a wholesale rewrite

### 2. Re-run the prompt-validity audit after the prompt update

The audit report should be regenerated as part of this change so the repository records the post-fix status.

Rationale:
- The prompt-validity tooling was added specifically to catch and verify this kind of drift

## Risks / Trade-offs

- [Small wording change misses a subtle mismatch] → Mitigation: keep the edit spec-led and rerun the audit immediately after the prompt update
- [Audit report changes for unrelated files] → Mitigation: document that the rerun updates the whole report, not only the rating prompt row
