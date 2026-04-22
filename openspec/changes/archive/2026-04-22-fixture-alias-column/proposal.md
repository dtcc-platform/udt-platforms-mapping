## Why

The eval's name-matching is case-insensitive substring search, so variant names in discovery responses (e.g., "CityEnergyAnalyst" vs "City Energy Analyst") produce false negatives. A researcher has no way to record these corrections without editing the eval script itself.

## What Changes

- Add an optional `Aliases` column to every fixture table in `tests/discovery-fixtures.md`
- The eval prompt reads the `Aliases` cell for each platform and treats any listed name as an additional match target (case-insensitive substring)
- Known variant names are back-filled for platforms already observed to produce name mismatches
- The coverage report format is unchanged

## Capabilities

### New Capabilities

- `fixture-alias-column`: The `Aliases` column in the fixture table — its schema, formatting convention, and how the eval uses it for matching

### Modified Capabilities

- `discovery-fixtures-file`: New optional column added to table schema
- `discovery-eval-prompt`: Step 3 matching logic extended to check aliases

## Impact

- `tests/discovery-fixtures.md` — column added to all five gap-category tables
- `tests/eval-discovery.md` — Step 3 matching instruction updated
- No changes to response files, prompts, or the coverage report format
