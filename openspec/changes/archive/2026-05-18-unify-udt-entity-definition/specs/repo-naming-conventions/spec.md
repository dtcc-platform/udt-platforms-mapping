## MODIFIED Requirements

### Requirement: Phase folders use phase-specific naming grammar

Plan artifacts SHALL use noun phrases such as `platform-comparison-set.md` and `platform-discovery-benchmark.md`.

Act artifacts SHALL use verb phrases such as `discover-entities.md`, `compare-platforms.md`, `benchmark-platform-discovery.md`, and `report-platform-discovery.md`.

Observe artifacts SHALL identify the research action and model or generated output, such as `entity-discovery-claude.md`, `platform-comparison-gemini.md`, and `platform-discovery-coverage.md`.

Reflect artifacts SHALL identify the research object and synthesis product, such as `platform-ecosystem.md` and `platform-comparison-ecosystem.csv`.

OpenSpec behavior specs SHALL use noun phrases for stable contracts, such as `entity-definition`, `platform-comparison-rubric`, and `platform-source-policy`.

The canonical merged UDT entity definition spec SHALL be named `entity-definition`, not `platform-definition`, `initiative-definition`, or `udt-entity-definition`.

#### Scenario: Researcher scans phase folders

- **WHEN** a researcher opens `plan/`, `act/`, `observe/`, or `reflect/`
- **THEN** filenames communicate the artifact role without requiring knowledge of old thread identifiers

#### Scenario: Contributor names a merged entity definition

- **WHEN** a contributor creates or updates the canonical merged UDT entity definition
- **THEN** the OpenSpec capability name is `entity-definition`
- **THEN** the name does not begin with `udt-`
