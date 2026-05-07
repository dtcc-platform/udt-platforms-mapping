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
