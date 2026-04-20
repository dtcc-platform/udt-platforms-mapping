## Why

Discovery and comparison are distinct phases with different goals, tools, and AI modes — but both prompts currently embed the full scope file (all 13 rubrics) and produce overlapping outputs (discovery scores dimensions it shouldn't; comparison reassesses layer/relevance it shouldn't own). Separating them produces smaller, focused prompts, a single owner for each concern, and a scope file split that matches the two-phase workflow.

## What Changes

- **BREAKING** Split `docs/01-scope.md` into two files: `docs/01-discovery-scope.md` (Layer taxonomy + criteria table only) and `docs/01-comparison-scope.md` (12 dimension rubrics only). The original `docs/01-scope.md` is retired.
- **BREAKING** Drop `Relevance` and `Phase` columns from the inventory CSV. The CSV becomes comparison-only — discovery outputs live in markdown response files only.
- Rewrite the discovery prompt to output only: Name, Link, Org, License, Type, Layer, and Reason (for excluded platforms). No dimension scoring. Layer classification uses a single four-row criteria table (`core-platform`, `backbone`, `domain-module`, `excluded`).
- Rewrite the comparison prompt to score only the 12 dimensions. Remove Layer/Relevance reassessment — those are owned by discovery. Comparison receives discovery rows as input and carries Layer forward unchanged.
- Retire the `relevance-score` spec — Relevance no longer exists as a scored field.
- Drop the seed list from both scope files — it was anchored to Relevance scores which no longer exist.

## Capabilities

### New Capabilities

- `platform-discovery-scope-file`: Defines requirements for the new `docs/01-discovery-scope.md` — the Layer taxonomy table with four rows (`core-platform`, `backbone`, `domain-module`, `excluded`), each with a Definition and observable Criteria column.
- `platform-comparison-scope-file`: Defines requirements for the new `docs/01-comparison-scope.md` — the 12 dimension rubrics only, no Layer taxonomy or Relevance rubric.

### Modified Capabilities

- `platform-discovery-prompt`: Rewrite — output is Layer classification only (no dimension scores); pastes `docs/01-discovery-scope.md` not the full scope; summary table is `Name | Link | Layer | Reason`; excluded platforms get a one-sentence Reason field.
- `platform-comparison-prompt`: Remove Layer/Relevance reassessment; paste `docs/01-comparison-scope.md` only; input rows carry Layer from discovery unchanged; output is 12 dimension scores + profiles.
- `platform-inventory-csv`: Drop `Relevance` and `Phase` columns; CSV is comparison-only; new column order: `Name, Link, Layer, Arch, Open, City, Mature, Integ, Gov, Viz, DM, Sim, IoT, Std, Infra, Model, Date`.
- `platform-discovery-scope`: Retire — replaced by `platform-discovery-scope-file` and `platform-comparison-scope-file`.

## Impact

- `docs/01-scope.md` — retired
- `docs/01-discovery-scope.md` — new file
- `docs/01-comparison-scope.md` — new file
- `docs/05-platform-inventory.csv` — column schema change; existing discovery rows dropped; Relevance and Phase columns removed
- `prompts/platform-discovery.md` — full rewrite
- `prompts/platform-comparison.md` — partial rewrite (remove reassessment sections)
- `openspec/specs/relevance-score/spec.md` — retired
- `openspec/specs/platform-discovery-scope/spec.md` — retired, replaced by two new specs
