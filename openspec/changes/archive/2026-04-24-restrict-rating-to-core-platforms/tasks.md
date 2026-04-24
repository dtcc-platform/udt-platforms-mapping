## 1. Narrow the rating scope contract

- [x] 1.1 Update `plan/rating/platforms.md` to use only canonical core-platform rows with `Name` and `Link`
- [x] 1.2 Remove `Layer` from `act/rating/prompt.md` and make the core-platform-only scope explicit
- [x] 1.3 Remove `Layer` from `reflect/rating/reporting/prompt.md` and its CSV schema

## 2. Align the current rating selection

- [x] 2.1 Remove any non-core-platform rows from `plan/rating/platforms.md`
- [x] 2.2 Clarify in the file header why aliases do not belong there

## 3. Validate the change

- [x] 3.1 Confirm `act/rating/prompt.md` Part 1 no longer includes `Layer`
- [x] 3.2 Confirm `reflect/rating/reporting/prompt.md` no longer expects `Layer`
- [x] 3.3 Re-run any relevant prompt-validity or consistency checks after implementation
