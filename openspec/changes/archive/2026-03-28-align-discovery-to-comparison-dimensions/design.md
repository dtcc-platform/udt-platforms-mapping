## Context

Discovery is a breadth pass (15–30 platforms), comparison is a depth pass (2–5 platforms). The current discovery output shape — nine freeform bullet fields — doesn't share vocabulary or scoring with comparison. The fix is to replace the nine fields with six dimension fields (matching comparison exactly) plus the identification fields, each scored 1–5 with a single-line rationale. No rubric tables in discovery — agents apply a quick judgment using the same scale; comparison refines with the full rubric.

## Goals / Non-Goals

**Goals:**
- Discovery per-platform sections produce six scored dimension fields with aligned names
- Summary table carries dimension scores so marked rows are meaningful input to comparison
- Same formatting constraints as comparison (score notation, heading level, Markdown rules, example)

**Non-Goals:**
- Adding scoring rubric tables to the discovery prompt — rubrics live in comparison
- Changing the inclusion criteria or [SEARCH_SCOPE] token
- Changing the metadata block or save-as instruction

## Decisions

**Field set: identification block + six dimension fields**

Each platform section has two parts:
1. Identification: Name (as `##` heading), Organization, Link, License, Type, Inclusion criterion
2. Dimension analysis: one bullet per dimension, inline score + one-sentence rationale

```
## <Platform Name>

- **Organization:** ...
- **Link:** [label](url)
- **License:** ...
- **Type:** ...
- **Inclusion criterion:** ...

- **Technical Architecture (X/5):** one sentence
- **Openness & Licensing (X/5):** one sentence
- **City-Scale Capability (X/5):** one sentence
- **Maturity & Adoption (X/5):** one sentence
- **Integration Posture (X/5):** one sentence
- **Governance (X/5):** one sentence
```

Identification fields kept separate from dimension fields so the two blocks are visually distinct and parseable.

**Summary table: include all six dimension scores**

Current columns: Name, Organization, License, Type, Maturity, Inclusion Criterion, Select.
New columns: Name, Link, License, Type, Arch, Open, City, Mature, Integ, Gov, Inclusion Criterion, Select.

The six score columns use the same short labels as the comparison scoring table so marked rows paste directly without column renaming.

**Score notation matches comparison exactly**
- Inline in sections: `**Dimension (X/5):**`
- In table: bare number, `?` for unknown, no `/5` suffix

**No rubric tables in discovery**

Discovery agents score by judgment — they know the scale (1–5) and can apply it. The comparison prompt is where rubric tables live. Adding them to discovery would make an already-long prompt unwieldy.

## Risks / Trade-offs

- Scores from discovery are quick judgments, not rubric-verified — researchers should expect comparison to refine them. Mitigated by keeping discovery scores as lightweight signals, not authoritative assessments.
- Longer per-platform sections than before — acceptable, the six dimension scores are the point.
