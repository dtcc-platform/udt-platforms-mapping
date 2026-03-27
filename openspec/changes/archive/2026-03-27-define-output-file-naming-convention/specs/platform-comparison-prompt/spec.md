## ADDED Requirements

### Requirement: Comparison prompt usage header includes save-as filename instruction
The prompt template's usage header SHALL include an instruction telling the researcher what filename to use when saving the AI response, referencing the pattern defined in `docs/methodology.md`.

The instruction SHALL show a concrete example filename using the `comparison` prompt-type token and the `vs` join convention for two platforms (e.g., `responses/<platform-a>-vs-<platform-b>-comparison.md`).

#### Scenario: Researcher reads the usage header before pasting the prompt
- **WHEN** a researcher reads the usage instructions at the top of `prompts/platform-comparison.md`
- **THEN** they see the expected filename pattern and a concrete example before they begin the session
