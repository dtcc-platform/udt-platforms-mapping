## MODIFIED Requirements

### Requirement: observe/ holds canonical saved outputs by action and model

`observe/platform-discovery-chatgpt.md`, `observe/platform-discovery-claude.md`, and `observe/platform-discovery-gemini.md` SHALL contain saved web responses for platform discovery.
Saved initiative discovery responses SHALL use the pattern `observe/initiative-discovery-<model-short>.md`.
`observe/platform-comparison-chatgpt.md`, `observe/platform-comparison-claude.md`, and `observe/platform-comparison-gemini.md` SHALL contain saved web responses for platform comparison.
Observed workflow outputs, such as `observe/platform-discovery-coverage.md`, SHALL also live as direct files under `observe/`.

#### Scenario: Researcher saves a web response

- **WHEN** a researcher saves a canonical web response
- **THEN** the response is saved as a direct file under `observe/`
- **THEN** the filename identifies the research action and model
