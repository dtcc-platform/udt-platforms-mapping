## Context

All three prompt templates produce output that researchers save as Markdown files in `responses/`. The specs currently define what content to produce but not what Markdown syntax to use. Each AI model defaults to its own conventions — ChatGPT uses `[1]` numeric bracket citations and `【†source】` format, Gemini uses `> [!NOTE]` admonitions, some models use `==highlight==` or `[^1]` footnotes. These patterns either render incorrectly or not at all in standard viewers (GitHub, Obsidian, VS Code, Typora).

## Goals / Non-Goals

**Goals:**
- Define a single portable Markdown syntax rule that applies to all three prompt specs
- Ensure researchers can open any saved response in any standard Markdown viewer without formatting artifacts
- Enforce inline-link citation format so sources are always clickable and readable in plain text

**Non-Goals:**
- Defining a file naming or storage convention for saved responses (out of scope)
- Validating saved files with a linter (not part of this change)
- Restricting what content the model produces — only how it is formatted

## Decisions

### Decision: Add as a new `ADDED` requirement to each spec rather than a shared cross-cutting spec
Each capability spec gets its own portable Markdown requirement, keeping each spec self-contained.

**Rationale:** The three specs are independent. A shared "output formatting" spec would require referencing it from each prompt spec, adding indirection with no real benefit at this scale. Duplicating the single requirement across three specs is simpler and keeps each spec readable standalone.

**Alternative considered:** A shared `output-formatting` spec referenced by all three — rejected; over-engineered for one requirement.

### Decision: Scope to CommonMark + GFM
Permit CommonMark plus GitHub Flavored Markdown (pipe tables, fenced code blocks, task lists) as the allowed syntax set.

**Rationale:** GFM is the de facto standard — supported by GitHub, VS Code, Obsidian, Typora, and most static site generators. It is a strict superset of CommonMark, so files remain valid in pure CommonMark renderers for the constructs used here.

**Alternative considered:** CommonMark only (no GFM tables) — rejected; pipe tables are essential for inventory-aligned output.

### Decision: Place Markdown Syntax Rules immediately before the Output Format section in each prompt
The constraint appears at the point of use — right before the model is told what to produce.

**Rationale:** Models follow instructions more reliably when constraints are adjacent to the task they constrain. A preamble at the top of the prompt is further from the output instruction and more likely to be deprioritised.

## Risks / Trade-offs

- **Requirement drift across three specs** → Each spec has its own copy of the requirement. If the rule needs updating, all three must be changed. Mitigation: the rule is intentionally stable; any future change would be a new openspec change touching all three.
- **Model non-compliance** → Models may still emit non-compliant syntax despite the instruction. Mitigation: out of scope for this change — this establishes the requirement; enforcement tooling is a separate concern.
