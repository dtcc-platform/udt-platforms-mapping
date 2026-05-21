# Spec: repo-prompt-markdown-format

## Purpose

Defines the shared Markdown formatting contract for governed prompts.

## Requirements

### Requirement: Governed prompts define portable Markdown output

Each governed prompt template file in the live repository that instructs an AI model to emit Markdown output SHALL make `repo-prompt-markdown-format` available to the model either by declaring it as a required contract or by rendering equivalent rules into the resolved prompt.

Canonical web prompt templates that conform to `act-web-prompt-template` SHALL declare `openspec/specs/repo-prompt-markdown-format/spec.md` under `## Required Contracts`.

This shared contract SHALL apply to the governed prompt templates that explicitly rely on it, including current prompts such as `act/discover-entities.md` and `act/compare-platforms.md`.

The `act-web-prompt-template` contract SHALL reuse this shared Markdown formatting contract rather than duplicating it.

#### Scenario: Contributor reviews a governed prompt template

- **WHEN** a contributor opens a governed prompt template that emits Markdown
- **THEN** the prompt declares or renders the shared Markdown formatting rules
- **THEN** any shared web prompt structure requirements reference this contract instead of duplicating the formatting rules

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

### Requirement: Markdown output preserves output-contract structure

Markdown formatting rules SHALL NOT override the relevant observe output contract.

When the observe output contract requires specific metadata blocks, tables, columns, headings, allowed values, or section order, the output SHALL preserve those requirements exactly.

The output SHALL leave a blank line before and after every heading, table, and fenced code block.

#### Scenario: Formatting and output contract both apply

- **WHEN** a governed prompt has both Markdown formatting rules and an observe output contract
- **THEN** the observe output contract determines the required structure
- **THEN** the Markdown formatting rules determine the portable syntax used to render that structure
