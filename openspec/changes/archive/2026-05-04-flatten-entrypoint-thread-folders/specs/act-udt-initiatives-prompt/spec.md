## MODIFIED Requirements

### Requirement: UDT initiatives prompt file exists

The repository SHALL contain a file at `act/udt-initiatives.md` that provides a self-contained prompt template for AI-assisted initiative and project mapping of UDT-related efforts.

#### Scenario: Researcher finds the UDT initiatives prompt

- **WHEN** a researcher opens `act/`
- **THEN** `act/udt-initiatives.md` is available as the canonical `udt-initiatives` prompt template

### Requirement: UDT initiatives prompt declares required inputs

The prompt SHALL include a `## Required Inputs` section listing:

- `plan/udt-initiatives-scope.md`

#### Scenario: Prompt lists flattened required input

- **WHEN** a researcher opens `act/udt-initiatives.md`
- **THEN** the required inputs list references `plan/udt-initiatives-scope.md`

### Requirement: UDT initiatives prompt uses the initiative table contract

The prompt SHALL instruct the model to return a summary table with exactly these columns:

- `Initiative`
- `Link`
- `Uses`
- `Reason`

The prompt SHALL preserve `Uses = ?` when the technical substrate is unclear.

#### Scenario: Prompt provides the initiative table contract

- **WHEN** the researcher resolves `act/udt-initiatives.md`
- **THEN** the resolved prompt contains the `Initiative`, `Link`, `Uses`, `Reason` summary table format
- **THEN** the prompt allows `Uses = ?` when the technical substrate is unclear

### Requirement: UDT initiatives prompt is web-canonical

The prompt SHALL resolve `plan/udt-initiatives-scope.md` into one copy-ready prompt block.
The prompt SHALL instruct the user to paste the resolved prompt into a web interface and save the response to `observe/udt-initiatives/web-<model-short>.md`.

#### Scenario: Researcher runs the canonical prompt

- **WHEN** a researcher resolves `act/udt-initiatives.md`
- **THEN** the prompt incorporates `plan/udt-initiatives-scope.md`
- **THEN** the prompt tells the researcher to save the web response under `observe/udt-initiatives/`
