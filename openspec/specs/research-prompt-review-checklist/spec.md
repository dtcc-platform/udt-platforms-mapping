# Spec: research-prompt-review-checklist

## Purpose

Defines the minimum review criteria for third-party review of any saved resolved prompt.

## Requirements

### Requirement: Prompt review checklist applies to all resolved prompts

Third-party prompt review SHALL use this checklist for any saved resolved prompt, regardless of research action, target runner, or prompt type.

The checklist SHALL define minimum review criteria and SHALL NOT prevent the reviewer from adding action-specific findings.

#### Scenario: Reviewer checks any resolved prompt

- **WHEN** a reviewer reviews a saved resolved prompt
- **THEN** the reviewer applies the minimum prompt-review checklist
- **THEN** the reviewer may add action-specific findings when the resolved prompt or target runner creates additional risks

### Requirement: Reviewer checks source coverage and composition fidelity

The reviewer SHALL check that the resolved prompt includes the source manifest's required contracts and required run inputs.

The reviewer SHALL check that the resolved prompt does not include stale, unrelated, or extra contracts that change the governed task.

The reviewer SHALL check that contract requirements are not dropped, weakened, contradicted, or hidden by resolver glue.

The reviewer SHALL check that the resolved prompt does not invent behavior outside the manifest, required contracts, and required run inputs.

#### Scenario: Reviewer checks composition fidelity

- **WHEN** a resolved prompt is reviewed
- **THEN** the reviewer verifies required manifest coverage
- **THEN** the reviewer verifies required contract and run input inclusion
- **THEN** the reviewer flags missing, stale, extra, weakened, contradicted, or invented behavior

### Requirement: Reviewer checks prompt executability

The reviewer SHALL check that the resolved prompt starts with a runnable task or query suitable for the target runner.

When the target runner is a web research tool, the reviewer SHALL check that the first non-empty line names a concrete research topic.

The reviewer SHALL check that provenance metadata, inlined contracts, resolver notes, or other context do not obscure or interrupt execution.

The reviewer SHALL check that the target runner is clear, including whether the prompt is meant for a web research model, a chat model, or an AI CLI with filesystem access.

The reviewer SHALL check that save or write-location guidance is clear when the governed output contract requires a saved artifact.

When the target runner uses uploaded prompt files or attachments, the reviewer SHALL check that launcher guidance tells the runner to read the attached file as the complete prompt.

#### Scenario: Reviewer checks target-runner fit

- **WHEN** a resolved prompt is intended for a web research tool
- **THEN** the reviewer verifies that the prompt begins with a clear research topic
- **THEN** the reviewer verifies that context and metadata do not prevent the runner from recognizing the task
- **THEN** the reviewer verifies that output save guidance is clear

#### Scenario: Reviewer checks attachment launcher guidance

- **WHEN** a resolved prompt is intended to be uploaded as a file to a web research tool
- **THEN** the reviewer verifies that launcher guidance tells the tool to read the attached file as the complete prompt

### Requirement: Reviewer checks output contract executability

The reviewer SHALL check that required output metadata, tables, columns, headings, allowed values, and save paths are executable by the target runner.

The reviewer SHALL check that output instructions preserve the governing observe contract and do not introduce extra columns, sections, citation formats, or summaries outside the contract.

The reviewer SHALL check that formatting instructions do not conflict with the output contract.

#### Scenario: Reviewer checks output contract

- **WHEN** a resolved prompt includes an observe output contract
- **THEN** the reviewer verifies that the required output structure is clear and executable
- **THEN** the reviewer flags extra or conflicting output instructions

### Requirement: Reviewer checks ambiguity and conflict

The reviewer SHALL check for ambiguous wording, conflicting requirements, unclear ordering, or conflicting responsibilities across composed contracts.

The reviewer SHALL check whether uncertainty handling, boundary decisions, or tie-breaks are clear enough for the target runner to apply.

#### Scenario: Reviewer finds ambiguity

- **WHEN** composed contracts leave the target runner with unclear or conflicting instructions
- **THEN** the reviewer identifies the ambiguity or conflict
- **THEN** the reviewer explains why it could affect the research output

### Requirement: Reviewer reports findings in a standard shape

Prompt review output SHALL include:

- a `pass` or `fail` faithfulness judgment
- the reviewed resolved prompt path
- the reviewer agent
- concise findings, or `No findings`
- OpenSpec proposal intent for each finding that requires a repository change

OpenSpec proposal intent SHALL include a suggested change name, affected capabilities, why the change is needed, and what should change.

The reviewer MAY include additional advisory notes when they do not require repository changes.

#### Scenario: Review passes

- **WHEN** the reviewer finds no required changes
- **THEN** the review reports `pass`
- **THEN** the review reports `No findings`

#### Scenario: Review finds required repository change

- **WHEN** the reviewer finds that a resolved prompt is not faithful, executable, or clear enough because of repository-governed wording
- **THEN** the review reports `fail`
- **THEN** the review includes OpenSpec proposal intent for the required fix
