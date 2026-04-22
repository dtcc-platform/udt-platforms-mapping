## 1. Create new folder structure

- [x] 1.1 Create `plan/discovery/`, `plan/rating/`
- [x] 1.2 Create `act/discovery/`, `act/rating/`
- [x] 1.3 Create `observe/discovery/`, `observe/rating/`
- [x] 1.4 Create `reflect/discovery/benchmarking/`, `reflect/discovery/reporting/`
- [x] 1.5 Create `reflect/rating/benchmarking/`, `reflect/rating/reporting/`
- [x] 1.6 Add `.gitkeep` to empty scaffolded dirs (`observe/rating/`, `reflect/rating/benchmarking/`, `reflect/rating/reporting/`)

## 2. Move plan files

- [x] 2.1 Move `docs/01-discovery-scope.md` → `plan/discovery/scope.md`
- [x] 2.2 Move `docs/01-comparison-scope.md` → `plan/rating/scope.md`
- [x] 2.3 Move `docs/03-source-policy.md` → `plan/rating/source-policy.md`
- [x] 2.4 Delete `docs/02-methodology.md`

## 3. Move act files

- [x] 3.1 Move `prompts/platform-discovery.md` → `act/discovery/prompt.md`
- [x] 3.2 Move `prompts/platform-comparison.md` → `act/rating/prompt.md`

## 4. Move observe files

- [x] 4.1 Move `responses/global-platforms-discovery-claude.md` → `observe/discovery/claude.md`
- [x] 4.2 Move `responses/global-platforms-discovery-chatgpt.md` → `observe/discovery/chatgpt.md`
- [x] 4.3 Move `responses/global-platforms-discovery-gemini.md` → `observe/discovery/gemini.md`
- [x] 4.4 Move `responses/global-platforms-comparison-*.md` → `observe/rating/<model>.md` for each file

## 5. Move reflect files

- [x] 5.1 Move `evals/discovery/benchmark.md` → `reflect/discovery/benchmarking/benchmark.md`
- [x] 5.2 Move `evals/discovery/run.md` → `reflect/discovery/benchmarking/prompt.md`
- [x] 5.3 Move `evals/discovery/reports/coverage.md` → `reflect/discovery/benchmarking/coverage.md`
- [x] 5.4 Move `prompts/platform-inventory.md` → `reflect/discovery/reporting/prompt.md`
- [x] 5.5 Move `docs/05-platform-inventory.csv` → `reflect/discovery/reporting/ecosystem.csv`
- [x] 5.6 Move `docs/05-platform-inventory.html` → `reflect/discovery/reporting/ecosystem-map.html`

## 6. Create scaffolded rating prompt stubs

These `prompt.md` files do not exist yet — create them as stubs so the rating cycle folder structure is complete and self-explanatory.

- [x] 6.1 Create `reflect/rating/benchmarking/prompt.md` — stub with heading and placeholder instruction referencing `observe/rating/*.md` and `reflect/rating/benchmarking/benchmark.md`
- [x] 6.2 Create `reflect/rating/reporting/prompt.md` — stub with heading and placeholder instruction referencing `observe/rating/` and output paths `ecosystem.csv`, `ecosystem-map.html`

## 7. Update internal path references

- [x] 7.1 Update `act/discovery/prompt.md` — fix scope path (`plan/discovery/scope.md`), save-as path (`observe/discovery/<model>.md`), remove methodology reference
- [x] 7.2 Update `act/rating/prompt.md` — fix scope path (`plan/rating/scope.md`), save-as path (`observe/rating/<model>.md`), remove methodology reference
- [x] 7.3 Update `reflect/discovery/benchmarking/prompt.md` — fix glob path (`observe/discovery/*.md`), fixture path (`reflect/discovery/benchmarking/benchmark.md`), report output path (`reflect/discovery/benchmarking/coverage.md`)
- [x] 7.4 Update `reflect/discovery/reporting/prompt.md` — fix scan path (`observe/discovery/`), output paths (`ecosystem.csv`, `ecosystem-map.html`)
- [x] 7.5 Update `plan/discovery/scope.md` header — remove any references to old `docs/` path
- [x] 7.6 Update `plan/rating/scope.md` header — remove any references to old `docs/` path

## 8. Update README and AGENTS.md

- [x] 8.1 Rewrite `README.md` — explain two-cycle AR methodology, four phases, folder map (`phase/cycle/`); state that all `prompt.md` files are generated via OpenSpec workflow (not hand-edited); explain git practices for iteration (feature branches per run, conventional commits e.g. `observe(discovery):`, tags for milestones)
- [x] 8.2 Update `AGENTS.md` — fix all path references to match new structure

## 9. Remove old folders

- [x] 9.1 Delete `docs/` folder (all files moved or deleted)
- [x] 9.2 Delete `prompts/` folder (all files moved)
- [x] 9.3 Delete `responses/` folder (all files moved)
- [x] 9.4 Delete `evals/` folder (all files moved)
