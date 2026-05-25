# act/

`act/` contains contract manifests for governed research, benchmarking, and reporting workflows.

Manifest filenames use object/action/role names that align with the governing OpenSpec capability without repeating the `act-` phase prefix, such as `entity-discovery.md`, `platform-comparison.md`, `entity-discovery-benchmark.md`, or `platform-discovery-report.md`.

Each manifest lists the specs and run inputs that affect the action. Web-oriented manifests are resolved into concrete prompts before use; CLI-oriented manifests are run by an AI CLI with filesystem access.

For prompt review, save the generated resolved prompt snapshot under `act/<action>-resolved-<resolver-short>.md` and review that snapshot against the manifest and required contracts. The saved snapshot is review evidence, not a replacement for the manifest.

For entity discovery, the repository-local `udt:discover` skill is a shortcut for resolving `act/entity-discovery.md` for web use. It should read the live manifest and required contracts, produce the copy-ready prompt, then use assistant-side `/copy` when available or tell the researcher to run `/copy`.

Manifest structure is governed by [act-prompt-manifest](../openspec/specs/act-prompt-manifest/spec.md), prompt review is governed by [research-prompt-review](../openspec/specs/research-prompt-review/spec.md), and action behavior is governed by the corresponding OpenSpec research specs. Manifest and prompt behavior changes should go through an OpenSpec change so the contract, rationale, and accepted deltas remain traceable.

The root [README.md](../README.md) explains the full repository workflow. Governing research workflow structure lives in [research-workflow-structure](../openspec/specs/research-workflow-structure/spec.md).
