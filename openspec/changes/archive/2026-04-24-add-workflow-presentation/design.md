## Context

The repository already treats workflow knowledge as governed material: prompts, planning files, observations, and workflow audits are all traceable and inspectable. A presentation that teaches the workflow should follow the same principle.

The user wants the presentation to remain short and aligned with evolving repository behavior. That rules against managing many per-slide specs. It also argues for keeping the presentation under the existing workflow-level root rather than scattering it across docs or ad hoc deck files.

## Goals / Non-Goals

**Goals:**
- Introduce one governed presentation capability for the workflow tutorial.
- Keep the generated artifact simple: one Pandoc-ready `deck.md`.
- Add a runnable generator prompt so the deck can be refreshed from repository context.
- Make the presentation explicitly tutorial-oriented and consistent with live workflow specs.

**Non-Goals:**
- Add per-slide baseline specs.
- Add `workflow/docs/` in this change.
- Define a complete Pandoc build pipeline or template system.
- Replace the README as the primary reference document.

## Decisions

### Decision: Use one spec for the whole presentation

The capability will be governed by a single baseline spec `workflow-presentation`.

Why:
- The user wants fewer contracts and lower cognitive load.
- The presentation is short and should act as one coherent tutorial, not a collection of separately governed slide contracts.

Alternative considered:
- One spec per slide.
- Rejected because it adds too many artifacts for a short tutorial deck.

### Decision: Use one generator prompt plus one generated deck

The live workflow presentation area will contain:
- `workflow/presentation/prompt.md`
- `workflow/presentation/deck.md`

Why:
- The prompt is the runnable artifact.
- The deck is the renderable Pandoc-ready output.
- This keeps generation explicit without multiplying files.

Alternative considered:
- Only `deck.md` with no generator prompt.
- Rejected because the user wants the presentation to stay aligned with changes, which is easier if the regeneration workflow is explicit.

### Decision: Treat the presentation as a workflow-level artifact

The presentation will live under `workflow/`, not under `reflect/` and not inside `openspec/specs/`.

Why:
- `openspec/specs/` is the governance layer, not the generated artifact layer.
- `workflow/` already holds workflow-level artifacts outside the research cycles.
- The deck is about the whole method, not one cycle outcome.

## Risks / Trade-offs

- [The deck may become stale if the prompt is not rerun after workflow changes] → The spec should explicitly require consistency with live workflow specs and README.
- [The capability may become too broad if the deck grows] → Keep the initial tutorial arc short and bounded.
- [Pandoc rendering details may vary later] → Defer build-pipeline details until there is an actual rendering workflow to govern.
