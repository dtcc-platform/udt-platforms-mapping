## ADDED Requirements

### Requirement: Rating reporting owns ecosystem CSV and HTML outputs

The structured ecosystem export files SHALL belong to the rating reporting phase, not the discovery reporting phase.

The repository SHALL treat these as the canonical rating reporting outputs:
- `reflect/rating/reporting/ecosystem.csv`
- `reflect/rating/reporting/ecosystem-map.html`

#### Scenario: Researcher looks for structured export outputs

- **WHEN** a researcher wants CSV or HTML ecosystem outputs
- **THEN** they use the rating reporting workflow under `reflect/rating/reporting/`

### Requirement: Rating ecosystem CSV is comparison-oriented

`reflect/rating/reporting/ecosystem.csv` SHALL contain rows derived from rating/comparison responses rather than raw discovery reporting summaries.

#### Scenario: Researcher opens the rating ecosystem CSV

- **WHEN** a researcher opens `reflect/rating/reporting/ecosystem.csv`
- **THEN** the file reflects structured rating output rather than discovery-only extraction
