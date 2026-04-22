## Why

The coverage report groups results under `## Tag:` section headings, recreating the multi-table structure that was just removed from the benchmark. A flat single table with a `Tags` column is consistent with the benchmark design and easier to scan.

## What Changes

- The recall section of the coverage report becomes one flat table: `Platform | Layer | Tags | <model-1> | <model-2> | ...`
- The `## Tag: <tag>` section headings are removed
- `run.md` Step 5 report template is updated to match

## Capabilities

### New Capabilities

_(none)_

### Modified Capabilities

- `discovery-eval-prompt`: report template changes — recall section is a single flat table instead of per-tag sections
- `discovery-coverage-report`: report structure changes — single recall table with Tags column

## Impact

- `evals/discovery/run.md` — Step 5 report template updated
- `evals/discovery/reports/coverage.md` — rewritten with flat table
