## Why

Prompt review currently says that a different agent should review a resolved prompt, but the minimum review criteria are embedded informally in prose. That leaves too much room for different reviewer agents to check different things or treat review as style feedback.

This change creates a generic prompt-review checklist contract that applies to every resolved prompt, while still allowing reviewer judgment for action-specific risks.

## What Changes

- Add a new `research-prompt-review-checklist` capability.
- Define the minimum checks a third-party prompt reviewer must perform for any resolved prompt.
- Keep the checklist action-agnostic so it works for entity discovery, comparison, reporting, benchmarking, and future prompts.
- Require review output to include a pass/fail judgment, findings, and OpenSpec proposal intent when repository changes are needed.
- Update `research-prompt-review` so review agents use the checklist contract.
- Update README prompt-review documentation with the third-party contract review analogy and a simpler workflow diagram.

## Capabilities

### New Capabilities

- `research-prompt-review-checklist`: Defines the minimum review criteria for third-party review of any resolved prompt.

### Modified Capabilities

- `research-prompt-review`: Requires prompt review to use the generic review checklist and keeps review workflow separate from review criteria.

## Impact

- Adds `openspec/specs/research-prompt-review-checklist/spec.md`.
- Updates `openspec/specs/research-prompt-review/spec.md`.
- Updates `README.md`.
- No changes to prompt output columns, entity classification, or saved research result filenames.
