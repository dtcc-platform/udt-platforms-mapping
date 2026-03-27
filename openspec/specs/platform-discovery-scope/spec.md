### Requirement: Scope document exists at docs/scope.md
The repository SHALL contain a file at `docs/scope.md` that operationalises the inclusion boundary for the UDT platform review, providing concrete guidance for discovery sessions.

#### Scenario: Researcher reads scope before starting a discovery session
- **WHEN** a researcher opens `docs/scope.md` before running the discovery prompt
- **THEN** they find actionable inclusion guidance, explicit exclusion examples, a seed list of known platforms, and a target corpus size

### Requirement: Scope document states inclusion criteria in operational terms
The scope document SHALL restate the three inclusion criteria from `docs/methodology.md` in operational terms — specifying what evidence is sufficient for each criterion (e.g., official documentation, product page, repository description).

#### Scenario: Researcher assesses a borderline platform
- **WHEN** a researcher encounters a platform that may or may not qualify
- **THEN** the scope document provides enough concrete guidance to make a consistent include/exclude decision without consulting other documents

### Requirement: Scope document lists explicit exclusion examples
The scope document SHALL include at least five named exclusion examples, each with a one-line rationale explaining why it falls outside the moderate inclusion boundary.

#### Scenario: Researcher encounters a smart city IoT platform
- **WHEN** a researcher finds a platform that is purely a smart city IoT platform
- **THEN** the scope document's exclusion list confirms it is out of scope and explains why

### Requirement: Scope document provides a seed list of known qualifying platforms
The scope document SHALL include a seed list of at least six platforms already known to qualify, distributed across the three inclusion criteria, to anchor discovery sessions and calibrate the boundary.

The seed list SHALL include at minimum: Cesium, iTwin, DTCC, Eclipse Ditto, FIWARE, Virtual Singapore.

#### Scenario: Researcher starts a discovery session
- **WHEN** a researcher begins a new discovery session
- **THEN** the seed list gives them a baseline set of known qualifiers to extend, not a blank slate

### Requirement: Scope document states a target corpus size
The scope document SHALL state a target range for the number of platforms in the review corpus (15–30 platforms), framed as a planning heuristic rather than a hard constraint.

#### Scenario: Researcher assesses when to stop discovery
- **WHEN** a researcher has accumulated a set of platforms
- **THEN** the scope document's target range helps them judge whether the corpus is sufficiently representative
