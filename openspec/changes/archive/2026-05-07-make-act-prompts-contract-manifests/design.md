# Design: act prompt contract manifests

## Manifest Contract

Add `repo-act-prompt-manifest` as a cross-cutting spec for governed `act/*.md` files.

A governed act prompt manifest has:

- a title
- optional researcher-facing usage note
- `## Required Contracts`
- optional `## Required Run Inputs`
- resolver or execution instructions
- a minimal prompt body

The manifest may include short comments beside each contract or input explaining its purpose. Those comments are orientation only and must not introduce independent behavior.

## Behavior Boundary

The manifest must not duplicate behavior governed by specs. Examples of behavior that should move out of the manifest:

- research scope
- evidence rules
- classification rules
- scoring rules
- output tables and sections
- Markdown formatting rules
- report aggregation logic
- benchmark matching logic

Allowed manifest behavior:

- how to resolve the prompt
- what contracts and run inputs to inline
- whether the prompt is intended for a web model or CLI model
- where the resulting response or generated files should be saved when that location is already governed by an output contract

## Prompt Specs

Each existing governed act prompt spec will require its corresponding `act/*.md` file to conform to `repo-act-prompt-manifest`.

The prompt-specific spec remains the place for task behavior. For example:

- `act-discover-platforms-prompt` governs platform discovery scope and contract composition
- `act-compare-platforms-prompt` governs comparison scope and contract composition
- report prompt specs govern filesystem scanning and output locations
- benchmark prompt specs govern benchmark input/output behavior

## Prompt Files

When implemented, live prompt files should become thin manifests. For example:

```md
# Discover Platforms Prompt

Use this template to generate a paste-ready web prompt.

## Required Contracts

- `openspec/specs/act-discover-platforms-prompt/spec.md` — governs the platform discovery research task and required contract composition
- `openspec/specs/platform-definition/spec.md` — defines allowed artifact Type values and classification rules
- `openspec/specs/observe-platform-discovery/spec.md` — defines the saved output shape
- `openspec/specs/repo-prompt-markdown-format/spec.md` — defines portable Markdown output rules

Produce a fully resolved prompt:

- inline each required contract under a heading naming the source file
- append the prompt body below
- output one copy-ready block only

---

## Prompt

Perform platform discovery according to the inlined required contracts.
Return only the final deliverable.
```

## Validation

Validation should ensure all changed OpenSpec artifacts are structurally valid. Manual review remains needed to verify that prompt files no longer duplicate governed behavior.
