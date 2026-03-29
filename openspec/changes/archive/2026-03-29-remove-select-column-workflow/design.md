## Context

The discovery summary table currently includes a `Select` column that the researcher fills with `x` to mark platforms before copying rows into the comparison prompt. This mechanism was introduced to provide a visual planning aid but creates unnecessary friction:

- Researchers must edit a generated response file just to add marks
- Marks must be cleared afterwards (methodology step 6)
- The `x` values travel into the pasted comparison table as noise
- The same goal is achieved by simply copying the desired rows directly

## Goals / Non-Goals

**Goals:**
- Remove the `Select` column from the discovery summary table
- Simplify the comparison workflow to direct row selection (copy what you want)
- Remove `x`-marking language from all prompts, specs, and methodology

**Non-Goals:**
- Changing any other aspect of the discovery or comparison output formats
- Altering the summary table column structure beyond removing `Select`
- Changing how the comparison prompt processes the pasted rows

## Decisions

**Remove `Select` column entirely rather than making it optional.**
Rationale: an optional column would still require documenting the convention and would leave ambiguity. The column has no value to the model — it is only a researcher tracking aid that can be replaced by the natural act of selecting rows to copy.

**No replacement mechanism.**
Rationale: the researcher workflow is "I want to compare these platforms" → copy those rows → paste. A dedicated marking step adds no information. Researchers who want to plan their selection can use any external tool (a notes file, a highlighter in their editor) without it being part of the prompt spec.

## Risks / Trade-offs

- **Stale response files**: Existing discovery response files (`responses/platforms-discovery-claude.md`, `responses/platforms-discovery-chatgpt.md`) already lack the `Select` column — they were generated before it was introduced. Removing the spec requirement aligns the spec with reality for these files. Future re-runs will produce tables without the column.
- **No rollback needed**: This is a pure subtraction. Nothing breaks if a researcher manually adds a Select column to their local copy — the comparison prompt does not validate table structure.
