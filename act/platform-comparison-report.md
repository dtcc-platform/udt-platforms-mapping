# Report Platform Comparison Prompt

Use this manifest in an AI CLI with filesystem access.

## Required Contracts

- `openspec/specs/act-platform-comparison-report/spec.md` - governs platform comparison export behavior and filesystem scope
- `openspec/specs/reflect-platform-comparison-ecosystem/spec.md` - defines the generated CSV and HTML export shape

## Required Run Inputs

- `observe/platform-comparison-*.md` - provides candidate platform comparison responses

Run this prompt in an AI CLI session from the repository root.

The CLI model should read required run inputs directly from the repository, follow the required contracts, and write the governed output files.

---

## Prompt

Run platform comparison reporting according to the inlined required contracts and run inputs.
