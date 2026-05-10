## Why

Resolving `act/discover-platforms.md` into a web-ready prompt is now a repeated operational step, and researchers should not need to remember the exact resolver wording each time. A local Codex skill can provide a concise shortcut such as `udt:discover` while keeping OpenSpec specs and act manifests as the source of truth.

## What Changes

- Add a local Codex skill for `udt:discover` / `udt-discover` that resolves the platform discovery manifest for web use.
- Document that the skill is a resolver shortcut, not a replacement for the governed specs or manifest.
- Define copy behavior: after resolving, the skill should use assistant-side `/copy` when available; otherwise it should emit one copy-ready block and tell the researcher to run `/copy`.
- Update README and act documentation to mention the shortcut next to the manual resolve command.

## Capabilities

### New Capabilities

- `repo-agent-skills`: Defines repository-local agent skills as operational shortcuts over governed OpenSpec manifests, including `udt:discover`.

### Modified Capabilities

- `repo-readme`: Documents `udt:discover` as the researcher-facing shortcut for resolving platform discovery prompts.

## Impact

- Adds `.codex/skills/udt-discover/SKILL.md`.
- Updates `README.md` and `act/README.md`.
- Adds `openspec/specs/repo-agent-skills/spec.md` and updates `openspec/specs/repo-readme/spec.md`.
- No change to platform discovery behavior contracts; the skill resolves existing contracts rather than owning research behavior.
