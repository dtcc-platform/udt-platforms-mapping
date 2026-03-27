## ADDED Requirements

### Requirement: Platform discovery prompt file exists
The repository SHALL contain a file at `prompts/platform-discovery.md` that provides a self-contained prompt template for AI-assisted discovery of UDT platforms.

#### Scenario: File is present and non-empty
- **WHEN** a researcher navigates to `prompts/platform-discovery.md`
- **THEN** the file exists and contains a complete, copy-pasteable prompt

### Requirement: Discovery prompt embeds inclusion criteria
The prompt template SHALL include all three inclusion criteria from `docs/methodology.md` — Explicit Urban Digital Twin, City-Scale Capabilities, and Adjacent Architecture or Governance — so the model can apply them without additional context.

#### Scenario: Researcher pastes prompt without supplemental docs
- **WHEN** a researcher copies the prompt and pastes it into an AI chat session without pasting `docs/methodology.md`
- **THEN** the model has sufficient criteria to correctly classify a platform as in-scope or out-of-scope

### Requirement: Discovery prompt requests structured output aligned with inventory
The prompt template SHALL instruct the model to return results in a structure that maps to the columns of `docs/platform-inventory.md` (platform name, origin, type, license, maturity, city-scale capability, integration posture, and notes).

#### Scenario: Response is used to populate inventory
- **WHEN** an AI responds to the discovery prompt
- **THEN** the response contains clearly labelled fields that can be directly transferred to platform-inventory.md rows

### Requirement: Discovery prompt uses a parameterized search scope token
The prompt template SHALL include a `[SEARCH_SCOPE]` placeholder that the researcher replaces with a specific domain, region, or technology focus before using the prompt.

#### Scenario: Researcher customizes search scope
- **WHEN** a researcher replaces `[SEARCH_SCOPE]` with a value such as "European city-scale platforms" or "platforms using CityGML"
- **THEN** the model scopes its discovery results to that domain without other prompt changes needed
