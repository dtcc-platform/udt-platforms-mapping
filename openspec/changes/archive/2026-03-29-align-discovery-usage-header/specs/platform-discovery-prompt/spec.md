## MODIFIED Requirements

### Requirement: Discovery prompt usage header includes save-as filename instruction
The prompt template's usage header SHALL include numbered step-by-step instructions telling the researcher to replace `[SEARCH_SCOPE]` with their focus area, paste the completed prompt into their AI session, and save the response using the filename pattern defined in `docs/methodology.md`, with a concrete example using the `discovery` prompt-type token (e.g., `responses/european-platforms-discovery.md`).

#### Scenario: Researcher reads the usage header before pasting the prompt
- **WHEN** a researcher reads the usage instructions at the top of `prompts/platform-discovery.md`
- **THEN** they see numbered steps and the expected filename pattern before they begin the session
