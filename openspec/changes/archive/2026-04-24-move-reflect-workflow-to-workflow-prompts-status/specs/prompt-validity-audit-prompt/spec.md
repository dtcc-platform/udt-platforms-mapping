## MODIFIED Requirements

### Requirement: Prompt-validity audit prompt exists as a CLI maintenance prompt

The repository SHALL contain a file at `workflow/prompts-status/prompt.md`. This file SHALL be a CLI-only maintenance prompt that audits live repository prompt files for validity and freshness. It SHALL NOT be a Web-mode prompt.

The prompt SHALL instruct the AI to inspect live prompt files under `act/` and `reflect/` only.

#### Scenario: Researcher runs the prompt-validity audit
- **WHEN** a researcher tells their AI CLI to run `workflow/prompts-status/prompt.md`
- **THEN** the AI executes the audit directly in CLI mode without asking for run mode selection

#### Scenario: Archived change prompts exist
- **WHEN** prompt-like files exist under `openspec/changes/` or `openspec/changes/archive/`
- **THEN** the audit ignores them and checks only the live prompts under `act/` and `reflect/`

### Requirement: Audit prompt writes a report file

The audit prompt SHALL write its results to `workflow/prompts-status/report.md`, overwriting any existing file.

The prompt SHALL be runnable by a researcher telling the AI CLI either `run workflow/prompts-status/prompt.md` or `run the prompt validity audit`.

#### Scenario: Researcher reruns the audit after a change
- **WHEN** a researcher reruns the prompt-validity audit
- **THEN** the previous `workflow/prompts-status/report.md` is replaced with a new report reflecting the current repository state
