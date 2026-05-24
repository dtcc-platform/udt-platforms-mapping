## 1. Baseline Spec Updates

- [x] 1.1 Update `research-prompt-review` so resolved prompt snapshots are stored under `act/<action>-resolved-<resolver-short>.md`.
- [x] 1.2 Update `research-prompt-review` so prompt review happens in stdout/chat by default.
- [x] 1.3 Require prompt reviewers to be different agents from prompt resolvers.
- [x] 1.4 Require review findings that need repository changes to be proposed as OpenSpec change intent.
- [x] 1.5 Update `research-workflow-structure` so `act/` owns resolved prompt artifacts and `observe/` owns saved research outputs plus optional review evidence.

## 2. Documentation and Skill Updates

- [x] 2.1 Update `README.md` methodology, working-with-agents, prompt-review text, and diagrams to match the simplified workflow.
- [x] 2.2 Update `.codex/skills/udt-discover/SKILL.md` to save resolved prompts under `act/`.
- [x] 2.3 Remove stale `/copy` behavior from the `udt-discover` skill.
- [x] 2.4 Ensure the skill instructs researchers to use a different reviewer agent and to handle required fixes through OpenSpec proposals.
- [x] 2.5 Update act prompt manifest/template contracts and `act/entity-discovery.md` so resolved-prompt save guidance is governed.

## 3. Verification

- [x] 3.1 Run `openspec validate update-prompt-review-workflow --strict`.
- [x] 3.2 Run `openspec validate --all --strict`.
- [x] 3.3 Search for stale prompt review storage wording.
