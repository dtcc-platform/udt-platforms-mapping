### Requirement: Platform discovery prompt file exists

The repository SHALL contain a file at `prompts/platform-discovery.md` that provides a self-contained prompt template for AI-assisted discovery of UDT platforms.

#### Scenario: File is present and non-empty

- **WHEN** a researcher navigates to `prompts/platform-discovery.md`
- **THEN** the file exists and contains a complete, copy-pasteable prompt

### Requirement: Discovery prompt pastes docs/01-discovery-scope.md only

The prompt template SHALL include a `[PASTE_SCOPE_HERE]` placeholder where the researcher pastes the full content of `docs/01-discovery-scope.md` before running a session. The placeholder SHALL be preceded by a guard instruction telling the model: if `[PASTE_SCOPE_HERE]` still appears verbatim, stop and ask the user to paste `docs/01-discovery-scope.md` before continuing.

The usage header SHALL direct the researcher to paste `docs/01-discovery-scope.md` — not `docs/01-scope.md` or `docs/01-comparison-scope.md`.

The discovery prompt SHALL NOT embed or reference dimension rubrics (Arch, Open, City, etc.). Those are defined in `docs/01-comparison-scope.md` and belong to the comparison phase only.

#### Scenario: Researcher runs the prompt without pasting scope

- **WHEN** a researcher pastes the discovery prompt into an AI session without replacing `[PASTE_SCOPE_HERE]`
- **THEN** the model stops and asks them to provide the discovery scope content before producing any output

#### Scenario: Researcher runs the prompt after pasting scope

- **WHEN** a researcher pastes `docs/01-discovery-scope.md` content into the `[PASTE_SCOPE_HERE]` slot
- **THEN** the model proceeds with the Layer criteria table available and produces a complete discovery response

### Requirement: Discovery prompt requests Layer classification output only

The prompt template SHALL instruct the model to return one `##`-level Markdown section per platform containing identification fields and a Layer assignment. No dimension scoring is required or expected.

**For in-scope platforms** (`core-platform`, `backbone`, `domain-module`): identification fields only — Organization, Link, License, Type, Layer.

**For excluded platforms** (`excluded`): identification fields plus a single **Reason** field — one sentence explaining why the platform is outside the study boundary.

The `Layer` field SHALL contain exactly one of: `core-platform`, `backbone`, `domain-module`, or `excluded`, assigned using the criteria table from the pasted scope content.

The prompt template SHALL include a concrete example section demonstrating the exact field labels and Layer field placement for both in-scope and excluded platforms.

The prompt template SHALL state that the response contains exactly three parts, in order: the metadata block, the summary table, and the per-platform sections.

#### Scenario: Response is used to select platforms for comparison

- **WHEN** an AI responds to the discovery prompt
- **THEN** each in-scope platform section contains Organization, Link, License, Type, and Layer — enough to select platforms for a comparison session

#### Scenario: Discovery session finds an excluded platform

- **WHEN** the model encounters a platform that does not meet any in-scope criteria
- **THEN** the platform appears in the summary table with `Layer=excluded` and a one-sentence Reason in its per-platform section; no dimension scores appear

#### Scenario: Discovery session finds a domain-module platform

- **WHEN** an AI responds to the discovery prompt
- **THEN** domain-specific analytics or simulation tools appear with `Layer=domain-module`, not filtered out for not being full platforms

### Requirement: Discovery prompt summary table contains Layer and Reason columns

The summary table SHALL be output immediately after the metadata block and before per-platform sections. The table SHALL use exactly these columns: **Name**, **Link**, **Layer**, **Reason**.

The `Reason` column SHALL be blank for in-scope platforms and contain a brief phrase (not a full sentence) for excluded platforms.

All discovered platforms SHALL appear in the summary table regardless of Layer value. The table SHALL be ordered: `core-platform` first, then `backbone`, then `domain-module`, then `excluded`.

#### Scenario: Researcher scans the summary table to select platforms for comparison

- **WHEN** a researcher opens a discovery response
- **THEN** the summary table shows Name, Link, Layer, and Reason for every discovered platform, allowing quick selection of in-scope platforms for pasting into the comparison prompt

#### Scenario: Researcher copies rows for comparison

- **WHEN** a researcher selects in-scope platforms from the summary table
- **THEN** they can exclude `excluded` rows by filtering on the Layer column

### Requirement: Discovery prompt includes DTCC as a required research entry

The prompt template SHALL instruct the model to include DTCC (Digital Twin Cities Centre) as a required research target in every discovery session. DTCC SHALL be researched from primary sources (dtcc.chalmers.se, official GitHub repository) and SHALL appear with a full identification block and a `Layer` assignment.

#### Scenario: Researcher runs a discovery session

- **WHEN** an AI responds to the discovery prompt
- **THEN** a DTCC per-platform section appears with identification fields and Layer assignment regardless of what other platforms were discovered

#### Scenario: Researcher prepares rows for comparison

- **WHEN** a researcher selects rows from the discovery summary table to paste into the comparison prompt
- **THEN** the DTCC row is available in the summary table and can be selected alongside other platforms

### Requirement: Discovery prompt may be run in deep research mode for reassessment

The prompt template SHALL note that the discovery prompt can be run in a deep research interface when a more thorough Layer classification is needed — for example, to reassess a specific platform's layer assignment with primary-source evidence. Running the discovery prompt in deep research mode is the standard mechanism for layer reassessment; no separate reassessment prompt is needed.

#### Scenario: Researcher reassesses a platform layer

- **WHEN** a researcher wants to verify or update the Layer assignment for a specific platform
- **THEN** they run the discovery prompt in deep research mode, targeting that platform, and update the inventory with the result

### Requirement: Discovery prompt enforces agent-agnostic output structure
The prompt template SHALL include a concrete example of the per-platform section structure and SHALL comply with the shared Markdown contract defined in `prompt-markdown-format`.

In addition to that shared contract, the prompt SHALL specify these discovery-specific formatting constraints:

- **Platform heading level:** `##` for every platform section
- **Score notation:** `**Dimension (X/5):**` inline in sections; bare number in table cells; `?` for unknown
- **Citation override note:** the Markdown rules section SHALL explicitly state that the inline-link citation rule overrides the model's default citation format
- **Citation override note:** the Markdown rules section SHALL explicitly state that the inline-link citation rule overrides the model's default citation format
- **Research-mode suppression:** the prompt SHALL instruct the model to return only the final deliverable with no exposed research plan, executive summary, or provider-specific wrapper

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

### Requirement: Discovery prompt output begins with a model metadata block
The prompt template SHALL instruct the model to begin its response with a fenced YAML code block containing provenance metadata, so that saved response files are self-documenting.

The metadata block SHALL contain exactly three fields:
- `model` — the AI model's name and version as reported by the model itself
- `date` — the session date in `YYYY-MM-DD` format
- `prompt` — the name of the prompt template used (`platform-discovery`)

The metadata block SHALL appear before any other content in the response.

#### Scenario: Response is saved as a file and opened later
- **WHEN** a researcher opens a saved discovery response file
- **THEN** the first visible element is the metadata block identifying the model, date, and prompt template

#### Scenario: Model self-reports its name and version
- **WHEN** the prompt instructs the model to fill in the `model` field
- **THEN** the model populates the field with its own name and version to the best of its ability

### Requirement: Discovery prompt usage header includes save-as filename instruction
The prompt template's usage header SHALL include numbered step-by-step instructions telling the researcher to paste the prompt into their AI session and save the response as `responses/global-platforms-discovery.md`. The reference to `docs/methodology.md` SHALL be updated to `docs/02-methodology.md`. The step to replace `[SEARCH_SCOPE]` SHALL be removed.

The usage header SHALL also state that the prompt can be used either in an AI web research chat or in an AI CLI session. For web chat use, it SHALL tell the researcher to manually save the final Markdown response into `responses/`. For CLI use, it MAY retain the existing direct save instruction.

#### Scenario: Researcher reads the usage header before pasting the prompt
- **WHEN** a researcher reads the usage instructions at the top of `prompts/platform-discovery.md`
- **THEN** they see two numbered steps (paste, save) with no placeholder replacement step, the correct save-as filename `responses/global-platforms-discovery.md`, and an explicit note that web-chat sessions require manual save/export into `responses/`

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

### Requirement: Discovery prompt instructs use of primary sources
The prompt template SHALL instruct the model to base final factual claims on primary sources only — official websites, public repositories, published papers, and official documentation.

The prompt template SHALL instruct the model that factual claims in the per-platform identification and dimension bullets MUST be supported with inline Markdown links to primary sources, and that unsupported claims SHALL be written as unknown or `?` rather than sourced from secondary materials.

The prompt template MAY allow secondary sources to be used only for candidate discovery during research, provided the final inclusion decision and any factual claim in the saved output are supported by primary sources.

#### Scenario: Researcher pastes prompt without supplemental context
- **WHEN** an AI responds to the discovery prompt
- **THEN** all platform details are sourced from primary sources, not secondary summaries or AI-generated assumptions

#### Scenario: Secondary material helps discover a candidate
- **WHEN** an AI encounters a platform first through a secondary article or aggregator
- **THEN** it verifies the platform against a primary source before including it in the final output, and it does not cite the secondary source for final factual claims

#### Scenario: Only a secondary source is available for a claim
- **WHEN** an AI can find a secondary article but no primary source for a platform fact
- **THEN** it leaves that fact unknown or uses `?` instead of citing the secondary article

#### Scenario: Platform detail sections contain factual prose
- **WHEN** an AI writes factual content in the identification and scored dimension bullets
- **THEN** those factual sentences include inline Markdown links to primary sources

