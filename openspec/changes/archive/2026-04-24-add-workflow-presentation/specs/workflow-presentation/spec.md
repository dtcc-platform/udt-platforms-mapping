## ADDED Requirements

### Requirement: Workflow presentation area exists

The repository SHALL contain a workflow-level presentation area at `workflow/presentation/`.

This area SHALL contain:
- `prompt.md` — the runnable generator prompt
- `deck.md` — the generated Pandoc-ready Markdown deck

#### Scenario: Researcher looks for the workflow presentation

- **WHEN** a researcher wants the repository's workflow tutorial deck
- **THEN** they find it under `workflow/presentation/`

### Requirement: Workflow presentation prompt exists as a CLI generator prompt

The repository SHALL contain a file at `workflow/presentation/prompt.md`. This file SHALL be a CLI-only prompt that generates or refreshes `workflow/presentation/deck.md`.

The prompt SHALL instruct the AI to read the workflow-relevant repository context before writing the deck, including:
- `README.md`
- `openspec/specs/ar-folder-layout/spec.md`
- `openspec/specs/prompt-run-modes/spec.md`
- `openspec/specs/workflow-prompts-status/spec.md`
- the current live `plan/`, `act/`, `observe/`, and `reflect/` structure as needed for accuracy

#### Scenario: Researcher runs the workflow presentation generator

- **WHEN** a researcher tells their AI CLI to run `workflow/presentation/prompt.md`
- **THEN** the AI generates or refreshes `workflow/presentation/deck.md` in CLI mode

### Requirement: Workflow presentation deck is Pandoc-ready Markdown

The generated file at `workflow/presentation/deck.md` SHALL be a valid Markdown slide deck intended for Pandoc conversion.

The deck SHALL be a single coherent presentation source rather than per-slide files.

The deck SHALL remain short and tutorial-oriented rather than exhaustive.

#### Scenario: Researcher converts the deck with Pandoc

- **WHEN** a researcher uses `workflow/presentation/deck.md` as Pandoc input
- **THEN** the file is already structured as one complete Markdown deck source

### Requirement: Workflow presentation teaches the repository workflow as a tutorial

The generated deck SHALL explain the repository workflow as a tutorial for new or returning contributors.

The tutorial arc SHALL include:
- why the repository splits one large prompt into separate artifacts
- why `discovery` and `rating` are separate kinds of work
- the role of `plan/`, `act/`, `observe/`, and `reflect/`
- the role of OpenSpec in governing prompt and workflow changes
- the role of workflow-level artifacts under `workflow/`
- the role of the human researcher in reviewing boundaries, criteria, and prompt contracts

#### Scenario: New contributor reads the deck

- **WHEN** a new contributor reads `workflow/presentation/deck.md`
- **THEN** they understand the repository as a governed Action Research workflow rather than a loose collection of prompts

### Requirement: Workflow presentation stays aligned with live repository behavior

The generator prompt SHALL instruct the AI to prefer the current live baseline specs and current repository structure over historical or archived phrasing.

The deck SHALL NOT describe retired workflows, removed baseline specs, or superseded prompt mechanics as if they were current.

#### Scenario: Workflow changed since the last deck version

- **WHEN** the repository workflow has changed and the researcher reruns `workflow/presentation/prompt.md`
- **THEN** the refreshed `deck.md` reflects the current live workflow rather than stale historical behavior
