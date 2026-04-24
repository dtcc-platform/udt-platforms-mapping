## ADDED Requirements

### Requirement: Rating reporting prompt file exists

The repository SHALL contain a file at `reflect/rating/reporting/prompt.md` that provides a self-contained AI CLI prompt for generating the structured rating reporting outputs from files in `observe/rating/`.

#### Scenario: File is present and non-empty

- **WHEN** a researcher navigates to `reflect/rating/reporting/prompt.md`
- **THEN** the file exists and contains a complete CLI prompt

### Requirement: Rating reporting prompt scans observe/rating automatically

The prompt SHALL instruct the model to read all relevant files in `observe/rating/` without requiring manual path input.

#### Scenario: Researcher runs the prompt

- **WHEN** a researcher runs `reflect/rating/reporting/prompt.md`
- **THEN** the model scans `observe/rating/` automatically

### Requirement: Rating reporting prompt generates CSV and HTML outputs

The prompt SHALL instruct the model to generate:
- `reflect/rating/reporting/ecosystem.csv`
- `reflect/rating/reporting/ecosystem-map.html`

#### Scenario: Researcher completes rating reporting

- **WHEN** the model finishes the rating reporting prompt
- **THEN** it writes `ecosystem.csv` and `ecosystem-map.html` under `reflect/rating/reporting/`
