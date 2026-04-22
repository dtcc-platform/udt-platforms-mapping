# udt-platforms-map

A structured research repository for mapping the Urban Digital Twin (UDT) ecosystem, using action research methodology to discover, evaluate, and visualise platforms similar or adjacent to DTCC.

## Methodology

This repository follows an **action research** loop with two independent research cycles. Each cycle runs the same four phases:

```
PLAN → ACT → OBSERVE → REFLECT
```

| Phase       | What happens                                                    |
| ----------- | --------------------------------------------------------------- |
| **Plan**    | Define scope, criteria, and source policy for the cycle         |
| **Act**     | Run the prompt against AI models                                |
| **Observe** | Save raw model responses                                        |
| **Reflect** | Benchmark recall, synthesise findings, visualise the ecosystem  |

## Cycles

| Cycle         | Question                                          |
| ------------- | ------------------------------------------------- |
| `discovery`   | Which UDT platforms exist across the ecosystem?   |
| `rating`      | How do platforms compare on key dimensions?       |

## Folder Structure

Everything lives at `phase/cycle/`:

```
plan/
  discovery/      scope.md
  rating/         scope.md, source-policy.md

act/
  discovery/      prompt.md
  rating/         prompt.md

observe/
  discovery/      <model>.md  (raw discovery responses)
  rating/         <model>.md  (raw rating responses)

reflect/
  discovery/
    benchmarking/ benchmark.md, prompt.md, coverage.md
    reporting/    prompt.md, ecosystem.csv, ecosystem-map.html
  rating/
    benchmarking/ prompt.md  (stub — pending design)
    reporting/    prompt.md  (stub — pending design)
```

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
