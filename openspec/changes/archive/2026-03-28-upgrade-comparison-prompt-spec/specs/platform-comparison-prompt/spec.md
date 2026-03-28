## MODIFIED Requirements

### Requirement: Comparison prompt covers the six research dimensions with scoring
The prompt template SHALL instruct the model to compare platforms across all six dimensions — technical architecture, openness and licensing, city-scale capability, platform maturity, integration posture, and governance model — and assign each platform a score of 1–5 per dimension using a rubric defined in the prompt. The rubric for each dimension SHALL be self-contained in the prompt so the model can apply it without additional context.

#### Scenario: Response covers all dimensions with scores
- **WHEN** an AI responds to the comparison prompt
- **THEN** the response addresses each of the six dimensions for every platform and assigns a numeric 1–5 score with rationale

#### Scenario: Researcher compares scores across agents
- **WHEN** a researcher runs the same comparison on two different AI agents
- **THEN** both responses use the same dimension labels and scoring scale, making scores comparable

### Requirement: Comparison prompt requests a four-part structured output
The prompt template SHALL instruct the model to produce output in exactly four parts, in this order:

1. **Scoring table** — one row per platform, one column per dimension score, plus a link column
2. **Per-platform profiles** — one structured profile per platform with all six dimension analyses, sources, and scores
3. **Landscape observations** — gaps in the landscape, where DTCC sits relative to others, which platforms are directly comparable, which are complementary
4. **Functional categorization** — each platform assigned to one or more categories: `visualization`, `data-management`, `simulation`, `iot-sensing`, `standards`, `infrastructure`

#### Scenario: Researcher extracts summary data
- **WHEN** an AI responds to the comparison prompt
- **THEN** Part 1 contains a Markdown table with one row per platform and numeric scores per dimension

#### Scenario: Researcher reads a platform profile
- **WHEN** a researcher reads Part 2 of the response
- **THEN** each platform has a self-contained profile with organization, link, license, type, dimension analyses with scores, and a sources section

#### Scenario: Researcher understands DTCC's position
- **WHEN** a researcher reads Part 3
- **THEN** the response explicitly positions DTCC relative to comparable and complementary platforms in the landscape

#### Scenario: Researcher filters platforms by function
- **WHEN** a researcher reads Part 4
- **THEN** each platform is assigned to one or more functional categories using the defined tag vocabulary

### Requirement: Comparison prompt includes DTCC as a required reference entry
The prompt template SHALL include a description of DTCC (Digital Twin Cities Centre) as a reference platform and SHALL instruct the model to include DTCC as an entry in the comparison, so that every response positions the landscape relative to DTCC.

#### Scenario: Response is used to position DTCC in the landscape
- **WHEN** an AI responds to the comparison prompt
- **THEN** DTCC appears as a platform entry and the landscape observations section explicitly addresses where DTCC sits relative to comparable and complementary platforms

### Requirement: Comparison prompt requires explicit uncertainty handling
The prompt template SHALL instruct the model to distinguish inferred claims from verified facts, state "unknown" or "unclear" when information is not findable, and never fabricate URLs, license names, or deployment claims.

#### Scenario: Model cannot find license information
- **WHEN** an AI cannot locate a platform's license from primary sources
- **THEN** the response states "unknown" rather than guessing or inferring

#### Scenario: Model infers a score from indirect evidence
- **WHEN** an AI assigns a dimension score based on indirect evidence
- **THEN** the response explicitly flags this as an inference (e.g., "likely X based on [evidence]")

### Requirement: Comparison prompt enforces agent-agnostic output structure
The prompt template SHALL include a concrete example of the per-platform profile structure so any agent can reproduce the exact shape mechanically. The prompt SHALL also include a complete list of prohibited Markdown syntax to prevent agent-specific formatting artifacts.

The prompt SHALL specify:
- **Permitted syntax only:** ATX headings (`#`), `**bold**`, `_italic_`, `[text](url)` links, fenced code blocks, GFM pipe tables, `-` unordered lists, `1.` ordered lists
- **Citation format:** inline links `[Description](https://...)` only — no numeric brackets (`[1]`), no footnotes (`[^1]`), no AI-specific citation formats (e.g., `【†source】`)
- **Prohibited syntax:** custom containers (`:::`, `!!!`, `> [!NOTE]`), extended syntax (`==highlight==`, `^superscript^`, `~subscript~`), raw HTML
- **Whitespace:** blank line before and after every heading, table, and code block
- **Profile heading level:** every platform profile SHALL use `###` as the top-level heading so profiles nest consistently under part headings
- **Score notation:** dimension scores SHALL always be written as `X/5` (e.g., `4/5`) — no other formats (`★★★★☆`, `4 out of 5`, `80%`, bold numbers) are permitted
- **Score placement:** in profiles, scores SHALL appear inline with the dimension label as `**Dimension (X/5):**` — e.g., `**Technical Architecture (4/5):**`
- **Score in table:** in the scoring table, score cells SHALL contain only the numeric value (e.g., `4`) with `?` for unknown — no `/5` suffix in table cells

The prompt SHALL include a concrete example profile for one fictional platform demonstrating the exact heading levels, field labels, score notation, and sources section structure.

#### Scenario: Two agents respond to the same prompt
- **WHEN** a researcher runs the comparison prompt on ChatGPT and on Claude
- **THEN** both responses use identical heading levels, field labels, and score notation — the only difference is the content

#### Scenario: Response is opened in a standard Markdown viewer
- **WHEN** a researcher saves the response as a `.md` file and opens it in GitHub, VS Code, Obsidian, or Typora
- **THEN** all formatting renders correctly with no raw syntax visible, no broken elements, and no AI-specific artifacts

#### Scenario: Model uses AI-specific citation format
- **WHEN** an AI model would normally respond with numeric bracket citations or footnotes
- **THEN** the prompt instruction overrides this and the model uses `[Description](https://...)` inline links instead

### Requirement: Comparison prompt requires a per-platform sources section
The prompt template SHALL instruct the model to include a **Sources** section within each per-platform profile, listing at least one primary source per dimension as an inline Markdown link with an access date.

#### Scenario: Researcher verifies a claim
- **WHEN** a researcher wants to verify a dimension claim for a platform
- **THEN** the platform's Sources section contains a direct link to the primary source used

## REMOVED Requirements

### Requirement: Comparison prompt requests a structured table output
**Reason**: Superseded by the more specific four-part output requirement. The scoring table is now Part 1 of the required four-part structure, with a defined column schema.
**Migration**: The summary table is now Part 1 of the required output — no action needed.
