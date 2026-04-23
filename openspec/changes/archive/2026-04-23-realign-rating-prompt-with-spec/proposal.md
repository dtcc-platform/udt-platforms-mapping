## Why

`act/rating/prompt.md` is currently marked `review-needed` by the prompt-validity audit because its governing baseline spec was updated after the prompt file. Even when the behavioral gap is small, leaving the prompt chronologically behind its governing spec weakens trust in the prompt/spec relationship.

## What Changes

- Refresh `act/rating/prompt.md` so it clearly reflects the latest baseline spec wording
- Remove any remaining ambiguity around citation override and the authority of `plan/rating/platforms.md`
- Re-run the prompt-validity audit to confirm the rating prompt no longer appears stale relative to its governing spec

## Capabilities

### New Capabilities
- None

### Modified Capabilities
- `act-rating-prompt`: refresh the live prompt wording so it matches the current governing spec and resolves the audit freshness finding

## Impact

- Updates `act/rating/prompt.md`
- Updates the prompt-validity audit report after rerun
- Does not change the rating spec contract itself
