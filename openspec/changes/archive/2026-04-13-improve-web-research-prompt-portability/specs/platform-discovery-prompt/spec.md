## MODIFIED Requirements

### Requirement: Discovery prompt usage header includes save-as filename instruction
The prompt template's usage header SHALL include numbered step-by-step instructions telling the researcher to paste the prompt into their AI session and save the response as `responses/global-platforms-discovery.md`. The reference to `docs/methodology.md` SHALL be updated to `docs/02-methodology.md`. The step to replace `[SEARCH_SCOPE]` SHALL be removed.

The usage header SHALL also state that the prompt can be used either in an AI web research chat or in an AI CLI session. For web chat use, it SHALL tell the researcher to manually save the final Markdown response into `responses/`. For CLI use, it MAY retain the existing direct save instruction.

#### Scenario: Researcher reads the usage header before pasting the prompt
- **WHEN** a researcher reads the usage instructions at the top of `prompts/platform-discovery.md`
- **THEN** they see two numbered steps (paste, save) with no placeholder replacement step, the correct save-as filename `responses/global-platforms-discovery.md`, and an explicit note that web-chat sessions require manual save/export into `responses/`

### Requirement: Discovery prompt enforces agent-agnostic output structure
The prompt template SHALL include a concrete example of the per-platform section structure and SHALL comply with the shared Markdown contract defined in `prompt-markdown-format`.

In addition to that shared contract, the prompt SHALL specify these discovery-specific formatting constraints:

- **Platform heading level:** `##` for every platform section
- **Score notation:** `**Dimension (X/5):**` inline in sections; bare number in table cells; `?` for unknown
- **Citation override note:** the Markdown rules section SHALL explicitly state that the inline-link citation rule overrides the model's default citation format
- **Research-mode suppression:** if the interface supports Research or Deep Research, the prompt SHALL instruct the model to do planning internally and return only the final deliverable, with no generated research plan, executive summary, `Sources` section, methodology section, or product-native report wrapper

The prompt template SHALL state that no extra headings or sections are permitted beyond the required metadata block, summary table, and `##` platform sections.

#### Scenario: Two agents respond to the same discovery prompt
- **WHEN** a researcher runs the discovery prompt on two different agents
- **THEN** both responses use the same heading level, field labels, and score notation with no agent-specific formatting artifacts

#### Scenario: Model uses AI-specific citation format by default
- **WHEN** an AI model would normally respond with bracket citations or `【†source】` style references
- **THEN** the prompt override instruction suppresses this and the model uses `[Description](https://...)` inline links instead

#### Scenario: Research-mode interface would normally emit a plan
- **WHEN** a researcher runs the discovery prompt in a Research or Deep Research web interface
- **THEN** the response omits any exposed plan, executive summary, or provider-specific report wrapper and contains only the required metadata block, summary table, and platform sections

### Requirement: Discovery prompt instructs use of primary sources
The prompt template SHALL instruct the model to base final factual claims on primary sources only — official websites, public repositories, published papers, and official documentation.

The prompt template SHALL instruct the model that factual claims in the per-platform identification and dimension bullets MUST be supported with inline Markdown links to primary sources, and that unsupported claims SHALL be written as unknown or `?` rather than sourced from secondary materials.

The prompt template MAY allow secondary sources to be used only for candidate discovery during research, provided the final inclusion decision and any factual claim in the saved output are supported by primary sources.

#### Scenario: Researcher pastes prompt without supplemental context
- **WHEN** an AI responds to the discovery prompt
- **THEN** all platform details in the final output are sourced from primary sources, not secondary summaries or AI-generated assumptions

#### Scenario: Secondary material helps discover a candidate
- **WHEN** an AI encounters a platform first through a secondary article or aggregator
- **THEN** it verifies the platform against a primary source before including it in the final output, and it does not cite the secondary source for final factual claims

#### Scenario: Only a secondary source is available for a claim
- **WHEN** an AI can find a secondary article but no primary source for a platform fact
- **THEN** it leaves that fact unknown or uses `?` instead of citing the secondary article

### Requirement: Discovery prompt requires explicit uncertainty handling
The prompt template SHALL instruct the model to state `?` when a dimension score cannot be assessed from available sources, and to never fabricate platform details, license names, or deployment claims.

The prompt template SHALL also instruct the model to avoid implying global completeness and to prefer omission over weakly supported inclusion when primary-source evidence is insufficient.

#### Scenario: Model cannot assess a dimension
- **WHEN** an AI cannot find sufficient information to score a dimension
- **THEN** the response uses `?` rather than guessing

#### Scenario: Model cannot verify a platform detail
- **WHEN** an AI cannot confirm a license name or deployment from primary sources
- **THEN** the response states the information is unknown rather than fabricating it

#### Scenario: Model finds a borderline platform with incomplete evidence
- **WHEN** an AI finds only partial evidence for a platform that may be in scope
- **THEN** it omits the platform or marks unsupported facts as unknown rather than overstating certainty or implying a complete global inventory
