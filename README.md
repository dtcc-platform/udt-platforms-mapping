# udt-platforms-map

A structured research repository for mapping the Urban Digital Twin (UDT) ecosystem around DTCC using an Action Research workflow.

## Why This Repository Exists

This repository is designed to make the research workflow trustworthy.

- Final outputs are cheap to generate; durable value comes from preserving scope decisions, prompt contracts, raw observations, and later reflections.
- Researchers may do the research work themselves or delegate it to an AI agent at any phase, but the workflow stays inspectable either way.
- Research intent is primarily recorded in the `plan/` files and git history.
- Agent-facing prompt behavior is governed through `openspec/` and git, so prompt evolution is documented rather than improvised.
- Changes in the UDT ecosystem are tracked through committed observations, benchmark updates, and iteration history.

The goal is not to optimize for one-off prompt generation. The goal is to preserve mature thinking, explicit intentions, and repeatable research practice over time.

## Repository At A Glance

This repository follows two Action Research cycles:

| Cycle       | Question                                        |
| ----------- | ----------------------------------------------- |
| `discovery` | Which UDT platforms exist across the ecosystem? |
| `rating`    | How do platforms compare on key dimensions?     |

Each cycle uses the same four phases:

```
PLAN → ACT → OBSERVE → REFLECT
```

| Phase       | What happens                                                 |
| ----------- | ------------------------------------------------------------ |
| **Plan**    | Define scope, rubrics, source policy, and current run inputs |
| **Act**     | Run the prompt against a model or agent                      |
| **Observe** | Save the raw response exactly as produced                    |
| **Reflect** | Benchmark, synthesize, and produce higher-level outputs      |

## Fast Paths

Use these when you want to get oriented quickly.

| I want to...                           | Start here                                 |
| -------------------------------------- | ------------------------------------------ |
| run discovery                          | `act/discovery/prompt.md`                  |
| choose platforms for comparison        | `plan/rating/platforms.md`                 |
| run rating                             | `act/rating/prompt.md`                     |
| benchmark discovery recall             | `reflect/discovery/benchmarking/prompt.md` |
| inspect the current discovery criteria | `plan/discovery/scope.md`                  |
| inspect rating rubrics                 | `plan/rating/rubrics.md`                   |
| change any prompt contract             | `openspec/specs/` and `openspec/changes/`  |

## How To Work In This Repo

### 1. Understand the current cycle state

Read the relevant `plan/` files first.

- Discovery runs use `plan/discovery/scope.md`.
- Rating runs use `plan/rating/rubrics.md`, `plan/rating/platforms.md`, and `plan/rating/source-policy.md`.
- `plan/rating/platforms.md` is per-run data for the current comparison set.

### 2. Run act-phase prompts through an AI CLI

Act-phase prompts are executed through an AI CLI such as Claude Code, Codex CLI, or Gemini CLI.

Tell the CLI to run the prompt file directly:

```text
Run act/discovery/prompt.md
Run act/rating/prompt.md
```

The CLI asks:

> Run as CLI or Web?

- `CLI`: the AI reads the declared input files from the repository and writes the result to `observe/<cycle>/cli-<model-short>.md`.
- `Web`: the AI emits a fully resolved prompt with required inputs inlined; paste that into a web chat and save the result to `observe/<cycle>/web-<model-short>.md`.

There are no placeholder tokens, no cut-lines, and no manual paste steps in the current workflow.

### 3. Save raw outputs under `observe/`

Raw responses belong directly in:

- `observe/discovery/`
- `observe/rating/`

File names follow:

```text
cli-<model-short>.md
web-<model-short>.md
```

The `cli-` or `web-` prefix is the authority on which interface produced the file.

### 4. Reflect on results

Discovery benchmarking is currently implemented.

```text
Run reflect/discovery/benchmarking/prompt.md
```

That prompt reads all files in `observe/discovery/`, checks them against `reflect/discovery/benchmarking/benchmark.md`, and writes `reflect/discovery/benchmarking/coverage.md`.

## Traceability Model

Different kinds of knowledge are intentionally stored in different places.

| What is being tracked                       | Primary location                          |
| ------------------------------------------- | ----------------------------------------- |
| research scope, criteria, and run intent    | `plan/`                                   |
| prompt behavior and prompt contract changes | `openspec/specs/` and `openspec/changes/` |
| raw model output                            | `observe/`                                |
| evaluation and synthesis                    | `reflect/`                                |
| iteration history across all of the above   | git                                       |

## Folder Structure

Everything lives under `phase/cycle/`:

```text
plan/
  discovery/      scope.md
  rating/         scope.md, source-policy.md, rubrics.md, platforms.md

act/
  discovery/      prompt.md
  rating/         prompt.md

observe/
  discovery/      cli-<model>.md | web-<model>.md
  rating/         cli-<model>.md | web-<model>.md

reflect/
  discovery/
    benchmarking/ benchmark.md, prompt.md, coverage.md
    reporting/    prompt.md, ecosystem.csv, ecosystem-map.html
  rating/
    benchmarking/ prompt.md
    reporting/    prompt.md
```

## Naming Conventions

Every file and folder follows an explicit convention.

### Folder names

| Level             | Values                                  | Notes                                  |
| ----------------- | --------------------------------------- | -------------------------------------- |
| Phase             | `plan/`, `act/`, `observe/`, `reflect/` | Fixed set for the Action Research loop |
| Cycle             | `discovery/`, `rating/`                 | Fixed set for the two research cycles  |
| Reflect subfolder | `benchmarking/`, `reporting/`           | Under each `reflect/<cycle>/`          |

### File names

| Location                        | Pattern                                            | Example                                      |
| ------------------------------- | -------------------------------------------------- | -------------------------------------------- |
| `plan/<cycle>/` definitions     | `scope.md`, `rubrics.md`, `source-policy.md`       | `plan/rating/rubrics.md`                     |
| `plan/rating/` per-run data     | `platforms.md`                                     | `plan/rating/platforms.md`                   |
| `act/<cycle>/`                  | `prompt.md`                                        | `act/discovery/prompt.md`                    |
| `observe/<cycle>/` responses    | `<interface>-<model-short>.md`                     | `web-claude.md`, `cli-codex.md`              |
| `reflect/<cycle>/benchmarking/` | `benchmark.md`, `prompt.md`, `coverage.md`         | `reflect/discovery/benchmarking/coverage.md` |
| `reflect/<cycle>/reporting/`    | `prompt.md`, `ecosystem.csv`, `ecosystem-map.html` | `reflect/discovery/reporting/ecosystem.csv`  |

### Response metadata

Every response file begins with exactly this YAML block shape:

```yaml
model: <self-reported model name and version>
date: <YYYY-MM-DD>
prompt: platform-discovery # or: platform-comparison
```

## OpenSpec And Prompt Changes

All `prompt.md` files in this repository are generated and maintained through OpenSpec. They are not hand-edited directly when their contract changes.

To evolve a prompt or governed workflow:

```bash
openspec new change "<change-name>"
```

The OpenSpec flow is:

```text
proposal → design → specs → tasks → implementation → archive
```

OpenSpec artifacts follow these locations:

| Artifact                 | Location                                 | Pattern                                       |
| ------------------------ | ---------------------------------------- | --------------------------------------------- |
| baseline capability spec | `openspec/specs/<name>/spec.md`          | `act-discovery-prompt`, `plan-rating-rubrics` |
| active change            | `openspec/changes/<name>/`               | kebab-case verb phrase                        |
| archived change          | `openspec/changes/archive/<dated-name>/` | `YYYY-MM-DD-<name>`                           |

## Git Conventions

Each cycle run is an iteration. Use git to make that iteration legible.

| Convention         | Pattern                       | Example                                   |
| ------------------ | ----------------------------- | ----------------------------------------- |
| phase-cycle commit | `<phase>(<cycle>): <subject>` | `observe(discovery): add gpt-4o response` |
| generic commit     | `<type>(<scope>): <subject>`  | `refactor(specs): flatten coverage table` |
| feature branch     | `<phase>/<cycle>-round-<N>`   | `observe/discovery-round-2`               |
| tag                | `<cycle>-v<N>`                | `discovery-v1`                            |

The combination of `plan/`, `observe/`, `reflect/`, OpenSpec artifacts, and git history is the repository's audit trail.
