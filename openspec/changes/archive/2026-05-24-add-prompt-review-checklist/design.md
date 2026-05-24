## Context

The repository uses prompt review to catch prompt-composition and interpretation problems before running research. The process is governed by `research-prompt-review`, but the reviewer checklist is not yet a reusable contract.

Separating process from review criteria keeps the workflow clear:

- `research-prompt-review` governs when and how review happens.
- `research-prompt-review-checklist` governs what the third-party reviewer must check.

## Goals / Non-Goals

**Goals:**

- Define a minimum prompt-review checklist for any resolved prompt.
- Preserve reviewer judgment beyond the minimum checklist.
- Keep review focused on contract faithfulness, composition, executability, and target-runner fit.
- Make required repository fixes flow through OpenSpec proposal intent.
- Document the process in README using the third-party contract review analogy.

**Non-Goals:**

- Turn prompt review into a rigid script.
- Require saved review artifacts by default.
- Define action-specific review rules for entity discovery only.
- Replace human judgment or third-party agent judgment.

## Decisions

- Create a separate `research-prompt-review-checklist` capability rather than expanding `research-prompt-review` with a long checklist. This keeps workflow and criteria independently understandable.
- Use SHALL for the minimum checklist and MAY for additional reviewer findings. This gives repeatability without preventing useful judgment.
- Require proposal intent for fixes that change repository behavior, specs, manifests, documentation, skills, or generated prompt conventions.
- Keep README high-level and refer to the spec for the checklist details instead of duplicating every check.

## Risks / Trade-offs

- A checklist can become mechanical. Mitigation: explicitly allow reviewer-added findings beyond the minimum checks.
- A separate spec adds one more contract. Mitigation: it clarifies the value of review and keeps `research-prompt-review` shorter.
