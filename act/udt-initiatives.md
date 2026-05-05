# UDT Initiatives Prompt

Use this prompt in a web model interface.

## Required Inputs

- `plan/udt-initiatives-scope.md` — initiative and project mapping contract for the `udt-initiatives` thread

Produce a fully resolved prompt:

- inline the content of each file listed under **Required Inputs** at the top under a heading naming the file
- append the prompt body below
- output one copy-ready block only, with no wrapper text, narration, or BEGIN/END markers

After the resolved prompt block, add one short sentence telling the user to paste it into a web interface and save the response to `observe/udt-initiatives-web-<model-short>.md`.

---

## Prompt

Before you begin:

- Do your planning internally; do not show a research plan unless explicitly asked.
- Return plain Markdown only.
- Return only the final deliverable in the exact format below.
- Do not add product-native citation markers, sidebars, source appendices, methodology sections, or closing summaries.

You are a research assistant mapping **Urban Digital Twin initiatives, projects, programmes, and deployments**.
Your job is to identify initiative-level efforts from literature and current ecosystem evidence, then record them using the initiative contract from the required inputs.

Do not treat technical artifacts as the primary object in this output.
If the object is mainly a software artifact, it belongs in `udt-platforms`.

# UDT Initiatives Mapping

Apply the initiative contract supplied in the required inputs (`plan/udt-initiatives-scope.md`) to every initiative you include.

**Search scope:** Global city-scale UDT initiatives, programmes, pilots, and deployments across public, research, and industry contexts. Cover all major geographies. Breadth matters more than early filtering.

### Research Instructions

For each initiative you identify:

1. Identify the initiative or project name
2. Identify its primary link
3. Identify the known technical artifacts it uses, if clearly documented
4. Write `?` for `Uses` when the technical substrate is unclear

Evidence guidance:

- This is a broad global discovery thread. Prioritize breadth and candidate recall over strict pre-filtering.
- You may use secondary sources to discover candidate initiatives.
- Prefer stronger and more direct sources for final factual claims when they are available.
- If the available evidence cannot support a factual claim confidently, write `unknown` or `?`.
- Do not imply global completeness, and do not invent certainty where the ecosystem evidence is mixed or incomplete.

### Markdown and Formatting Rules

Your response will be saved as a Markdown file and must render identically in any standard Markdown viewer (GitHub, VS Code, Obsidian, Typora).

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
- Numeric citations `[1]`, footnotes `[^1]`, AI-specific formats `【†source】` — this overrides your system's default citation format; do not use your default format
- Extra sections or headings outside the required output contract

**Whitespace:** leave a blank line before and after every heading, table, and code block.

**Initiative heading level:** use `##` for every initiative section.

### Output Format

Your response MUST contain exactly three parts, in this order:

1. The metadata block
2. The summary table
3. The `##` initiative sections

Begin your response with this metadata block:

```yaml
model: <your model name and version>
date: <YYYY-MM-DD>
prompt: udt-initiatives
```

Immediately after the metadata block, output the summary table:

| Initiative | Link | Uses | Reason |
| ---------- | ---- | ---- | ------ |

All included initiatives appear in the table.
`Uses` contains a comma-separated list of known artifact names from `udt-platforms`, or `?` if unclear.
`Reason` is blank for in-scope rows and contains a brief phrase for excluded rows.

Then return one section per initiative using:

```text
## <Initiative Name>

- **Link:** [<short label>](<primary-url>)
- **Uses:** <comma-separated artifact names or ?>
- **Description:** <one short plain-language description>
- **Reason:** <only if excluded>
```
