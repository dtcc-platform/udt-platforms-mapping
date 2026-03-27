## Context

The repository defines a five-step research workflow (discover → log → write → inventory → source) and designates `prompts/` as the home for AI-assisted prompt templates. The directory has a `.gitkeep` but no templates. Three research activities need templates: platform discovery, platform comparison, and license analysis.

Existing reference documents (`docs/methodology.md`, `docs/license-review.md`) already define the inclusion criteria, research dimensions, and license scoring guide that the prompts should operationalize.

## Goals / Non-Goals

**Goals:**
- Produce three self-contained Markdown prompt templates in `prompts/`
- Each template should be copy-pasteable into any chat-based AI interface without modification
- Templates should embed the relevant criteria from methodology and license docs so researchers don't need to provide that context separately
- Outputs should be structured to produce data compatible with `docs/platform-inventory.md` columns

**Non-Goals:**
- Automation or API integration — these are manual, copy-paste prompts
- Coverage of the logging template (that lives in `search_logs/`, not `prompts/`)
- Updating `docs/methodology.md` or `docs/license-review.md` — those are stable inputs, not outputs

## Decisions

### Decision: One file per prompt type
Each template gets its own file (`platform-discovery.md`, `platform-comparison.md`, `license-analysis.md`) rather than a single combined file.

**Rationale:** Researchers use each template independently in different sessions. A monolithic file adds friction. Separate files also allow templates to evolve independently.

**Alternative considered:** Single `prompts/README.md` with all three templates inline — rejected because it conflates navigation with usage.

### Decision: Embed criteria inline rather than reference docs by name
Templates include the relevant inclusion criteria, research dimensions, and scoring rubric directly in the prompt text.

**Rationale:** When pasting into an AI session, the model has no access to repo files. Embedding criteria makes prompts self-contained. Researchers should not need to paste additional context.

**Alternative considered:** Instruct researchers to paste `docs/methodology.md` alongside the prompt — rejected as error-prone and adds friction.

### Decision: Use a structured output section in each template
Each template ends with an explicit "Output Format" instruction that specifies the expected structure of the AI response.

**Rationale:** Consistent output makes it easier to extract data for `platform-inventory.md`. Without this, responses vary in structure across sessions.

### Decision: Parameterize with `[PLACEHOLDER]` tokens
Variable inputs (platform name, platforms to compare, license URL) are marked with `[ALL_CAPS_BRACKETS]` tokens.

**Rationale:** Makes it immediately obvious what the researcher needs to fill in before pasting. Consistent with common prompt template conventions.

## Risks / Trade-offs

- **Criteria drift** → If `docs/methodology.md` or `docs/license-review.md` are updated, the embedded criteria in templates will silently become stale. Mitigation: add a note in each template header pointing to the source doc so researchers can spot discrepancies.
- **Template verbosity** → Embedding full criteria makes templates long. Mitigation: this is acceptable — the goal is self-containment over brevity.
- **AI model variance** → Output quality will vary across models. Mitigation: templates are model-agnostic; researchers choose the model. No mitigation needed at the template level.
