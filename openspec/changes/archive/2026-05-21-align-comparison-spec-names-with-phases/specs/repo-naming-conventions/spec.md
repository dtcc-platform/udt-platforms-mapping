## MODIFIED Requirements

### Requirement: Phase folders use phase-specific naming grammar

Plan artifacts SHALL use noun phrases such as `platform-comparison-set.md` and `platform-discovery-benchmark.md`.

Act artifacts SHALL use verb phrases such as `discover-entities.md`, `compare-platforms.md`, `benchmark-platform-discovery.md`, and `report-platform-discovery.md`.

Observe artifacts SHALL identify the research action and model or generated output, such as `entity-discovery-claude.md`, `platform-comparison-gemini.md`, and `platform-discovery-coverage.md`.

Reflect artifacts SHALL identify the research object and synthesis product, such as `platform-ecosystem.md` and `platform-comparison-ecosystem.csv`.

OpenSpec capability names SHALL use phase-object-role grammar:

- `plan-<object>-<artifact-role>` for planned definitions, inputs, rubrics, source policies, and benchmark fixtures
- `act-<object>-<artifact-role>` for research actions, prompt execution contracts, benchmarking actions, and reporting actions
- `observe-<object>-<artifact-role>` for saved outputs and generated observations
- `reflect-<object>-<artifact-role>` for synthesis, reporting, and reflection outputs

Live `act/` manifest filenames MAY remain verb-first because they are executable action prompts, while OpenSpec capability names SHALL remain phase-object-role.

Comparison-related OpenSpec capabilities SHALL use names such as `act-platform-comparison`, `act-platform-discovery-benchmark`, `plan-platform-comparison-rubric`, and `plan-platform-source-policy`.

Tiny run-input files MAY be governed by the consuming `act-` capability when their only behavior is how the action consumes them.

#### Scenario: Researcher scans phase folders

- **WHEN** a researcher opens `plan/`, `act/`, `observe/`, or `reflect/`
- **THEN** filenames communicate the artifact role without requiring knowledge of old thread identifiers

#### Scenario: Contributor names a phase-aligned spec

- **WHEN** a contributor creates or renames an OpenSpec capability
- **THEN** the capability name follows `<phase>-<object>-<artifact-role>`
- **THEN** live act manifest filenames may still use verb-first names such as `compare-platforms.md`

#### Scenario: Contributor names comparison specs

- **WHEN** a contributor updates platform comparison contracts
- **THEN** the comparison action capability is `act-platform-comparison`
- **THEN** the comparison rubric capability is `plan-platform-comparison-rubric`
- **THEN** the source policy capability is `plan-platform-source-policy`
