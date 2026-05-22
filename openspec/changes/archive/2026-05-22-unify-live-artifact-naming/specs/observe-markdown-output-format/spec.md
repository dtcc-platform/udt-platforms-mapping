## MODIFIED Requirements

### Requirement: Governed prompts define portable Markdown output

Each governed prompt template file in the live repository that instructs an AI model to emit Markdown output SHALL make `observe-markdown-output-format` available to the model either by declaring it as a required contract or by rendering equivalent rules into the resolved prompt.

Canonical web prompt templates that conform to `act-web-prompt-template` SHALL declare `openspec/specs/observe-markdown-output-format/spec.md` under `## Required Contracts`.

This shared contract SHALL apply to governed Markdown outputs that explicitly rely on it, including current outputs produced from prompts such as `act/entity-discovery.md` and `act/platform-comparison.md`.

The `act-web-prompt-template` contract SHALL reuse this shared Markdown output formatting contract rather than duplicating it.

#### Scenario: Contributor reviews a governed prompt template

- **WHEN** a contributor opens a governed prompt template that emits Markdown
- **THEN** the prompt declares or renders the shared Markdown output formatting rules
- **THEN** any shared web prompt structure requirements reference this contract instead of duplicating the formatting rules
