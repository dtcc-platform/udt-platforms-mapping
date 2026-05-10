## 1. Skill

- [x] 1.1 Add `.codex/skills/udt-discover/SKILL.md` with trigger metadata for `udt:discover`, `udt-discover`, and platform discovery web resolution requests.
- [x] 1.2 Document the skill workflow: read the live manifest, read required contracts, inline contracts, append prompt body, and produce one copy-ready block.
- [x] 1.3 Document conditional `/copy` behavior: use assistant-side `/copy` when available, otherwise tell the researcher to run `/copy`.

## 2. Specs

- [x] 2.1 Add `openspec/specs/repo-agent-skills/spec.md` to govern repository-local operational skills.
- [x] 2.2 Update `openspec/specs/repo-readme/spec.md` to require README documentation for repository-local skill shortcuts and `udt:discover`.

## 3. Documentation

- [x] 3.1 Update `README.md` to document `udt:discover` alongside the manual resolve command and `/copy` workflow.
- [x] 3.2 Update `act/README.md` to explain that common manifest resolution can be invoked through `udt:discover`.
- [x] 3.3 Add `repo-agent-skills` to the README governing spec pointer list.

## 4. Validation

- [x] 4.1 Run `openspec validate add-udt-discover-skill --strict`.
- [x] 4.2 Run `openspec validate --all --strict`.
- [x] 4.3 Review `git status --short` and leave unrelated user changes unstaged.
