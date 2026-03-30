## MODIFIED Requirements

### Requirement: License analysis prompt uses a discovery table row token

The prompt template SHALL include a single `[PASTE_SELECTED_PLATFORM_HERE]` placeholder token where the researcher pastes one row (plus the header row) from the discovery response summary table. The model SHALL derive the platform name from the Name column, use the Link column to locate the license source, and treat the License column value as a seed signal to verify or correct.

The placeholder SHALL be immediately preceded by the canonical guard instruction specifying `[PASTE_SELECTED_PLATFORM_HERE]` as the token to check for, instructing the model to stop and ask the user for the platform row if the placeholder is still present.

#### Scenario: Researcher pastes a discovery row

- **WHEN** a researcher copies the header row and one data row from a discovery summary table and pastes them into `[PASTE_SELECTED_PLATFORM_HERE]`
- **THEN** the model identifies the platform, locates the license from the Link, and produces a full license analysis

#### Scenario: Researcher runs license analysis without a prior discovery session

- **WHEN** a researcher manually constructs a single-row table matching the discovery summary table schema and pastes it into `[PASTE_SELECTED_PLATFORM_HERE]`
- **THEN** the model produces a full license analysis using the provided fields

#### Scenario: Prompt is used via @file reference without filling in the placeholder

- **WHEN** a model receives the prompt with the literal text `[PASTE_SELECTED_PLATFORM_HERE]` still present
- **THEN** the model stops and asks the user to paste the platform row before continuing, and does not generate any license analysis output
