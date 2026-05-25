## Why

The separate entity discovery benchmark workflow is too heavy for the current research loop. Known missed or at-risk candidates should instead be part of the discovery prompt as a transparent recall checklist, so each model can report whether it found them and explain misses during the same research run.

## What Changes

- Add a new `plan-entity-discovery-recall-checklist` contract for known recall-check entities.
- Add the recall checklist as a required contract in `act/entity-discovery.md`.
- Require entity discovery output to include a recall-check table and explanatory paragraphs below the main summary table.
- Document the tradeoff in the discovery manifest: the checklist improves completeness and explanation but is not a blind recall benchmark because the model can see the known candidates.
- Remove the standalone entity discovery benchmark prompt, plan fixture, observe report, and their OpenSpec capabilities.
- Remove benchmark-specific wording from phase documentation where it no longer applies.

## Capabilities

### New Capabilities

- `plan-entity-discovery-recall-checklist`: Defines known entity recall-check cases as individual requirements.

### Modified Capabilities

- `act-entity-discovery`: Adds the recall checklist contract to the discovery prompt and requires miss categorization.
- `observe-entity-discovery`: Adds the recall-check output section and explanation paragraphs.
- `research-workflow-structure`: Removes standalone benchmark action/report assumptions from the phase structure.
- `act-entity-discovery-benchmark`: Retires the standalone benchmark action.
- `observe-entity-discovery-benchmark-report`: Retires the standalone benchmark report.

## Impact

- Affected files under `act/`, `observe/`, `plan/`, `openspec/specs/`, and phase README documentation.
- Future known recall cases are added by changing `plan-entity-discovery-recall-checklist` with one requirement per entity.
