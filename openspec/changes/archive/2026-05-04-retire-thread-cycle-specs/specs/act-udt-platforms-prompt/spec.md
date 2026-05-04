## MODIFIED Requirements

### Requirement: UDT platforms prompt requests Type classification output only

The prompt SHALL instruct the model to classify technical artifacts only.
The prompt SHALL instruct the model to return one `##`-level Markdown section per artifact and to assign exactly one `Type` value:

- `platform`
- `framework`
- `module`
- `excluded`

The prompt SHALL own the concrete output-format instructions for `udt-platforms` web responses.
The summary table SHALL use exactly these columns:

- `Name`
- `Link`
- `Type`
- `Reason`

The prompt SHALL state that `Reason` is blank for in-scope rows and contains a brief phrase for `excluded` rows.
The prompt SHALL state that only `Type = platform` rows are eligible for later platform comparison.
The prompt SHALL include a per-artifact section template with `Link`, `Type`, and conditional `Reason` fields.
The prompt SHALL describe `udt-platforms` as a broad global discovery thread and instruct the model to prefer stronger evidence when available without turning the thread into a strict source-policy workflow.

#### Scenario: Prompt provides the output format without relying on scope

- **WHEN** the researcher resolves `act/udt-platforms.md`
- **THEN** the resolved prompt contains the `Name`, `Link`, `Type`, `Reason` summary table format
- **THEN** the resolved prompt contains the per-artifact section template
- **THEN** the output-format instructions come from the prompt template rather than `plan/udt-platforms-scope.md`

#### Scenario: Platform comparison receives platform rows only

- **WHEN** `udt-platform-comparison` selects candidates from `udt-platforms`
- **THEN** only rows where `Type = platform` are eligible
