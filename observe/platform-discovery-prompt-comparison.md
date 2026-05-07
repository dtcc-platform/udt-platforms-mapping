# Platform Discovery Prompt Comparison

```yaml
date: 2026-05-06
artifact: platform-discovery-prompt-comparison
status: research-cycle-observation
```

This observation compares the existing canonical platform discovery prompt with a generated prompt derived from the new behavior-spec setup.

The canonical prompt remains `act/discover-platforms.md`.
The generated prompt is saved as `act/discover-platforms-spec-derived.md`.
It is not canonical; it is a research-cycle artifact for understanding the difference between a maintained prompt template and a prompt generated directly from behavior and output contracts.

## Compared Prompts

- Existing canonical prompt: `act/discover-platforms.md`
- Generated spec-derived prompt: `act/discover-platforms-spec-derived.md`

## Review Question

Does `act/discover-platforms.md` faithfully implement the `platform-definition` behavior contract and the `observe-platform-discovery` output contract?

## Existing Canonical Prompt

`act/discover-platforms.md` is a maintained web prompt template.
It has a resolver layer that tells the user or agent to inline required contracts before producing the copy-ready prompt.

````markdown
# Discover Platforms Prompt

Use this prompt in a web model interface.

## Required Contracts

- `openspec/specs/platform-definition/spec.md` — `Type` classification behavior for platform discovery
- `openspec/specs/observe-platform-discovery/spec.md` — saved platform discovery output contract

Produce a fully resolved prompt:

- inline the content of each file listed under **Required Contracts** at the top under a heading naming the file
- append the prompt body below
- output one copy-ready block only, with no wrapper text, narration, or BEGIN/END markers

After the resolved prompt block, add one short sentence telling the user to paste it into a web interface and save the response to `observe/platform-discovery-<model-short>.md`.

---

## Prompt

Before you begin:

- Return plain Markdown only.
- Return only the final deliverable in the format below.
- Do not add product-native citation markers, sidebars, source appendices, methodology sections, or closing summaries.

You are a research assistant mapping the technical Urban Digital Twin ecosystem.

Use `openspec/specs/platform-definition/spec.md` as the authoritative Type classification contract.
Apply its Type criteria and interpretation rules before assigning each artifact exactly one `Type`.
Classify by observable presentation and role in the UDT ecosystem, not by name alone.
Use the tie-break guidance when an artifact resembles more than one Type.
Preserve uncertainty when evidence is weak or ambiguous; do not upgrade an artifact to `platform` without observable support.
Produce output conforming to the `observe-platform-discovery` OpenSpec contract.

This is a broad global discovery action:

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
````

## Generated Spec-Derived Prompt

This prompt is saved at `act/discover-platforms-spec-derived.md`.

This prompt was generated from:

- `openspec/specs/platform-definition/spec.md`
- `openspec/specs/observe-platform-discovery/spec.md`
- `openspec/specs/act-discover-platforms-prompt/spec.md`

````markdown
# Discover Platforms Spec-Derived Prompt

This prompt is generated from the current platform discovery behavior and output specs.
It is a research-cycle comparison artifact, not the canonical platform discovery prompt.
The canonical prompt remains `act/discover-platforms.md`.

## Source Specs

- `openspec/specs/platform-definition/spec.md`
- `openspec/specs/observe-platform-discovery/spec.md`
- `openspec/specs/act-discover-platforms-prompt/spec.md`

## Prompt

You are mapping technical Urban Digital Twin artifacts.

Use `openspec/specs/platform-definition/spec.md` as the behavior contract for classification.
Use `openspec/specs/observe-platform-discovery/spec.md` as the output contract.

### Task

Discover technical artifacts in the Urban Digital Twin ecosystem.
Prioritize breadth and candidate recall, but do not imply global completeness.

For every included artifact:

1. Decide whether it is a technical artifact in scope for platform discovery.
2. Assign exactly one `Type`: `platform`, `framework`, `module`, or `excluded`.
3. Classify by observable presentation and role in the UDT ecosystem, not by name alone.
4. Apply the `platform-definition` tie-break order for borderline artifacts.
5. Preserve uncertainty when evidence is weak or ambiguous.

Do not classify an artifact as `platform` only because it has an ambitious name, belongs to a smart-city initiative, or appears near UDT language.

Only `Type = platform` rows are eligible for later platform comparison.

### Output Rules

Return plain Markdown only.
Do not include methodology sections, source appendices, sidebars, closing summaries, numeric citations, footnotes, product-native citation markers, or raw HTML.

Begin with this metadata block:

```yaml
model: <your model name and version>
date: <YYYY-MM-DD>
prompt: platform-discovery
```

Then return this summary table:

| Name | Link | Type | Reason |
| ---- | ---- | ---- | ------ |

Use exactly these columns.
`Reason` is blank for in-scope rows and contains a brief phrase for `excluded` rows.

Then return one `##` section per artifact:

```text
## <Artifact Name>

- **Link:** [<short label>](<primary-url>)
- **Type:** <platform | framework | module | excluded>
- **Reason:** <only if excluded>
```
````

## Comparison

| Aspect                  | `act/discover-platforms.md`                                                                | `act/discover-platforms-spec-derived.md`                                         |
| ----------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| Role                    | Maintained canonical prompt template in `act/`                                             | Research-cycle generated prompt for review                                      |
| Contract boundary       | Includes a resolver step that inlines required contracts                                   | Assumes behavior and output contracts are directly available                    |
| Prompt ergonomics       | Better for repeated web use because it includes paste/save instructions                    | Shorter and more direct, but less explicit about resolution workflow            |
| Classification behavior | Faithfully names Type criteria, tie-breaks, and uncertainty handling                       | Faithfully expresses the same behavior as numbered task steps                   |
| Output contract         | Names `observe-platform-discovery`, but starts the requested output with the summary table | Explicitly includes the metadata block required by `observe-platform-discovery` |
| Reviewer use            | Best source for actual runs                                                                | Useful for checking whether the canonical prompt follows the specs              |
| Main risk               | Can drift from output-contract details if not regenerated after spec changes               | Can be too mechanical and omit local workflow ergonomics                        |

## Findings

The generated prompt makes the spec-to-prompt relationship more direct.
It exposes that `observe-platform-discovery` requires a metadata block with `model`, `date`, and `prompt: platform-discovery`.

The existing canonical prompt is more ergonomic for repeated web use because it includes resolver instructions and save-location guidance.

The main improvement candidate for `act/discover-platforms.md` is to add the metadata block required by `observe-platform-discovery`, while keeping the current resolver and save-location instructions.
