# plan/

`plan/` contains run inputs that governed `act/` manifests use before execution.

These files provide selected comparison sets, benchmark fixtures, and run-specific scope or seed material. Stable behavior definitions, source policies, scoring rules, and output contracts live in `openspec/specs/`.

Examples:

- `platform-comparison-set.md` defines the selected platform input for comparison.
- `platform-discovery-benchmark.md` defines the benchmark fixture input for `act/platform-discovery-benchmark.md`.

The root [README.md](../README.md) explains the full repository workflow. Governing research workflow contracts live in [openspec/specs](../openspec/specs/), including [research-workflow-structure](../openspec/specs/research-workflow-structure/spec.md).
