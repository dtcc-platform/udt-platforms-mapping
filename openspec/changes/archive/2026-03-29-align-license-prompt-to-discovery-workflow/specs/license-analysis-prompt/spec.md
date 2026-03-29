## REMOVED Requirements

### Requirement: License analysis prompt uses a parameterized platform token
**Reason**: Replaced by a structured table row token that aligns with the discovery workflow. The two freeform tokens (`[PLATFORM_NAME]`, `[LICENSE_URL_OR_TEXT]`) are superseded by a single paste token fed from the discovery summary table.
**Migration**: Use `[PASTE_SELECTED_PLATFORM_HERE]` instead. Paste the header row and the platform row from the discovery summary table. The model derives the platform name from the Name column and uses the Link column to locate the license.

## ADDED Requirements

### Requirement: License analysis prompt uses a discovery table row token
The prompt template SHALL include a single `[PASTE_SELECTED_PLATFORM_HERE]` placeholder token where the researcher pastes one row (plus the header row) from the discovery response summary table. The model SHALL derive the platform name from the Name column, use the Link column to locate the license source, and treat the License column value as a seed signal to verify or correct.

#### Scenario: Researcher pastes a discovery row
- **WHEN** a researcher copies the header row and one data row from a discovery summary table and pastes them into `[PASTE_SELECTED_PLATFORM_HERE]`
- **THEN** the model identifies the platform, locates the license from the Link, and produces a full license analysis

#### Scenario: Researcher runs license analysis without a prior discovery session
- **WHEN** a researcher manually constructs a single-row table matching the discovery summary table schema and pastes it into `[PASTE_SELECTED_PLATFORM_HERE]`
- **THEN** the model produces a full license analysis using the provided fields

### Requirement: License analysis prompt usage header follows the discovery-to-prompt pattern
The prompt template's usage header SHALL instruct the researcher to open the discovery response, copy the header row and the platform row from the summary table, replace `[PASTE_SELECTED_PLATFORM_HERE]` with those rows, and paste the completed prompt into their AI session.

#### Scenario: Researcher reads the usage header
- **WHEN** a researcher reads the usage instructions at the top of `prompts/license-analysis.md`
- **THEN** they see the same row-paste pattern used by the comparison prompt, with a save-as filename instruction
