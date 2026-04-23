# Spec: ar-folder-layout

## Purpose

TBD — Defines the top-level folder structure for the repository, organised as action research phases (`plan/`, `act/`, `observe/`, `reflect/`) with one subfolder per research cycle (`discovery/`, `rating/`).
## Requirements
### Requirement: Repository is organised as action research phases at top level

The repository SHALL use four top-level folders matching the action research phases: `plan/`, `act/`, `observe/`, and `reflect/`. Each phase folder SHALL contain exactly one subfolder per research cycle. The only research cycles are `discovery/` and `rating/`.

No files SHALL live at the phase root level — all content is inside a cycle subfolder. Each cycle is fully self-contained within its phase folder.

#### Scenario: Researcher navigates the repository

- **WHEN** a researcher opens the repository root
- **THEN** they see four folders (`plan/`, `act/`, `observe/`, `reflect/`) plus `README.md`, `AGENTS.md`, and tooling config — no loose content files

#### Scenario: Researcher follows one complete cycle

- **WHEN** a researcher wants to understand the discovery cycle end-to-end
- **THEN** they read `plan/discovery/`, `act/discovery/`, `observe/discovery/`, and `reflect/discovery/` in sequence without navigating outside those paths

### Requirement: plan/ holds research design documents per cycle

`plan/discovery/` SHALL contain `scope.md` defining the Layer classification criteria. `plan/rating/` SHALL contain `scope.md` defining the rating dimensions and `source-policy.md` defining acceptable source types and citation format. No other files are required in `plan/`.

#### Scenario: Researcher prepares a discovery session

- **WHEN** a researcher prepares to run a discovery prompt
- **THEN** they find the scope at `plan/discovery/scope.md`

#### Scenario: Researcher prepares a rating session

- **WHEN** a researcher prepares to run a rating prompt
- **THEN** they find the scope at `plan/rating/rubrics.md` and the source policy at `plan/rating/source-policy.md`

### Requirement: act/ holds one prompt.md per cycle

`act/discovery/prompt.md` SHALL be the discovery prompt template. `act/rating/prompt.md` SHALL be the rating prompt template. No other files are required in `act/`.

#### Scenario: Researcher looks for the prompt to run

- **WHEN** a researcher wants to run a discovery session
- **THEN** they find the prompt at `act/discovery/prompt.md`

### Requirement: observe/ holds raw model responses per cycle

`observe/discovery/` SHALL contain raw discovery response files from AI models. `observe/rating/` SHALL contain raw rating response files. Response files sit directly in the cycle folder with no `responses/` subfolder. File names SHALL NOT include the cycle type — the folder provides that context.

File names SHALL be prefixed with either `cli-` or `web-` indicating the interface that produced the response, followed by a short model identifier (for example, `web-claude.md`, `cli-claude-code.md`). The prefix is the single authority on which interface produced the response; the YAML metadata block inside the file SHALL NOT carry a separate `interface` field.

#### Scenario: Researcher saves a discovery response produced in a web chat

- **WHEN** a researcher saves a model's discovery response produced in a web chat
- **THEN** it goes to `observe/discovery/web-<model-short>.md` — with the `web-` prefix identifying the interface

#### Scenario: AI saves a discovery response produced in CLI mode

- **WHEN** an AI CLI runs `act/discovery/prompt.md` in CLI mode and produces a response
- **THEN** the AI saves it to `observe/discovery/cli-<model-short>.md`

#### Scenario: Researcher scans the observe/ folder by interface

- **WHEN** a researcher lists `observe/discovery/`
- **THEN** they can tell at a glance which files came from CLI sessions and which came from web chats, without opening them

### Requirement: reflect/ holds benchmarking and reporting per cycle

`reflect/discovery/` SHALL contain two subfolders: `benchmarking/` and `reporting/`. `reflect/rating/` SHALL be scaffolded with the same two subfolders.

`reflect/discovery/benchmarking/` SHALL contain: `benchmark.md`, `prompt.md` (the eval runner), and `coverage.md` (the generated coverage report). `reflect/discovery/reporting/` SHALL contain: `prompt.md` (the inventory/reporting prompt), `ecosystem.csv`, and `ecosystem-map.html`.

Each subfolder follows the same pattern: a `prompt.md` that drives the work, outputs at the same level.

#### Scenario: Researcher runs the benchmarking eval

- **WHEN** a researcher runs the discovery benchmarking eval
- **THEN** the prompt is at `reflect/discovery/benchmarking/prompt.md` and the output lands at `reflect/discovery/benchmarking/coverage.md`

#### Scenario: Researcher generates the ecosystem report

- **WHEN** a researcher runs the reporting prompt
- **THEN** the prompt is at `reflect/discovery/reporting/prompt.md` and outputs are `ecosystem.csv` and `ecosystem-map.html` in the same folder

### Requirement: README explains the two-cycle action research structure

`README.md` SHALL explain the action research methodology, the four phases, and the two cycles. It SHALL include the folder map showing `phase/cycle/` hierarchy. It SHALL replace `docs/02-methodology.md`, which SHALL be removed.

`README.md` SHALL state that all `prompt.md` files in the repository are generated and maintained through an OpenSpec workflow — researchers do not hand-write them. It SHALL link or refer to the OpenSpec change workflow as the mechanism for evolving any prompt.

`README.md` SHALL explain that the iterative nature of each cycle is tracked using standard git practices: researchers are encouraged to use feature branches per cycle run, conventional commit messages (e.g. `observe(discovery): add gemini response`), and tags or releases to mark significant cycle milestones.

#### Scenario: New contributor reads the README

- **WHEN** a new contributor opens `README.md`
- **THEN** they understand the AR phases, both cycles, how to navigate to any artifact, that prompts come from OpenSpec, and how git is used to track iterations

#### Scenario: Researcher wants to modify a prompt

- **WHEN** a researcher wants to change the discovery prompt
- **THEN** the README directs them to the OpenSpec workflow rather than editing `act/discovery/prompt.md` directly

#### Scenario: Researcher runs a second discovery cycle

- **WHEN** a researcher runs the discovery cycle a second time with a different model
- **THEN** the README explains they should use a feature branch, save the response to `observe/discovery/`, and commit with a conventional message

