## Purpose

Defines the eval prompt file (`evals/discovery/run.md`) — a Claude Code CLI prompt that performs a recall check against all discovery response files, comparing them against the fixture to produce a coverage report.

## Requirements

### Requirement: evals/discovery/run.md exists as a Claude Code CLI eval prompt

The repository SHALL contain a file at `evals/discovery/run.md`. This file is a Claude Code CLI prompt — it contains instructions for Claude Code to execute a recall check against all discovery response files. It is NOT a web chat paste prompt.

The prompt SHALL instruct Claude Code to:

1. Read `evals/discovery/benchmark.md` and extract all expected platforms with their gap category, expected Layer, and Aliases
2. Glob all files matching `responses/global-platforms-discovery-*.md`
3. For each response file, extract the model name from the YAML metadata block (`model:` field) and parse the summary table to find discovered platform names
4. For each expected platform in the fixture, check — per response file — whether the platform name appears in the response summary table using the following match rule: build a match set containing the canonical `Name` plus all entries from the `Aliases` cell (split on `,`, trimmed); the platform is found if any member of the match set appears as a case-insensitive substring in the response `Name` column value
5. Record: found (with Layer match/mismatch noted if Layer differs from expected) or missing
6. Write a coverage report to `evals/discovery/reports/coverage.md`, overwriting if it exists

The prompt SHALL instruct Claude Code to use the model name from the response YAML metadata as the column header in the report, not the filename.

The prompt SHALL be runnable by a researcher telling Claude Code: "run the discovery eval" or "run evals/discovery/run.md".

#### Scenario: Researcher runs the eval against three model responses

- **WHEN** a researcher tells Claude Code to run `evals/discovery/run.md`
- **THEN** Claude Code reads the fixture and all discovery response files, produces a coverage report, and saves it to `evals/discovery/reports/coverage.md`

#### Scenario: Alias eliminates a false negative

- **WHEN** the fixture has "City Energy Analyst" with alias `CityEnergyAnalyst`, and a model's response summary table contains "CityEnergyAnalyst"
- **THEN** the eval records the platform as found, not missing

#### Scenario: A new discovery response is added to responses/

- **WHEN** a researcher adds a new file `responses/global-platforms-discovery-grok.md`
- **THEN** the next eval run automatically includes it without any changes to the eval prompt

#### Scenario: Researcher runs eval after updating the fixture

- **WHEN** a researcher adds a new expected platform to `evals/discovery/benchmark.md` and reruns the eval
- **THEN** the new platform appears in the coverage report for all models, showing found or missing

### Requirement: Eval prompt performs recall check only — not precision

The eval prompt SHALL check whether expected platforms appear in discovery responses (recall). It SHALL NOT penalise or flag platforms that appear in a response but are not in the fixture (precision). The report SHALL NOT contain a "false positive" or "unexpected finds" section.

#### Scenario: A model discovers a platform not in the fixture

- **WHEN** a model's discovery response includes a platform not listed in `evals/discovery/benchmark.md`
- **THEN** the eval prompt ignores it — the report only covers expected platforms from the fixture
