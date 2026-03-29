## Context

The discovery prompt already defines a target format, but the latest saved response still drifted in several ways that matter operationally: non-portable AI citation syntax appeared, secondary sources were used in place of primary sources, shortened inclusion labels broke consistency with the prompt, and an extra trailing sources paragraph appeared outside the required structure. The problem is not missing sections; it is that the current wording leaves too much room for model interpretation.

## Goals / Non-Goals

**Goals:**
- Make the discovery response shape deterministic enough to validate visually and reuse without cleanup
- Force canonical inclusion labels in both the table and per-platform sections
- Tie factual prose to primary-source inline links instead of allowing unsupported or secondary-source statements
- Prevent extra narrative sections before or after the required structure

**Non-Goals:**
- Changing discovery table columns or scoring dimensions
- Adding automated linting or validation scripts
- Changing the comparison or license prompts in this change

## Decisions

**Decision: Treat the output format as an exact contract, not a suggested structure.**
The prompt should say that the response contains exactly three parts in order: metadata block, summary table, platform sections. This is clearer than describing the sequence while still permitting extra prose, and it directly addresses the observed trailing-summary drift.

**Decision: Restrict inclusion values to the canonical set.**
The prompt and spec should name the only allowed values for `Inclusion criterion`: `Explicit UDT`, `City-Scale Capabilities`, and `Adjacent Architecture or Governance`. This avoids shortened variants like `Adjacent Architecture` that make downstream comparisons inconsistent.

**Decision: Require primary-source inline links in factual detail sentences.**
The existing “primary sources only” rule is too high-level. Tightening it to require inline primary-source links in factual detail sentences makes the citation rule actionable and makes unsupported prose easier to spot. When no primary source is available, the model should mark the fact as unknown rather than cite a secondary source.

**Decision: Forbid extra sections and catch-all summaries.**
Explicitly banning add-on sections such as `Sources`, `Notes`, or closing summaries keeps the file shape stable and prevents models from appending boilerplate after the platform sections.

## Risks / Trade-offs

- **[Stricter prompt may reduce fluency]** → Acceptable; these files are research artifacts, not narrative reports
- **[Per-sentence evidence rule may make sections denser]** → Mitigate by keeping each scored rationale to one sentence, as already required
- **[Models may still miss a rule occasionally]** → Mitigate by making the rules concrete, exhaustive, and redundant across prompt sections
