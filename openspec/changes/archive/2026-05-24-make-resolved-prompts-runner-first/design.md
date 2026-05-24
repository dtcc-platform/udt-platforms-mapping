## Context

The current saved resolved prompt is structurally faithful to the manifest and contracts, but it is not optimized for a web research tool that expects a clear query at the top. The runnable instruction appears only after hundreds of lines of metadata and contract text.

The resolved prompt artifact should satisfy two uses: it should be reviewable against contracts and also pasteable as the actual research prompt.

## Goals / Non-Goals

**Goals:**

- Put the executable research query first in saved resolved prompts.
- Preserve provenance metadata and required contract context.
- Keep the resolved prompt faithful to `act/entity-discovery.md` and its required contracts.
- Make `act/entity-discovery-resolved-codex.md` usable directly in ChatGPT Deep Research.

**Non-Goals:**

- Remove inlined contracts.
- Change output table shape or entity `Type` values.
- Change where research outputs are saved.
- Add a separate runner-only prompt artifact.

## Decisions

- The first heading of a saved resolved web prompt should be `# Prompt` or an equivalent runnable query heading. This gives web tools an immediate task.
- Provenance metadata should follow the query. Reviewers still have the source manifest, resolver, date, contracts, and run inputs, but that information no longer obscures the task.
- Inlined contracts should follow provenance under source-file headings. This keeps the prompt auditable and executable without requiring extra files.
- The entity discovery task text should use "Deeply research and map..." instead of only "Perform entity discovery..." because web research tools respond better to an explicit research query.

## Risks / Trade-offs

- Putting the query before contracts means the model sees the task before the detailed rules. Mitigation: the query explicitly says to follow the inlined contracts below.
- The resolved prompt still remains long. Mitigation: this change improves the first-screen signal without removing governing context.
