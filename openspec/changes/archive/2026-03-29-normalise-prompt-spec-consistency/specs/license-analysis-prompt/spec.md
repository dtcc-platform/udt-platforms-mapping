## REMOVED Requirements

### Requirement: License analysis prompt usage header follows the discovery-to-prompt pattern
**Reason**: Overlaps entirely with "License analysis prompt usage header includes save-as filename instruction". The save-as requirement is the canonical form; the discovery-to-prompt pattern requirement duplicates it with different framing.
**Migration**: The step-by-step usage header instruction is retained in "License analysis prompt usage header includes save-as filename instruction".

## MODIFIED Requirements

### Requirement: License analysis prompt usage header includes save-as filename instruction
The prompt template's usage header SHALL include numbered step-by-step instructions telling the researcher to open the discovery response, copy the header row and the platform row from the summary table, replace `[PASTE_SELECTED_PLATFORM_HERE]` with those rows, and paste the completed prompt into their AI session. It SHALL also tell the researcher what filename to use when saving the response, referencing the pattern defined in `docs/methodology.md`, with a concrete example using the `license` prompt-type token (e.g., `responses/<platform>-license.md`).

#### Scenario: Researcher reads the usage header before pasting the prompt
- **WHEN** a researcher reads the usage instructions at the top of `prompts/license-analysis.md`
- **THEN** they see the row-paste steps and the expected filename pattern before they begin the session

## ADDED Requirements

### Requirement: License analysis prompt requires explicit uncertainty handling
The prompt template SHALL instruct the model to state "unknown" or "unclear" when license information cannot be confirmed from primary sources, and to never fabricate license names, URLs, or tier descriptions.

#### Scenario: Model cannot locate a license
- **WHEN** an AI cannot find a platform's license from the repository root, package metadata, or official site
- **THEN** the response states the license is unknown rather than guessing

#### Scenario: Model cannot confirm a tier distinction
- **WHEN** an AI cannot verify whether a community vs. enterprise split exists
- **THEN** the response states "unclear" rather than assuming

### Requirement: License analysis prompt instructs use of primary sources
The prompt template SHALL instruct the model to locate and verify license information from primary sources only — repository root (`LICENSE`, `COPYING`), SPDX identifiers in package metadata, and official site documentation.

#### Scenario: Model locates license from primary source
- **WHEN** an AI responds to the license analysis prompt
- **THEN** the source of the license identification is a direct link to the repository or official documentation, not a secondary summary
