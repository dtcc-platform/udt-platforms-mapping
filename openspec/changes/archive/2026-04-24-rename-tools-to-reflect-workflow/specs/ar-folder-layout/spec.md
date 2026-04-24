## ADDED Requirements

### Requirement: reflect-workflow holds workflow-reflection prompts and reports

The repository SHALL use `reflect-workflow/` as the root folder for workflow-reflection artifacts that operate on the research machinery itself rather than on a single discovery or rating cycle.

`reflect-workflow/prompt-validity/` SHALL contain:
- `prompt.md` — the prompt-validity audit runner
- `report.md` — the generated audit report

#### Scenario: Researcher looks for workflow-audit artifacts

- **WHEN** a researcher wants to inspect or run the prompt-validity audit
- **THEN** they find it under `reflect-workflow/prompt-validity/`, not under a generic `tools/` root
