## MODIFIED Requirements

### Requirement: UDT initiatives prompt is web-canonical

The prompt SHALL resolve `plan/udt-initiatives-scope.md` into one copy-ready prompt block.
The prompt SHALL instruct the user to paste the resolved prompt into a web interface and save the response to `observe/udt-initiatives-web-<model-short>.md`.

#### Scenario: Researcher runs the canonical prompt

- **WHEN** a researcher resolves `act/udt-initiatives.md`
- **THEN** the prompt incorporates `plan/udt-initiatives-scope.md`
- **THEN** the prompt tells the researcher to save the web response as a direct file under `observe/`
