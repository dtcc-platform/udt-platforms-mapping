## 1. Update fixture tables

- [ ] 1.1 Add `Aliases` column header to all five gap-category tables in `tests/discovery-fixtures.md`
- [ ] 1.2 Back-fill known aliases: add `CityEnergyAnalyst` for City Energy Analyst, `CesiumJS` for Cesium / CesiumJS, and any other variants observed in the current coverage report

## 2. Update eval prompt

- [ ] 2.1 Update Step 1 in `tests/eval-discovery.md` to instruct Claude Code to extract the `Aliases` cell per platform in addition to `Name`, `Link`, and `Expected Layer`
- [ ] 2.2 Update Step 3 matching logic: for each fixture platform, build a match set = canonical Name + all aliases (split on `,`, trimmed); mark found if any member matches case-insensitively as a substring of the response Name value

## 3. Re-run eval and verify

- [ ] 3.1 Run `tests/eval-discovery.md` and confirm previously false-negative platforms (e.g., City Energy Analyst) now show ✓ found
- [ ] 3.2 Update `tests/reports/coverage.md` with the corrected results
