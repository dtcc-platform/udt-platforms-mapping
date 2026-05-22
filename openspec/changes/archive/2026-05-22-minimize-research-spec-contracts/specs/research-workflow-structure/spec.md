## MODIFIED Requirements

### Requirement: Research workflow is organised as action research phases

The repository SHALL use four top-level folders matching the action research phases: `plan/`, `act/`, `observe/`, and `reflect/`.

The `plan/`, `act/`, `observe/`, and `reflect/` folders SHALL expose canonical research artifacts as direct files.

Direct filenames SHALL identify the artifact's research object, research action, or artifact role.

The phase folders MAY contain local `README.md` files for documentation.

These README files SHALL NOT be treated as canonical research artifacts or standalone OpenSpec-governed contracts.

#### Scenario: Researcher navigates the workflow

- **WHEN** a researcher opens the repository root
- **THEN** they see the four research phase folders
- **THEN** the researcher can find planning inputs directly under `plan/`
- **THEN** the researcher can find research action prompts directly under `act/`
- **THEN** the researcher can find observed outputs directly under `observe/`
- **THEN** the researcher can find reflection artifacts directly under `reflect/`

### Requirement: plan/ holds research run inputs

`plan/` SHALL contain researcher-facing run inputs used by governed prompts.

`plan/` SHALL NOT be the canonical home for stable behavior definitions, source policies, scoring rubrics, output contracts, or prompt behavior contracts.

Stable behavior definitions, source policies, and scoring rubrics SHALL be governed in `openspec/specs/`.

Additional `plan/` files MAY contain run-specific scope notes, seed inputs, selected candidates, or temporary input material used by canonical prompts.

#### Scenario: Researcher starts from planning inputs

- **WHEN** a researcher opens `plan/`
- **THEN** they see run inputs as direct files
- **THEN** stable behavior definitions, policies, and rubrics are not treated as canonical plan artifacts

### Requirement: act/ holds canonical research action prompts

`act/` SHALL contain governed research action prompts and prompt manifests.

Each governed `act/` prompt SHALL identify its required OpenSpec contracts and run inputs according to `act-prompt-manifest`.

`act/` SHALL NOT contain placeholder prompts for undesigned research actions.

#### Scenario: Researcher finds canonical prompts

- **WHEN** a researcher opens `act/`
- **THEN** they see governed research action prompts as direct files
- **THEN** placeholder prompts for undesigned actions are absent

### Requirement: observe/ holds canonical saved research outputs

Saved web responses SHALL use filenames that identify the research action and model.

Generated workflow outputs SHALL live as direct files under `observe/` when they are observations of a run.

#### Scenario: Researcher saves a web response

- **WHEN** a researcher saves a canonical web response
- **THEN** the response is saved as a direct file under `observe/`
- **THEN** the filename identifies the research action and model

### Requirement: reflect/ holds synthesized research artifacts

`reflect/` SHALL contain synthesized reflection, reporting, and benchmark-analysis outputs as direct files whose names identify the research object and artifact function.

#### Scenario: Researcher finds reflection artifacts

- **WHEN** a researcher opens `reflect/`
- **THEN** reflection artifacts are direct files
- **THEN** filenames identify object and function
## REMOVED Requirements

### Requirement: Prompt interpretation review checks prompt fidelity against governing specs

**Reason**: This requirement governs review procedure rather than research workflow structure, and it no longer has a dedicated prompt-review capability after previous consolidation.

**Migration**: Use the OpenSpec change process directly when prompt interpretation exposes an ambiguity or mismatch.

### Requirement: Accepted prompt-review improvements become OpenSpec deltas

**Reason**: This repeats the repository's OpenSpec-first process rather than defining a distinct research workflow contract.

**Migration**: Capture accepted spec or prompt behavior changes through normal scoped OpenSpec changes.

### Requirement: Prompt interpretation review is sequential

**Reason**: Sequential prompt-review procedure is workflow process guidance, not a minimum research artifact structure requirement.

**Migration**: Later reviewers should use the current accepted repository state and propose scoped OpenSpec changes when they find further improvements.
