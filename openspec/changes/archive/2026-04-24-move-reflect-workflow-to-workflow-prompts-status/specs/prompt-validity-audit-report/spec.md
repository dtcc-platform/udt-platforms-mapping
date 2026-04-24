## MODIFIED Requirements

### Requirement: Prompt-validity audit report has a structured summary

The file at `workflow/prompts-status/report.md` SHALL contain a header block followed by a single flat summary table with one row per audited prompt.

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
- **WHEN** a researcher opens `workflow/prompts-status/report.md`
- **THEN** they first see the audit header and then a flat table summarizing every audited prompt

#### Scenario: Multiple prompts are checked
- **WHEN** the audit evaluates more than one live prompt
- **THEN** the summary table contains one row per prompt with no additional grouping sections inside the table
