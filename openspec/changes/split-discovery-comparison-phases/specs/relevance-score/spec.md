## REMOVED Requirements

### Requirement: Relevance rubric defined in docs/01-scope.md
**Reason**: Relevance (0–5) is retired as a scored field. The Layer criteria table in `docs/01-discovery-scope.md` replaces the Relevance rubric as the inclusion and classification mechanism. Layer uses observable criteria (checkable against primary sources) rather than a scored rubric, making classification consistent across sessions without judgment-based scoring.
**Migration**: Remove the Relevance column from the inventory CSV. Remove Relevance scoring from both prompts. Use the Layer criteria table in `docs/01-discovery-scope.md` for platform classification.

### Requirement: Relevance rubric covers the full 0–5 range with level descriptions
**Reason**: Retired with Relevance. The 0–5 scale is replaced by the four-row Layer criteria table (`core-platform`, `backbone`, `domain-module`, `excluded`).
**Migration**: No replacement. The Layer criteria table is the new classification system.

### Requirement: docs/01-scope.md contains all 13 scoring rubrics as the canonical source
**Reason**: `docs/01-scope.md` is retired. The 13 rubrics are split: `docs/01-discovery-scope.md` contains the Layer criteria table (replaces Relevance rubric); `docs/01-comparison-scope.md` contains the 12 dimension rubrics.
**Migration**: See `platform-discovery-scope-file` and `platform-comparison-scope-file` specs.
