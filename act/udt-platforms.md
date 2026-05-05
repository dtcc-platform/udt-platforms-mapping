# UDT Platforms Prompt

Use this prompt in a web model interface.

## Required Inputs

- `plan/udt-platforms-scope.md` — `Type` classification criteria for the `udt-platforms` thread

Produce a fully resolved prompt:

- inline the content of each file listed under **Required Inputs** at the top under a heading naming the file
- append the prompt body below
- output one copy-ready block only, with no wrapper text, narration, or BEGIN/END markers

After the resolved prompt block, add one short sentence telling the user to paste it into a web interface and save the response to `observe/udt-platforms-web-<model-short>.md`.

---

## Prompt

Before you begin:

- Return plain Markdown only.
- Return only the final deliverable in the format below.
- Do not add product-native citation markers, sidebars, source appendices, methodology sections, or closing summaries.

You are a research assistant mapping the technical Urban Digital Twin ecosystem.

Classify each artifact using the `Type` criteria from the required inputs.

This is a broad global discovery thread:

- prioritize breadth and candidate recall
- prefer stronger evidence when available
- use `unknown` or `?` when the evidence is not sufficient
- do not imply global completeness

Return one `##`-level section per artifact and assign exactly one `Type` value:

- `platform`
- `framework`
- `module`
- `excluded`

The summary table must use exactly these columns:

- `Name`
- `Link`
- `Type`
- `Reason`

Only `Type = platform` rows are eligible for later platform comparison.

### Markdown and Formatting Rules

Your response must render correctly in standard Markdown viewers such as GitHub, VS Code, Obsidian, and Typora, without AI-specific formatting artifacts.

**Permitted syntax only:**

- ATX headings: `#`, `##`, `###`, `####`
- Emphasis: `**bold**`, `_italic_`
- Links: `[text](url)` inline only
- Lists: `-` unordered, `1.` ordered
- Tables: GFM pipe tables
- Code: fenced code blocks with `` ``` ``

**Prohibited syntax:**

- Custom containers: `:::`, `!!!`, `> [!NOTE]`, `> [!WARNING]`
- Extended syntax: `==highlight==`, `^superscript^`, `~subscript~`
- Raw HTML
- Numeric citations `[1]`, footnotes `[^1]`, AI-specific formats `【†source】`

### Output Format

Begin your response with this summary table:

| Name | Link | Type | Reason |
| ---- | ---- | ---- | ------ |

`Reason` is blank for in-scope rows and contains a brief phrase for `excluded` rows.

Then return one section per artifact using:

```text
## <Artifact Name>

- **Link:** [<short label>](<primary-url>)
- **Type:** <platform | framework | module | excluded>
- **Reason:** <only if excluded>
```
