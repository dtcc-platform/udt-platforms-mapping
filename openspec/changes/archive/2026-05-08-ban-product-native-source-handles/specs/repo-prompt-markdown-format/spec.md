## MODIFIED Requirements

### Requirement: Markdown output uses portable syntax

Markdown output produced by governed prompts SHALL render correctly in standard Markdown viewers such as GitHub, VS Code, Obsidian, and Typora.

The output SHALL use only these Markdown constructs:

- ATX headings: `#`, `##`, `###`, `####`
- emphasis: `**bold**`, `_italic_`
- inline links: `[text](url)`
- unordered lists using `-`
- ordered lists using `1.`
- GFM pipe tables
- fenced code blocks using triple backticks

When a governed output includes a link, the link SHALL use Markdown inline-link syntax with a real URL target, such as `[Official page](https://example.com)`.

#### Scenario: Model emits governed Markdown

- **WHEN** a model produces Markdown from a governed prompt
- **THEN** it uses only the permitted portable Markdown constructs
- **THEN** links use Markdown inline-link syntax with real URL targets

### Requirement: Markdown output excludes non-portable and AI-specific artifacts

Markdown output produced by governed prompts SHALL NOT include non-portable Markdown extensions, raw HTML, product-native source handles, or AI-product-specific citation artifacts.

The output SHALL NOT include:

- custom containers such as `:::`, `!!!`, `> [!NOTE]`, or `> [!WARNING]`
- extended syntax such as `==highlight==`, `^superscript^`, or `~subscript~`
- raw HTML
- numeric citations such as `[1]`
- footnotes such as `[^1]`
- AI-specific source markers such as `【†source】`
- product-native citation handles such as `citeturn11view6`
- product-native URL handles such as `urlOfficial pageturn8search14`
- opaque search or view handles such as `turn8search14`, `turn11view6`, or similar non-URL source identifiers
- source handles that cannot be resolved by a standard Markdown viewer
- extra methodology sections, source appendices, closing summaries, or other sections outside the relevant output contract

#### Scenario: Model output is saved to the repository

- **WHEN** a governed prompt response is saved as Markdown
- **THEN** it has no non-portable syntax, product-native source handles, or AI-product-specific artifacts
