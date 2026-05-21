## Context

The active act specs are mostly aligned to phase-object-role naming. Three remaining action capabilities still use the old `-prompt` suffix even though they govern action behavior rather than prompt wording alone.

The live files under `act/` already use researcher-facing verb phrases and should stay as-is. The OpenSpec capability names should identify the phase, object, and artifact role.

## Goals / Non-Goals

**Goals:**

- Rename the remaining active `act-*prompt` capabilities for report and benchmark actions.
- Update live act manifest required contract paths and self-declared behavior contract names.
- Preserve existing reporting, benchmarking, and reflect output behavior.
- Keep naming guidance consistent with the renamed capabilities.

**Non-Goals:**

- Do not rename live files under `act/`.
- Do not change reporting extraction, sorting, CSV, HTML, or synthesis behavior.
- Do not design platform comparison benchmarking beyond preserving the current stub.

## Decisions

- Use `act-platform-comparison-benchmark` for the platform comparison benchmark stub.
  - Rationale: the object is `platform-comparison`; the role is `benchmark`.
  - Alternative considered: `act-benchmark-platform-comparison`. That preserves the live verb-first file shape but does not follow capability naming guidance.

- Use `act-platform-comparison-report` for comparison ecosystem export behavior.
  - Rationale: it matches `act-<object>-<artifact-role>` and pairs with `reflect-platform-comparison-ecosystem`.
  - Alternative considered: `act-platform-comparison-reporting`. The shorter noun role is consistent with `benchmark`.

- Use `act-platform-discovery-report` for platform discovery ecosystem synthesis behavior.
  - Rationale: it names the action by object and role without retaining the prompt suffix.
  - Alternative considered: `act-platform-ecosystem-report`. That describes the output more than the source action.

## Risks / Trade-offs

- Stale references may keep pointing to retired `-prompt` specs -> Mitigate with active-file reference scans during apply.
- Remaining archived references will still contain old names -> Leave archived history unchanged.
- The live act filenames remain verb-first while specs are object-first -> This is intentional and documented in `repo-naming-conventions`.
