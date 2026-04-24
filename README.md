# udt-platforms-map

A structured research repository for mapping the Urban Digital Twin (UDT) ecosystem around DTCC using an Action Research workflow.

## Why Not One Prompt?

The core design choice in this repository is to split what could be one large prompt into separate artifacts.

The most important split is between `discovery` and `rating`:

- `discovery` asks what exists and how it should be classified
- `rating` asks how a selected set should be evaluated against explicit criteria

This is not only a workflow choice. It is a semantic and epistemological one. Keeping those phases separate preserves the meaning of each result and avoids collapsing search, classification, selection, and evaluation into one prompt.

Splitting the prompt also improves the workflow:

- better stability, because scope, criteria, source policy, prompt contract, and run inputs can change independently
- better consistency, because the model gets clearer boundaries between policy, inputs, instructions, and output format
- better traceability, because later edits are easier to interpret
- better human judgment, because researchers review explicit boundaries instead of burying them inside prompt text
- better collaboration, because contributors can refine different parts of the process without rewriting one shared prompt

The repository is intended to function as a shared knowledge space for a joint research endeavour. Different contributors can propose new platforms, criteria changes, fixtures, and benchmark refinements through issues and pull requests. It stores not only outputs, but also the metadata of the research process: intent, scope, criteria, prompt contracts, observations, and reflections.

The tradeoff is higher process overhead. Splitting prompts does not automatically improve raw model quality, especially in Web mode where the inputs are flattened into one resolved prompt anyway. The main gain is workflow quality and research trust.

## At A Glance

The repository follows two Action Research cycles:

| Cycle       | Question                                        |
| ----------- | ----------------------------------------------- |
| `discovery` | Which UDT platforms exist across the ecosystem? |
| `rating`    | How do platforms compare on key dimensions?     |

Each cycle uses the same four phases:

```text
PLAN → ACT → OBSERVE → REFLECT
```

| Phase      | Purpose                                                      |
| ---------- | ------------------------------------------------------------ |
| `plan/`    | Define scope, rubrics, source policy, and current run inputs |
| `act/`     | Run the prompt against a model or agent                      |
| `observe/` | Save the raw response exactly as produced                    |
| `reflect/` | Benchmark, synthesize, and produce higher-level outputs      |

## Quick Start

| I want to...                    | Go to...                                   |
| ------------------------------- | ------------------------------------------ |
| run discovery                   | `act/discovery/prompt.md`                  |
| run rating                      | `act/rating/prompt.md`                     |
| choose platforms for comparison | `plan/rating/platforms.md`                 |
| inspect discovery criteria      | `plan/discovery/scope.md`                  |
| inspect rating rubrics          | `plan/rating/rubrics.md`                   |
| inspect source rules            | `plan/rating/source-policy.md`             |
| benchmark discovery recall      | `reflect/discovery/benchmarking/prompt.md` |
| change a prompt contract        | `openspec/specs/` and `openspec/changes/`  |

## How To Work In This Repo

### 1. Read the planning files first

- Discovery runs use `plan/discovery/scope.md`.
- Rating runs use `plan/rating/rubrics.md`, `plan/rating/platforms.md`, and `plan/rating/source-policy.md`.
- `plan/rating/platforms.md` is per-run data for the current comparison set.

### 2. Run act-phase prompts through an AI CLI

Run the prompt file directly:

```text
Run act/discovery/prompt.md
Run act/rating/prompt.md
```

The CLI asks:

> Run as CLI or Web?

- `CLI`: the AI reads the declared input files from the repository and writes the result to `observe/<cycle>/cli-<model-short>.md`.
- `Web`: the AI emits a fully resolved prompt with required inputs inlined; paste that into a web chat and save the result to `observe/<cycle>/web-<model-short>.md`.

There are no placeholder tokens, cut-lines, or manual paste steps in the current workflow.

### 3. Save raw outputs under `observe/`

- Discovery responses go in `observe/discovery/`.
- Rating responses go in `observe/rating/`.
- File names follow `cli-<model-short>.md` or `web-<model-short>.md`.
- The `cli-` or `web-` prefix is the authority on which interface produced the file.

### 4. Reflect on results

Discovery benchmarking is currently implemented:

```text
Run reflect/discovery/benchmarking/prompt.md
```

That prompt reads all files in `observe/discovery/`, checks them against `reflect/discovery/benchmarking/benchmark.md`, and writes `reflect/discovery/benchmarking/coverage.md`.

## Repository Structure

The repository is organized by Action Research phase: `plan/`, `act/`, `observe/`, and `reflect/`.

Each phase contains `discovery/` and `rating/` artifacts. The folder layout is part of the method: planning files live in `plan/`, prompts live in `act/`, raw model outputs live in `observe/`, and evaluation or synthesis artifacts live in `reflect/`.

## Traceability Model

Different kinds of knowledge are intentionally stored in different places.

| What is tracked                             | Primary location                          |
| ------------------------------------------- | ----------------------------------------- |
| research scope, criteria, and run intent    | `plan/`                                   |
| prompt behavior and prompt contract changes | `openspec/specs/` and `openspec/changes/` |
| raw model output                            | `observe/`                                |
| evaluation and synthesis                    | `reflect/`                                |
| iteration history across all of the above   | git                                       |

`plan/rating/platforms.md` is especially important because it makes the selected comparison set git-diffable across runs.

## Response Files

- Response files live directly in `observe/<cycle>/`.
- File names follow `<interface>-<model-short>.md`.
- The filename prefix is the authority on interface: `cli-` or `web-`.

## OpenSpec And Prompt Changes

Each OpenSpec baseline spec is a contract for a governed repository artifact or workflow.

For prompts, that contract defines what the agent is supposed to do when the prompt is run. The agent performs the prompt against that contract; it does not invent the workflow from scratch each time.

That is why all `prompt.md` files in this repository are generated and maintained through OpenSpec. They are not hand-edited directly when their contract changes. If a prompt changes, the change should first be recorded as a contract change in OpenSpec so the reasoning and behavior change are documented properly.

When different models or agents execute the same prompt differently, the better fix is usually to add or tighten requirements in the governing OpenSpec spec rather than editing the prompt directly. A spec change makes the missing constraint explicit, records why the change is needed, and improves the contract used to regenerate future prompts. That usually produces more reproducible results across agents, because the workflow becomes better specified at the contract level instead of relying on increasingly ad hoc prompt wording.

To evolve a prompt or governed workflow:

```bash
openspec new change "<change-name>"
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
