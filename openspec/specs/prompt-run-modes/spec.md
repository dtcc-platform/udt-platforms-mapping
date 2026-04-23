# Spec: prompt-run-modes

## Purpose

Defines the shared run-modes contract for prompt files — the `## Required Inputs` declaration section, the CLI-or-Web mode ask, the per-mode behaviors (file resolution vs. resolved-prompt emission), and the response filename prefix convention.

## Requirements

### Requirement: Run-modes prompts declare a Required Inputs section

Each run-modes-compliant prompt file SHALL include a `## Required Inputs` section. The section SHALL contain a Markdown unordered list in which each list item names one input file and its role, in the form:

- `<repository-relative path>` — short description of what this file provides

The paths SHALL be repository-relative. The list SHALL be the complete set of files the prompt needs — no other files are implicitly read.

#### Scenario: Researcher opens a run-modes prompt file

- **WHEN** a researcher opens `act/discovery/prompt.md` or `act/rating/prompt.md`
- **THEN** the Required Inputs section enumerates every file the prompt consumes, with repository-relative paths and short descriptions

#### Scenario: AI CLI reads the prompt file

- **WHEN** an AI CLI opens a run-modes prompt
- **THEN** it can determine the complete set of input files by reading the Required Inputs section alone, without parsing the prompt body

### Requirement: Run-modes prompts instruct the AI to ask the user which mode to run

Each run-modes-compliant prompt SHALL include a `## Run Modes` section. The section SHALL instruct the AI, before executing any other part of the prompt, to ask the user:

> Run as CLI or Web?

The section SHALL define two modes — **CLI** and **Web** — with the following behaviors:

- **CLI**: the AI reads every file listed in Required Inputs, executes the prompt body using that content, and saves the response to `observe/<cycle>/cli-<model-short>.md`
- **Web**: the AI produces a fully resolved prompt — the content of each Required Inputs file inlined at the top of the prompt under a heading naming the file, followed by the prompt body below — and outputs it as a copy-ready block for the researcher to paste into a web chat. The researcher saves the web-chat response to `observe/<cycle>/web-<model-short>.md`

The AI SHALL NOT guess the mode. If the user does not specify a mode, the AI SHALL ask before proceeding.

#### Scenario: Researcher runs a prompt without specifying mode

- **WHEN** a researcher tells their AI CLI to run a run-modes prompt
- **THEN** the AI's first action is to ask "Run as CLI or Web?" — it does not begin executing the prompt body

#### Scenario: Researcher chooses CLI mode

- **WHEN** the researcher answers "CLI"
- **THEN** the AI reads every file in Required Inputs, produces a response to the prompt, and saves the response to `observe/<cycle>/cli-<model-short>.md`

#### Scenario: Researcher chooses Web mode

- **WHEN** the researcher answers "Web"
- **THEN** the AI outputs a resolved prompt with each Required Inputs file inlined at the top under a heading, followed by the prompt body — and does not itself attempt to answer the prompt

### Requirement: Web-mode output is the resolved prompt only

In Web mode, the AI's primary output SHALL be the fully resolved prompt body — a single block suitable for copying directly into a web chat session. The AI SHALL NOT wrap the resolved prompt in BEGIN/END markers, add AI-generated narration inside the resolved block, or otherwise introduce content that would need to be stripped before pasting.

The AI MAY append a short note after the resolved block telling the researcher where to save the web-chat response (e.g., "Save the web-chat response to `observe/discovery/web-<model-short>.md`"), but this note SHALL be clearly separated from the resolved prompt so it is not mistaken for part of the prompt.

#### Scenario: Researcher copies the resolved prompt

- **WHEN** a researcher selects the resolved prompt block from the Web-mode output
- **THEN** they can paste it directly into a web chat with no cleanup, header-stripping, or footer-removal

### Requirement: Response filenames carry an interface prefix

Response files saved under `observe/<cycle>/` SHALL be named with one of two prefixes:

- `cli-<model-short>.md` — produced by a CLI session
- `web-<model-short>.md` — produced by a web chat session

The prefix is the single authority on which interface produced the response. The YAML metadata block inside the file SHALL NOT carry a separate `interface` field — the filename prefix is sufficient.

#### Scenario: Researcher lists the observe/ folder

- **WHEN** a researcher lists `observe/discovery/` or `observe/rating/`
- **THEN** every file begins with `cli-` or `web-`, and the interface is identifiable without opening any file

#### Scenario: CLI-produced response is saved

- **WHEN** an AI CLI completes a CLI-mode run of a run-modes prompt
- **THEN** the AI saves the response to `observe/<cycle>/cli-<model-short>.md`

#### Scenario: Web-chat response is saved

- **WHEN** a researcher saves a web-chat response for a run-modes prompt
- **THEN** the file is named `observe/<cycle>/web-<model-short>.md`

### Requirement: Run-modes contract applies only to act/ prompts

The run-modes contract SHALL apply to `act/discovery/prompt.md` and `act/rating/prompt.md` only. Reflect-phase prompts (`reflect/*/prompt.md`) SHALL NOT declare a Run Modes section — they are CLI-only by nature (they read bulk response files and/or write generated artifacts).

A reflect-phase prompt MAY include a Required Inputs section for readability, but it is not a run-modes-compliant prompt and the ask-mode interaction SHALL NOT happen.

#### Scenario: Researcher runs a reflect-phase prompt

- **WHEN** a researcher tells their AI CLI to run `reflect/discovery/benchmarking/prompt.md`
- **THEN** the prompt executes directly in CLI mode without the AI asking for mode selection
