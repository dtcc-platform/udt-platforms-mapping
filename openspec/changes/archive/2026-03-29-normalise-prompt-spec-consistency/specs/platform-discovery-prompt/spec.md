## REMOVED Requirements

### Requirement: Discovery prompt output uses portable Markdown syntax
**Reason**: Duplicate of "Discovery prompt enforces agent-agnostic output structure", which is the superset requirement. Citation format (the only additional item) is folded into the agent-agnostic requirement.
**Migration**: Citation format rule is now part of "Discovery prompt enforces agent-agnostic output structure".

## MODIFIED Requirements

### Requirement: Discovery prompt enforces agent-agnostic output structure
The prompt template SHALL include a concrete example of the per-platform section structure and SHALL specify the following formatting constraints:

- **Permitted syntax:** ATX headings (`#`), `**bold**`, `_italic_`, `[text](url)` links, fenced code blocks, GFM pipe tables, `-` unordered lists, `1.` ordered lists
- **Citation format:** inline links `[Description](https://...)` only — no numeric brackets (`[1]`), no footnotes (`[^1]`), no AI-specific citation formats
- **Prohibited syntax:** custom containers (`:::`, `!!!`, `> [!NOTE]`), extended syntax (`==highlight==`, `^superscript^`, `~subscript~`), raw HTML
- **Whitespace:** blank line before and after every heading, table, and code block
- **Platform heading level:** `##` for every platform section
- **Score notation:** `**Dimension (X/5):**` inline in sections; bare number in table cells; `?` for unknown

#### Scenario: Two agents respond to the same discovery prompt
- **WHEN** a researcher runs the discovery prompt on two different agents
- **THEN** both responses use the same heading level, field labels, and score notation with no agent-specific formatting artifacts

## ADDED Requirements

### Requirement: Discovery prompt requires explicit uncertainty handling
The prompt template SHALL instruct the model to state `?` when a dimension score cannot be assessed from available sources, and to never fabricate platform details, license names, or deployment claims.

#### Scenario: Model cannot assess a dimension
- **WHEN** an AI cannot find sufficient information to score a dimension
- **THEN** the response uses `?` rather than guessing

#### Scenario: Model cannot verify a platform detail
- **WHEN** an AI cannot confirm a license name or deployment from primary sources
- **THEN** the response states the information is unknown rather than fabricating it

### Requirement: Discovery prompt instructs use of primary sources
The prompt template SHALL instruct the model to base its findings on primary sources only — official websites, public repositories, published papers, and official documentation.

#### Scenario: Researcher pastes prompt without supplemental context
- **WHEN** an AI responds to the discovery prompt
- **THEN** all platform details are sourced from primary sources, not secondary summaries or AI-generated assumptions
