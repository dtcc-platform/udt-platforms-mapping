## Context

The shared Markdown-format spec is still useful, but it refers to a generic `prompts/` layout that no longer exists in the live repository. Current governed prompts live under concrete paths such as `act/discovery/prompt.md`, `act/rating/prompt.md`, and selected `reflect/` prompts.

This creates an unnecessary mismatch between the shared contract and the actual prompt set that depends on it.

## Goals / Non-Goals

**Goals:**
- Keep `prompt-markdown-format` as a shared contract
- Update its wording so it names the live governed prompt set accurately
- Preserve the actual portable Markdown behavior already shared across prompts

**Non-Goals:**
- Introduce a new formatting policy
- Rewrite discovery or rating prompt behavior beyond what the shared contract already covers
- Restructure prompt paths

## Decisions

### Decision: Keep the Markdown-format contract separate

The contract remains a standalone baseline spec because the behavior is genuinely shared across multiple prompts and is already treated as a shared dependency by prompt-status and prompt specs.

Alternative considered:
- folding formatting rules into each prompt spec
  - rejected because it would duplicate the same contract and make shared formatting changes noisier

### Decision: Realign wording rather than broaden scope

The spec should refer to governed prompt templates in the live repository rather than to a generic `prompts/` directory. The change is textual and contractual, not architectural.

Alternative considered:
- broadening the spec to all Markdown-emitting files
  - rejected because the contract is about governed prompt templates, not every Markdown artifact in the repo

## Risks / Trade-offs

- [Shared contract remains one more level of indirection] → Keep it because the behavior is still genuinely reused.
- [Spec may still be too generic if future prompts diverge] → Revisit only if the shared Markdown contract stops being shared in practice.

## Migration Plan

1. Update the `prompt-markdown-format` baseline wording.
2. Verify that prompt specs which reference it still make sense with the updated wording.
3. Leave prompt behavior unchanged unless a direct contradiction is found.

## Open Questions

- Whether some `reflect/` prompts should also explicitly cite the shared Markdown contract is deferred.
