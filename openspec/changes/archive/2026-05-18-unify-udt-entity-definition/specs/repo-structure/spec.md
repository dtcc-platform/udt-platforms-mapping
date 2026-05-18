## MODIFIED Requirements

### Requirement: Repository is organised as action research phases at top level

The repository SHALL use four top-level folders matching the action research phases: `plan/`, `act/`, `observe/`, and `reflect/`.

The `plan/`, `act/`, `observe/`, and `reflect/` folders SHALL expose canonical artifacts as direct files. Direct filenames SHALL identify the artifact's research object, research action, or artifact role.

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

The repository SHALL NOT use a top-level `calibration/` folder for live workflow state.

The phase folders MAY contain local `README.md` files for documentation. These README files are not canonical research artifacts.

#### Scenario: Researcher navigates the repository

- **WHEN** a researcher opens the repository root
- **THEN** they see the four phase folders
- **THEN** the researcher can find canonical planning inputs directly under `plan/`
- **THEN** the researcher can find canonical prompts directly under `act/`
- **THEN** the researcher can find observed outputs directly under `observe/`
- **THEN** the researcher can find reflection artifacts directly under `reflect/`

### Requirement: plan/ holds research definitions and run inputs

`plan/` SHALL contain researcher-facing run inputs used by governed prompts.

`plan/` SHALL NOT be the canonical home for stable behavior definitions, source policies, scoring rubrics, output contracts, or prompt behavior contracts.

Stable behavior definitions, source policies, and scoring rubrics SHALL be governed in `openspec/specs/`.

`openspec/specs/entity-definition/spec.md` SHALL be the canonical definition contract for UDT entities, including technical artifacts, initiatives, exclusions, and initiative-to-artifact substrate interpretation.

`openspec/specs/platform-definition/spec.md` and `openspec/specs/initiative-definition/spec.md` SHALL NOT be active canonical definition contracts after migration to `entity-definition`.

`plan/platform-comparison-set.md` SHALL contain the selected platform comparison set.
`plan/platform-discovery-benchmark.md` SHALL contain the platform discovery benchmark fixture.

Additional `plan/` files MAY contain run-specific scope notes, seed inputs, selected candidates, or temporary input material used by canonical prompts.

#### Scenario: Researcher starts from planning inputs

- **WHEN** a researcher opens `plan/`
- **THEN** they see run inputs as direct files
- **THEN** stable behavior definitions, policies, and rubrics are not treated as canonical plan artifacts
- **THEN** the researcher can identify `openspec/specs/entity-definition/spec.md` as the canonical UDT entity definition contract
- **THEN** no canonical planning input uses the old `udt-` thread-prefixed filename pattern

### Requirement: act/ holds canonical research action prompts

`act/discover-entities.md` SHALL be the canonical entity discovery prompt template.
`act/discover-platforms.md` and `act/discover-initiatives.md` SHALL NOT be active canonical discovery prompt templates after migration to `act/discover-entities.md`.
`act/compare-platforms.md` SHALL be the canonical platform comparison prompt template.
`act/benchmark-platform-discovery.md` SHALL be the canonical platform discovery benchmark prompt.
`act/report-platform-discovery.md` SHALL be the canonical platform discovery reporting prompt.
`act/benchmark-platform-comparison.md` SHALL be the platform comparison benchmarking prompt stub.
`act/report-platform-comparison.md` SHALL be the canonical platform comparison reporting prompt.

#### Scenario: Researcher finds canonical prompts

- **WHEN** a researcher opens `act/`
- **THEN** they see research action prompts as direct files
- **THEN** `discover-entities.md` is the canonical discovery prompt
- **THEN** no canonical prompt uses the old `udt-` thread-prefixed filename pattern

### Requirement: observe/ holds canonical saved outputs by action and model

Saved entity discovery responses SHALL use the pattern `observe/entity-discovery-<model-short>.md`.
`observe/platform-comparison-chatgpt.md`, `observe/platform-comparison-claude.md`, and `observe/platform-comparison-gemini.md` SHALL contain saved web responses for platform comparison.
Observed workflow outputs, such as `observe/platform-discovery-coverage.md`, SHALL also live as direct files under `observe/`.

Saved platform discovery and initiative discovery responses SHALL NOT be active canonical discovery outputs after migration to entity discovery.

#### Scenario: Researcher saves a web response

- **WHEN** a researcher saves a canonical web response
- **THEN** the response is saved as a direct file under `observe/`
- **THEN** the filename identifies the research action and model
