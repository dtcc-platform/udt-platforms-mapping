## Context

After the previous cleanup passes the license prompt usage header still differs from comparison and discovery: it carries an extra blockquote referencing `docs/license-review.md` as a "source of truth". The other two prompts embed their reference material directly and don't add extra blockquotes. The license taxonomy and rubric are already embedded in the prompt body, so the blockquote is redundant.

The score notation issue: the Output Format section says `**Score notation:** in the Score field, bare number only (1–5). Do not write `/5`.` but the output template shows `- **Score:** [1–5]`. This leaves it unclear whether the heading should include the score inline (`**Openness & Licensing (3/5):**`) or just the field label with a bare number. The discovery and comparison prompts show `**Dimension (X/5):**` in profiles and bare number in tables — the license output has neither a table nor a profile heading, so a plain `**Score:** 3` is the right format, but the instruction should say so clearly.

## Goals / Non-Goals

**Goals:**
- Remove the redundant blockquote from the license usage header
- Rewrite the score notation note to be explicit about the output field format
- Add one sentence to methodology.md explaining the scoring handoff

**Non-Goals:**
- Restructuring the license prompt output format beyond the score notation clarification
- Adding cross-references or links between prompts

## Decisions

**Blockquote removal:** Delete the `> **Source of truth for license taxonomy and scoring:** \`docs/license-review.md\`` line entirely. The taxonomy and rubric are self-contained in the prompt body. No information is lost.

**Score notation clarification:** Replace the existing `**Score notation:**` line with wording that explicitly says the Score field in the output uses a bare number (e.g., `**Score:** 3`) and does not use the `(X/5)` inline form — that form is for discovery/comparison profile headings, not for the license output's flat field list.

**Methodology sentence:** Add to the Discovery to Comparison Workflow section: a note that discovery scores are judgment-based first-pass signals and the comparison prompt deepens them with full rubric-based research. Place it after the workflow steps, before the Optional license analysis note.
