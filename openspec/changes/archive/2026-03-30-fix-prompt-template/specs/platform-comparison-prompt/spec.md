## MODIFIED Requirements

### Requirement: Comparison prompt usage header includes save-as filename instruction

The prompt template's usage header SHALL include an instruction telling the researcher what filename to use when saving the AI response, referencing the pattern defined in `docs/methodology.md`.

The instruction SHALL show a concrete example filename using the `comparison` prompt-type token and the `vs` join convention for two platforms (e.g., `responses/<platform-a>-vs-<platform-b>-comparison.md`).

The usage header SHALL also include a step directing the researcher to paste into their AI session starting from the cut-line (the blockquote `> Paste into your AI session from this line onwards.`), not from the top of the file.

#### Scenario: Researcher reads the usage header before pasting the prompt

- **WHEN** a researcher reads the usage instructions at the top of `prompts/platform-comparison.md`
- **THEN** they see the expected filename pattern, a concrete example, and an explicit step telling them to paste from the cut-line onwards

#### Scenario: Researcher pastes only the AI-facing section

- **WHEN** a researcher follows the usage instructions and pastes from the cut-line onwards into a fresh AI session
- **THEN** the model receives no human-facing usage steps, only the AI prompt body, and produces the comparison report without confusion
