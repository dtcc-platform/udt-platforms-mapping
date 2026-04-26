## Why

The repository has accumulated workflow-only structure that is now heavier than needed. The intended operating model is simpler: keep `plan/`, `act/`, `observe/`, and `reflect/` as the canonical research interface, use OpenSpec as the shared contract layer for prompt calibration, and move agent-comparison artifacts into a dedicated archival area.

## What Changes

- Introduce a top-level `calibration/` area for archival prompt/result comparisons using the path pattern `calibration/<research>/<cycle>/<agent>/`.
- Keep canonical research execution in `plan/`, `act/`, `observe/`, and `reflect/`.
- Add `act/check-prompts-status.md` as the maintained entry point for prompt/spec status checks.
- Retire the top-level `workflow/` area from the active repository model.
- Retire the workflow presentation capability and remove it from the active folder contract.
- Reframe `observe/` as the home of accepted reference outputs and canonical saved outputs, while calibration artifacts live outside it.
- Update README and folder-contract language to describe the repository as two coordinated parts:
  - prompt calibration
  - research execution

## Capabilities

### New Capabilities
- `act-check-prompts-status`: A CLI maintenance prompt under `act/` for checking prompt/spec alignment and writing a status report.
- `calibration-archive`: The archival prompt/result comparison area at `calibration/<research>/<cycle>/<agent>/`.

### Modified Capabilities
- `ar-folder-layout`: Retire `workflow/`, introduce `calibration/`, and define the simplified canonical repository model.
- `workflow-prompts-status`: Move the maintained prompt-status behavior from `workflow/prompts-status/` to `act/check-prompts-status.md`.
- `workflow-presentation`: Retire the workflow presentation capability from the active repository model.

## Impact

- Affects top-level folder semantics and path contracts.
- Affects prompt-status prompt and report paths.
- Retires `workflow/presentation/` from the active model.
- Requires README and spec alignment with the simplified calibration-versus-research workflow.
