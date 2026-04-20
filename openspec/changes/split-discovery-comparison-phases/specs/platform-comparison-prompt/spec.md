## MODIFIED Requirements

### Requirement: Comparison prompt includes a [PASTE_SCOPE_HERE] guard

The prompt template SHALL include a `[PASTE_SCOPE_HERE]` placeholder where the researcher pastes the full content of `docs/01-comparison-scope.md` before running a session. The placeholder SHALL be preceded by a guard instruction telling the model: if `[PASTE_SCOPE_HERE]` still appears verbatim, stop and ask the user to paste `docs/01-comparison-scope.md` before continuing.

The usage header SHALL direct the researcher to paste `docs/01-comparison-scope.md` — not `docs/01-scope.md` or `docs/01-discovery-scope.md`.

#### Scenario: Researcher runs the comparison without pasting scope

- **WHEN** a researcher pastes the comparison prompt into an AI session without replacing `[PASTE_SCOPE_HERE]`
- **THEN** the model stops and asks them to provide the comparison scope content before producing any output

#### Scenario: Researcher runs the comparison after pasting scope

- **WHEN** a researcher pastes `docs/01-comparison-scope.md` content into the `[PASTE_SCOPE_HERE]` slot
- **THEN** the model proceeds with all 12 dimension rubrics available and produces a complete comparison response

### Requirement: Comparison prompt Part 1 scoring table includes functional category columns

The Part 1 scoring table SHALL include a `Layer` column and the six dimension columns and six functional category columns. It SHALL NOT include a `Relevance` column — Relevance is retired.

The `Layer` column SHALL appear immediately after `Link`. It SHALL carry the Layer value from the pasted discovery row unchanged. The comparison AI SHALL NOT reassess or revise the Layer assignment — Layer is owned by the discovery phase.

Each score column SHALL use the same 1–5 integer scoring format — bare integer, `?` for unknown, no `/5` suffix in table cells.

The prompt SHALL include a legend immediately below the Part 1 table instruction listing each abbreviated column header with its full name and one-line description.

#### Scenario: Researcher reads the Part 1 table

- **WHEN** an AI responds to the comparison prompt
- **THEN** the Part 1 table header contains exactly: `Name`, `Link`, `Layer`, `Arch`, `Open`, `City`, `Mature`, `Integ`, `Gov`, `Viz`, `DM`, `Sim`, `IoT`, `Std`, `Infra`

#### Scenario: Researcher compares functional strengths across platforms

- **WHEN** an AI responds to the comparison prompt
- **THEN** every platform row contains a numeric 1–5 score (or `?`) in every dimension and category column, and the Layer value from the discovery row

#### Scenario: Layer value is carried through unchanged

- **WHEN** a discovery row with `Layer=backbone` is pasted into the comparison prompt
- **THEN** the Part 1 table contains `backbone` in the Layer column for that platform; the comparison AI does not reassess or revise it

## REMOVED Requirements

### Requirement: Comparison prompt Part 1 scoring table includes functional category columns (Layer/Relevance reassessment)
**Reason**: Relevance is retired. Layer reassessment is removed — discovery owns Layer. The Part 1 table retains Layer as a carried-through value but comparison never revises it.
**Migration**: Remove Relevance column and layer revision instruction from the prompt. Layer is read-only in comparison.
