## 1. Contracts

- [x] 1.1 Update the baseline folder-layout contract to replace `discovery` and `rating` with `udt-platforms`, `udt-initiatives`, and `udt-platform-comparison`.
- [x] 1.2 Update the baseline calibration contract examples to use the new cycle names.
- [x] 1.3 Add baseline cycle contracts for `udt-platforms`, `udt-initiatives`, and `udt-platform-comparison`.

## 2. Canonical Paths

- [x] 2.1 Create or rename canonical cycle folders under `plan/`, `act/`, `observe/`, and `reflect/` to match the new cycle names.
- [x] 2.2 Replace old path references in live prompts, plan files, and reflection prompts so they point to the new cycle paths.
- [x] 2.3 Retire or replace old `discovery` / `rating`-named prompt and plan artifacts that are superseded by the new cycle model.

## 3. Cycle Inputs And Outputs

- [x] 3.1 Replace the outgoing discovery Layer contract with the `udt-platforms` technical-artifact table contract.
- [x] 3.2 Introduce the `udt-initiatives` initiative table contract, including the `Uses` field.
- [x] 3.3 Update the comparison-cycle selection contract so only `Type = platform` rows from `udt-platforms` are eligible.

## 4. Documentation

- [x] 4.1 Rewrite README cycle descriptions, quick-start references, and diagrams to use the new cycle names and handoff rules.
- [x] 4.2 Update any remaining baseline spec wording that still treats initiatives as part of the old discovery cycle or treats the third cycle as generic rating.

## 5. Verification

- [x] 5.1 Run the prompt-status check after the path and contract changes are implemented.
- [x] 5.2 Verify that no active README or baseline spec still presents `discovery` / `rating` as the canonical cycle model.
