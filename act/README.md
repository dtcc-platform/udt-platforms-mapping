# act/

`act/` contains canonical prompt templates for running governed research, benchmarking, and reporting workflows.

Prompt filenames identify the research thread and function. Thread prompts use names such as `udt-platforms.md`, while specialized prompts include a function suffix such as `udt-platforms-benchmarking.md` or `udt-platforms-reporting.md`.

Prompt behavior is governed by OpenSpec prompt specs. Prompt changes should go through an OpenSpec change so the contract, rationale, and accepted deltas remain traceable.

The root [README.md](../README.md) explains the full repository workflow. Governing prompt-review and documentation contracts live in [repo-prompt-review](../openspec/specs/repo-prompt-review/spec.md) and [repo-readme](../openspec/specs/repo-readme/spec.md).
