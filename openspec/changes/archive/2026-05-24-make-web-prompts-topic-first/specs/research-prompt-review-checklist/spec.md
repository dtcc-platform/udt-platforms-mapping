## MODIFIED Requirements

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
