## Context

Prompt review exists to catch interpretation and composition issues before running expensive or time-consuming research prompts. The current contract stores both the resolved prompt and reviewer outputs in `observe/`, which makes the workflow heavier than necessary and blurs the difference between an executable action prompt and observed research results.

The desired workflow keeps the durable prompt artifact in `act/`, performs review in stdout/chat, and turns any accepted repository change into an OpenSpec proposal.

## Goals / Non-Goals

**Goals:**

- Make resolved prompts direct `act/` artifacts with conventional names.
- Make prompt review lightweight by default: stdout/chat feedback instead of mandatory review files.
- Ensure the reviewer is a different agent from the resolver.
- Preserve the "why" for fixes by requiring OpenSpec proposals for accepted changes.
- Keep `observe/` focused on research outputs and optional observed evidence.

**Non-Goals:**

- Add prompt-review subfolders.
- Require review outputs to be saved by default.
- Change the entity discovery result filename convention.
- Change the entity discovery prompt contract itself.

## Decisions

- Resolved prompts live in `act/` because they are executable action artifacts generated from an `act/` manifest and required contracts.
- Governed manifests may include resolved-prompt save guidance because the location is governed by `research-prompt-review` and `research-workflow-structure`, not invented by the manifest.
- Review feedback happens in stdout/chat by default because the goal is fast agreement on prompt faithfulness before a research run, not producing another required artifact.
- The reviewing agent must differ from the resolving agent. This reduces the chance that the same interpretation error is repeated without challenge.
- Reviewers should output an OpenSpec proposal intent when repository changes are needed. They should not patch specs, manifests, documentation, or skills directly as part of review.
- Optional saved review evidence may still live in `observe/` when a researcher explicitly wants an audit trail, but it is not required for the normal flow.

## Risks / Trade-offs

- Not saving review output by default reduces historical audit detail. Mitigation: allow optional observed review evidence under `observe/` when needed.
- Saving resolved prompts under `act/` may make the folder contain both manifests and generated prompt artifacts. Mitigation: filename role suffixes such as `-resolved-codex` distinguish generated artifacts from canonical manifests.
- Requiring OpenSpec proposals for fixes may add overhead for small issues. Mitigation: this only applies to accepted repository changes, preserving contract history when behavior or workflow changes.
