## ADDED Requirements

### Requirement: Prompt-validity audit report has a structured summary

The file at `tools/prompt-validity/report.md` SHALL contain a header block followed by a single flat summary table with one row per audited prompt.

The header block SHALL state:
- audit date
- number of prompts checked
- the directories scanned

The summary table SHALL contain exactly these columns:
- `Prompt`
- `Status`
- `Governing Spec`
- `Shared Contracts`
- `Required Inputs`
- `Reason`

#### Scenario: Researcher opens the report
- **WHEN** a researcher opens `tools/prompt-validity/report.md`
- **THEN** they first see the audit header and then a flat table summarizing every audited prompt

#### Scenario: Multiple prompts are checked
- **WHEN** the audit evaluates more than one live prompt
- **THEN** the summary table contains one row per prompt with no additional grouping sections inside the table

### Requirement: Report includes detailed findings for each prompt

After the summary table, the report SHALL contain one `##` section per audited prompt in path order.

Each prompt section SHALL include:
- the final status
- the governing spec path
- the declared required inputs
- the freshness dependencies considered
- the latest git commit reference for the prompt
- the latest git commit reference for any newer freshness dependency, if applicable
- a flat bullet list of findings

#### Scenario: Prompt is review-needed because spec is newer
- **WHEN** a prompt's governing spec has a newer git change than the prompt
- **THEN** the prompt's detail section names both paths and records the freshness finding

#### Scenario: Prompt is invalid because of a missing file
- **WHEN** a required input file is missing
- **THEN** the prompt's detail section lists the missing path in its findings bullets

### Requirement: Report records ignored runtime-input churn correctly

If a runtime-input file is newer than a prompt but does not create a contract mismatch, the report SHALL NOT classify the prompt as stale on that basis alone.

The report MAY mention the newer runtime-input change in the detailed findings, but the status SHALL remain `valid` unless another freshness or validity problem is found.

#### Scenario: Per-run platforms file changed
- **WHEN** `plan/rating/platforms.md` changed after `act/rating/prompt.md` and the prompt contract still matches its governing spec
- **THEN** the report does not mark `act/rating/prompt.md` as `review-needed` or `invalid` on that basis alone
