# Spec: research-workflow-structure

## Purpose

Defines the live research workflow phase structure and canonical researcher-facing artifact locations.

## Requirements

### Requirement: Research workflow is organised as action research phases

The repository SHALL use four top-level folders matching the action research phases: `plan/`, `act/`, `observe/`, and `reflect/`.

The `plan/`, `act/`, `observe/`, and `reflect/` folders SHALL expose canonical research artifacts as direct files. Direct filenames SHALL identify the artifact's research object, research action, or artifact role.

The canonical live research objects are:

- entities
- platforms
- initiatives

The canonical live research actions are:

- discover entities
- compare platforms
- benchmark platform discovery
- report platform discovery
- benchmark platform comparison
- report platform comparison

The phase folders MAY contain local `README.md` files for documentation. These README files are documentation aids and SHALL NOT be treated as canonical research artifacts or standalone OpenSpec-governed contracts.

#### Scenario: Researcher navigates the workflow

- **WHEN** a researcher opens the repository root
- **THEN** they see the four research phase folders
- **THEN** the researcher can find canonical planning inputs directly under `plan/`
- **THEN** the researcher can find canonical prompts directly under `act/`
- **THEN** the researcher can find observed outputs directly under `observe/`
- **THEN** the researcher can find reflection artifacts directly under `reflect/`

### Requirement: plan/ holds research run inputs

`plan/` SHALL contain researcher-facing run inputs used by governed prompts.

`plan/` SHALL NOT be the canonical home for stable behavior definitions, source policies, scoring rubrics, output contracts, or prompt behavior contracts.

Stable behavior definitions, source policies, and scoring rubrics SHALL be governed in `openspec/specs/`.

`openspec/specs/plan-entity-definition/spec.md` SHALL be the canonical definition contract for UDT entities, including technical artifacts, initiatives, exclusions, and initiative-to-artifact substrate interpretation.

`plan/platform-comparison-set.md` SHALL contain the selected platform comparison set.
`plan/platform-discovery-benchmark.md` SHALL contain the platform discovery benchmark fixture.

The behavior for consuming `plan/platform-comparison-set.md` SHALL be governed by `act-platform-comparison`.

The behavior for consuming `plan/platform-discovery-benchmark.md` SHALL be governed by `act-platform-discovery-benchmark`.

Additional `plan/` files MAY contain run-specific scope notes, seed inputs, selected candidates, or temporary input material used by canonical prompts.

#### Scenario: Researcher starts from planning inputs

- **WHEN** a researcher opens `plan/`
- **THEN** they see run inputs as direct files
- **THEN** stable behavior definitions, policies, and rubrics are not treated as canonical plan artifacts
- **THEN** the researcher can identify `openspec/specs/plan-entity-definition/spec.md` as the canonical UDT entity definition contract

### Requirement: act/ holds canonical research action prompts

`act/discover-entities.md` SHALL be the canonical entity discovery prompt template.
`act/compare-platforms.md` SHALL be the canonical platform comparison prompt template.
`act/benchmark-platform-discovery.md` SHALL be the canonical platform discovery benchmark prompt.
`act/report-platform-discovery.md` SHALL be the canonical platform discovery reporting prompt.
`act/benchmark-platform-comparison.md` SHALL be the platform comparison benchmarking prompt stub.
`act/report-platform-comparison.md` SHALL be the canonical platform comparison reporting prompt.

#### Scenario: Researcher finds canonical prompts

- **WHEN** a researcher opens `act/`
- **THEN** they see research action prompts as direct files
- **THEN** `discover-entities.md` is the canonical discovery prompt

### Requirement: observe/ holds canonical saved research outputs

Saved entity discovery responses SHALL use the pattern `observe/entity-discovery-<model-short>.md`.
`observe/platform-comparison-chatgpt.md`, `observe/platform-comparison-claude.md`, and `observe/platform-comparison-gemini.md` SHALL contain saved web responses for platform comparison.
Observed workflow outputs, such as `observe/platform-discovery-coverage.md`, SHALL also live as direct files under `observe/`.

#### Scenario: Researcher saves a web response

- **WHEN** a researcher saves a canonical web response
- **THEN** the response is saved as a direct file under `observe/`
- **THEN** the filename identifies the research action and model

### Requirement: reflect/ holds synthesized research artifacts

`reflect/` SHALL contain synthesized reflection, reporting, and benchmark-analysis outputs as direct files whose names identify the research object and artifact function.

`reflect/platform-ecosystem.md` SHALL contain the platform discovery ecosystem synthesis.
`reflect/platform-comparison-ecosystem.csv` and `reflect/platform-comparison-ecosystem-map.html` SHALL contain platform comparison structured reflection outputs.

#### Scenario: Researcher finds reflection artifacts

- **WHEN** a researcher opens `reflect/`
- **THEN** reflection artifacts are direct files
- **THEN** filenames identify object and function

### Requirement: Prompt interpretation review checks prompt fidelity against governing specs

The prompt interpretation review workflow SHALL ask a reviewing agent to compare a generated or updated prompt against its governing OpenSpec spec.

The review SHALL answer whether the prompt is a faithful interpretation of the spec and whether the spec or prompt can be made clearer.

#### Scenario: Reviewer checks a generated prompt

- **WHEN** an agent generates a prompt from a governing spec
- **THEN** a reviewing agent compares the prompt against that spec
- **THEN** the reviewer identifies any mismatch, ambiguity, or improvement opportunity

### Requirement: Accepted prompt-review improvements become OpenSpec deltas

Any accepted improvement from prompt interpretation review SHALL be captured as an OpenSpec delta before changing the baseline prompt or baseline spec.

Review comments SHALL NOT be stored as standalone calibration artifacts.

#### Scenario: Reviewer finds an ambiguity

- **WHEN** a reviewer finds that a prompt interpretation exposes an ambiguous spec requirement
- **THEN** the ambiguity is resolved through a scoped OpenSpec delta
- **THEN** the prompt is regenerated or updated from the improved contract

### Requirement: Prompt interpretation review is sequential

The workflow SHALL allow later reviewing agents to see the current accepted change state, including earlier accepted deltas from previous reviewers.

The workflow SHALL NOT require isolated calibration branches or blind independent proposals.

#### Scenario: Later reviewer follows accepted deltas

- **WHEN** one agent generates a prompt and an earlier review produces an accepted OpenSpec delta
- **THEN** a later reviewing agent reviews the prompt against the updated current spec/change state
- **THEN** the later reviewing agent may propose another OpenSpec delta if it finds a further improvement
