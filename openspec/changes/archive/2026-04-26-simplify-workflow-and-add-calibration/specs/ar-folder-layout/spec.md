## MODIFIED Requirements

### Requirement: Repository is organised as action research phases at top level
The repository SHALL use four top-level folders matching the action research phases: `plan/`, `act/`, `observe/`, and `reflect/`. Each phase folder SHALL contain exactly one subfolder per research cycle. The only research cycles are `discovery/` and `rating/`.

The repository MAY also contain a top-level `calibration/` folder for archival prompt/result comparisons across agents.

No files SHALL live at the phase root level for cycle-specific research content — all research-cycle content is inside a cycle subfolder. Each cycle is fully self-contained within its phase folder.

#### Scenario: Researcher navigates the repository
- **WHEN** a researcher opens the repository root
- **THEN** they see four phase folders (`plan/`, `act/`, `observe/`, `reflect/`) and MAY also see `calibration/` plus `README.md`, `AGENTS.md`, and tooling config

#### Scenario: Researcher follows one complete cycle
- **WHEN** a researcher wants to understand the discovery cycle end-to-end
- **THEN** they read `plan/discovery/`, `act/discovery/`, `observe/discovery/`, and `reflect/discovery/` in sequence without navigating outside those paths

### Requirement: plan/ holds research design documents per cycle
`plan/discovery/` SHALL contain `scope.md` defining the Layer classification criteria. `plan/rating/` SHALL contain `rubrics.md` defining the rating dimensions, `source-policy.md` defining acceptable source types and citation format, and `platforms.md` defining the selected comparison set. No other files are required in `plan/`.

#### Scenario: Researcher prepares a discovery session
- **WHEN** a researcher prepares to run a discovery prompt
- **THEN** they find the scope at `plan/discovery/scope.md`

#### Scenario: Researcher prepares a rating session
- **WHEN** a researcher prepares to run a rating prompt
- **THEN** they find the scope at `plan/rating/rubrics.md` and the source policy at `plan/rating/source-policy.md`

### Requirement: act/ holds canonical prompts and maintenance prompts
`act/discovery/prompt.md` SHALL be the discovery prompt template. `act/rating/prompt.md` SHALL be the rating prompt template. `act/check-prompts-status.md` SHALL be the prompt-status maintenance prompt.

#### Scenario: Researcher looks for the prompt to run
- **WHEN** a researcher wants to run a discovery session
- **THEN** they find the prompt at `act/discovery/prompt.md`

#### Scenario: Researcher looks for the prompt-status check
- **WHEN** a researcher wants to check prompt/spec alignment
- **THEN** they find the maintenance prompt at `act/check-prompts-status.md`

### Requirement: observe/ holds canonical saved outputs per cycle
`observe/discovery/` SHALL contain discovery response files from canonical executions. `observe/rating/` SHALL contain rating response files from canonical executions. Response files sit directly in the cycle folder with no `responses/` subfolder. File names SHALL NOT include the cycle type — the folder provides that context.

File names SHALL be prefixed with either `cli-` or `web-` indicating the interface that produced the response, followed by a short model identifier. The prefix is the single authority on which interface produced the response; the YAML metadata block inside the file SHALL NOT carry a separate `interface` field.

Artifacts under `calibration/` SHALL NOT be treated as the canonical output area for these executions.

#### Scenario: Researcher saves a discovery response produced in a web chat
- **WHEN** a researcher saves a model's discovery response produced in a web chat
- **THEN** it goes to `observe/discovery/web-<model-short>.md`

#### Scenario: AI saves a discovery response produced in CLI mode
- **WHEN** an AI CLI runs `act/discovery/prompt.md` in CLI mode and produces a response
- **THEN** the AI saves it to `observe/discovery/cli-<model-short>.md`

### Requirement: reflect/ holds benchmarking and reporting per cycle
`reflect/discovery/` SHALL contain two subfolders: `benchmarking/` and `reporting/`. `reflect/rating/` SHALL contain a `reporting/` subfolder.

`reflect/discovery/benchmarking/` SHALL contain: `benchmark.md`, `prompt.md`, and `coverage.md`. `reflect/discovery/reporting/` SHALL contain: `prompt.md` and `ecosystem.md`. `reflect/rating/reporting/` SHALL contain: `prompt.md`, `ecosystem.csv`, and `ecosystem-map.html`.

Each subfolder follows the same pattern: a `prompt.md` that drives the work, outputs at the same level.

#### Scenario: Researcher runs the benchmarking eval
- **WHEN** a researcher runs the discovery benchmarking eval
- **THEN** the prompt is at `reflect/discovery/benchmarking/prompt.md` and the output lands at `reflect/discovery/benchmarking/coverage.md`

#### Scenario: Researcher generates the ecosystem report
- **WHEN** a researcher runs the reporting prompt
- **THEN** the prompt is at `reflect/discovery/reporting/prompt.md` and the output is `ecosystem.md` in the same folder

### Requirement: README explains the canonical research interface and calibration area
`README.md` SHALL explain the action research methodology, the four phases, and the two cycles. It SHALL explain that canonical research execution happens through `plan/`, `act/`, `observe/`, and `reflect/`, while prompt/result comparison happens under `calibration/`.

`README.md` SHALL state that all governed `prompt.md` files in the repository are generated and maintained through OpenSpec. It SHALL refer researchers to the OpenSpec change workflow as the mechanism for evolving any prompt.

`README.md` SHALL explain that prompt calibration and research execution are distinct parts of the workflow.

#### Scenario: New contributor reads the README
- **WHEN** a new contributor opens `README.md`
- **THEN** they understand the canonical research interface, the calibration area, that prompts come from OpenSpec, and how git is used to track iterations

#### Scenario: Researcher wants to modify a prompt
- **WHEN** a researcher wants to change the discovery prompt
- **THEN** the README directs them to the OpenSpec workflow rather than editing `act/discovery/prompt.md` directly
