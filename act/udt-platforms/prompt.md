# UDT Platforms Prompt

Run this prompt through an AI CLI (Claude Code, Codex CLI, Gemini CLI). Tell the CLI: **"Run `act/udt-platforms/prompt.md`"**. The CLI will ask you whether to run in CLI or Web mode and handle the rest.

## Required Inputs

- `plan/udt-platforms/scope.md` — `Type` classification criteria for the `udt-platforms` cycle
- `plan/udt-platforms/source-policy.md` — evidence ranking, unacceptable sources, and contradiction-handling rules for the `udt-platforms` cycle

## Run Modes

Before executing the prompt body below, ask the user:

> Run as CLI or Web?

Then proceed based on the answer:

- **CLI** — Read each file listed under **Required Inputs** and execute the prompt body, using the file contents as the `Type` criteria and source-policy rules. Save the response to `observe/udt-platforms/cli-<model-short>.md`.
- **Web** — Produce a fully resolved prompt: inline the content of each file listed under **Required Inputs** at the top of the prompt under a heading naming the file (e.g., `## plan/udt-platforms/scope.md`), then append the prompt body below. Output the resolved prompt as a single copy-ready block with no wrapper, narration, or BEGIN/END markers. Append a short note after the resolved block telling the user to paste it into a web chat and save the response to `observe/udt-platforms/web-<model-short>.md`.

If the user has not specified a mode, ask before proceeding — do not guess.

---

## Prompt

Before you begin:

- Do your planning internally; do not show a research plan unless explicitly asked.
- Return plain Markdown only.
- Return only the final deliverable in the exact format below.
- Do not add product-native citation markers, sidebars, source appendices, methodology sections, or closing summaries.

You are a research assistant mapping the **technical Urban Digital Twin ecosystem**.
Your job is to identify technical artifacts from literature and current ecosystem evidence, then classify each artifact using the `Type` criteria from the required inputs while following the source-priority rules from the required inputs.

Track initiatives and projects only as context during research. Do **not** make initiatives primary rows in this output. They belong in the separate `udt-initiatives` cycle.

# UDT Platforms Mapping — Technical Artifacts

Apply the `Type` criteria supplied in the required inputs (`plan/udt-platforms/scope.md`) to every artifact you include. Follow the evidence ranking and contradiction-handling rules supplied in `plan/udt-platforms/source-policy.md`. All four `Type` values (`platform`, `framework`, `module`, `excluded`) are valid outputs from a mapping session.

**Search scope:** Global city-scale UDT platforms and technical building blocks, including commercial and open-source artifacts. Cover all major geographies. Do not limit mapping to systems that market themselves explicitly as "digital twin platforms" — reusable frameworks and modules are in scope when they are materially relevant to UDT work.

### Required Entry: DTCC

**DTCC (Digital Twin Cities Centre)** is a required entry in every `udt-platforms` run. Research it from primary sources — [dtcc.chalmers.se](https://dtcc.chalmers.se) and the [official GitHub repository](https://github.com/dtcc-platform) — and classify it using the same `Type` criteria as any other artifact.

### Research Instructions

For each artifact you identify (including DTCC):

1. Locate the organization behind it
2. Identify its primary link
3. Locate the software license if available
4. Identify the artifact type in plain language
5. Assign one `Type` value using the required-input criteria

Source policy:

- Use `plan/udt-platforms/source-policy.md` as the governing evidence policy for this run.
- You may use secondary sources to discover candidate artifacts.
- For final factual claims, prefer the highest-ranked acceptable sources available.
- If higher-ranked sources cannot support a factual claim, write `unknown` or `?`.
- Prefer omission over weakly supported inclusion; do not imply global completeness.

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

**Artifact heading level:** use `##` for every artifact section.

### Output Format

Your response MUST contain exactly three parts, in this order:

1. The metadata block
2. The summary table
3. The `##` artifact sections

Begin your response with this metadata block:

```yaml
model: <your model name and version>
date: <YYYY-MM-DD>
prompt: udt-platforms
```

Immediately after the metadata block, output the summary table:

| Name | Link | Type | Reason |
| ---- | ---- | ---- | ------ |

All included artifacts appear in the table.
`Reason` is blank for in-scope rows and contains a brief phrase for `excluded` rows.

Then return one section per artifact.

**For in-scope artifacts** (`platform`, `framework`, `module`), use:

```text
## <Artifact Name>

- **Organization:** <name> ([primary source](<url>))
- **Link:** [<short label>](<primary-url>)
- **License:** <exact license name, open-source / proprietary / open-core> ([primary source](<url>))
- **Artifact Type:** <short plain-language description> ([primary source](<url>))
- **Type:** <platform | framework | module>
```

**For excluded artifacts**, use:

```text
## <Artifact Name>

- **Organization:** <name>
- **Link:** [<label>](<url>)
- **License:** <license>
- **Artifact Type:** <type>
- **Type:** excluded
- **Reason:** <one sentence — why this artifact is outside the study boundary>
```
