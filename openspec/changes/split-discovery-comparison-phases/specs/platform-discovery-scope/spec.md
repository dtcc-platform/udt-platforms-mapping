## REMOVED Requirements

### Requirement: docs/01-scope.md contains all 13 scoring rubrics as the canonical source
**Reason**: `docs/01-scope.md` is retired. The single combined scope file is replaced by two phase-specific files: `docs/01-discovery-scope.md` (Layer criteria table) and `docs/01-comparison-scope.md` (12 dimension rubrics). Having one file serve both phases created coupling and required both prompts to embed the full 13-rubric set.
**Migration**: Create `docs/01-discovery-scope.md` (see `platform-discovery-scope-file` spec) and `docs/01-comparison-scope.md` (see `platform-comparison-scope-file` spec). Delete `docs/01-scope.md`.

### Requirement: Scope document provides a seed list of known qualifying platforms
**Reason**: The seed list was anchored to Relevance scores (e.g. "Cesium — Relevance 3"). Relevance is retired. The Layer criteria table in `docs/01-discovery-scope.md` is self-contained and requires no calibration examples.
**Migration**: Remove the seed list entirely. No replacement.

### Requirement: Scope document states a target corpus size
**Reason**: Target corpus size (15–30) was a heuristic tied to the platform review framing. The study is now ecosystem mapping with no fixed corpus target — discovery runs until the researcher judges coverage is sufficient.
**Migration**: Remove the target corpus statement. No replacement.

### Requirement: Scope document defines the ecosystem layer taxonomy
**Reason**: Superseded by the `platform-discovery-scope-file` spec which defines a tighter, criteria-backed Layer table in `docs/01-discovery-scope.md`.
**Migration**: The new `docs/01-discovery-scope.md` replaces this requirement.
