## Why

The repository maintains two redundant license-specific artifacts — `docs/04-license-review.md` and `prompts/license-analysis.md` — whose substantive content is already partially covered by the Openness & Licensing dimension in `docs/01-scope.md`. The license prompt produces a structured citation-rich report that is not needed for a landscape survey; the comparison prompt's Open dimension paragraph already fulfils that role. The only real gap is that the `Open` rubric leaves "open data formats" and "restrictive data formats" undefined.

## What Changes

- **`docs/01-scope.md`**: Annotate three rubric levels in the `Open` dimension to close the gap:
  - Level 5: define "open data formats" as OGC standards, CityGML, IFC, or equivalent
  - Level 4: distinguish strong copyleft (GPL — derivatives must be open) from weak copyleft (LGPL/MPL — linking permitted without triggering copyleft)
  - Level 3: define "restrictive data formats" as proprietary export formats with no open standard alternative
- **`docs/04-license-review.md`**: **BREAKING** — delete. Content absorbed into the `Open` rubric.
- **`prompts/license-analysis.md`**: **BREAKING** — delete. The structured license report it produces is superseded by the Open dimension analysis in the comparison prompt.
- **`docs/02-methodology.md`**: Remove the reference to `prompts/license-analysis.md` in the workflow description.

## Capabilities

### New Capabilities

_(none)_

### Modified Capabilities

- `platform-discovery-scope`: Open rubric criteria updated with data format and copyleft annotations

## Impact

- `docs/01-scope.md` — Open rubric levels 3, 4, 5 updated
- `docs/04-license-review.md` — deleted
- `prompts/license-analysis.md` — deleted
- `docs/02-methodology.md` — license-analysis reference removed
- Existing `responses/*-license.md` files are not affected (historical records)
