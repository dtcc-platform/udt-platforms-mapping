## MODIFIED Requirements

### Requirement: UDT platforms prompt declares plan/udt-platforms/scope.md as a required input

The prompt SHALL include a `## Required Inputs` section listing:

- `plan/udt-platforms/scope.md`

#### Scenario: Researcher reviews the prompt header
- **WHEN** the researcher opens `act/udt-platforms/prompt.md`
- **THEN** the required-input list includes the scope file and does not require a separate source-policy file

### Requirement: UDT platforms prompt requests Type classification output only

The prompt SHALL instruct the model to return one `##`-level Markdown section per artifact and to assign exactly one `Type` value:

- `platform`
- `framework`
- `module`
- `excluded`

The summary table SHALL use exactly these columns:

- `Name`
- `Link`
- `Type`
- `Reason`

Only `Type = platform` rows are eligible for later platform comparison.
The prompt SHALL describe `udt-platforms` as a broad global discovery thread and MAY include lightweight evidence guidance that favors stronger sources without relying on a governed source-policy input.

#### Scenario: Model is asked to classify a candidate artifact
- **WHEN** the prompt is executed for `udt-platforms`
- **THEN** the model receives the Type contract and broad-discovery framing without requiring a separate source-policy file
