## MODIFIED Requirements

### Requirement: Comparison prompt uses a single selection table token

The prompt template SHALL include a single `[PASTE_SELECTED_PLATFORMS_HERE]` placeholder token where the researcher pastes the rows they want to compare from the discovery response summary table, including the header row. The model SHALL treat every data row in the pasted table as a comparison target.

The placeholder SHALL be immediately preceded by the canonical guard instruction specifying `[PASTE_SELECTED_PLATFORMS_HERE]` as the token to check for, instructing the model to stop and ask the user for the table if the placeholder is still present.

#### Scenario: Researcher customizes platforms to compare

- **WHEN** a researcher copies two rows (plus the header) from a discovery summary table and pastes them into `[PASTE_SELECTED_PLATFORMS_HERE]`
- **THEN** the model produces a comparison specifically for those two platforms

#### Scenario: Researcher compares more than two platforms

- **WHEN** a researcher copies three or more rows (plus the header) into `[PASTE_SELECTED_PLATFORMS_HERE]`
- **THEN** the model produces a comparison covering all pasted platforms without requiring any other prompt changes

#### Scenario: Prompt is used via @file reference without filling in the placeholder

- **WHEN** a model receives the prompt with the literal text `[PASTE_SELECTED_PLATFORMS_HERE]` still present
- **THEN** the model stops and asks the user to paste the platform rows before continuing, and does not generate any comparison output
