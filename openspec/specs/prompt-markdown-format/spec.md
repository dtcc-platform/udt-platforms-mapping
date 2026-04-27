### Requirement: Prompt templates define a shared portable Markdown contract

Each governed prompt template file in the live repository that instructs an AI model to emit Markdown output SHALL include a `### Markdown and Formatting Rules` section defining the project's shared portable Markdown contract.

This shared contract SHALL apply to the governed prompt templates that explicitly rely on it, including current prompts such as `act/udt-platforms/prompt.md` and `act/udt-platform-comparison/prompt.md`.

The shared contract SHALL require output that renders correctly in standard Markdown viewers such as GitHub, VS Code, Obsidian, and Typora, without AI-specific formatting artifacts.
