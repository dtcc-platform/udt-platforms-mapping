# Proposal: update README for manifest-based prompt workflow

## Summary

Update the README documentation to explain the current repository model:

- specs define expected model behavior
- `act/` files are contract manifests, not copy-ready prompts
- resolving a manifest produces a concrete prompt for a model or agent
- resolving the same manifest with different agents can reveal ambiguity in the specs

## Motivation

The prompt architecture changed from maintained prompt implementations to manifest-based prompt composition. The root README still describes prompts as copy-ready operational implementations, which is now misleading for researchers.

The README should make the new mental model easy to understand from the first screen. A researcher should see that prompt tuning happens mainly by clarifying specs, then resolving manifests into prompts and comparing agent interpretations.

## Scope

In scope:

- rewrite the root README introduction around specs, manifests, resolved prompts, and interpretation checks
- update root workflow instructions so researchers resolve `act/` manifests before running prompts
- replace the old prompt-review diagram with two diagrams:
  - research run flow
  - interpretation and improvement loop
- update the Specs list to include `repo-act-prompt-manifest` and `repo-web-prompt-template`
- update `act/README.md` to describe manifest files rather than canonical prompt templates
- update `repo-readme` so the documentation contract matches the manifest-based workflow

Out of scope:

- changing prompt manifests
- changing behavior specs or output contracts
- changing research artifacts
