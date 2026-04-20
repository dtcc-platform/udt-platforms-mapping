## ADDED Requirements

### Requirement: docs/01-comparison-scope.md exists and contains the 12 dimension rubrics

The repository SHALL contain a file at `docs/01-comparison-scope.md`. This file is the sole scope reference for comparison sessions — researchers paste its full content into the `[PASTE_SCOPE_HERE]` slot in the comparison prompt before running a session.

The file SHALL contain the 12 dimension and functional category rubrics (Arch, Open, City, Mature, Integ, Gov, Viz, DM, Sim, IoT, Std, Infra) as the canonical source for comparison scoring. Each rubric SHALL define criteria for scores 0–5.

The file SHALL NOT contain the Layer criteria table, the Relevance rubric, a seed list, or target corpus size. Those belong in `docs/01-discovery-scope.md` or are retired.

The file SHALL include a brief header explaining its purpose: it defines the dimension scoring rubrics used in the comparison phase.

#### Scenario: Researcher prepares a comparison session

- **WHEN** a researcher is about to run a comparison session
- **THEN** they paste the full content of `docs/01-comparison-scope.md` into the `[PASTE_SCOPE_HERE]` slot in the comparison prompt — not the full `docs/01-scope.md` or the discovery scope

#### Scenario: Comparison AI scores a platform dimension

- **WHEN** a comparison AI reads the rubrics and assesses a platform's Technical Architecture
- **THEN** it assigns a score 1–5 per the Arch rubric criteria from the pasted scope content

#### Scenario: Researcher updates a dimension rubric

- **WHEN** a researcher needs to refine the criteria for a dimension score level
- **THEN** they edit `docs/01-comparison-scope.md` only; the comparison prompt receives the updated rubric at run time via the paste step

#### Scenario: Researcher runs discovery after updating comparison scope

- **WHEN** a researcher updates `docs/01-comparison-scope.md`
- **THEN** discovery sessions are unaffected — discovery pastes `docs/01-discovery-scope.md` which is unchanged
