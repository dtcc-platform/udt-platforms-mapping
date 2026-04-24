# UDT Platforms Map

A governed research repository for mapping and comparing the Urban Digital Twin ecosystem around DTCC.

It uses Action Research structure and OpenSpec so prompts, criteria, outputs, and workflow changes stay inspectable over time.

# Why Not One Prompt?

One large prompt makes change hard to understand.

It mixes:

- scope
- criteria
- source policy
- prompt contract
- run inputs

This repository splits those so later changes are easier to review and trust.

# Discovery And Rating

`discovery` and `rating` answer different questions.

- `discovery`: what exists and how should it be classified?
- `rating`: how should a selected set be compared?

Keeping them separate avoids collapsing search, classification, selection, and evaluation into one step.

# The Four Phases

Every cycle uses the same structure:

- `plan/` defines scope, rubrics, source policy, and current run inputs
- `act/` holds the runnable prompt
- `observe/` stores raw model outputs
- `reflect/` benchmarks or synthesizes results

This makes the workflow easier to follow and compare across runs.

# How Artifacts Move

The normal flow is:

`plan` -> `act` -> `observe` -> `reflect`

What changes slowly stays in planning and governed specs.

What changes every run stays in observation files and current run inputs.

# OpenSpec Governs Change

Prompt and workflow changes are not treated as casual edits.

OpenSpec governs:

- baseline specs
- active changes
- archived change history

That keeps the method explicit instead of hiding it inside prompt wording.

# Workflow-Level Artifacts

Not everything belongs to one research cycle.

The `workflow/` area holds artifacts about the method itself, such as:

- `workflow/prompts-status/` for prompt-status auditing
- `workflow/presentation/` for this tutorial deck

This keeps workflow knowledge visible without mixing it into discovery or rating outputs.

# Human In The Loop

Agents can help run research steps, but the workflow keeps human judgment explicit.

Researchers still decide:

- scope boundaries
- comparison sets
- criteria changes
- prompt contract changes
- how to interpret results

The goal is not just cheap output. The goal is a trustworthy and inspectable research process.

# How To Use The Repo

Start with planning files, then run the act prompt through an AI CLI.

Save raw outputs under `observe/`.

Use `reflect/` to benchmark or synthesize.

Use OpenSpec when the workflow or prompt contract changes.
