## MODIFIED Requirements

### Requirement: License analysis prompt usage header includes save-as filename instruction
The prompt template's usage header SHALL include numbered step-by-step instructions telling the researcher to open the discovery response, copy the header row and the platform row from the summary table, replace `[PASTE_SELECTED_PLATFORM_HERE]` with those rows, and paste the completed prompt into their AI session. It SHALL also tell the researcher what filename to use when saving the response, referencing the pattern defined in `docs/02-methodology.md`, with a concrete example using the `license` prompt-type token (e.g., `responses/<platform>-license.md`).

The usage header SHALL be separated from the AI-facing prompt body by a horizontal rule (`---`) followed immediately by a `> Paste into your AI session from this line onwards.` blockquote, matching the convention used in `prompts/platform-discovery.md` and `prompts/platform-comparison.md`.

The usage header SHALL NOT include a separate blockquote for the license taxonomy source of truth — the taxonomy is embedded in the prompt body.

The usage header SHALL also state that the prompt can be used in either an AI web research chat or an AI CLI session. For web chat use, it SHALL tell the researcher to manually save the final Markdown response into `responses/`.

#### Scenario: Researcher reads the usage header before pasting the prompt
- **WHEN** a researcher reads the usage instructions at the top of `prompts/license-analysis.md`
- **THEN** they see the row-paste steps, the expected filename pattern, and an explicit note that web-chat sessions require manual save/export into `responses/`, with no extra blockquotes beyond the save-as instruction

#### Scenario: Researcher follows the cut-line convention
- **WHEN** a researcher pastes from the `> Paste into your AI session from this line onwards.` blockquote onwards into their AI session
- **THEN** the model receives only the AI-facing prompt body — no usage steps, filename instructions, or web-chat guidance are included in the pasted content
