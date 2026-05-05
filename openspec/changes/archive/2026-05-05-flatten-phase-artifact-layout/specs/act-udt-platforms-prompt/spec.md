## MODIFIED Requirements

### Requirement: UDT platforms prompt executes through one governed path

The prompt SHALL instruct the user to use the resolved prompt in a web interface rather than treat CLI execution as the canonical path.
The prompt SHALL resolve `plan/udt-platforms-scope.md` into one copy-ready prompt block.
The prompt SHALL instruct the user to save the web response to `observe/udt-platforms-web-<model-short>.md`.

#### Scenario: Researcher runs the canonical prompt

- **WHEN** a researcher resolves `act/udt-platforms.md`
- **THEN** the prompt incorporates `plan/udt-platforms-scope.md`
- **THEN** the prompt tells the researcher to save the web response as a direct file under `observe/`
