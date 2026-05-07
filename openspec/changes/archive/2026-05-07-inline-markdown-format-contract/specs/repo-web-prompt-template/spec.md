## MODIFIED Requirements

### Requirement: Canonical web prompts reuse shared Markdown formatting

Canonical web prompt templates that conform to this contract and ask models to emit Markdown SHALL require `repo-prompt-markdown-format` as an inlined required contract.

The prompt SHALL list `openspec/specs/repo-prompt-markdown-format/spec.md` under `## Required Contracts`.

The web prompt template contract SHALL NOT require each prompt template to duplicate the full shared Markdown formatting rules in the prompt body.

#### Scenario: Prompt emits Markdown

- **WHEN** a conforming canonical web prompt asks a model to emit Markdown
- **THEN** it lists `repo-prompt-markdown-format` as a required contract
- **THEN** the resolver inlines the shared Markdown formatting contract before the prompt body
- **THEN** the prompt body can reference the inlined Markdown formatting contract instead of duplicating it
