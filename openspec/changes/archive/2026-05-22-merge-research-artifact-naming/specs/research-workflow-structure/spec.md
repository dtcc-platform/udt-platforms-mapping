## ADDED Requirements

### Requirement: Live artifact names use researcher-facing object/action/role language

Live research artifact filenames SHALL use researcher-facing names that describe the artifact's research object, action, or role.

Live filenames SHALL NOT repeat the `udt-` prefix because the repository context supplies the Urban Digital Twin domain.

#### Scenario: Contributor names a live artifact

- **WHEN** a contributor creates or renames a live research artifact
- **THEN** the filename uses object/action/role language
- **THEN** the filename does not begin with `udt-`

### Requirement: Phase folders use phase-specific naming grammar

Plan artifacts SHALL use noun phrases for run inputs, definitions, rubrics, policies, or fixtures.

Act artifacts SHALL use verb phrases for executable research actions, reporting actions, and benchmark actions.

Observe artifacts SHALL identify the research action and model or generated output.

Reflect artifacts SHALL identify the research object and synthesis or export product.

OpenSpec capability names SHALL use phase-object-role grammar:

- `plan-<object>-<artifact-role>` for planned definitions, inputs, rubrics, source policies, and benchmark fixtures
- `act-<object>-<artifact-role>` for research actions, prompt execution contracts, benchmarking actions, and reporting actions
- `observe-<object>-<artifact-role>` for saved outputs and generated observations
- `reflect-<object>-<artifact-role>` for synthesis, reporting, and reflection outputs

Live `act/` filenames SHALL use verb-first action names when they are executable prompts.

OpenSpec capability names SHALL remain phase-first even when the governed live `act/` filename is verb-first.

Phase-local structural contracts SHALL use the phase prefix when the contract governs artifacts in one phase folder.

Cross-phase research governance contracts SHALL use the `research-` prefix.

#### Scenario: Researcher scans phase folders

- **WHEN** a researcher opens `plan/`, `act/`, `observe/`, or `reflect/`
- **THEN** filenames communicate the artifact role using the phase naming grammar

#### Scenario: Contributor names a phase-aligned spec

- **WHEN** a contributor creates or renames an OpenSpec capability for one workflow phase
- **THEN** the capability name follows `<phase>-<object>-<artifact-role>`
- **THEN** live `act/` filenames may still use verb-first names such as `compare-platforms.md`

#### Scenario: Contributor names a cross-phase research spec

- **WHEN** a contributor creates or renames an OpenSpec capability governing the research workflow across phases
- **THEN** the capability name uses the `research-` prefix
