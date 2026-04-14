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

### Requirement: Scope document states a target corpus size
The scope document SHALL state a target range for the number of platforms in the review corpus (15–30 platforms), framed as a planning heuristic rather than a hard constraint.

#### Scenario: Researcher assesses when to stop discovery
- **WHEN** a researcher has accumulated a set of platforms
- **THEN** the scope document's target range helps them judge whether the corpus is sufficiently representative
