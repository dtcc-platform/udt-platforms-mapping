## Why

The prompt review workflow currently stores resolved prompt snapshots and per-agent review outputs under `observe/`, but the intended workflow is simpler: resolved executable prompts should live in `act/`, while prompt review should happen in stdout/chat unless a repository change is needed.

When a reviewer finds a required fix, that fix should become a scoped OpenSpec proposal so the reason for changing specs, manifests, documentation, or skills is preserved.

## What Changes

- Store resolved prompt artifacts directly under `act/` using `act/<action>-resolved-<resolver-short>.md`.
- Treat prompt review as stdout/chat feedback by default, not a persisted `observe/` artifact.
- Require the prompt reviewer to be a different agent from the resolver.
- Require reviewers to propose needed repository changes as OpenSpec proposal intent instead of rewriting prompts directly.
- Clarify that accepted prompt-review fixes are implemented through OpenSpec changes before baseline specs, manifests, documentation, or skills are changed.
- Update research workflow structure documentation so `act/` owns resolved executable prompt artifacts and `observe/` remains for model outputs and optional observed evidence.
- Allow governed act prompt manifests and web prompt templates to include resolved-prompt save guidance when the location is governed by the prompt-review workflow.
- Update the `udt-discover` skill so resolving entity discovery saves the resolved prompt under `act/` and removes stale `/copy` behavior.
- Update README prompt-review guidance and diagrams to match the simplified workflow.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `research-prompt-review`: Clarify prompt review artifact ownership, stdout review behavior, different-agent review, and OpenSpec proposal handling for required fixes.
- `research-workflow-structure`: Clarify that resolved executable prompts are direct `act/` artifacts, while prompt review feedback is stdout by default and only optional observed evidence belongs in `observe/`.
- `act-prompt-manifest`: Allow resolver glue to include governed resolved-prompt save guidance.
- `act-web-prompt-template`: Require web prompt templates to include governed resolved-prompt save guidance when prompt review or saved resolution is expected.

## Impact

- Affects `openspec/specs/research-prompt-review/spec.md`.
- Affects `openspec/specs/research-workflow-structure/spec.md`.
- Affects `openspec/specs/act-prompt-manifest/spec.md`.
- Affects `openspec/specs/act-web-prompt-template/spec.md`.
- Affects `act/entity-discovery.md`.
- Affects `README.md`.
- Affects `.codex/skills/udt-discover/SKILL.md`.
- No changes to discovery output table columns, allowed entity `Type` values, or saved research result filenames.
