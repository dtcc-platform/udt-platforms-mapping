## MODIFIED Requirements

### Requirement: UDT initiatives prompt uses the initiative table contract

The prompt SHALL instruct the model to map initiative-level efforts rather than technical artifacts.
The prompt SHALL instruct the model to return a summary table with exactly these columns:

- `Initiative`
- `Link`
- `Uses`
- `Reason`

The prompt SHALL preserve `Uses = ?` when the technical substrate is unclear.
The prompt SHALL instruct the model to use a comma-separated list of artifact names from `udt-platforms` when an initiative's technical substrate is clear.
The prompt SHALL describe `udt-initiatives` as a broad global discovery thread that prioritizes recall.

#### Scenario: Prompt provides the initiative table contract

- **WHEN** the researcher resolves `act/udt-initiatives.md`
- **THEN** the resolved prompt contains the `Initiative`, `Link`, `Uses`, `Reason` summary table format
- **THEN** the prompt allows `Uses = ?` when the technical substrate is unclear
