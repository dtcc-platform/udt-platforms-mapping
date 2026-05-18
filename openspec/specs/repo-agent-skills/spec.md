# Spec: repo-agent-skills

## Purpose

Defines repository-local agent skills as operational shortcuts over governed OpenSpec workflows.

## Requirements

### Requirement: Repository-local agent skills are operational shortcuts

Repository-local agent skills SHALL live under `.codex/skills/`.

Repository-local agent skills SHALL be operational shortcuts over governed repository workflows.

Repository-local agent skills SHALL NOT be the authoritative source for research behavior when an OpenSpec contract or `act/` manifest governs that behavior.

When a skill resolves a governed act manifest, it SHALL read the live manifest and the manifest's required contracts at execution time.

#### Scenario: Agent uses a repository-local skill

- **WHEN** an agent uses a repository-local skill for a governed research action
- **THEN** the skill follows the live manifest and required OpenSpec contracts
- **THEN** the skill does not replace the governing specs or manifest as the source of truth

### Requirement: UDT discovery skill resolves entity discovery for web use

The repository SHALL provide a local skill at `.codex/skills/udt-discover/SKILL.md`.

The skill SHALL trigger for user requests such as `udt:discover`, `udt-discover`, and requests to resolve `act/discover-entities.md` for web use.

The skill SHALL resolve `act/discover-entities.md` by inlining each required contract under a heading naming the source file, appending the prompt body, and producing one copy-ready prompt block.

The skill SHALL use the current live manifest and contracts rather than cached prompt text.

After producing the resolved prompt, the skill SHALL use assistant-side `/copy` when the current client exposes it.

When assistant-side `/copy` is not available, the skill SHALL tell the researcher to run `/copy` on the generated prompt.

The skill SHALL tell the researcher to save the web response to `observe/entity-discovery-<model-short>.md`.

#### Scenario: Researcher invokes udt discovery

- **WHEN** a researcher asks for `udt:discover`
- **THEN** the agent resolves `act/discover-entities.md` for web use
- **THEN** the resolved prompt reflects the live required contracts
- **THEN** the agent uses `/copy` when available or gives the `/copy` fallback
- **THEN** the agent tells the researcher where to save the response
