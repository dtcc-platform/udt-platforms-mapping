# Prompt Consistency Review

Use this prompt to verify that the three UDT research prompt files and their specs are internally consistent and free of gaps.

Paste the completed prompt into a Codex or AI session that has read access to this repository.

> **Save response as:** `responses/prompt-consistency-review.md`. See `docs/methodology.md` for the full convention.

---

## Prompt

You are a technical reviewer auditing the research prompt toolset for the `udt-platforms-map` repository.

Read the following files in full before proceeding:

- `prompts/platform-discovery.md`
- `prompts/platform-comparison.md`
- `prompts/license-analysis.md`
- `openspec/specs/platform-discovery-prompt/spec.md`
- `openspec/specs/platform-comparison-prompt/spec.md`
- `openspec/specs/license-analysis-prompt/spec.md`
- `docs/methodology.md`

---

### Review Checklist

Work through each check below. For each item, report **PASS**, **FAIL**, or **WARN** with a one-sentence explanation. Group results under the section headings.

---

#### 1. Usage Header Consistency

Check all three prompt files (`platform-discovery.md`, `platform-comparison.md`, `license-analysis.md`).

- **1.1** Each usage header uses a numbered-step list (not inline prose).
- **1.2** Each usage header has exactly one `> **Save response as:**` blockquote and no other blockquotes.
- **1.3** The save-as example follows the `responses/<scope>-<prompt-type>.md` pattern from `docs/methodology.md`.

---

#### 2. Section Naming Consistency

- **2.1** All three prompts have a section named exactly `### Research Instructions`.
- **2.2** All three prompts have a section named exactly `### Markdown and Formatting Rules`.
- **2.3** All three prompts have a section named exactly `### Output Format`.

---

#### 3. Research Conduct Instructions

- **3.1** All three prompts instruct the model to use primary sources only.
- **3.2** All three prompts instruct the model to state "unknown" or "unclear" rather than fabricating information.
- **3.3** All three prompts instruct the model to cite sources with inline links `[Description](https://...)`.

---

#### 4. Metadata Block

- **4.1** All three prompts instruct the model to begin its response with a fenced YAML block containing `model`, `date`, and `prompt` fields.
- **4.2** The `prompt` field value matches the prompt name in each file (`platform-discovery`, `platform-comparison`, `license-analysis`).

---

#### 5. Score Notation

- **5.1** Discovery prompt: scores use `**Dimension (X/5):**` in per-platform sections and bare number in the summary table.
- **5.2** Comparison prompt: scores use `**Dimension (X/5):**` in profiles and bare number in the scoring table.
- **5.3** License prompt: the Score output field uses a bare number only (e.g., `**Score:** 3`) — not the `(X/5)` inline form.
- **5.4** No prompt uses `★`, `%`, or "out of 5" notation.

---

#### 6. Concrete Examples

- **6.1** Discovery prompt includes a concrete per-platform section example with the correct field labels and score notation.
- **6.2** Comparison prompt includes a concrete per-platform profile example using `###` as the heading level.
- **6.3** License prompt includes a concrete output example covering all five response sections.

---

#### 7. Spec–Prompt Alignment

For each requirement in the three spec files, verify the corresponding prompt satisfies it. Flag any requirement whose scenario WHEN/THEN condition is not met by the current prompt content.

- **7.1** All requirements in `openspec/specs/platform-discovery-prompt/spec.md` are satisfied by `prompts/platform-discovery.md`.
- **7.2** All requirements in `openspec/specs/platform-comparison-prompt/spec.md` are satisfied by `prompts/platform-comparison.md`.
- **7.3** All requirements in `openspec/specs/license-analysis-prompt/spec.md` are satisfied by `prompts/license-analysis.md`.

---

#### 8. Methodology Alignment

- **8.1** The Discovery to Comparison Workflow in `docs/methodology.md` matches the actual token names and file paths used in the prompts.
- **8.2** `docs/methodology.md` explains that discovery scores are judgment-based first-pass signals that comparison deepens with rubric-based research.
- **8.3** The file naming examples in `docs/methodology.md` are consistent with the save-as instructions in the prompt usage headers.

---

### Markdown and Formatting Rules

Your response will be saved as a Markdown file.

**Permitted syntax only:**
- ATX headings: `#`, `##`, `###`, `####`
- Emphasis: `**bold**`, `_italic_`
- Links: `[text](url)` inline only
- Lists: `-` unordered, `1.` ordered
- Tables: GFM pipe tables
- Code: fenced code blocks with ` ``` `

**Prohibited syntax:**
- Custom containers: `:::`, `!!!`, `> [!NOTE]`, `> [!WARNING]`
- Extended syntax: `==highlight==`, `^superscript^`, `~subscript~`
- Raw HTML
- Numeric citations `[1]`, footnotes `[^1]`, AI-specific formats `【†source】`

**Whitespace:** leave a blank line before and after every heading, table, and code block.

---

### Output Format

Begin your response with this metadata block:

```yaml
model: <your model name and version>
date: <YYYY-MM-DD>
prompt: prompt-consistency-review
```

Then produce a structured report with one section per checklist group (1–8). Use a table for each group:

| Check | Status | Notes |
| ----- | ------ | ----- |
| 1.1   | PASS   | …     |

End with a **Summary** section listing:
- Total checks: N
- PASS: N
- WARN: N
- FAIL: N
- Any FAIL or WARN items that warrant follow-up action
