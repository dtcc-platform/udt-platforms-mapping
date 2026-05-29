## ADDED Requirements

### Requirement: Static publication output is separate from research phase folders

The repository SHALL support a top-level `docs/` folder for static publication output generated from research artifacts.

The `docs/` folder SHALL NOT be treated as a fifth action research phase.

The `docs/` folder SHALL NOT become the canonical source location for `plan/`, `act/`, `observe/`, or `reflect/` research artifacts.

Published observation pages SHALL live under the `docs/observations/` category folder.

Published reflection pages SHALL live under the `docs/reflections/` category folder.

The public `docs/index.html` home page SHALL include an `observations` category section linking to generated pages under `docs/observations/`.

The public `docs/index.html` home page SHALL include a `reflections` category section linking to generated pages under `docs/reflections/`.

Phase-local `README.md` files SHALL NOT be treated as publishable research artifact pages.

#### Scenario: Researcher distinguishes source artifacts from publication output

- **WHEN** a researcher opens the repository
- **THEN** canonical research source artifacts remain under the four phase folders
- **THEN** generated public pages may be found under `docs/`

#### Scenario: Observation artifacts are published under docs observe

- **WHEN** `observe/platform-discovery-chatgpt.md` is published
- **THEN** the generated page lives at `docs/observations/platform-discovery-chatgpt.html`
- **THEN** `docs/index.html` links to `./observations/platform-discovery-chatgpt.html` from the `observations` category section

#### Scenario: Reflection artifacts are published under docs reflect

- **WHEN** `reflect/platform-ecosystem.md` is published
- **THEN** the generated page lives at `docs/reflections/platform-ecosystem.html`
- **THEN** `docs/index.html` links to `./reflections/platform-ecosystem.html` from the `reflections` category section

#### Scenario: Phase README files are not published as artifacts

- **WHEN** `observe/README.md` or `reflect/README.md` exists
- **THEN** it is not listed as a research artifact page in `docs/index.html`

### Requirement: Repository scripts hold operational automation

The repository SHALL support a top-level `scripts/` folder for operational automation.

Scripts SHALL NOT be treated as canonical research artifacts.

Scripts SHALL NOT be placed in `act/` unless they are themselves governed research action prompts or prompt artifacts.

The repository SHALL provide `scripts/publish.sh` as the canonical command for publishing observation and reflection Markdown artifacts to `docs/`.

The publish command SHALL fail with a clear error when `pandoc` is unavailable.

#### Scenario: Contributor adds publication automation

- **WHEN** a contributor adds a script that publishes research artifacts to static pages
- **THEN** the script may live under `scripts/`
- **THEN** the script is not treated as an `act/` prompt

#### Scenario: Contributor publishes observation and reflection pages

- **WHEN** a contributor runs `scripts/publish.sh` from the repository
- **THEN** eligible direct Markdown files under `observe/` are published to `docs/observations/`
- **THEN** eligible direct Markdown files under `reflect/` are published to `docs/reflections/`
- **THEN** `docs/index.html` is updated with grouped publication links

#### Scenario: Pandoc is missing

- **WHEN** a contributor runs `scripts/publish.sh` without `pandoc` available
- **THEN** the command exits with an error explaining that `pandoc` is required
