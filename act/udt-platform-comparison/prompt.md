# UDT Platform Comparison Prompt

Run this prompt through an AI CLI (Claude Code, Codex CLI, Gemini CLI). Tell the CLI: **"Run `act/udt-platform-comparison/prompt.md`"**. The CLI will ask you whether to run in CLI or Web mode and handle the rest.

## Required Inputs

- `plan/udt-platform-comparison/rubrics.md` — dimension rubrics used for 1–5 scoring
- `plan/udt-platform-comparison/platforms.md` — the selected platforms to compare (must include DTCC)
- `plan/udt-platform-comparison/source-policy.md` — acceptable source types and citation conventions

## Run Modes

Before executing the prompt body below, ask the user:

> Run as CLI or Web?

Then proceed based on the answer:

- **CLI** — Read each file listed under **Required Inputs** and execute the prompt body. Save the response to `observe/udt-platform-comparison/cli-<model-short>.md`.
- **Web** — Produce a fully resolved prompt with all required-input files inlined at the top, then append the prompt body below. Output the resolved prompt as a single copy-ready block with no wrapper or narration. Append a short note telling the user to paste it into a web chat and save the response to `observe/udt-platform-comparison/web-<model-short>.md`.

If the user has not specified a mode, ask before proceeding — do not guess.

---

## Prompt

Before you begin:

- If your interface supports Research or Deep Research, use it.
- Do your planning internally; do not show a research plan unless explicitly asked.
- Return plain Markdown only.
- Return only the final deliverable in the exact three-part format below.
- Do not add product-native citation markers, sidebars, source appendices, methodology sections, executive summaries, or closing summaries.

You are a research assistant helping to benchmark the Urban Digital Twin platform landscape for DTCC.

Apply the source policy from the required inputs for all final factual claims. Use the rubrics from the required inputs to score every platform on all twelve dimensions. Treat the platforms table from the required inputs as the complete, authoritative comparison scope.

**Platforms to compare:** Use the rows in `plan/udt-platform-comparison/platforms.md`. Compare every platform in that file. Do not add comparison candidates beyond those rows unless the user explicitly asks you to expand scope. This workflow is platform-only; do not broaden the comparison to frameworks or modules. Treat the DTCC row as the reference platform for Part 3 landscape observations. If it is absent, stop and ask the user to add it before producing any output.

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
- Numeric citations `[1]`, footnotes `[^1]`, AI-specific formats `【†source】` — this overrides your default citation format; use `[Description](https://...)` inline links instead

**Whitespace:** leave a blank line before and after every heading, table, and code block.

**Score notation:**

- In profile sections: `**Dimension Name (X/5):**`
- In the scoring table: bare number only; use `?` for unknown

**Profile heading level:** use `###` for every platform profile heading.

### Output Format

Begin your response with this metadata block:

```yaml
model: <your model name and version>
date: <YYYY-MM-DD>
prompt: udt-platform-comparison
```

**Part 1 — Scoring Table**

| Name | Link | Arch | Open | City | Mature | Integ | Gov | Viz | DM | Sim | IoT | Std | Infra |
| ---- | ---- | ---- | ---- | ---- | ------ | ----- | --- | --- | -- | --- | --- | --- | ----- |

Use bare numbers (1–5) in score cells. Use `?` for unknown.

**Part 2 — Platform Profiles**

One `###` profile per platform including:

- `Organization`
- `Link`
- `Description`
- `Type`
- `License`
- six dimension analyses with inline scores
- a per-platform `#### Sources` section

**Part 3 — Landscape Observations**

Use exactly these four subheadings in this order:

#### Landscape Gaps

#### DTCC's Position

#### Comparable Platforms

#### Complementary Platforms
