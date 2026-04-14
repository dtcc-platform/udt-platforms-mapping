## REMOVED Requirements

### Requirement: Scope document states inclusion criteria in operational terms
**Reason:** The three named inclusion criteria (Explicit UDT, City-Scale Capabilities, Adjacent Architecture or Governance) are replaced by the Relevance 0–5 rubric. Operational guidance is now expressed as score-level descriptions in the rubric.
**Migration:** Use the Relevance rubric levels 3–5 in `docs/01-scope.md` as the replacement for the three inclusion criteria. Levels 3–5 map to the former inclusion categories respectively.

### Requirement: Scope document lists explicit exclusion examples
**Reason:** Named exclusion criteria (Spec or Standard, Single Domain, General Purpose) are replaced by Relevance levels 0–1. The concept of "excluded with a named label" no longer exists; out-of-scope platforms receive Relevance 0 or 1.
**Migration:** Platforms previously labelled with exclusion criteria now receive Relevance 0 (not assessed) or Relevance 1 (assessed and found out of scope). The `Criterion` column in discovery responses is replaced by the `Relevance` score column.

### Requirement: Scope document states formal exclusion criteria
**Reason:** Replaced by Relevance rubric. There are no longer three named exclusion criteria.
**Migration:** See above. Relevance 0 = not assessed; Relevance 1 = out of scope.

### Requirement: Exclusion criterion labels match discovery prompt output
**Reason:** The `Criterion` column using named labels (`Spec or Standard`, `Single Domain`, `General Purpose`) is removed from the discovery prompt output. The Relevance score column replaces it.
**Migration:** Discovery summary tables now include a `Relevance` column (0–5) instead of a `Criterion` column with named exclusion labels.

## MODIFIED Requirements

### Requirement: Scope document exists at docs/scope.md
The repository SHALL contain a file at `docs/01-scope.md` (formerly referenced as `docs/scope.md`) that contains all scoring rubrics — Relevance (0–5) plus the 12 dimension and functional category rubrics — and serves as the canonical rubric source pasted into AI sessions.

The file SHALL retain brief prose context explaining what a UDT platform is and the purpose of the study, so it remains useful as a standalone onboarding document.

#### Scenario: Researcher reads scope before starting a discovery session
- **WHEN** a researcher opens `docs/01-scope.md` before running the discovery prompt
- **THEN** they find the Relevance 0–5 rubric, all 12 dimension/category rubrics, and brief context on what qualifies as a UDT platform

#### Scenario: Researcher prepares a prompt session
- **WHEN** a researcher is about to run a discovery or comparison session
- **THEN** they paste the full content of `docs/01-scope.md` into the `[PASTE_SCOPE_HERE]` slot in the prompt

### Requirement: Scope document provides a seed list of known qualifying platforms
The scope document SHALL include a seed list of at least six platforms already known to qualify, anchored to Relevance scores using the new rubric (each entry annotated with its Relevance level).

The seed list SHALL include at minimum: Cesium (Relevance 3), iTwin (Relevance 3), DTCC (Relevance 5), Eclipse Ditto (Relevance 3), FIWARE (Relevance 3), Virtual Singapore (Relevance 5).

#### Scenario: Researcher starts a discovery session
- **WHEN** a researcher begins a new discovery session
- **THEN** the seed list gives them baseline examples calibrated to the Relevance scale
