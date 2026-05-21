## MODIFIED Requirements

### Requirement: Governed prompts define portable Markdown output

Each governed prompt template file in the live repository that instructs an AI model to emit Markdown output SHALL make `repo-prompt-markdown-format` available to the model either by declaring it as a required contract or by rendering equivalent rules into the resolved prompt.

Canonical web prompt templates that conform to `act-web-prompt-template` SHALL declare `openspec/specs/repo-prompt-markdown-format/spec.md` under `## Required Contracts`.

This shared contract SHALL apply to the governed prompt templates that explicitly rely on it, including current prompts such as `act/discover-entities.md` and `act/compare-platforms.md`.

The `act-web-prompt-template` contract SHALL reuse this shared Markdown formatting contract rather than duplicating it.

#### Scenario: Contributor reviews a governed prompt template

- **WHEN** a contributor opens a governed prompt template that emits Markdown
- **THEN** the prompt declares or renders the shared Markdown formatting rules
- **THEN** any shared web prompt structure requirements reference this contract instead of duplicating the formatting rules
