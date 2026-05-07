# Discover Initiatives Prompt

Use this template to generate a paste-ready web prompt.

## Required Contracts

- `openspec/specs/act-discover-initiatives-prompt/spec.md` - governs the initiative discovery research task, scope, evidence behavior, and required contract composition
- `openspec/specs/initiative-definition/spec.md` - defines initiative and project inclusion behavior
- `openspec/specs/observe-initiative-discovery/spec.md` - defines the saved output shape for initiative discovery results
- `openspec/specs/repo-prompt-markdown-format/spec.md` - defines portable Markdown output rules

Produce a fully resolved prompt:

- inline each required contract under a heading naming the source file
- append the prompt body below
- output one copy-ready block only, with no wrapper text, narration, or BEGIN/END markers

After the resolved prompt block, add one short sentence telling the user to paste it into a web interface and save the response to `observe/initiative-discovery-<model-short>.md`.

---

## Prompt

You are a research assistant mapping Urban Digital Twin initiatives, projects, programmes, and deployments.

Perform initiative discovery according to the inlined required contracts.

Return only the final deliverable.
