## MODIFIED Requirements

### Requirement: Root README explains repository workflow and navigation

`README.md` SHALL be the repository-wide documentation entrypoint.

It SHALL present the repository as a spec-first research repository for collaborating with AI agents on Urban Digital Twin platform research.

It SHALL explain that expected model behavior is separated from prompt wording.

It SHALL explain that OpenSpec specs are behavior contracts, `plan/` contains run inputs, `act/` contains contract manifests, `observe/` stores raw outputs, and `reflect/` stores synthesis.

It SHALL explain that resolving an `act/` manifest combines required specs and run inputs into a concrete prompt for a model or agent.

It SHALL explain that repository-local skills can provide shortcuts for resolving governed manifests, while OpenSpec specs and act manifests remain the source of truth.

It SHALL document `udt:discover` as a shortcut for resolving `act/discover-platforms.md` for web use and explain the `/copy` fallback when automatic copy is unavailable.

It SHALL explain that resolving the same manifest with different agents can reveal ambiguous spec interpretation and support contract improvement.

It SHALL explain the action research workflow, the roles of `plan/`, `act/`, `observe/`, and `reflect/`, the canonical research objects and actions, and the relationship between OpenSpec, manifests, resolved prompts, outputs, reflection, and git history.

It SHALL do this as a concise researcher-facing orientation page, using phase README files for local folder detail and `openspec/specs/` for formal repository contracts.

It SHALL retain separate diagrams for the research execution flow and prompt interpretation improvement workflow.

It SHALL keep future-direction notes concise when they are included.

It SHALL include a small pointer to the governing repo-wide specs for structure, naming, prompt review, act prompt manifests, web prompt templates, agent skills, and README documentation.

It SHALL explain that live artifact names use researcher-facing object/action/role language and do not repeat the `udt-` prefix.

#### Scenario: Contributor opens the repository

- **WHEN** a contributor reads `README.md`
- **THEN** they understand the repository workflow at a high level
- **THEN** they understand that specs define behavior and `plan/` contains run inputs
- **THEN** they understand that `act/` files are manifests that must be resolved into prompts
- **THEN** they understand that repository-local skills can shortcut common manifest resolution tasks
- **THEN** they can find the phase folders and their local README files
- **THEN** they can find the formal governing specs without the README duplicating their full contract text
