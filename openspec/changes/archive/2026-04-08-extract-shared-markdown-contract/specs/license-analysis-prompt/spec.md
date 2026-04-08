## MODIFIED Requirements

### Requirement: License analysis prompt output uses portable Markdown syntax

The prompt template SHALL comply with the shared Markdown contract defined in `prompt-markdown-format`.

In addition to that shared contract, the instruction SHALL appear under the section heading `### Markdown and Formatting Rules` and SHALL specify:

- **Score notation:** in the Score field, bare number only (1–5) — do not write `/5`

#### Scenario: Model uses AI-specific citation format

- **WHEN** an AI model would normally respond with numeric bracket citations like `[1]` or `【†source】`
- **THEN** the prompt instruction overrides this and the model uses `[Description](https://...)` inline links instead

#### Scenario: Response is opened in a standard Markdown viewer

- **WHEN** a researcher saves the response as a `.md` file and opens it in GitHub, VS Code, Obsidian, or Typora
- **THEN** all formatting renders correctly with no raw syntax visible and no broken elements
