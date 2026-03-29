## MODIFIED Requirements

### Requirement: License analysis prompt usage header includes save-as filename instruction
The prompt template's usage header SHALL include numbered step-by-step instructions telling the researcher to open the discovery response, copy the header row and the platform row from the summary table, replace `[PASTE_SELECTED_PLATFORM_HERE]` with those rows, and paste the completed prompt into their AI session. It SHALL also tell the researcher what filename to use when saving the response, referencing the pattern defined in `docs/methodology.md`, with a concrete example using the `license` prompt-type token (e.g., `responses/<platform>-license.md`).

The usage header SHALL NOT include a separate blockquote for the license taxonomy source of truth — the taxonomy is embedded in the prompt body.

#### Scenario: Researcher reads the usage header before pasting the prompt
- **WHEN** a researcher reads the usage instructions at the top of `prompts/license-analysis.md`
- **THEN** they see the row-paste steps and the expected filename pattern before they begin the session, with no extra blockquotes beyond the save-as instruction
