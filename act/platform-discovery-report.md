# Report Platform Discovery Prompt

Use this manifest in an AI CLI with filesystem access.

## Required Contracts

- `openspec/specs/act-platform-discovery-report/spec.md` - governs platform discovery reporting behavior and filesystem scope
- `openspec/specs/reflect-platform-ecosystem/spec.md` - defines the generated ecosystem summary shape

## Required Run Inputs

- `observe/entity-discovery-*.md` - provides candidate entity discovery responses

Run this prompt in an AI CLI session from the repository root.

The CLI model should read required run inputs directly from the repository, follow the required contracts, and write the governed output file.

---

## Prompt

Run platform discovery reporting according to the inlined required contracts and run inputs.
