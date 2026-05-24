## 1. Contract Updates

- [x] 1.1 Update `act-web-prompt-template` so saved resolved web prompts start with the executable research query.
- [x] 1.2 Update `research-prompt-review` so resolved prompt metadata appears after the runnable query.
- [x] 1.3 Update `act-entity-discovery` so the canonical prompt requires an explicit runnable research query.

## 2. Manifest, Skill, and Artifact Updates

- [x] 2.1 Update `act/entity-discovery.md` with runner-first resolver instructions and a stronger research query.
- [x] 2.2 Update `.codex/skills/udt-discover/SKILL.md` so it writes runner-first resolved prompts.
- [x] 2.3 Regenerate `act/entity-discovery-resolved-codex.md` in runner-first form.

## 3. Verification

- [x] 3.1 Run `openspec validate make-resolved-prompts-runner-first --strict`.
- [x] 3.2 Run `openspec validate --all --strict`.
- [x] 3.3 Verify the resolved prompt starts with the executable query and no metadata before it.
