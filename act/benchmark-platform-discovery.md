# Benchmark Platform Discovery Prompt

Use this manifest in an AI CLI with filesystem access.

## Required Contracts

- `openspec/specs/act-benchmark-platform-discovery-prompt/spec.md` - governs the platform discovery coverage evaluation behavior
- `openspec/specs/observe-platform-discovery-coverage/spec.md` - defines the saved coverage report shape

## Required Run Inputs

- `plan/platform-discovery-benchmark.md` - provides the expected artifact fixture
- `observe/entity-discovery-*.md` - provides entity discovery responses to evaluate for platform recall

Run this prompt in an AI CLI session from the repository root.

The CLI model should read required run inputs directly from the repository, follow the required contracts, and write the governed output file.

---

## Prompt

Run the platform discovery coverage evaluation according to the inlined required contracts and run inputs.
