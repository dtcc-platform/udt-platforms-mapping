### Requirement: Prompt templates define a shared portable Markdown contract

Each prompt template file in `prompts/` that instructs an AI model to emit Markdown output SHALL include a `### Markdown and Formatting Rules` section defining the project's shared portable Markdown contract.

The shared contract SHALL require output that renders correctly in standard Markdown viewers such as GitHub, VS Code, Obsidian, and Typora, without AI-specific formatting artifacts.

The shared contract SHALL use the structured `**Permitted syntax only:**` / `**Prohibited syntax:**` format and SHALL specify:

- **Permitted syntax only:** ATX headings (`#`), `**bold**`, `_italic_`, `[text](url)` links, fenced code blocks, GFM pipe tables, `-` unordered lists, `1.` ordered lists
- **Citation format:** inline links `[Description](https://...)` only — no numeric brackets (`[1]`), no footnotes (`[^1]`), no AI-specific citation formats
- **Prohibited syntax:** custom containers (`:::`, `!!!`, `> [!NOTE]`), extended syntax (`==highlight==`, `^superscript^`, `~subscript~`), raw HTML
- **Whitespace:** blank line before and after every heading, table, and code block

#### Scenario: Researcher opens a saved response in a standard Markdown viewer

- **WHEN** a researcher saves a prompt response as a `.md` file and opens it in GitHub, VS Code, Obsidian, or Typora
- **THEN** the output renders without raw syntax leakage, broken elements, or AI-specific formatting artifacts

#### Scenario: Model would otherwise use non-portable citation syntax

- **WHEN** an AI model would normally emit numeric citations, footnotes, or AI-specific source markers
- **THEN** the prompt's shared Markdown contract overrides that behavior and requires inline Markdown links instead
