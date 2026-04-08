## MODIFIED Requirements

### Requirement: Discovery prompt enforces agent-agnostic output structure

The prompt template SHALL include a concrete example of the per-platform section structure and SHALL comply with the shared Markdown contract defined in `prompt-markdown-format`.

In addition to that shared contract, the prompt SHALL specify these discovery-specific formatting constraints:

- **Platform heading level:** `##` for every platform section
- **Score notation:** `**Dimension (X/5):**` inline in sections; bare number in table cells; `?` for unknown
- **Citation override note:** the Markdown rules section SHALL explicitly state that the inline-link citation rule overrides the model's default citation format

The prompt template SHALL state that no extra headings or sections are permitted beyond the required metadata block, summary table, and `##` platform sections.

#### Scenario: Two agents respond to the same discovery prompt

- **WHEN** a researcher runs the discovery prompt on two different agents
- **THEN** both responses use the same heading level, field labels, and score notation with no agent-specific formatting artifacts

#### Scenario: Model uses AI-specific citation format by default

- **WHEN** an AI model would normally respond with bracket citations or `【†source】` style references
- **THEN** the prompt override instruction suppresses this and the model uses `[Description](https://...)` inline links instead

#### Scenario: Model would normally add extra sections

- **WHEN** an AI model would normally add a heading such as `## Sources` or `## Notes`
- **THEN** the prompt instruction suppresses that and the response contains only the required headings
