## ADDED Requirements

### Requirement: Live artifact names use researcher-facing object/action/role language

Live repository artifact filenames SHALL use researcher-facing names that describe the artifact's research object, action, or role.

Live filenames SHALL NOT repeat the `udt-` prefix because the repository context supplies the Urban Digital Twin domain.

Live documentation and specs SHALL NOT describe canonical live artifacts as research threads. They SHALL use clearer terms such as research object, research action, artifact role, prompt, saved output, or synthesis.

#### Scenario: Contributor names a live artifact

- **WHEN** a contributor creates or renames a live canonical artifact
- **THEN** the filename uses object/action/role language
- **THEN** the filename does not begin with `udt-`
- **THEN** the governing docs avoid thread-centered language for the live workflow

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
