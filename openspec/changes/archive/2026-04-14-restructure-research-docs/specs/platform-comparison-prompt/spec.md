## REMOVED Requirements

### Requirement: Comparison prompt defines functional category rubrics
**Reason:** Functional category rubrics (Viz, DM, Sim, IoT, Std, Infra) are no longer embedded inline in the comparison prompt. All rubric definitions are supplied at run time by pasting `docs/01-scope.md` into the `[PASTE_SCOPE_HERE]` slot.
**Migration:** Rubrics are maintained in `docs/01-scope.md` and pasted into the prompt before each session via `[PASTE_SCOPE_HERE]`. The requirement that the same rubrics appear in `docs/02-methodology.md` is also removed — `01-scope.md` is the single canonical source.

### Requirement: Comparison prompt covers the six research dimensions with scoring
**Reason:** Superseded by the updated requirement below that covers all twelve dimensions (six research + six functional) with rubrics supplied via pasted scope rather than inline.
**Migration:** See MODIFIED requirement below.

## MODIFIED Requirements

### Requirement: Comparison prompt covers twelve dimensions with scoring
The prompt template SHALL instruct the model to compare platforms across all twelve dimensions — the six research dimensions (Technical Architecture, Openness & Licensing, City-Scale Capability, Maturity & Adoption, Integration Posture, Governance) and the six functional categories (Visualization, Data Management, Simulation, IoT Sensing, Standards, Infrastructure) — and assign each platform a score of 1–5 per dimension using rubrics defined in the pasted scope content.

The prompt SHALL state that rubrics are supplied via `[PASTE_SCOPE_HERE]` and are not embedded inline.

#### Scenario: Response covers all twelve dimensions with scores
- **WHEN** an AI responds to the comparison prompt
- **THEN** the response addresses each of the twelve dimensions for every platform and assigns a numeric 1–5 score with rationale

#### Scenario: Researcher compares scores across agents
- **WHEN** a researcher runs the same comparison on two different AI agents
- **THEN** both responses use the same dimension labels and scoring scale, making scores comparable

### Requirement: Comparison prompt includes a [PASTE_SCOPE_HERE] guard
The prompt template SHALL include a `[PASTE_SCOPE_HERE]` placeholder where the researcher pastes the full content of `docs/01-scope.md` before running a session. The placeholder SHALL be preceded by a guard instruction telling the model: _if `[PASTE_SCOPE_HERE]` still appears verbatim, stop and ask the user to paste `docs/01-scope.md` before continuing._

The usage header SHALL be updated to include a step directing the researcher to paste `docs/01-scope.md` into the `[PASTE_SCOPE_HERE]` slot as the first preparation step.

#### Scenario: Researcher runs the comparison without pasting scope
- **WHEN** a researcher pastes the comparison prompt into an AI session without replacing `[PASTE_SCOPE_HERE]`
- **THEN** the model stops and asks them to provide the scope content before producing any output

#### Scenario: Researcher runs the comparison after pasting scope
- **WHEN** a researcher pastes `docs/01-scope.md` content into the `[PASTE_SCOPE_HERE]` slot
- **THEN** the model proceeds with all 13 rubrics available and produces a complete comparison response
