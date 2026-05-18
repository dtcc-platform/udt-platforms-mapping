## REMOVED Requirements

### Requirement: Repository-local agent skills are operational shortcuts

**Reason**: Local agent skills are operational tooling, not research workflow contracts.

**Migration**: Keep skill instructions in `.codex/skills/` outside OpenSpec governance. Research behavior remains governed by `act/` manifests and research specs.

#### Scenario: Agent uses a repository-local skill

- **WHEN** an agent uses a repository-local skill for a governed research action
- **THEN** OpenSpec governs the underlying research manifest and contracts, not the local skill mechanics

### Requirement: UDT discovery skill resolves entity discovery for web use

**Reason**: Skill behavior is operational tooling and is outside OpenSpec's research workflow scope.

**Migration**: Keep `.codex/skills/udt-discover/SKILL.md` as local operational guidance. Use `act/discover-entities.md` and its required contracts as the research source of truth.

#### Scenario: Researcher invokes udt discovery

- **WHEN** a researcher asks for `udt:discover`
- **THEN** any skill behavior follows local skill documentation outside OpenSpec governance
