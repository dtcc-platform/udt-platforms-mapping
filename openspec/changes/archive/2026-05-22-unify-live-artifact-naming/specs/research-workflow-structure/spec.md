## MODIFIED Requirements

### Requirement: Phase folders use phase-specific naming grammar

Plan artifacts SHALL use noun phrases for run inputs, definitions, rubrics, policies, or fixtures.

Act artifacts SHALL use object/action/role names for executable research actions, reporting actions, and benchmark actions.

Observe artifacts SHALL identify the research action and model or generated output.

Reflect artifacts SHALL identify the research object and synthesis or export product.

OpenSpec capability names SHALL use phase-object-role grammar:

- `plan-<object>-<artifact-role>` for planned definitions, inputs, rubrics, source policies, and benchmark fixtures
- `act-<object>-<artifact-role>` for research actions, prompt execution contracts, benchmarking actions, and reporting actions
- `observe-<object>-<artifact-role>` for saved outputs and generated observations
- `reflect-<object>-<artifact-role>` for synthesis, reporting, and reflection outputs

Live artifact filenames SHALL use the same object/action/role naming convention as the governed capability without repeating the phase prefix supplied by the folder.

Phase-local structural contracts SHALL use the phase prefix when the contract governs artifacts in one phase folder.

Cross-phase research governance contracts SHALL use the `research-` prefix.

#### Scenario: Researcher scans phase folders

- **WHEN** a researcher opens `plan/`, `act/`, `observe/`, or `reflect/`
- **THEN** filenames communicate the artifact role using the phase naming grammar

#### Scenario: Contributor names a phase-aligned spec

- **WHEN** a contributor creates or renames an OpenSpec capability for one workflow phase
- **THEN** the capability name follows `<phase>-<object>-<artifact-role>`
- **THEN** the matching live artifact filename uses the object/action/role portion without the phase prefix

#### Scenario: Contributor names a cross-phase research spec

- **WHEN** a contributor creates or renames an OpenSpec capability governing the research workflow across phases
- **THEN** the capability name uses the `research-` prefix
