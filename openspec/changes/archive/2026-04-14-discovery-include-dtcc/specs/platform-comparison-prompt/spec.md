## MODIFIED Requirements

### Requirement: Comparison prompt includes DTCC as a required reference entry

The prompt template SHALL NOT include a hardcoded description of DTCC. Instead, the prompt SHALL instruct the model to treat the DTCC row from the pasted discovery table as the reference platform for landscape observations in Part 3.

The prompt SHALL note that the researcher MUST include the DTCC row when selecting platforms to paste into `[PASTE_SELECTED_PLATFORMS_HERE]`, so that Part 3 can orient landscape observations around DTCC.

The prompt SHALL retain the requirement that every response positions the landscape relative to DTCC — the change is only in how DTCC's profile data enters the prompt (via the pasted table row, not via a hardcoded block).

#### Scenario: Response is used to position DTCC in the landscape

- **WHEN** an AI responds to the comparison prompt with the DTCC row included in the pasted table
- **THEN** DTCC appears as a platform entry and the landscape observations section explicitly addresses where DTCC sits relative to comparable and complementary platforms

#### Scenario: Researcher pastes DTCC row from discovery into comparison

- **WHEN** a researcher copies the DTCC row from the discovery summary table and includes it in the platforms pasted into `[PASTE_SELECTED_PLATFORMS_HERE]`
- **THEN** the model uses that row's scores and metadata as DTCC's profile for the comparison, with no separate hardcoded block needed

#### Scenario: DTCC platform evolves and description drifts

- **WHEN** DTCC's capabilities change between research sessions
- **THEN** the researcher re-runs discovery to get an updated DTCC row and pastes that updated row into comparison, rather than needing to edit the comparison prompt itself

#### Scenario: Researcher omits the DTCC row from the pasted table

- **WHEN** a researcher pastes platforms into comparison without including the DTCC row
- **THEN** Part 3 landscape observations (DTCC's Position, Comparable Platforms, Complementary Platforms) cannot orient around DTCC; the comparison prompt should note that the DTCC row must be included
