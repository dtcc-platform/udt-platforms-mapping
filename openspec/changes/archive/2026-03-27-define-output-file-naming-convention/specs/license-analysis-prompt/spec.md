## ADDED Requirements

### Requirement: License analysis prompt usage header includes save-as filename instruction
The prompt template's usage header SHALL include an instruction telling the researcher what filename to use when saving the AI response, referencing the pattern defined in `docs/methodology.md`.

The instruction SHALL show a concrete example filename using the `license` prompt-type token (e.g., `responses/<platform>-license.md`).

#### Scenario: Researcher reads the usage header before pasting the prompt
- **WHEN** a researcher reads the usage instructions at the top of `prompts/license-analysis.md`
- **THEN** they see the expected filename pattern and a concrete example before they begin the session
