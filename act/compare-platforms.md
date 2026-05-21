# Compare Platforms Prompt

Use this template to generate a paste-ready web prompt.

## Required Contracts

- `openspec/specs/act-platform-comparison/spec.md` - governs the platform comparison task, selected-scope behavior, and required contract composition
- `openspec/specs/plan-platform-comparison-rubric/spec.md` - defines comparison dimensions and scoring behavior
- `openspec/specs/plan-platform-source-policy/spec.md` - defines acceptable evidence and citation behavior
- `openspec/specs/observe-platform-comparison/spec.md` - defines the saved output shape for platform comparison results
- `openspec/specs/repo-prompt-markdown-format/spec.md` - defines portable Markdown output rules

## Required Run Inputs

- `plan/platform-comparison-set.md` - provides the selected platforms for this comparison run

Produce a fully resolved prompt:

- inline each required contract and run input under a heading naming the source file
- append the prompt body below
- output one copy-ready block only, with no wrapper text, narration, or BEGIN/END markers

After the resolved prompt block, add one short sentence telling the user to paste it into a web interface and save the response to `observe/platform-comparison-<model-short>.md`.

---

## Prompt

You are a research assistant benchmarking the Urban Digital Twin platform landscape for DTCC.

Perform platform comparison according to the inlined required contracts and run inputs.

Return only the final deliverable.
