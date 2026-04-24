## Why

Rating is only meaningful in this repository for full UDT platforms, not for backbones or domain modules. Keeping `Layer` in the rating selection and scoring artifacts encourages a broader comparison scope that blurs the semantic split between discovery and rating.

## What Changes

- Restrict the rating workflow to `core-platform` entries only
- Remove `Layer` from `plan/rating/platforms.md` because inclusion in rating already implies `core-platform`
- Remove `Layer` from the Part 1 scoring table in `act/rating/prompt.md`
- Update rating reporting so its extracted CSV schema no longer expects or emits `Layer`
- Clarify that aliases do not belong in rating scope because rating compares selected canonical rows, not fuzzy-matched names

## Capabilities

### New Capabilities

### Modified Capabilities

- `act-rating-prompt`: narrow the comparison contract to core platforms and remove `Layer` from Part 1 output
- `plan-rating-platforms`: make the selection file a two-column canonical core-platform scope boundary
- `reflect-rating-reporting-prompt`: remove `Layer` from the extracted Part 1 schema and downstream CSV contract
- `reflect-rating-reporting-ecosystem`: define the rating export as core-platform-only and layer-free

## Impact

- Affects `plan/rating/platforms.md`
- Affects `act/rating/prompt.md`
- Affects `reflect/rating/reporting/prompt.md`
- Changes the expected Part 1 table and rating export CSV schema
