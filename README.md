# udt-platforms-map

This repository supports Urban Digital Twin platform research with AI agents as research collaborators.

## Purpose

The goal is to map and compare the Urban Digital Twin platform ecosystem in a way that is credible, repeatable, and reviewable.

This is not a collection of one-off prompts. The repository is organized around a research methodology so human judgment is part of the whole process: defining scope, choosing inputs, running governed research actions, preserving outputs, reviewing interpretations, and reflecting findings back into the next cycle.

AI agents help execute and review research work, but the repository keeps the research definitions, assumptions, and output contracts explicit.

## Why Spec-First

OpenSpec provides the contract layer between researcher intent and agent execution.

Specs define the working research reality that agents must use: what counts as a platform, framework, module, initiative, or excluded boundary case; how platforms should be compared; what evidence is acceptable; and what output shape must be produced.

This matters because the UDT ecosystem and our understanding of it are not fixed. As definitions, comparison methods, and evidence expectations improve, those changes are captured as OpenSpec deltas. The repository therefore tracks not only research outputs, but also how the research team's understanding evolves over time.

Specs are research behavior contracts, not implementation plans. They let agents collaborate against shared definitions instead of improvising from prompt wording alone.

## Methodology

The core research loop follows action research:

```text
PLAN -> ACT -> OBSERVE -> REFLECT
```

- `plan/` contains run inputs such as selected comparison sets, benchmark fixtures, and run-specific scope material.
- `act/` contains contract manifests and resolved executable prompts for research, benchmarking, and reporting actions.
- `observe/` stores saved model outputs, generated coverage artifacts, and optional saved review evidence.
- `reflect/` contains synthesized reporting, comparison, prompt-review, and reflection artifacts.

Phase structure and artifact naming are governed by `research-workflow-structure`.

```mermaid
flowchart TD
    P["plan/\nrun inputs and scope"]
    A["act/\nresearch manifests"]
    O["observe/\nmodel outputs and generated artifacts"]
    F["reflect/\nsynthesis and reporting"]
    C["OpenSpec change\naccepted clarification"]

    P --> A
    A --> O
    O --> F
    F --> C
    C --> P
    C --> A
```

## OpenSpec Naming

Formal contracts live in `openspec/specs/`.

Naming rules are governed by `research-workflow-structure`. In short, `research-*` specs govern cross-phase research workflow concerns, while `plan-*`, `act-*`, `observe-*`, and `reflect-*` specs govern one phase.

## Research Actions

Entity discovery is intentionally broad. It finds technical artifacts, initiatives, projects, programmes, deployments, and useful boundary candidates, then classifies them using the stable `Type` contract.

Platform comparison is the stricter evaluative stage. Only rows classified as `Type = platform` by entity discovery are eligible for platform comparison.

Canonical actions include:

- entity discovery
- platform comparison
- platform discovery benchmark
- platform discovery report
- platform comparison report

## Working With Agents

Start from the relevant OpenSpec contract, the matching `act/` manifest, and any required `plan/` input.

For a web research run:

```text
Resolve act/entity-discovery.md for web use.
```

The resolver inlines the manifest's required contracts, appends the manifest prompt body, and saves the resolved prompt as `act/entity-discovery-resolved-<resolver-short>.md`. Paste that prompt into the selected web model, then save the response to `observe/entity-discovery-<model-short>.md`.

When uploading the resolved prompt as a file to a web research tool, use this launcher message:

```text
The attached file contains the complete research prompt. Read the file content as the query and execute it exactly. Do not ask me for another topic unless the file cannot be read.
```

The repository-local shortcut for the same entity discovery resolve step is:

```text
udt:discover
```

Repository-local skills are operational shortcuts. They are not the source of truth; the specs, manifests, and run inputs are.

## Prompt Review

Prompt review checks whether a resolved prompt faithfully composes its manifest, required specs, and run inputs.

The resolved prompt is the working contract between the researcher and the agent that will run the research. One agent drafts that contract from the approved specs and inputs; a different agent reviews it as a third party against the same shared context before execution.

The point is to align agents on one interpretation of the specs before spending time on deep research runs. Even when resolution is mostly inlining, review is still valuable because the final prompt can fail at the composition layer: missing contracts, stale contracts, confusing order, resolver glue, ambiguous combined instructions, or a prompt that is faithful on paper but not executable in the target web tool.

The process and storage rules are governed by `research-prompt-review`. The minimum third-party review criteria are governed by `research-prompt-review-checklist`.

Use this when prompt generation or agent interpretation matters:

1. Save the resolved prompt snapshot as `act/<action>-resolved-<resolver-short>.md`.
2. Ask a different reviewer agent to compare it against the source manifest, required contracts, required inputs, and `research-prompt-review-checklist`.
3. Review happens in stdout/chat by default; save `observe/<action>-prompt-review-<reviewer-short>.md` only when an audit artifact is useful.
4. If a fix is needed, the reviewer proposes an OpenSpec change intent instead of rewriting the prompt directly.
5. Convert accepted issues into scoped OpenSpec changes, then regenerate the resolved prompt.

The checklist covers the minimum checks: source coverage, composition fidelity, prompt executability, target-runner fit, output contract clarity, ambiguity, conflict, and whether a repository fix needs an OpenSpec proposal. Reviewer agents can still add action-specific findings.

```mermaid
flowchart TD
    M["act/ manifest"]
    S["Required specs"]
    P["Required plan inputs"]
    R["act/\nresolved prompt"]
    K["research-prompt-review-checklist"]
    V["Third-party reviewer\nstdout review"]
    D["OpenSpec proposal"]

    M --> R
    S --> R
    P --> R
    K --> V
    R --> V
    V -->|required fix| D
    D --> S
    D --> M
    D --> R
```

## Health Checks

Use these checks when reviewing, handing off, or committing repository work:

```bash
openspec validate --all --strict
git status --short
```

Use `openspec validate <change-name> --strict` before applying or archiving a specific OpenSpec change.

These checks confirm repository contract health and working-tree state. They do not verify research truth, evidence quality, or model-output completeness.

## Report Missing Candidates

If a platform, framework, module, initiative, or relevant excluded boundary case is missing, open a GitHub issue with the **Missing research candidate** form.

Use:

```text
Issues -> New issue -> Missing research candidate
```

Add the candidate name, a link if available, and any short note that helps triage it. Classification can be handled later.
