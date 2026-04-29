## 1. Calibration Contract Update

- [x] 1.1 Update `calibration-archive` to support shared prompt artifacts and isolated OpenSpec proposals.
- [x] 1.2 Update the calibration contract so prompt generation precedes branching for review/proposal work.
- [x] 1.3 Update the calibration contract to require isolated review/proposal context before merge.
- [x] 1.4 Update the calibration contract to require a dedicated calibration branch for synthesis before accepted changes return to `main`.

## 2. Documentation Update

- [x] 2.1 Update `ar-folder-layout` or related structural docs so the README must explain the isolation rule.
- [x] 2.2 Update the README to describe the new calibration flow and link back to this proposal as a detailed rationale.

## 3. Verification

- [x] 3.1 Verify the new calibration model no longer implies result-based calibration as the default.
- [x] 3.2 Verify the new model clearly distinguishes shared prompt visibility from isolated proposal visibility, and does not require separate comparison reports.
