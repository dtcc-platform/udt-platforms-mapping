# act/

`act/` contains contract manifests for governed research, benchmarking, and reporting workflows.

Manifest filenames use verb phrases that identify the research action, such as `discover-entities.md`, `compare-platforms.md`, `benchmark-platform-discovery.md`, or `report-platform-discovery.md`.

Each manifest lists the specs and run inputs that affect the action. Web-oriented manifests are resolved into concrete prompts before use; CLI-oriented manifests are run by an AI CLI with filesystem access.

For entity discovery, the repository-local `udt:discover` skill is a shortcut for resolving `act/discover-entities.md` for web use. It should read the live manifest and required contracts, produce the copy-ready prompt, then use assistant-side `/copy` when available or tell the researcher to run `/copy`.

Manifest structure is governed by [act-prompt-manifest](../openspec/specs/act-prompt-manifest/spec.md), and action behavior is governed by the corresponding OpenSpec research specs. Manifest and prompt behavior changes should go through an OpenSpec change so the contract, rationale, and accepted deltas remain traceable.

The root [README.md](../README.md) explains the full repository workflow. Prompt interpretation review is governed by [research-workflow-structure](../openspec/specs/research-workflow-structure/spec.md).
