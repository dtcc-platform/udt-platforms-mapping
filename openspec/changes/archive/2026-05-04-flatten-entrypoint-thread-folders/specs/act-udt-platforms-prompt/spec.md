## MODIFIED Requirements

### Requirement: UDT platforms prompt file exists

The repository SHALL contain a file at `act/udt-platforms.md` that provides a self-contained prompt template for AI-assisted technical-artifact mapping of UDT platforms.

#### Scenario: Researcher finds the UDT platforms prompt

- **WHEN** a researcher opens `act/`
- **THEN** `act/udt-platforms.md` is available as the canonical `udt-platforms` prompt template

### Requirement: UDT platforms prompt requests Type classification output only

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

### Requirement: UDT platforms prompt declares plan/udt-platforms-scope.md as a required input

The prompt SHALL include a `## Required Inputs` section listing:

- `plan/udt-platforms-scope.md`

#### Scenario: Prompt lists flattened required input

- **WHEN** a researcher opens `act/udt-platforms.md`
- **THEN** the required inputs list references `plan/udt-platforms-scope.md`

### Requirement: UDT platforms prompt executes through one governed path

The prompt SHALL instruct the user to use the resolved prompt in a web interface rather than treat CLI execution as the canonical path.
The prompt SHALL resolve `plan/udt-platforms-scope.md` into one copy-ready prompt block.
The prompt SHALL instruct the user to save the web response to `observe/udt-platforms/web-<model-short>.md`.

#### Scenario: Researcher runs the canonical prompt

- **WHEN** a researcher resolves `act/udt-platforms.md`
- **THEN** the prompt incorporates `plan/udt-platforms-scope.md`
- **THEN** the prompt tells the researcher to save the web response under `observe/udt-platforms/`
