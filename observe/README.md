# observe/

`observe/` contains saved model outputs and generated coverage artifacts.

Saved web outputs should identify the research action and model in the filename, such as `entity-discovery-claude.md` or `platform-comparison-gemini.md`.

Generated workflow outputs also live here as direct files when they are observations of a run, such as benchmarking coverage.

Resolved prompt snapshots used for prompt review also live here, using `observe/<action>-resolved-prompt-<resolver-short>.md`.

Per-agent prompt review outputs live here using `observe/<action>-prompt-review-<reviewer-short>.md`.

The root [README.md](../README.md) explains the full repository workflow. Governing research workflow structure lives in [research-workflow-structure](../openspec/specs/research-workflow-structure/spec.md), and prompt review behavior lives in [research-prompt-review](../openspec/specs/research-prompt-review/spec.md).
