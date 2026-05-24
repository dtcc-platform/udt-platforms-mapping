## MODIFIED Requirements

### Requirement: Review agents compare resolved prompts against governing contracts

Each prompt review SHALL compare the saved resolved prompt snapshot against its source manifest, required OpenSpec contracts, and required run inputs.

Each review SHALL be performed by an agent different from the agent that resolved the prompt snapshot.

Each review SHALL apply the `research-prompt-review-checklist` contract.

Each review SHALL produce a pass/fail faithfulness judgment and actionable findings in stdout/chat by default.

Prompt reviewers SHALL NOT rewrite the governed prompt freely; they SHALL identify contract interpretation issues and propose OpenSpec changes when repository changes are required.

#### Scenario: Different reviewer checks a resolved prompt

- **WHEN** Codex resolves `act/entity-discovery-resolved-codex.md`
- **THEN** a different reviewer agent reviews the resolved prompt against `act/entity-discovery.md` and the listed contracts and inputs
- **THEN** the reviewer applies `research-prompt-review-checklist`
- **THEN** the review identifies issues using the checklist criteria
- **THEN** the review produces a pass/fail judgment and findings in stdout/chat
- **THEN** the review does not treat itself as a replacement prompt
