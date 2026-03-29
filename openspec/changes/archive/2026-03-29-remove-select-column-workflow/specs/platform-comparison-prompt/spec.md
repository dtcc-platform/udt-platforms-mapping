## MODIFIED Requirements

### Requirement: Comparison prompt uses a single selection table token
The prompt template SHALL include a single `[PASTE_SELECTED_PLATFORMS_HERE]` placeholder token where the researcher pastes the rows they want to compare from the discovery response summary table, including the header row. The model SHALL treat every data row in the pasted table as a comparison target.

#### Scenario: Researcher customizes platforms to compare
- **WHEN** a researcher copies two rows (plus the header) from a discovery summary table and pastes them into `[PASTE_SELECTED_PLATFORMS_HERE]`
- **THEN** the model produces a comparison specifically for those two platforms

#### Scenario: Researcher compares more than two platforms
- **WHEN** a researcher copies three or more rows (plus the header) into `[PASTE_SELECTED_PLATFORMS_HERE]`
- **THEN** the model produces a comparison covering all pasted platforms without requiring any other prompt changes
