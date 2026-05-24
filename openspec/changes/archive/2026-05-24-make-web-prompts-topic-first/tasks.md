## 1. Contract Updates

- [x] 1.1 Update `act-web-prompt-template` so saved web prompts start with a plain `Research topic:` line.
- [x] 1.2 Update `act-entity-discovery` so entity discovery resolved prompts name the concrete UDT entity ecosystem topic.
- [x] 1.3 Update `research-prompt-review-checklist` so reviewers check first-line topic clarity for web research runners.

## 2. Prompt Updates

- [x] 2.1 Update `act/entity-discovery.md` with topic-first resolver instructions and prompt body.
- [x] 2.2 Update `.codex/skills/udt-discover/SKILL.md` to write topic-first resolved prompts.
- [x] 2.3 Regenerate `act/entity-discovery-resolved-codex.md` with `Research topic:` as the first line.
- [x] 2.4 Add attachment-based web runner launcher guidance to specs, README, manifest, and skill.

## 3. Verification

- [x] 3.1 Run `openspec validate make-web-prompts-topic-first --strict`.
- [x] 3.2 Run `openspec validate --all --strict`.
- [x] 3.3 Verify `act/entity-discovery-resolved-codex.md` starts with the concrete research topic.
