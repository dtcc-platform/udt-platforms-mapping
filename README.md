# udt-platforms-map

A structured research repository for mapping the Urban Digital Twin (UDT) ecosystem, using action research methodology to discover, evaluate, and visualise platforms similar or adjacent to DTCC.

## Methodology

This repository follows an **action research** loop with two independent research cycles. Each cycle runs the same four phases:

```
PLAN → ACT → OBSERVE → REFLECT
```

| Phase       | What happens                                                   |
| ----------- | -------------------------------------------------------------- |
| **Plan**    | Define scope, criteria, and source policy for the cycle        |
| **Act**     | Run the prompt against AI models                               |
| **Observe** | Save raw model responses                                       |
| **Reflect** | Benchmark recall, synthesise findings, visualise the ecosystem |

## Cycles

| Cycle       | Question                                        |
| ----------- | ----------------------------------------------- |
| `discovery` | Which UDT platforms exist across the ecosystem? |
| `rating`    | How do platforms compare on key dimensions?     |

## Folder Structure

Everything lives at `phase/cycle/`:

```
plan/
  discovery/      scope.md
  rating/         scope.md, source-policy.md, rubrics.md, platforms.md

act/
  discovery/      prompt.md
  rating/         prompt.md

observe/
  discovery/      cli-<model>.md | web-<model>.md  (raw discovery responses)
  rating/         cli-<model>.md | web-<model>.md  (raw rating responses)

reflect/
  discovery/
    benchmarking/ benchmark.md, prompt.md, coverage.md
    reporting/    prompt.md, ecosystem.csv, ecosystem-map.html
  rating/
    benchmarking/ prompt.md  (stub — pending design)
    reporting/    prompt.md  (stub — pending design)
```

## Design

### Run modes replace the paste workflow

Act-phase prompts (`act/discovery/prompt.md`, `act/rating/prompt.md`) are executed through an AI CLI (Claude Code, Codex CLI, Gemini CLI). The CLI reads the prompt and asks:

> Run as CLI or Web?

- **CLI** — the AI reads the prompt's declared input files directly from the repository, runs the prompt, and saves the response to `observe/<cycle>/cli-<model>.md`.
- **Web** — the AI assembles a fully resolved prompt (declared inputs inlined at the top under per-file headings, then the prompt body) and emits it as a single copy-ready block. The researcher pastes it into a web chat (Research / Deep Research interfaces are preferred) and saves the response to `observe/<cycle>/web-<model>.md`.

Each act-phase prompt declares its inputs in a `## Required Inputs` section — a flat Markdown list of repository-relative paths. There are no placeholder tokens, no cut-lines, and no manual pasting of scope content.

Reflect-phase prompts are CLI-only (they scan bulk responses and/or write generated artifacts) and do not participate in the mode ask.

### `plan/` holds two kinds of artifact — definitions and per-run data

Not every file in `plan/` changes at the same cadence:

| Kind               | Files                                                                 | Changes                                 |
| ------------------ | --------------------------------------------------------------------- | --------------------------------------- |
| **Definition**     | `scope.md`, `rubrics.md`, `source-policy.md`                          | Slow-moving — reused across cycle runs  |
| **Per-run data**   | `plan/rating/platforms.md`                                            | Changes each rating cycle run           |

`plan/rating/platforms.md` is a three-column (`Name`, `Link`, `Layer`) table holding the platforms selected for the **current** rating cycle. Making it a file (rather than a CLI argument or a paste) means the selection is **git-diffable** — `git log plan/rating/platforms.md` is the authoritative record of which platforms were compared in each cycle run, and reviewers can see "cycle 2 dropped X, added Y" at a glance.

The DTCC row MUST be present in `platforms.md`; the rating prompt's Part 3 landscape observations orient around DTCC.

### Response filename convention

Response files in `observe/*/` carry a `cli-` or `web-` prefix naming the interface that produced them:

```
observe/discovery/
  web-claude.md          ← Claude via web chat
  web-chatgpt.md         ← ChatGPT via web chat
  cli-claude-code.md     ← Claude Code CLI
```

The prefix is the single authority — the YAML metadata block inside each file does **not** carry a separate `interface` field. Benchmarking and reporting tools can slice results by interface from the filename.

## Prompts are generated, not hand-written

All `prompt.md` files in this repository are produced and maintained through an **OpenSpec workflow** — they are not edited directly. To modify a prompt, create a change proposal via OpenSpec:

```bash
openspec new change "<change-name>"
```

The workflow guides you through proposal → design → specs → tasks → implementation → archive.

## Iterative Research with Git

Each cycle run is an iteration. Use standard git practices to track progress:

- **Feature branches** — one branch per cycle run (e.g. `observe/discovery-round-2`)
- **Conventional commits** — scope commits to their phase and cycle:
  - `plan(discovery): refine layer criteria`
  - `act(discovery): update discovery prompt via openspec`
  - `observe(discovery): add gpt-4o response`
  - `reflect(discovery): rerun benchmarking eval`
- **Tags** — mark significant milestones (e.g. `discovery-v1`, `rating-v1`)

## Running the Discovery Eval

```
Run reflect/discovery/benchmarking/prompt.md
```

Tell Claude Code to run that file. It reads all responses from `observe/discovery/`, checks recall against `reflect/discovery/benchmarking/benchmark.md`, and writes the coverage report to `reflect/discovery/benchmarking/coverage.md`.
