### Requirement: Platform discovery prompt file exists
The repository SHALL contain a file at `prompts/platform-discovery.md` that provides a self-contained prompt template for AI-assisted discovery of UDT platforms.

#### Scenario: File is present and non-empty
- **WHEN** a researcher navigates to `prompts/platform-discovery.md`
- **THEN** the file exists and contains a complete, copy-pasteable prompt

### Requirement: Discovery prompt includes DTCC as a required research entry
The prompt template SHALL instruct the model to include DTCC (Digital Twin Cities Centre) as a required research target in every discovery session, in addition to all other platforms discovered during the session. DTCC SHALL be researched from primary sources (dtcc.chalmers.se, official GitHub repository) the same way as any other platform.

DTCC SHALL appear as a full per-platform section (Relevance 3–5 tier, complete identification block and all 12 dimension fields) and as a row in the summary table. The instruction to include DTCC SHALL be explicit in the prompt — not optional or researcher-dependent.

#### Scenario: Researcher runs a discovery session
- **WHEN** an AI responds to the discovery prompt
- **THEN** a DTCC per-platform section appears in the response with a full identification block and 12-dimension scoring, regardless of what other platforms were discovered

#### Scenario: DTCC's information has changed since a previous session
- **WHEN** a researcher runs a new discovery session
- **THEN** the model researches DTCC from primary sources and reflects current information, rather than relying on a static description embedded in a prompt

#### Scenario: Researcher prepares rows for comparison
- **WHEN** a researcher selects rows from the discovery summary table to paste into the comparison prompt
- **THEN** the DTCC row is available in the summary table and can be selected and pasted alongside other platforms in the same operation

### Requirement: Discovery prompt requests structured output aligned with inventory
The prompt template SHALL instruct the model to return one `##`-level Markdown section per platform containing:

- **For Relevance 3–5 platforms** (in scope): full two-block structure — identification fields (Organization, Link, License, Type, Layer, Relevance) plus all 12 scored dimension fields.
- **For Relevance 1–2 platforms** (out of scope): identification fields only (Organization, Link, License, Type, Layer, Relevance) plus a single **Reason** field (one sentence explaining why the platform is out of scope). No dimension scoring required.

The `Layer` field SHALL contain one of: `core-platform`, `backbone`, or `domain-module`, assigned based on the platform's primary architectural role using the layer taxonomy from the pasted scope content.

The score scale (1–5) SHALL match the comparison prompt's scoring scale. The prompt SHALL instruct agents to score by judgment using the rubrics supplied via `[PASTE_SCOPE_HERE]`.

The `Relevance` field SHALL contain a bare integer 0–5, not a named criterion label.

The prompt template SHALL include a concrete example section demonstrating the exact field labels, score notation, two-block structure, and `Layer` field placement.

The prompt template SHALL state that the response contains exactly three parts, in order: the metadata block, the summary table, and the per-platform sections. It SHALL forbid extra top-level sections or trailing summary content outside that structure.

All discovered platforms SHALL appear in the summary table regardless of Relevance score. The summary table SHALL be ordered by Relevance score descending (5 first, 0 last). The summary table SHALL include a `Layer` column. Relevance 1–2 per-platform sections SHALL appear after all Relevance 3–5 sections.

The prompt template SHALL instruct the model that the research instruction "Verify it meets a Relevance score of 3 or higher" is replaced by "Score all discovered platforms on the Relevance rubric and include all in the summary table."

DTCC SHALL appear as a required entry with a full per-platform section. The prompt SHALL explicitly instruct the model to include DTCC in addition to all discovered platforms.

#### Scenario: Response is used to populate inventory

- **WHEN** an AI responds to the discovery prompt
- **THEN** each platform section — including DTCC — contains the identification fields (including Layer and Relevance) and twelve scored dimension fields, making all data directly transferable to the inventory CSV

#### Scenario: Future session re-discovers a previously rejected platform
- **WHEN** a researcher runs a new discovery session and the model finds a platform that was previously assessed as Relevance 1–2
- **THEN** the prior session's response contains a record of the rejection reason, allowing the researcher to recognise it as previously assessed

#### Scenario: Discovery session identifies many out-of-scope candidates

- **WHEN** the model discovers 10 platforms of which 4 are Relevance 1–2
- **THEN** all 10 appear in the summary table with Layer and Relevance values; the 4 out-of-scope entries have brief sections with a Reason field; the 6 in-scope entries have full 12-dimension sections

#### Scenario: Discovery scores feed into comparison

- **WHEN** a researcher pastes rows from the discovery summary table into the comparison prompt
- **THEN** all twelve dimension and category scores plus the Layer value from discovery provide starting signals that comparison refines with deep research

#### Scenario: Two agents respond to the same discovery prompt
- **WHEN** a researcher runs the discovery prompt on two different AI agents
- **THEN** both responses use identical field labels, score notation (`X/5`), and section structure; both include a DTCC section

#### Scenario: DTCC section appears even when DTCC is not found by search
- **WHEN** an AI's web search does not surface DTCC during discovery
- **THEN** the model still includes a DTCC section by researching it directly from primary sources as instructed

### Requirement: Discovery prompt response begins with a required summary table

The prompt template SHALL instruct the model to output the summary table immediately after the metadata block and before any per-platform sections. The table is required and SHALL use the following columns:

**Name**, **Link**, **License**, **Type**, **Relevance**, **Arch**, **Open**, **City**, **Mature**, **Integ**, **Gov**, **Viz**, **DM**, **Sim**, **IoT**, **Std**, **Infra**

The summary table SHALL include all discovered platforms. Platforms with Relevance 0 (not assessed) SHALL NOT appear — 0 is reserved for CSV rows that have not been evaluated, not for platforms found during a session. Every platform the model discovers and includes in the response SHALL have a Relevance score of at least 1.

The `Relevance` column SHALL contain a bare integer 1–5 for all rows in a discovery response. Score columns (Arch through Infra) SHALL contain bare numbers 1–5 or `?` for in-scope platforms (Relevance 3–5); they MAY contain `0` for out-of-scope platforms (Relevance 1–2) where dimension scoring was not performed.

#### Scenario: Researcher opens a discovery response to start a comparison
- **WHEN** a researcher opens a saved discovery response
- **THEN** the summary table contains all discovered platforms; out-of-scope platforms are visually distinguishable by their low Relevance score and `0` dimension scores

#### Scenario: Researcher copies rows for comparison
- **WHEN** a researcher selects platforms to paste into the comparison prompt
- **THEN** they can easily skip Relevance 1–2 rows by filtering on the Relevance column

#### Scenario: Rows are pasted into the comparison prompt
- **WHEN** a researcher copies rows of included platforms from the summary table and pastes them into the comparison prompt
- **THEN** the comparison prompt receives all twelve seed scores plus the Relevance score as context

### Requirement: Discovery prompt includes a [PASTE_SCOPE_HERE] guard
The prompt template SHALL include a `[PASTE_SCOPE_HERE]` placeholder where the researcher pastes the full content of `docs/01-scope.md` before running a session. The placeholder SHALL be preceded by a guard instruction telling the model: _if `[PASTE_SCOPE_HERE]` still appears verbatim, stop and ask the user to paste `docs/01-scope.md` before continuing._

The usage header SHALL be updated to include a step directing the researcher to paste `docs/01-scope.md` into the `[PASTE_SCOPE_HERE]` slot as the first preparation step.

#### Scenario: Researcher runs the prompt without pasting scope
- **WHEN** a researcher pastes the discovery prompt into an AI session without replacing `[PASTE_SCOPE_HERE]`
- **THEN** the model stops and asks them to provide the scope content before producing any output

#### Scenario: Researcher runs the prompt after pasting scope
- **WHEN** a researcher pastes `docs/01-scope.md` content into the `[PASTE_SCOPE_HERE]` slot
- **THEN** the model proceeds with all 13 rubrics available and produces a complete discovery response

### Requirement: Discovery prompt does not request deep research
The prompt template SHALL NOT instruct the model to use a Research or Deep Research mode. Discovery is a first-pass survey; depth of research is not required. Primary source requirements are relaxed compared to the comparison prompt — the model MAY use judgment and secondary sources to score dimensions, and SHOULD note when claims are approximate.

#### Scenario: Discovery prompt is pasted into a Research-capable interface
- **WHEN** a researcher uses the discovery prompt in an interface that supports Research mode
- **THEN** the prompt does not activate Research mode; a lightweight first-pass response is produced

#### Scenario: Model applies judgment-based scoring
- **WHEN** an AI scores a platform during discovery
- **THEN** it uses the rubrics from the pasted scope content and applies judgment; it does not need to verify every claim against a primary source

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

### Requirement: Discovery prompt instructs multi-layer ecosystem search

The prompt template SHALL explicitly instruct the model to search across all three ecosystem layers — core platforms, infrastructure backbones, and domain-specific analytics/simulation tools — and not to limit discovery to platforms that self-identify as "digital twin" systems. The instruction SHALL reference the three layer values defined in the pasted scope content.

#### Scenario: Discovery session finds a domain-module platform

- **WHEN** an AI responds to the discovery prompt
- **THEN** the response includes domain-specific analytics or simulation tools (e.g., climate risk toolkits, urban traffic simulators) as well as full platforms and backbone components, each assigned the appropriate `Layer` value

#### Scenario: Discovery session finds a backbone component

- **WHEN** an AI responds to the discovery prompt
- **THEN** infrastructure enabling layers (e.g., context brokers, city model databases, rendering engines) appear in the response with `Layer=backbone`, not filtered out because they are not full platforms
