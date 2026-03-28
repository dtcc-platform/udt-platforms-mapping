## MODIFIED Requirements

### Requirement: Comparison prompt uses parameterized platform name tokens
The prompt template SHALL include a single `[PASTE_SELECTED_PLATFORMS_HERE]` placeholder token where the researcher pastes the `x`-marked rows from the discovery response summary table. The model SHALL treat every row in the pasted table as a comparison target.

#### Scenario: Researcher customizes platforms to compare
- **WHEN** a researcher pastes two `x`-marked rows from a discovery summary table into `[PASTE_SELECTED_PLATFORMS_HERE]`
- **THEN** the model produces a comparison specifically for those two platforms

#### Scenario: Researcher compares more than two platforms
- **WHEN** a researcher pastes three or more rows into `[PASTE_SELECTED_PLATFORMS_HERE]`
- **THEN** the model produces a comparison covering all pasted platforms without requiring any other prompt changes

## REMOVED Requirements

### Requirement: Comparison prompt accepts inventory context
**Reason**: Replaced by the selection table input — the pasted rows from the discovery summary already contain key context fields (Type, License, Maturity). A separate inventory paste token is redundant.
**Migration**: Paste selected rows from the discovery response summary table into `[PASTE_SELECTED_PLATFORMS_HERE]` instead.
