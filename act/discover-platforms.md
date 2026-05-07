# Discover Platforms Prompt

Use this template to generate a paste-ready web prompt.

## Required Contracts

- `openspec/specs/act-discover-platforms-prompt/spec.md` - governs the platform discovery research task, scope, evidence behavior, and required contract composition
- `openspec/specs/platform-definition/spec.md` - defines allowed artifact `Type` values and classification rules
- `openspec/specs/observe-platform-discovery/spec.md` - defines the saved output shape for platform discovery results
- `openspec/specs/repo-prompt-markdown-format/spec.md` - defines portable Markdown output rules

Produce a fully resolved prompt:

- inline each required contract under a heading naming the source file
- append the prompt body below
- output one copy-ready block only, with no wrapper text, narration, or BEGIN/END markers

After the resolved prompt block, add one short sentence telling the user to paste it into a web interface and save the response to `observe/platform-discovery-<model-short>.md`.

---

## Prompt

You are a research assistant mapping the technical Urban Digital Twin ecosystem.

Perform platform discovery according to the inlined required contracts.

Return only the final deliverable.
