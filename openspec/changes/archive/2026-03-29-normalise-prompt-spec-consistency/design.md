## Context

Six inconsistencies were identified across the three prompt files, their specs, and methodology. They fall into three categories: stale prompt language, duplicated spec requirements, and missing spec requirements. All are mechanical fixes — no new capabilities are introduced.

## Goals / Non-Goals

**Goals:**
- One "what to do" section name across all three prompts: `### Research Instructions`
- One portable-Markdown requirement per spec (merged into the existing "agent-agnostic output structure" requirement)
- One usage-header requirement in the license spec
- Uncertainty handling and primary sources formally required in all three specs

**Non-Goals:**
- Changing any research behaviour or output format
- Addressing the discovery prompt's usage-header style difference (inline vs. numbered steps) — this is a deliberate usability choice for discovery's examples-heavy scope description
- Changing methodology content

## Decisions

**Canonical section name: `### Research Instructions`**
Already used in the discovery prompt. Comparison's "Rules" is behavioural but functionally equivalent. License's "Review Checklist" is a checklist but serves the same role. "Research Instructions" is the most general and human-readable of the three.

**Remove the standalone "portable Markdown syntax" requirements from discovery and comparison specs rather than merging content**
The "agent-agnostic output structure" requirement in each spec already captures permitted/prohibited syntax, whitespace, and score notation. The "portable Markdown syntax" requirement is a subset that adds only "citation format" — which should be folded into the agent-agnostic requirement instead. Removing the standalone requirement and updating the agent-agnostic one to include citation format explicitly is cleaner than keeping two overlapping requirements.

**Add uncertainty handling and primary sources as ADDED requirements, not MODIFIED**
These behaviours exist in the prompts but are not spec requirements. Adding them as new requirements (not modifying existing ones) is the correct delta operation — no existing requirement changes.

## Risks / Trade-offs

- Renaming `### Rules` in the comparison prompt is visible to researchers reading the file — low risk, purely cosmetic.
- Removing the "portable Markdown syntax" requirements reduces the requirement count in two specs — this is intentional consolidation, not loss of coverage.
