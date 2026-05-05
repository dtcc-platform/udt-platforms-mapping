## MODIFIED Requirements

### Requirement: Comparison prompt executes through one governed path

The prompt SHALL instruct the user to use the resolved prompt in a web interface rather than treat CLI execution as the canonical path.
The prompt SHALL resolve all three required inputs into one copy-ready prompt block.
The prompt SHALL instruct the user to save the web response to `observe/udt-platform-comparison-web-<model-short>.md`.

#### Scenario: Researcher runs the canonical prompt

- **WHEN** a researcher resolves `act/udt-platform-comparison.md`
- **THEN** the prompt incorporates the flattened comparison planning inputs
- **THEN** the prompt tells the researcher to save the web response as a direct file under `observe/`
