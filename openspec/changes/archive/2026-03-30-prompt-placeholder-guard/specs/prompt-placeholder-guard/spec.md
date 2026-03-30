## ADDED Requirements

### Requirement: Placeholder guard canonical wording is defined

The project SHALL maintain a canonical guard instruction wording for use before any required user-data placeholder in a prompt file. The canonical wording is:

> **Before proceeding:** If the placeholder below still contains the literal text `[PLACEHOLDER]`, stop and ask the user to supply the required data before continuing. Do not attempt to generate output without it.

Where `[PLACEHOLDER]` is substituted with the exact placeholder token used in that prompt (e.g. `[PASTE_SELECTED_PLATFORMS_HERE]`).

#### Scenario: New prompt file is added with a required placeholder

- **WHEN** a contributor adds a new prompt file that contains a required user-data placeholder
- **THEN** the contributor places the canonical guard instruction immediately before the placeholder, substituting the exact placeholder token into the wording

#### Scenario: Existing prompt file already uses the guard

- **WHEN** a contributor reads any prompt file that has a required placeholder
- **THEN** they find the guard instruction immediately preceding the placeholder, using the canonical wording

### Requirement: Guard instruction is placed immediately before the placeholder

Each required user-data placeholder in a prompt file SHALL be preceded immediately by the canonical guard instruction block, with no intervening content between the guard and the placeholder it protects.

#### Scenario: Model receives the prompt with an unfilled placeholder

- **WHEN** a model processes a prompt where the placeholder literal text is still present
- **THEN** the model stops before generating any output and asks the user to supply the required data

#### Scenario: Model receives the prompt with a filled placeholder

- **WHEN** a model processes a prompt where the placeholder has been replaced with real data
- **THEN** the model proceeds normally without asking for data
