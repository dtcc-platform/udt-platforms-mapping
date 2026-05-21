## MODIFIED Requirements

### Requirement: Phase folders use phase-specific naming grammar

Plan artifacts SHALL use noun phrases such as `platform-comparison-set.md` and `platform-discovery-benchmark.md`.

Act artifacts SHALL use verb phrases such as `discover-entities.md`, `compare-platforms.md`, `benchmark-platform-discovery.md`, and `report-platform-discovery.md`.

Observe artifacts SHALL identify the research action and model or generated output, such as `entity-discovery-claude.md`, `platform-comparison-gemini.md`, and `platform-discovery-coverage.md`.

Reflect artifacts SHALL identify the research object and synthesis product, such as `platform-ecosystem.md` and `platform-comparison-ecosystem.csv`.

OpenSpec capability names SHALL use phase-object-role grammar:

- `plan-<object>-<artifact-role>` for planned definitions, inputs, rubrics, source policies, and benchmark fixtures
- `act-<object>-<artifact-role>` for research actions, prompt execution contracts, benchmarking actions, reporting actions, and act prompt meta-contracts
- `observe-<object>-<artifact-role>` for saved outputs and generated observations
- `reflect-<object>-<artifact-role>` for synthesis, reporting, and reflection outputs

Live `act/` manifest filenames MAY remain verb-first because they are executable action prompts, while OpenSpec capability names SHALL remain phase-object-role.

Phase-local structural contracts SHALL use the phase prefix when the contract governs artifacts in one phase folder.

The canonical merged UDT entity definition spec SHALL be named `plan-entity-definition`.

The canonical entity discovery action spec SHALL be named `act-entity-discovery`.

The canonical act prompt manifest spec SHALL be named `act-prompt-manifest`.

The canonical act web prompt template spec SHALL be named `act-web-prompt-template`.

Comparison-related OpenSpec capabilities SHALL use names such as `act-platform-comparison`, `act-platform-discovery-benchmark`, `act-platform-comparison-benchmark`, `act-platform-comparison-report`, `act-platform-discovery-report`, `plan-platform-comparison-rubric`, and `plan-platform-source-policy`.

Tiny run-input files MAY be governed by the consuming `act-` capability when their only behavior is how the action consumes them.

#### Scenario: Researcher scans phase folders

- **WHEN** a researcher opens `plan/`, `act/`, `observe/`, or `reflect/`
- **THEN** filenames communicate the artifact role without requiring knowledge of old thread identifiers

#### Scenario: Contributor names a phase-aligned spec

- **WHEN** a contributor creates or renames an OpenSpec capability
- **THEN** the capability name follows `<phase>-<object>-<artifact-role>`
- **THEN** live act manifest filenames may still use verb-first names such as `compare-platforms.md`

#### Scenario: Contributor names entity discovery specs

- **WHEN** a contributor updates the entity definition or entity discovery action contracts
- **THEN** the entity definition capability is `plan-entity-definition`
- **THEN** the entity discovery action capability is `act-entity-discovery`

#### Scenario: Contributor names act prompt meta-contracts

- **WHEN** a contributor updates act prompt manifest or web prompt template contracts
- **THEN** the act prompt manifest capability is `act-prompt-manifest`
- **THEN** the act web prompt template capability is `act-web-prompt-template`

#### Scenario: Contributor names comparison specs

- **WHEN** a contributor updates platform comparison contracts
- **THEN** the comparison action capability is `act-platform-comparison`
- **THEN** the comparison benchmark capability is `act-platform-comparison-benchmark`
- **THEN** the comparison report capability is `act-platform-comparison-report`
- **THEN** the platform discovery report capability is `act-platform-discovery-report`
- **THEN** the comparison rubric capability is `plan-platform-comparison-rubric`
- **THEN** the source policy capability is `plan-platform-source-policy`

