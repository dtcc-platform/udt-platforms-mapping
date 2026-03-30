## Context

`prompts/platform-comparison.md` (and `platform-discovery.md`) follow a two-section structure: a human-facing usage guide at the top, followed by the AI prompt body. The usage guide includes numbered steps that reference the placeholder token and a `> Save response as:` blockquote.

When a researcher pastes the entire file into a fresh AI session, the model receives those human-facing steps as context. In practice this has caused Claude to interpret the prompt as a document describing a workflow to read or summarise, rather than as instructions to execute — returning an empty or meta-response instead of the comparison report.

The root cause is that there is no structural boundary marking where the AI-facing content begins. Researchers are expected to know to skip the usage block, but this is not enforced or even clearly indicated in the file.

## Goals / Non-Goals

**Goals:**
- Introduce a visible cut-line in each prompt file that clearly separates human operator instructions from the AI-facing prompt body
- Update usage instructions to tell researchers explicitly to paste from the cut-line onwards
- Apply consistently to both `platform-comparison.md` and `platform-discovery.md`

**Non-Goals:**
- Changing the content or logic of the AI prompt bodies
- Moving usage instructions to a separate file or README
- Adding tooling to auto-extract the AI section

## Decisions

**Decision: Cut-line as a blockquote instruction, not a comment or heading**

A Markdown blockquote on its own line — e.g., `> Paste into your AI session from this line onwards.` — is the clearest boundary. It is visible when the file is read as plain text, renders prominently in Markdown viewers, and requires zero tooling.

Alternatives considered:
- HTML comment (`<!-- PASTE FROM HERE -->`): invisible in rendered Markdown, easy to miss
- New `## AI Prompt` heading: works but relies on the researcher knowing to start at that heading; the cut-line approach is more explicit
- Separate file for the AI body: higher friction — researchers would need to open two files

**Decision: Keep the guard instruction inside the AI section, below the cut-line**

The guard (`**Before proceeding:** If the placeholder…`) must remain in the AI-facing section so it is included when the researcher pastes from the cut-line. Moving it above the cut-line would remove it from the pasted content and defeat its purpose.

**Decision: Apply to both prompt files in this change**

`platform-discovery.md` has the same structural pattern (human usage guide + AI body) and the same failure mode. Fixing only the comparison prompt leaves the discovery prompt vulnerable to the same issue.

## Risks / Trade-offs

- [Risk] Researchers paste from the top out of habit → Mitigation: The usage instructions explicitly name the cut-line and tell researchers what to paste; the visual separator is hard to miss
- [Risk] Future prompt files added without the cut-line → Mitigation: The new `prompt-paste-boundary` spec makes the convention normative and checkable
- [Trade-off] The cut-line adds ~2 lines of visual noise to the raw file when read as a document → Acceptable: the benefit of eliminating prompt misinterpretation outweighs minor visual clutter

## Migration Plan

1. Edit `prompts/platform-comparison.md`: update the usage header step 4 to say "Paste into your AI session from the cut-line below" and insert the cut-line immediately before the `## Prompt` heading
2. Edit `prompts/platform-discovery.md`: same change
3. No response files need updating — this is a prompt template edit only
4. Rollback: revert the two file edits; no data or schema migrations involved
