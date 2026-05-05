## MODIFIED Requirements

### Requirement: Root README explains repository workflow and navigation

`README.md` SHALL be the repository-wide documentation entrypoint.

It SHALL present the repository as a spec-first research repository for collaborating with AI agents on Urban Digital Twin platform research.

It SHALL explain the action research workflow, the roles of `plan/`, `act/`, `observe/`, and `reflect/`, the canonical research objects and actions, and the relationship between OpenSpec, prompts, outputs, reflection, and git history.

It SHALL do this as a concise researcher-facing orientation page, using phase README files for local folder detail and `openspec/specs/` for formal repository contracts.

It SHALL retain separate diagrams for the research execution loop and prompt interpretation review workflow.

It SHALL keep future-direction notes concise when they are included.

It SHALL include a small pointer to the governing repo-wide specs for structure, naming, prompt review, and README documentation.

It SHALL explain that live artifact names use researcher-facing object/action/role language and do not repeat the `udt-` prefix.

#### Scenario: Contributor opens the repository

- **WHEN** a contributor reads `README.md`
- **THEN** they understand the repository workflow at a high level
- **THEN** they can find the phase folders and their local README files
- **THEN** they can find the formal governing specs without the README duplicating their full contract text

### Requirement: Root README explains research objects and platform comparison handoff

`README.md` SHALL explain:

- platform discovery as broad technical-artifact discovery
- initiative discovery as broad project, programme, and deployment discovery
- platform comparison as stricter side-by-side evaluation

It SHALL state that only rows classified as `Type = platform` by platform discovery are eligible for platform comparison.

#### Scenario: Researcher reads research object roles

- **WHEN** a researcher reads `README.md`
- **THEN** the README explains platform discovery, initiative discovery, and platform comparison
- **THEN** the README states that only `Type = platform` rows are eligible for platform comparison
