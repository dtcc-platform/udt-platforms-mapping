## MODIFIED Requirements

### Requirement: Comparison prompt uses a single selection table token
The prompt template SHALL include a single `[PASTE_SELECTED_PLATFORMS_HERE]` placeholder token where the researcher pastes the rows they want to compare from the discovery response summary table, including the header row. The model SHALL treat every data row in the pasted table as a comparison target.

The placeholder SHALL be preceded by the canonical guard instruction specifying `[PASTE_SELECTED_PLATFORMS_HERE]` as the token to check for, instructing the model to stop and ask the user for the table if the placeholder is still present.

The prompt template SHALL also instruct the model that the pasted table is the comparison scope boundary and that it MUST NOT add new comparison candidates outside the pasted rows unless the user explicitly asks for that expansion. When both instructions are present, the guard instruction SHALL appear before the scope-boundary instruction, and the scope-boundary instruction SHALL appear immediately before the placeholder. This constraint applies to candidates introduced autonomously by the model or research interface; platforms explicitly named in the prompt body as reference entries (such as DTCC) are not subject to this restriction.

#### Scenario: Researcher customizes platforms to compare
- **WHEN** a researcher copies two rows (plus the header) from a discovery summary table and pastes them into `[PASTE_SELECTED_PLATFORMS_HERE]`
- **THEN** the model produces a comparison specifically for those two platforms

#### Scenario: Research-mode interface tries to broaden scope
- **WHEN** a researcher runs the prompt in a Research or Deep Research interface
- **THEN** the model limits the comparison to the pasted platform rows and does not introduce extra platforms on its own

#### Scenario: Prompt is used via @file reference without filling in the placeholder
- **WHEN** a model receives the prompt with the literal text `[PASTE_SELECTED_PLATFORMS_HERE]` still present
- **THEN** the model stops and asks the user to paste the platform rows before continuing, and does not generate any comparison output

### Requirement: Comparison prompt enforces agent-agnostic output structure
The prompt template SHALL include a concrete example of the per-platform profile structure so any agent can reproduce the exact shape mechanically. The prompt SHALL comply with the shared Markdown contract defined in `prompt-markdown-format`.

In addition to that shared contract, the prompt SHALL specify:

- **Profile heading level:** every platform profile SHALL use `###` as the top-level heading so profiles nest consistently under part headings
- **Score notation:** dimension scores SHALL always be written as `X/5` (e.g., `4/5`) — no other formats (`★★★★☆`, `4 out of 5`, `80%`, bold numbers) are permitted
- **Score placement:** in profiles, scores SHALL appear inline with the dimension label as `**Dimension (X/5):**` — e.g., `**Technical Architecture (4/5):**`
- **Score in table:** in the scoring table, score cells SHALL contain only the numeric value (e.g., `4`) with `?` for unknown — no `/5` suffix in table cells
- **Research-mode suppression:** if the interface supports Research or Deep Research, the prompt SHALL instruct the model to do planning internally and return only the required three-part comparison output, with no generated research plan, executive summary, source appendix, methodology section, or provider-specific report wrapper

The prompt SHALL include a concrete example profile for one fictional platform demonstrating the exact heading levels, field labels, score notation, and sources section structure.

#### Scenario: Two agents respond to the same prompt
- **WHEN** a researcher runs the comparison prompt on ChatGPT and on Claude
- **THEN** both responses use identical heading levels, field labels, and score notation — the only difference is the content

#### Scenario: Response is opened in a standard Markdown viewer
- **WHEN** a researcher saves the response as a `.md` file and opens it in GitHub, VS Code, Obsidian, or Typora
- **THEN** all formatting renders correctly with no raw syntax visible, no broken elements, and no AI-specific artifacts

#### Scenario: Research-mode interface would normally emit a report shell
- **WHEN** a researcher runs the comparison prompt in a Research or Deep Research web interface
- **THEN** the response omits any exposed research plan, executive summary, or provider-native report shell and contains only the required three parts in the required order

### Requirement: Comparison prompt instructs use of primary sources
The prompt template SHALL instruct the model to base its comparison on primary sources (official documentation, repositories, published papers) and to cite sources for each claim.

The prompt template MAY allow secondary sources to be used only to discover relevant primary sources or candidate documentation paths, but final factual claims and saved output citations SHALL rely on primary sources.

#### Scenario: Response includes source citations
- **WHEN** an AI responds to the comparison prompt
- **THEN** each substantive claim is accompanied by a source reference or URL

#### Scenario: Model first finds a platform detail through a secondary article
- **WHEN** an AI uses a secondary source to discover a possible claim or document location
- **THEN** it verifies the claim against a primary source before including it in the final comparison

### Requirement: Comparison prompt requires explicit uncertainty handling
The prompt template SHALL instruct the model to distinguish inferred claims from verified facts, state "unknown" or "unclear" when information is not findable, and never fabricate URLs, license names, or deployment claims.

The prompt template SHALL also instruct the model to avoid broadening the comparison with unsupported claims about the whole market and to keep unsupported dimensions explicitly marked as unknown.

#### Scenario: Model cannot find license information
- **WHEN** an AI cannot locate a platform's license from primary sources
- **THEN** the response states "unknown" rather than guessing or inferring

#### Scenario: Model infers a score from indirect evidence
- **WHEN** an AI assigns a dimension score based on indirect evidence
- **THEN** the response explicitly flags this as an inference (e.g., "likely X based on [evidence]")

#### Scenario: Research-mode interface encourages broad market framing
- **WHEN** an AI would otherwise add unsupported claims about the wider market beyond the selected platforms
- **THEN** it limits itself to supported observations and uses "unknown" or "unclear" where evidence is incomplete

### Requirement: Comparison prompt usage header includes save-as filename instruction
The prompt template's usage header SHALL include an instruction telling the researcher what filename to use when saving the AI response, referencing the pattern defined in `docs/02-methodology.md`.

The instruction SHALL show a concrete example filename using the `comparison` prompt-type token and the `vs` join convention for two platforms (e.g., `responses/<platform-a>-vs-<platform-b>-comparison.md`).

The usage header SHALL also include a step directing the researcher to paste into their AI session starting from the cut-line (the blockquote `> Paste into your AI session from this line onwards.`), not from the top of the file.

The usage header SHALL state that the prompt can be used in either an AI web research chat or an AI CLI session. For web chat use, it SHALL tell the researcher to manually save the final Markdown response into `responses/`.

#### Scenario: Researcher reads the usage header before pasting the prompt
- **WHEN** a researcher reads the usage instructions at the top of `prompts/platform-comparison.md`
- **THEN** they see the expected filename pattern, a concrete example, an explicit step telling them to paste from the cut-line onwards, and an explicit note that web-chat sessions require manual save/export into `responses/`
