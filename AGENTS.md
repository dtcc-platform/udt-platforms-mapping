# Repository Instructions

This repository is spec-first and uses OpenSpec as a primary change-management workflow.

## Change Routing

Before making any non-trivial change, first decide whether the work should go through the OpenSpec method or be handled as a direct edit.

Treat the change as **OpenSpec-first** when any of the following are true:

- The request changes behavior, workflow, policy, or output contracts.
- The request adds, removes, restructures, or refactors content under `openspec/`.
- The request changes prompt structure, prompt contracts, or research workflow in `act/`, `plan/`, `observe/`, or `reflect/`.
- The user mentions proposals, specs, design, tasks, change management, or OpenSpec explicitly.

Treat the change as a **direct edit** when any of the following are true:

- The user explicitly asks for a direct edit.
- The change is a small typo, wording, formatting, or housekeeping fix with no behavioral or workflow impact.
- The change is clearly local and does not alter the repository's governed contract.

## Required Agent Behavior

If the correct route is not explicit from the user request, the agent must stop and ask a concise question before editing:

`Should I handle this through an OpenSpec change proposal or apply it directly?`

Do not silently choose direct baseline edits for spec or workflow changes when the user's intent about process is unclear.

## OpenSpec Default

When the work is routed through OpenSpec, prefer this sequence:

1. Create or update an OpenSpec change under `openspec/changes/<change-name>/`.
2. Capture rationale in `proposal.md`.
3. Add or update scoped spec deltas under the change.
4. Only update baseline specs directly when the user explicitly asks for that or when the change has already been accepted and is being folded in.

## Safety

- Never revert unrelated user changes in a dirty worktree.
- If baseline specs already differ from archived OpenSpec history, call that out before making structural spec edits.
- When in doubt on process, ask first.
