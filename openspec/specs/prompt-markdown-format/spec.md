## Purpose

Defines the shared portable Markdown contract used by governed prompt templates that instruct AI models to emit Markdown output.

## Requirements

### Requirement: Prompt templates define a shared portable Markdown contract

Each governed prompt template file in the live repository that instructs an AI model to emit Markdown output SHALL include a `### Markdown and Formatting Rules` section defining the project's shared portable Markdown contract.

This shared contract SHALL apply to the governed prompt templates that explicitly rely on it, including current prompts such as `act/udt-platforms.md` and `act/udt-platform-comparison.md`.

The shared contract SHALL require output that renders correctly in standard Markdown viewers such as GitHub, VS Code, Obsidian, and Typora, without AI-specific formatting artifacts.

#### Scenario: Governed prompt declares Markdown rules

- **WHEN** a governed prompt template relies on the shared portable Markdown contract
- **THEN** it includes a `### Markdown and Formatting Rules` section
- **THEN** the section requires standard Markdown output without AI-specific formatting artifacts
