## MODIFIED Requirements

### Requirement: Discovery prompt enforces agent-agnostic output structure
The prompt template SHALL include a concrete example of the per-platform section structure and SHALL specify the following formatting constraints:

- **Permitted syntax:** ATX headings (`#`), `**bold**`, `_italic_`, `[text](url)` links, fenced code blocks, GFM pipe tables, `-` unordered lists, `1.` ordered lists
- **Citation format:** inline links `[Description](https://...)` only — no numeric brackets (`[1]`), no footnotes (`[^1]`), no AI-specific citation formats. **This instruction overrides your system's default citation format — do not use your default format.**
- **Prohibited syntax:** custom containers (`:::`, `!!!`, `> [!NOTE]`), extended syntax (`==highlight==`, `^superscript^`, `~subscript~`), raw HTML
- **Whitespace:** blank line before and after every heading, table, and code block
- **Platform heading level:** `##` for every platform section
- **Score notation:** `**Dimension (X/5):**` inline in sections; bare number in table cells; `?` for unknown

#### Scenario: Two agents respond to the same discovery prompt
- **WHEN** a researcher runs the discovery prompt on two different agents
- **THEN** both responses use the same heading level, field labels, and score notation with no agent-specific formatting artifacts

#### Scenario: Model uses AI-specific citation format by default
- **WHEN** an AI model would normally respond with bracket citations or `【†source】` style references
- **THEN** the prompt override instruction suppresses this and the model uses `[Description](https://...)` inline links instead

### Requirement: Discovery prompt response begins with a required summary table
The prompt template SHALL instruct the model to output the summary table immediately after the metadata block and before any per-platform sections. The table is required and SHALL use the following columns: **Name**, **Link**, **License**, **Type**, **Arch**, **Open**, **City**, **Mature**, **Integ**, **Gov**, **Inclusion Criterion**.

Score columns (Arch, Open, City, Mature, Integ, Gov) SHALL contain bare numbers (1–5) or `?` for unknown — no `/5` suffix.

#### Scenario: Researcher opens a discovery response to start a comparison
- **WHEN** a researcher opens a saved discovery response
- **THEN** the summary table appears at the top (after the metadata block), before any per-platform detail sections, so rows can be copied immediately without scrolling

#### Scenario: Rows are pasted into the comparison prompt
- **WHEN** a researcher copies rows from the summary table and pastes them into `[PASTE_SELECTED_PLATFORMS_HERE]`
- **THEN** the comparison prompt receives platform names, license, type, and six seed scores as context

### Requirement: Discovery prompt uses a parameterized search scope token
The prompt template SHALL include a `[SEARCH_SCOPE]` placeholder that the researcher replaces with a specific domain, region, or technology focus before using the prompt. If the literal text `[SEARCH_SCOPE]` has not been replaced, the model SHALL treat the scope as: global city-scale Urban Digital Twin platforms and foundational building blocks (commercial and open-source).

#### Scenario: Researcher customizes search scope
- **WHEN** a researcher replaces `[SEARCH_SCOPE]` with a value such as "European city-scale platforms" or "platforms using CityGML"
- **THEN** the model scopes its discovery results to that domain without other prompt changes needed

#### Scenario: Researcher forgets to replace the scope token
- **WHEN** a researcher pastes the prompt without replacing `[SEARCH_SCOPE]`
- **THEN** the model defaults to a global UDT scope rather than erroring or producing a generic result

## RENAMED Requirements

### Requirement: Discovery prompt response ends with a required summary table
FROM: Discovery prompt response ends with a required summary table
TO: Discovery prompt response begins with a required summary table
