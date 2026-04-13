## Context

This repository uses prompt templates as governed interfaces. Their outputs are consumed manually and, in the case of discovery and comparison responses, later scanned by other prompts. The current prompts already enforce portable Markdown and inline-link citations, but they assume a fairly neutral "AI session" environment. Research-oriented web products now add product-specific planning, report shells, and citation formats by default, which increases the chance that otherwise correct research output fails the repository's output contract.

The change is cross-cutting because the same class of drift affects three prompt families differently:
- Discovery must preserve an exact three-part output contract.
- Comparison must preserve both the pasted-scope contract and its three-part output structure.
- License analysis must preserve a smaller flat structure and source-priority rules for license claims.

## Goals / Non-Goals

**Goals:**
- Make discovery, comparison, and license-analysis prompts explicitly compatible with Claude Research, ChatGPT Deep Research, and Gemini Deep Research style interfaces.
- Preserve the existing output schemas so saved files remain machine- and human-usable in this repository.
- Reduce formatting and citation drift by adding explicit anti-drift rules.
- Clarify evidentiary behavior: secondary sources may help discover candidates, but final claims must be supported by primary sources.
- Distinguish prompts that are portable to web chat from prompts that remain CLI-only.

**Non-Goals:**
- Do not redesign the core output structure of any prompt.
- Do not make `platform-inventory.md` web-chat compatible; it remains filesystem-dependent.
- Do not introduce provider-specific prompt forks for Claude, ChatGPT, or Gemini.
- Do not change downstream CSV schemas, response filenames, or scoring rubrics beyond wording needed for research-mode compatibility.

## Decisions

### Decision: Keep one shared prompt per workflow instead of provider-specific variants

The prompts should remain repository-native and provider-agnostic. Provider-specific forks would create prompt drift and triple the maintenance burden. Instead, the prompts will add a small research-mode preamble and explicit anti-drift rules that map well to all three major web research products.

Alternatives considered:
- Create one prompt variant per provider. Rejected because the requirements are mostly the same and divergence would become hard to govern.
- Leave prompts unchanged and rely on user wrapper text. Rejected because the repo should carry its own operational contract.

### Decision: Add explicit anti-drift rules rather than relying on existing Markdown constraints

The current Markdown contract forbids some syntax, but that alone does not stop research tools from adding plans, executive summaries, source appendices, or branded report frames. The prompts should explicitly suppress those behaviors at the top of the prompt body.

Alternatives considered:
- Strengthen only the Markdown rules section. Rejected because research products often decide response shape before they encounter lower sections.
- Accept provider-native report structures and normalize later. Rejected because it increases manual cleanup and weakens predictable outputs.

### Decision: Separate "source discovery" from "claim support"

Research modes are good at broad search. The prompts should allow secondary sources as discovery aids while preserving primary-source-only support for final factual claims. This keeps the prompt practical for global discovery without diluting evidence quality.

Alternatives considered:
- Forbid any use of secondary sources at any stage. Rejected because it unnecessarily limits discovery breadth and does not reflect how research agents actually find candidate platforms.
- Permit secondary-source support in final output. Rejected because it conflicts with the repository's source policy.

### Decision: Add web-chat usage guidance only where the task is portable

Discovery, comparison, and license-analysis prompts can still be used in web research chats if the user pastes input and saves output manually. The usage headers should say that explicitly. `platform-inventory.md` should remain unchanged because it depends on local file scanning.

Alternatives considered:
- Mark all prompts as web-chat compatible. Rejected because inventory is not.
- Keep usage guidance CLI-neutral. Rejected because users specifically need to know when manual save/export is expected.

## Risks / Trade-offs

- [Prompts become longer and more directive] -> Keep additions compact and place them near the top where they have the most leverage.
- [Different web products still leak native formatting] -> Add explicit prohibitions for plans, executive summaries, source appendices, and product-native citations in each prompt's governed contract.
- [Spec wording drifts away from the actual prompt body] -> Update all three prompt specs in the same change so implementation has a single authoritative contract.
- [Over-constraining research tools reduces useful breadth] -> Allow secondary sources for candidate discovery while requiring primary-source support for final claims.

## Migration Plan

No repository migration is needed. Existing saved responses remain valid historical artifacts. After implementation, new runs in Claude, ChatGPT, and Gemini research interfaces should be expected to follow the tighter prompt contract, with users still manually saving browser-chat outputs into `responses/` where applicable.

## Open Questions

- None. Decision: name both forms explicitly as `Research` or `Deep Research` for clarity and better cross-provider portability.
