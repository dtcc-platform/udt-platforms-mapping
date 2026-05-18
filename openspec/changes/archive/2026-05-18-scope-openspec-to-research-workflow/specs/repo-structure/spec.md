## REMOVED Requirements

### Requirement: Repository is organised as action research phases at top level

**Reason**: Replaced by `research-workflow-structure`, which names the research workflow scope explicitly.

**Migration**: Use `openspec/specs/research-workflow-structure/spec.md`.

#### Scenario: Researcher navigates the repository

- **WHEN** a researcher opens the repository root
- **THEN** they use `research-workflow-structure` for research phase structure governance

### Requirement: plan/ holds research definitions and run inputs

**Reason**: Replaced by `research-workflow-structure`.

**Migration**: Use `openspec/specs/research-workflow-structure/spec.md`.

#### Scenario: Researcher starts from planning inputs

- **WHEN** a researcher opens `plan/`
- **THEN** they use `research-workflow-structure` for planning input governance

### Requirement: act/ holds canonical research action prompts

**Reason**: Replaced by `research-workflow-structure`.

**Migration**: Use `openspec/specs/research-workflow-structure/spec.md`.

#### Scenario: Researcher finds canonical prompts

- **WHEN** a researcher opens `act/`
- **THEN** they use `research-workflow-structure` for action prompt location governance

### Requirement: observe/ holds canonical saved outputs by action and model

**Reason**: Replaced by `research-workflow-structure`.

**Migration**: Use `openspec/specs/research-workflow-structure/spec.md`.

#### Scenario: Researcher saves a web response

- **WHEN** a researcher saves a canonical web response
- **THEN** they use `research-workflow-structure` for saved output location governance

### Requirement: reflect/ holds synthesized reflection artifacts as direct files

**Reason**: Replaced by `research-workflow-structure`.

**Migration**: Use `openspec/specs/research-workflow-structure/spec.md`.

#### Scenario: Researcher finds reflection artifacts

- **WHEN** a researcher opens `reflect/`
- **THEN** they use `research-workflow-structure` for reflection artifact location governance
