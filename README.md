# udt-platforms-map

A spec-first research repository for governing Urban Digital Twin research agents and stabilizing the workflow they run.

This repository uses OpenSpec to govern prompt and workflow changes, and uses git to track how researchers and agents iterate on the work over time.

## Methodology

### Primary Goal

Research results in this repository are not treated as final truths.
They are treated as outputs that can be added to, corrected, or improved through repeated cycles.

What must become trusted and stabilized is the workflow:

- how intent is specified,
- how prompts are governed,
- how outputs are compared, and
- how changes are traced.

This repository is a medium for governing research agents through explicit contracts, Continual AI Review, execution, and reflection.

Contributors primarily improve the workflow by calibrating prompts, refining contracts, and adding new research cycles.
Agents primarily execute those cycles and generate research outputs within the governed workflow.

### Core Idea

Each OpenSpec baseline spec is a contract for a governed artifact or workflow.

For prompts, that contract defines what an agent is supposed to do when the prompt is run.
The prompt is the operational rendering of the contract, not the source of truth.

That is why prompt changes should go through OpenSpec:

- the behavior change gets documented before the prompt changes
- the reason for the change is preserved in proposal, design, and spec history
- future prompt regeneration starts from a clearer contract
- shared specs can be refactored once and then reused consistently across every dependent prompt contract

When different agents execute the same prompt differently, the stronger fix is usually to tighten the governing spec rather than patch the prompt directly.

Composing smaller prompts and smaller supporting artifacts is intentional.
It keeps scope, criteria, source policy, prompt contracts, and run inputs separable.
That makes changes easier to interpret, makes shared rules easier to reuse, and keeps humans in the loop by making the important boundaries reviewable instead of burying them in one large prompt.

### Repository Model

The repository is organized around complementary research threads.
These threads are not cycles in themselves.
The cycle is the repeated Action Research loop across phases:

```text
PLAN → ACT → OBSERVE → REFLECT
```

Each thread has its own artifacts across those phases.
That keeps prompts and supporting artifacts smaller, narrower, and easier to compose.
Composing smaller prompts is not only a prompt-design choice; it is the mechanism that lets humans steer the workflow without rewriting the whole system each time.

That decomposition is also what keeps humans in the loop:

- Scope can be adjusted without rewriting execution prompts
- Source policy can be tightened without rewriting reflection prompts
- One thread can be redirected without destabilizing the whole repository
- Reflection can connect threads and let results from one thread influence another

The plan phase carries the thread-level interpretation of the workflow:

- each thread has its own planning material describing its purpose and inputs
- plan-level dependency documentation explains how threads depend on and inform each other

The repository has two main parts:

- Continual AI Review: the archival layer under `calibration/`, used to compare prompt realizations and agent behavior against the same accepted contract
- Research execution: the canonical layer under `plan/`, `act/`, `observe/`, and `reflect/`, used to run the research itself and get accepted results

Git history is part of the workflow, not just storage.
Together, the repository structure and git history make it possible to inspect how a result was produced:

- the workflow shows which phase artifacts shaped the result
- the git log shows when those artifacts changed
- branches and calibration history show how prompt calibration happened
- the resulting history shows how much a saved result reflects an up-to-date view of the ecosystem rather than an older contract or older evidence base

In that sense:

- OpenSpec is the common abstraction layer shared by humans and agents for calibrating prompts and workflow behavior
- `calibration/` is the archival area where prompt and result deviations are made explicit
- the canonical repository structure is the accepted interface for doing the research and getting results

## How To Work In This Repo

### 1. Start in `plan/`

Start from the planning artifacts for the thread you are working on.
That is where purpose, scope, source policy, and thread dependencies are made explicit before execution.

### 2. Run canonical prompts from `act/`

Use:

```text
Run act/udt-platforms/prompt.md
Run act/udt-platform-comparison/prompt.md
```

Canonical prompts read their declared planning inputs and write or prepare outputs for the matching thread.

### 3. Save outputs under `observe/` and synthesize under `reflect/`

Saved canonical outputs belong in `observe/`.
Reflection, benchmarking, and reporting belong in `reflect/`.
This is where one thread can inform another and where the next cycle gets shaped.

### 4. Use `calibration/` for Continual AI Review, not canonical research state

When different agents realize the same accepted contract differently, store those prompt/result pairs under `calibration/`.
Those artifacts are for comparing prompt behavior, not for replacing the canonical research state.

## Workflow Diagrams

### Research Execution

```mermaid
flowchart TD
    P["plan/
purpose, scope, source policy, dependencies"]
    A["act/
canonical prompt"]
    O["observe/
saved result"]
    R["reflect/
benchmarking, reporting, synthesis"]
    N["next cycle
updated contracts and inputs"]

    P --> A
    A --> O
    O --> R
    R --> N
```

### Continual AI Review

```mermaid
flowchart TD
    M["main baseline
accepted spec and inputs"]

    W1["worktree a
agent-a branch"]
    W2["worktree b
agent-b branch"]
    W3["worktree c
agent-c branch"]

    P1["agent-a
generate prompt"]
    P2["agent-b
generate prompt"]
    P3["agent-c
generate prompt"]

    R1["agent-a
run prompt and save result"]
    R2["agent-b
run prompt and save result"]
    R3["agent-c
run prompt and save result"]

    C["calibration/
archive prompt + result pairs"]

    F["reflection on deviations
compare prompt realizations"]

    U["update contracts
if needed"]

    M -->|create worktrees| W1
    M -->|create worktrees| W2
    M -->|create worktrees| W3

    W1 --> P1
    W2 --> P2
    W3 --> P3

    P1 --> R1
    P2 --> R2
    P3 --> R3

    R1 -->|archive under calibration/| C
    R2 -->|archive under calibration/| C
    R3 -->|archive under calibration/| C

    C --> F
    F --> U
```

## Naming Conventions

| Kind                 | Pattern                           | Example                                           |
| -------------------- | --------------------------------- | ------------------------------------------------- |
| phase-cycle commit   | `<phase>(<cycle>): <subject>`     | `observe(udt-platforms): add claude response`     |
| spec/workflow commit | `<type>(<scope>): <subject>`      | `refactor(specs): rename cycles to udt-platforms` |
| agent branch         | `<agent>` or `<agent>-<research>` | `agent-a`, `agent-b-udt-platforms`                |

## Future Directions

- A possible future direction is to adopt a Markdown-native relationship layer such as [Tolaria](https://tolaria.md/) and use YAML frontmatter on governed files to express purpose, dependencies, and thread relationships directly in each document.
  If that happens, per-file frontmatter could replace or reduce the need for separate dependency-mapping documents, while keeping relationships inspectable through plain files and git history.
  This is only a future direction. The current repository does not require frontmatter on all Markdown files, and the current workflow remains the source of truth.
- Another future direction is to simplify the workflow for end users through higher-level skills that wrap the internal repository mechanics, similar in spirit to the skill-driven workflow system described by [The Unfinishable Map](https://unfinishablemap.org/workflow/).
  That would let users invoke named workflow actions while the underlying prompts, files, and git operations remain governed by the repository.
