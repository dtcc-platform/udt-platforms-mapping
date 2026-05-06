## ADDED Requirements

### Requirement: Platform comparison scores governed dimensions

Platform comparison SHALL evaluate selected platforms using governed comparison dimensions and scoring rules.

Each scored dimension SHALL use a 1-5 scale unless the evidence is insufficient.

When evidence is insufficient, platform comparison SHALL use `?`.

#### Scenario: Platform is scored

- **WHEN** platform comparison evaluates a selected platform
- **THEN** each governed dimension receives a score from 1 to 5 or `?`

### Requirement: Scoring uses rubric-defined evidence expectations

Platform comparison SHALL assign scores according to rubric-defined evidence expectations for each dimension.

Platform comparison SHALL NOT assign high scores based only on marketing claims or unsupported assertions.

#### Scenario: Evidence is weak

- **WHEN** a platform has only unsupported marketing claims for a dimension
- **THEN** platform comparison does not assign a high score for that dimension

### Requirement: Comparison scope remains platform-only

Platform comparison SHALL compare only artifacts classified as `platform`.

Platform comparison SHALL NOT broaden the selected comparison set to frameworks, modules, initiatives, or unrelated smart-city projects.

#### Scenario: Non-platform appears in comparison input

- **WHEN** a comparison input includes an artifact that is not classified as `platform`
- **THEN** platform comparison does not treat it as an eligible platform comparison target
