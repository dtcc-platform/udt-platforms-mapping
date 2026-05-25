## Why

The entity discovery benchmark still carries a `Tags` column and baseline entries that make it look like a broad fixture instead of a small set of accepted recall checks. The benchmark should stay minimal and use `Type` for classification rather than duplicating diagnostic tag concepts.

## What Changes

- Remove the `Tags` column from the entity discovery benchmark fixture.
- Remove broad baseline entries that are not needed as recall-miss benchmark cases.
- Seed the benchmark with accepted missing-candidate cases, starting with GeoDatalytics.
- Update the benchmark action and report contracts to stop requiring tags.
- Update the saved benchmark report shape to match the simplified fixture.

## Capabilities

### New Capabilities

### Modified Capabilities

- `act-entity-discovery-benchmark`: Reads benchmark fixtures without `Tags`.
- `observe-entity-discovery-benchmark-report`: Reports recall and novel finds without `Tags`.

## Impact

- Affected benchmark fixture, benchmark prompt contract, observed benchmark report, and archived change record.
- No changes to entity discovery classification rules.
