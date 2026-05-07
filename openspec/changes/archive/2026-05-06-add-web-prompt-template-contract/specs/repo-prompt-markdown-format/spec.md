## MODIFIED Requirements

### Requirement: Governed prompts define portable Markdown output

Each governed prompt template file in the live repository that instructs an AI model to emit Markdown output SHALL include a `### Markdown and Formatting Rules` section defining the project's shared portable Markdown contract.

This shared contract SHALL apply to the governed prompt templates that explicitly rely on it, including current prompts such as `act/discover-platforms.md`, `act/discover-initiatives.md`, and `act/compare-platforms.md`.

The `repo-web-prompt-template` contract SHALL reuse this shared Markdown formatting contract rather than duplicating it.

#### Scenario: Contributor reviews a governed prompt template

- **WHEN** a contributor opens a governed prompt template that emits Markdown
- **THEN** the prompt includes the shared Markdown and formatting rules
- **THEN** any shared web prompt structure requirements reference this contract instead of duplicating the formatting rules
