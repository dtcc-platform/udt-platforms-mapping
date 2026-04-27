## MODIFIED Requirements

### Requirement: UDT platforms prompt declares plan/udt-platforms/scope.md as a required input

The prompt SHALL include a `## Required Inputs` section listing:

- `plan/udt-platforms/scope.md`
- `plan/udt-platforms/source-policy.md`

#### Scenario: Researcher reviews the prompt header
- **WHEN** the researcher opens `act/udt-platforms/prompt.md`
- **THEN** the required-input list includes both the scope file and the source-policy file

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
The prompt SHALL also instruct the model to follow `plan/udt-platforms/source-policy.md` when selecting and characterizing evidence.

#### Scenario: Model is asked to classify a candidate artifact
- **WHEN** the prompt is executed for `udt-platforms`
- **THEN** the model receives both the Type contract and the instruction to follow the governed source policy while making that classification
