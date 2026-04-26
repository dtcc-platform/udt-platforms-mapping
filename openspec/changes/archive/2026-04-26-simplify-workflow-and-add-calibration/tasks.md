## 1. Retire workflow-level structure

- [x] 1.1 Remove `workflow/` from the active README and folder-model documentation
- [x] 1.2 Remove or relocate live `workflow/prompts-status/` artifacts to the new `act/` prompt-status path
- [x] 1.3 Remove or retire live `workflow/presentation/` artifacts from the active repository model

## 2. Introduce calibration and act-based prompt-status

- [x] 2.1 Add the live `act/check-prompts-status.md` prompt
- [x] 2.2 Add the live `act/check-prompts-status-report.md` output path or its generated artifact handling
- [x] 2.3 Add the top-level `calibration/` area and align its live usage with `calibration/<research>/<cycle>/<agent>/prompt.md` and `result.md`

## 3. Realign canonical contracts and documentation

- [x] 3.1 Update baseline specs to add `act-check-prompts-status`
- [x] 3.2 Update baseline specs to add `calibration-archive`
- [x] 3.3 Update `ar-folder-layout` and related contracts to retire `workflow/` and describe the canonical-versus-calibration split
- [x] 3.4 Update `README.md` so it explains the two-part model: prompt calibration and research execution

## 4. Verify and finalize

- [x] 4.1 Run the prompt-status check from its new `act/` entry point and confirm paths are aligned
- [x] 4.2 Verify no active README or baseline spec still describes `workflow/` as part of the live model
- [x] 4.3 Archive or remove retired live artifacts that no longer belong after the migration
