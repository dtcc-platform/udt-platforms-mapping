## Context

Three prompts each embed a Markdown formatting rules block. The canonical form — established in the discovery and comparison prompts — uses two labelled sub-sections (`**Permitted syntax only:**` / `**Prohibited syntax:**`) plus `**Whitespace:**` and `**Score notation:**` entries. The license prompt retains an older flat-bullet format and an older section title, and is missing the score notation entry. The comparison prompt has superfluous blank lines between list items inside the sub-sections.

## Goals / Non-Goals

**Goals:**
- All three prompts use the section title `### Markdown and Formatting Rules`
- All three prompts use the `**Permitted syntax only:** / **Prohibited syntax:**` structure
- All three prompts include a `**Score notation:**` entry appropriate to their output format
- Whitespace within the section is identical across all three prompts

**Non-Goals:**
- Changing any content of the permitted/prohibited lists
- Changing any other section of any prompt
- Defining a shared include or template mechanism — these remain standalone copy-paste files

## Decisions

**Canonical form is the discovery prompt's version, not the comparison prompt's.**
The discovery prompt has no extra blank lines between list items inside the sub-sections. The comparison prompt does. The discovery form is more compact and is the reference — the comparison prompt is normalised to match it.

**Score notation for the license prompt is distinct from discovery/comparison.**
Discovery and comparison use `**Dimension (X/5):**` inline. The license prompt uses a bullet field `**Score:** [1–5]`. The score notation entry for the license prompt therefore reads: "In the Score field: bare number only (1–5). Do not write `/5`."

## Risks / Trade-offs

- Purely cosmetic change to existing prompts — no model behaviour change expected.
- The comparison prompt's extra blank lines were not specified anywhere; removing them carries no risk.
