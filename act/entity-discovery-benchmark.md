# Entity Discovery Benchmark Prompt

Use this manifest in an AI CLI with filesystem access.

## Required Contracts

- `openspec/specs/act-entity-discovery-benchmark/spec.md` - governs the entity discovery benchmark evaluation behavior and benchmark fixture consumption
- `openspec/specs/observe-entity-discovery-benchmark-report/spec.md` - defines the saved benchmark report shape

## Required Run Inputs

- `plan/entity-discovery-benchmark.md` - provides the expected entity fixture
- `observe/entity-discovery-*.md` - provides entity discovery responses to evaluate for entity recall

Run this prompt in an AI CLI session from the repository root.

The CLI model should read required run inputs directly from the repository, follow the required contracts, and write the governed output file.

---

## Prompt

Run the entity discovery benchmark evaluation according to the inlined required contracts and run inputs.
