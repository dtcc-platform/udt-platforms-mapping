## ADDED Requirements

### Requirement: tests/eval-discovery.md exists as a Claude Code CLI eval prompt

The repository SHALL contain a file at `tests/eval-discovery.md`. This file is a Claude Code CLI prompt — it contains instructions for Claude Code to execute a recall check against all discovery response files. It is NOT a web chat paste prompt.

The prompt SHALL instruct Claude Code to:

1. Read `tests/discovery-fixtures.md` and extract all expected platforms with their gap category and expected Layer
2. Glob all files matching `responses/global-platforms-discovery-*.md`
3. For each response file, extract the model name from the YAML metadata block (`model:` field) and parse the summary table to find discovered platform names
4. For each expected platform in the fixture, check — per response file — whether the platform name appears (case-insensitive match against the summary table `Name` column)
5. Record: found (with Layer match/mismatch noted if Layer differs from expected) or missing
6. Write a coverage report to `tests/reports/YYYY-MM-DD-coverage.md` using today's date

The prompt SHALL instruct Claude Code to use the model name from the response YAML metadata as the column header in the report, not the filename.

The prompt SHALL be runnable by a researcher telling Claude Code: "run the discovery eval" or "run tests/eval-discovery.md".

#### Scenario: Researcher runs the eval against three model responses

- **WHEN** a researcher tells Claude Code to run `tests/eval-discovery.md`
- **THEN** Claude Code reads the fixture and all three discovery response files, produces a coverage report, and saves it to `tests/reports/YYYY-MM-DD-coverage.md`

#### Scenario: A new discovery response is added to responses/

- **WHEN** a researcher adds a new file `responses/global-platforms-discovery-grok.md`
- **THEN** the next eval run automatically includes it without any changes to the eval prompt

#### Scenario: Researcher runs eval after updating the fixture

- **WHEN** a researcher adds a new expected platform to `tests/discovery-fixtures.md` and reruns the eval
- **THEN** the new platform appears in the coverage report for all models, showing found or missing

### Requirement: Eval prompt performs recall check only — not precision

The eval prompt SHALL check whether expected platforms appear in discovery responses (recall). It SHALL NOT penalise or flag platforms that appear in a response but are not in the fixture (precision). The report SHALL NOT contain a "false positive" or "unexpected finds" section.

#### Scenario: A model discovers a platform not in the fixture

- **WHEN** a model's discovery response includes a platform not listed in `tests/discovery-fixtures.md`
- **THEN** the eval prompt ignores it — the report only covers expected platforms from the fixture
