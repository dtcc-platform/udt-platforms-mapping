## Why

Even after moving the executable prompt before metadata, ChatGPT Deep Research still treated the pasted resolved prompt as missing a specific query. The first visible text was a heading and role instruction, not an explicit research topic.

Resolved web prompts need a target-runner-friendly first line that looks like a concrete research topic before any heading, role, metadata, or contract text.

## What Changes

- Require saved resolved web prompts to start with a plain `Research topic:` line.
- Require the topic line to name the concrete research subject and action.
- Require attachment-based web research runs to include a short launcher message telling the runner to read and execute the attached resolved prompt file.
- Update entity discovery so the resolved prompt begins with the Urban Digital Twin entity ecosystem research topic.
- Update the prompt review checklist so reviewers check for a concrete first-line topic when the target runner is a web research tool.
- Update `udt-discover` so it prints the launcher message after saving the resolved prompt.
- Regenerate `act/entity-discovery-resolved-codex.md` with the topic-first format.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `act-web-prompt-template`: Require topic-first saved resolved web prompts.
- `act-entity-discovery`: Require a concrete entity discovery research topic for web runners.
- `research-prompt-review-checklist`: Add first-line topic clarity to target-runner-fit review.

## Impact

- Affects `openspec/specs/act-web-prompt-template/spec.md`.
- Affects `openspec/specs/act-entity-discovery/spec.md`.
- Affects `openspec/specs/research-prompt-review-checklist/spec.md`.
- Affects `act/entity-discovery.md`.
- Affects `.codex/skills/udt-discover/SKILL.md`.
- Regenerates `act/entity-discovery-resolved-codex.md`.
