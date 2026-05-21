## Context

OpenSpec is being narrowed to research workflow contracts. `repo-readme` currently governs root and phase README documentation details, which makes documentation maintenance part of the formal spec surface even when no research behavior changes.

Some durable expectations still matter: phase README files are documentation aids, and prompt interpretation review should be discoverable from the README. Those expectations can live in the workflow and prompt-review specs without preserving a standalone README governance capability.

## Goals / Non-Goals

**Goals:**

- Remove `repo-readme` as an active OpenSpec capability.
- Preserve research-relevant documentation expectations in existing research workflow specs.
- Remove active references that point readers to `repo-readme`.

**Non-Goals:**

- Do not remove root or phase README files.
- Do not prescribe detailed README wording through OpenSpec.
- Do not change research workflow behavior or prompt contracts.

## Decisions

- Retire `repo-readme` rather than rename it.
  - Rationale: documentation governance is not research behavior.
  - Alternative considered: rename it to `repo-documentation`. That would keep the same maintenance burden under a clearer name.

- Keep phase README expectations in `research-workflow-structure`.
  - Rationale: local README files support navigation but are explicitly not canonical research artifacts.
  - Alternative considered: remove all README mentions from specs. That would lose a useful distinction between documentation aids and canonical artifacts.

- Keep prompt interpretation review documentation expectations in `repo-prompt-review`.
  - Rationale: the README mention is part of making that workflow discoverable.
  - Alternative considered: drop README expectations from prompt review. That would make the workflow less visible to contributors.

## Risks / Trade-offs

- Documentation can drift without a dedicated README spec -> Accept this because README wording is not research behavior.
- Some active README links may point to retired `repo-readme` -> Mitigate with a reference scan during implementation.
