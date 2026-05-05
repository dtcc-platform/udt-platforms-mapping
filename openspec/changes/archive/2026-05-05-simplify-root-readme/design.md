## Context

The repository now has local README files in each phase folder and repo-wide specs for structure, naming, prompt review, and README documentation. The root README still carries detailed methodology and policy text that can make the entrypoint heavier than necessary.

The root README should orient researchers quickly, then delegate local details to phase README files and formal contracts to OpenSpec specs.

## Goals / Non-Goals

**Goals:**

- Make `README.md` shorter and more researcher-facing.
- Frame the repository as a place for collaborating with agents on Urban Digital Twin platform research.
- Preserve the two useful diagrams: research execution and prompt interpretation review.
- Keep future directions, but compress them into short notes.
- Keep a small pointer to `openspec/specs/` without making formal specs a large README section.

**Non-Goals:**

- Do not redesign the phase README files.
- Do not change canonical artifact names or repository structure.
- Do not change prompt behavior or output contracts.
- Do not remove OpenSpec as the formal source of truth.

## Decisions

- Keep the root README as orientation rather than contract text.
  - Rationale: specs already define formal requirements, and phase README files now explain local folder contents.
  - Alternative considered: keep the current long methodology section. This preserves context but duplicates details already available elsewhere.

- Keep two diagrams in the root README.
  - Rationale: the research execution loop and prompt interpretation review are easier to understand visually than as prose.
  - Alternative considered: one combined diagram. This would be shorter but would blur execution flow and prompt-review flow.

- Keep future directions as short bullets.
  - Rationale: the notes are useful context, but they should not dominate the entrypoint.
  - Alternative considered: remove future directions entirely. This would simplify the README but lose current design intent.

## Risks / Trade-offs

- Too much simplification could hide important workflow constraints -> Keep a tiny pointer to `openspec/specs/` and links to phase README files.
- The root README may become less self-contained -> Keep a compact "how to work" section with enough context to start.
- Phase README wording may drift from the simplified root framing -> Check phase README files during implementation and make small consistency edits only if needed.
