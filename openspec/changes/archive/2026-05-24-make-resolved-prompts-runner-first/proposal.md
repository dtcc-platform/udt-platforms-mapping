## Why

The saved entity discovery resolved prompt starts with metadata and long contract text before the executable research request. ChatGPT Deep Research interpreted that pasted file as missing a query, which shows the resolved artifact is reviewable but not reliably runnable.

Resolved prompts saved under `act/` need to be both reviewable and immediately usable in web research tools.

## What Changes

- Require saved resolved web prompts to start with a clear executable research query.
- Move provenance metadata below the runnable query instead of before it.
- Keep required contracts inlined, but place them after the top-level task and provenance metadata.
- Strengthen the entity discovery prompt body so it explicitly asks for deep research on the Urban Digital Twin entity ecosystem.
- Update `udt-discover` so regenerated resolved prompts use the runner-first layout.
- Regenerate `act/entity-discovery-resolved-codex.md` in runner-first form.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `act-web-prompt-template`: Require runner-first ordering for saved resolved web prompts.
- `research-prompt-review`: Clarify that resolved prompt snapshots must remain executable and place provenance after the runnable query.
- `act-entity-discovery`: Clarify that entity discovery prompts must provide an explicit research query suitable for web research tools.

## Impact

- Affects `openspec/specs/act-web-prompt-template/spec.md`.
- Affects `openspec/specs/research-prompt-review/spec.md`.
- Affects `openspec/specs/act-entity-discovery/spec.md`.
- Affects `act/entity-discovery.md`.
- Affects `.codex/skills/udt-discover/SKILL.md`.
- Regenerates `act/entity-discovery-resolved-codex.md`.
