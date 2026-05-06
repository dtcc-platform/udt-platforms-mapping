## MODIFIED Requirements

### Requirement: Root README explains repository workflow and navigation

`README.md` SHALL be the repository-wide documentation entrypoint.

It SHALL present the repository as a spec-first research repository for collaborating with AI agents on Urban Digital Twin platform research.

It SHALL explain that OpenSpec specs are behavior contracts, `plan/` contains run inputs, `act/` prompts operationally implement the contracts, `observe/` stores raw outputs, and `reflect/` stores synthesis.

It SHALL explain the action research workflow, the roles of `plan/`, `act/`, `observe/`, and `reflect/`, the canonical research objects and actions, and the relationship between OpenSpec, prompts, outputs, reflection, and git history.

It SHALL do this as a concise researcher-facing orientation page, using phase README files for local folder detail and `openspec/specs/` for formal repository contracts.

It SHALL retain separate diagrams for the research execution loop and prompt interpretation review workflow.

It SHALL keep future-direction notes concise when they are included.

It SHALL include a small pointer to the governing repo-wide specs for structure, naming, prompt review, and README documentation.

It SHALL explain that live artifact names use researcher-facing object/action/role language and do not repeat the `udt-` prefix.

#### Scenario: Contributor opens the repository

- **WHEN** a contributor reads `README.md`
- **THEN** they understand the repository workflow at a high level
- **THEN** they understand that specs define behavior and `plan/` contains run inputs
- **THEN** they can find the phase folders and their local README files
- **THEN** they can find the formal governing specs without the README duplicating their full contract text
