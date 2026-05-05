# plan/

`plan/` contains the planning inputs that governed prompts resolve before execution.

These files define scope, source policy, rubrics, selected platforms, and benchmark fixtures. Thread-specific files begin with the research-thread name, such as `udt-platforms`, `udt-initiatives`, or `udt-platform-comparison`.

Examples:

- `udt-platforms-scope.md` defines the `udt-platforms` discovery scope and type classification contract.
- `udt-initiatives-scope.md` defines the `udt-initiatives` discovery scope.
- `udt-platform-comparison-platforms.md` defines the selected platform input for comparison.
- `udt-platforms-benchmark.md` defines the benchmark fixture input for the `udt-platforms` benchmarking prompt.

The root [README.md](../README.md) explains the full repository workflow. Governing structure and documentation contracts live in [repo-structure](../openspec/specs/repo-structure/spec.md) and [repo-readme](../openspec/specs/repo-readme/spec.md).
