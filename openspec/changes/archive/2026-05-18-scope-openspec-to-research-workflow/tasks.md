## 1. Structure Spec Rename

- [x] 1.1 Add `openspec/specs/research-workflow-structure/spec.md` with the research phase and canonical artifact requirements from `repo-structure`.
- [x] 1.2 Remove `openspec/specs/repo-structure/spec.md`.
- [x] 1.3 Update active links and references from `repo-structure` to `research-workflow-structure`.

## 2. Agent Skill Scope

- [x] 2.1 Remove `openspec/specs/repo-agent-skills/spec.md`.
- [x] 2.2 Remove `repo-agent-skills` from formal spec lists and README governance language.
- [x] 2.3 Keep `.codex/skills/udt-discover/SKILL.md` as operational tooling outside OpenSpec governance.

## 3. Documentation

- [x] 3.1 Update `README.md` to describe OpenSpec as research-workflow governance only.
- [x] 3.2 Update phase README files to link to `research-workflow-structure`.
- [x] 3.3 Update `openspec/specs/repo-readme/spec.md` to remove OpenSpec governance of agent skills.

## 4. Verification

- [x] 4.1 Search active files for `repo-structure` and `repo-agent-skills` references and migrate or remove them.
- [x] 4.2 Run `openspec validate scope-openspec-to-research-workflow --strict`.
- [x] 4.3 Run `openspec validate --all --strict`.
