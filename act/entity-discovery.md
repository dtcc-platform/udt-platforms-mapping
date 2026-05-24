# Discover Entities Prompt

Use this template to generate a paste-ready web prompt.

## Required Contracts

- `openspec/specs/act-entity-discovery/spec.md` - governs the unified entity discovery research task, scope, evidence behavior, recall targets, and required contract composition
- `openspec/specs/plan-entity-definition/spec.md` - defines allowed entity `Type` values and classification rules
- `openspec/specs/observe-entity-discovery/spec.md` - defines the saved output shape for entity discovery results
- `openspec/specs/observe-markdown-output-format/spec.md` - defines portable Markdown output rules

Produce a fully resolved prompt:

- inline each required contract under a heading naming the source file
- append the prompt body below
- output one copy-ready block only, with no wrapper text, narration, or BEGIN/END markers
- when resolving for review or reuse, save the resolved prompt as `act/entity-discovery-resolved-<resolver-short>.md`

After the resolved prompt block, add one short sentence telling the user to paste it into a web interface and save the response to `observe/entity-discovery-<model-short>.md`.

---

## Prompt

You are a research assistant mapping the Urban Digital Twin entity ecosystem.

Perform entity discovery according to the inlined required contracts.

Return only the final deliverable.
