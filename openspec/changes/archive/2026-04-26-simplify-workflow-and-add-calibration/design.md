## Context

The current repository mixes two concerns:

- canonical research execution under the Action Research folders
- workflow-level maintenance and presentation artifacts under `workflow/`

Recent workflow exploration clarified a simpler model. The repository should keep `plan/`, `act/`, `observe/`, and `reflect/` as the accepted interface for doing research and keeping accepted results. Prompt comparison across agents should move into a separate archival area whose purpose is calibration rather than execution.

This change also removes the need for a workflow-only presentation area and simplifies prompt-status from a workflow subsystem into a runnable maintenance prompt under `act/`.

## Goals / Non-Goals

**Goals:**
- Keep canonical research execution in `plan/`, `act/`, `observe/`, and `reflect/`
- Introduce `calibration/` as a dedicated archival area for prompt/result comparison
- Move prompt-status checking to a single entry point at `act/check-prompts-status.md`
- Retire `workflow/` from the active repository model
- Align README and baseline folder contracts with the simplified model

**Non-Goals:**
- Flatten `act/discovery/prompt.md` and `act/rating/prompt.md` into root-level files
- Redesign discovery/rating prompt content in this change
- Expand calibration artifacts beyond `prompt.md` and `result.md`
- Keep the workflow presentation capability active

## Decisions

### Decision: Separate calibration from canonical research execution

The repository will distinguish:

- canonical research execution under `plan/`, `act/`, `observe/`, `reflect/`
- archival prompt calibration under `calibration/`

`calibration/` is chosen over `runs/` because the folder’s purpose is not merely to store executions. Its purpose is to compare prompt realizations and resulting outputs across agents against the same accepted contract.

Alternative considered:
- `runs/`
  - Rejected because it describes the fact that execution occurred, but not the purpose of the area.

### Decision: Use `calibration/<research>/<cycle>/<agent>/` as the archival path

Calibration paths will encode:

- research type such as `discovery` or `rating`
- cycle identifier such as `c1`
- agent identity

The folder content remains intentionally minimal:

- `prompt.md`
- `result.md`

Alternative considered:
- flatter `calibration/<agent>/...`
  - Rejected because it loses research and cycle meaning in the path.

### Decision: Keep canonical prompts under `act/<cycle>/prompt.md`

Canonical prompts remain:

- `act/discovery/prompt.md`
- `act/rating/prompt.md`

This preserves the existing governed research interface and avoids flattening path conventions in the same change.

Alternative considered:
- `act/discovery.md` and `act/rating.md`
  - Rejected because the current path structure is already live and understandable, and flattening would add extra churn.

### Decision: Move prompt-status into `act/check-prompts-status.md`

Prompt-status remains a maintained capability, but it no longer needs a separate top-level workflow area. It is better modeled as a runnable maintenance prompt in `act/`.

This keeps the capability discoverable while removing the extra `workflow/` abstraction.

Alternative considered:
- retire prompt-status entirely
  - Rejected because prompt/spec drift checks are still useful.
- keep `workflow/prompts-status/`
  - Rejected because it preserves an extra top-level concept the repository is intentionally dropping.

### Decision: Retire workflow presentation from the active model

The presentation capability is no longer needed as a governed workflow subsystem. The README is the primary explanation artifact, and a generated deck is no longer part of the intended active structure.

Alternative considered:
- keep presentation and README together
  - Rejected because it adds a second explanatory artifact to maintain.

## Risks / Trade-offs

- [README leads the live specs today] → This change must explicitly realign folder and capability contracts with the simpler model.
- [Retiring `workflow/` removes some previous structure] → Keep the underlying governance ideas in README and OpenSpec rather than in a separate folder.
- [Calibration could grow beyond two files over time] → Start with the minimal archival contract and expand later only if needed.
- [Prompt-status under `act/` broadens the meaning of `act/`] → Accept `act/` as the home of canonical runnable prompts, including maintenance prompts.

## Migration Plan

1. Add baseline contracts for `calibration/` and `act/check-prompts-status.md`.
2. Update `ar-folder-layout` to remove `workflow/` from the active model and add `calibration/`.
3. Retire the workflow presentation capability.
4. Replace workflow prompt-status path references with the new `act/check-prompts-status.md` path.
5. Update README to explain the two-part model:
   - prompt calibration
   - research execution

## Open Questions

- Whether `observe/` should eventually standardize a single accepted reference filename per research type is intentionally deferred.
- Whether additional calibration metadata should be added later is intentionally deferred.
