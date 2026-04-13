## MODIFIED Requirements

### Requirement: License analysis prompt output uses portable Markdown syntax
The prompt template SHALL comply with the shared Markdown contract defined in `prompt-markdown-format`.

In addition to that shared contract, the instruction SHALL appear under the section heading `### Markdown and Formatting Rules` and SHALL specify:

- **Score notation:** in the Score field, bare number only (1–5) — do not write `/5`
- **Research-mode suppression:** if the interface supports Research or Deep Research, the prompt SHALL instruct the model to do planning internally and return only the required license-analysis deliverable, with no generated research plan, executive summary, source appendix, methodology section, or provider-specific report wrapper

#### Scenario: Model uses AI-specific citation format
- **WHEN** an AI model would normally respond with numeric bracket citations like `[1]` or `【†source】`
- **THEN** the prompt instruction overrides this and the model uses `[Description](https://...)` inline links instead

#### Scenario: Response is opened in a standard Markdown viewer
- **WHEN** a researcher saves the response as a `.md` file and opens it in GitHub, VS Code, Obsidian, or Typora
- **THEN** all formatting renders correctly with no raw syntax visible and no broken elements

#### Scenario: Research-mode interface would normally emit a report shell
- **WHEN** a researcher runs the prompt in a Research or Deep Research web interface
- **THEN** the response omits any exposed plan, executive summary, or provider-native report wrapper and contains only the required license-analysis structure

### Requirement: License analysis prompt requires explicit uncertainty handling
The prompt template SHALL instruct the model to state "unknown" or "unclear" when license information cannot be confirmed from primary sources, and to never fabricate license names, URLs, or tier descriptions.

The prompt template SHALL also instruct the model to separate verified facts from any limited inference, and to prefer unknown over unsupported assumptions about enterprise tiers, bundled datasets, or licensing posture.

#### Scenario: Model cannot locate a license
- **WHEN** an AI cannot find a platform's license from the repository root, package metadata, or official site
- **THEN** the response states the license is unknown rather than guessing

#### Scenario: Model cannot confirm a tier distinction
- **WHEN** an AI cannot verify whether a community vs. enterprise split exists
- **THEN** the response states "unclear" rather than assuming

#### Scenario: Model finds indirect evidence for a paid tier
- **WHEN** an AI finds only partial or indirect evidence of a community-versus-enterprise split
- **THEN** it marks the distinction as unclear or explicitly inferred rather than presenting it as a verified fact

### Requirement: License analysis prompt instructs use of primary sources
The prompt template SHALL instruct the model to locate and verify license information from primary sources only — repository root (`LICENSE`, `COPYING`), SPDX identifiers in package metadata, and official site documentation.

The prompt template SHALL specify an evidence priority order for license claims: repository root license files first, package metadata or SPDX declarations second, official product or documentation pages third, and legal or pricing pages as supporting context for proprietary or open-core tier distinctions.

The prompt template MAY allow secondary sources to be used only to discover candidate repositories or official documentation locations, but not to support final license claims in the saved output.

#### Scenario: Model locates license from primary source
- **WHEN** an AI responds to the license analysis prompt
- **THEN** the source of the license identification is a direct link to the repository or official documentation, not a secondary summary

#### Scenario: Model distinguishes software licensing from commercial packaging
- **WHEN** an AI evaluates a platform with both open-source components and paid enterprise offerings
- **THEN** it cites primary sources that separately support the software license and the paid-tier or hosted-service distinction

#### Scenario: Model first finds a repository through a secondary source
- **WHEN** an AI uses a secondary source to discover a candidate repository or documentation page
- **THEN** it verifies the final claim against the repository or official documentation before including it in the response

### Requirement: License analysis prompt usage header includes save-as filename instruction
The prompt template's usage header SHALL include numbered step-by-step instructions telling the researcher to open the discovery response, copy the header row and the platform row from the summary table, replace `[PASTE_SELECTED_PLATFORM_HERE]` with those rows, and paste the completed prompt into their AI session. It SHALL also tell the researcher what filename to use when saving the response, referencing the pattern defined in `docs/02-methodology.md`, with a concrete example using the `license` prompt-type token (e.g., `responses/<platform>-license.md`).

The usage header SHALL NOT include a separate blockquote for the license taxonomy source of truth — the taxonomy is embedded in the prompt body.

The usage header SHALL also state that the prompt can be used in either an AI web research chat or an AI CLI session. For web chat use, it SHALL tell the researcher to manually save the final Markdown response into `responses/`.

#### Scenario: Researcher reads the usage header before pasting the prompt
- **WHEN** a researcher reads the usage instructions at the top of `prompts/license-analysis.md`
- **THEN** they see the row-paste steps, the expected filename pattern, and an explicit note that web-chat sessions require manual save/export into `responses/`, with no extra blockquotes beyond the save-as instruction
