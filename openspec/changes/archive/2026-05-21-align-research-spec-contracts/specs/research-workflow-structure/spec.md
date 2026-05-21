## ADDED Requirements

### Requirement: Prompt interpretation review checks prompt fidelity against governing specs

The prompt interpretation review workflow SHALL ask a reviewing agent to compare a generated or updated prompt against its governing OpenSpec spec.

The review SHALL answer whether the prompt is a faithful interpretation of the spec and whether the spec or prompt can be made clearer.

#### Scenario: Reviewer checks a generated prompt

- **WHEN** an agent generates a prompt from a governing spec
- **THEN** a reviewing agent compares the prompt against that spec
- **THEN** the reviewer identifies any mismatch, ambiguity, or improvement opportunity

### Requirement: Accepted prompt-review improvements become OpenSpec deltas

Any accepted improvement from prompt interpretation review SHALL be captured as an OpenSpec delta before changing the baseline prompt or baseline spec.

Review comments SHALL NOT be stored as standalone calibration artifacts.

#### Scenario: Reviewer finds an ambiguity

- **WHEN** a reviewer finds that a prompt interpretation exposes an ambiguous spec requirement
- **THEN** the ambiguity is resolved through a scoped OpenSpec delta
- **THEN** the prompt is regenerated or updated from the improved contract

### Requirement: Prompt interpretation review is sequential

The workflow SHALL allow later reviewing agents to see the current accepted change state, including earlier accepted deltas from previous reviewers.

The workflow SHALL NOT require isolated calibration branches or blind independent proposals.

#### Scenario: Gemini reviews after Claude

- **WHEN** Codex generates a prompt and Claude review produces an accepted OpenSpec delta
- **THEN** Gemini reviews the prompt against the updated current spec/change state
- **THEN** Gemini may propose another OpenSpec delta if it finds a further improvement
