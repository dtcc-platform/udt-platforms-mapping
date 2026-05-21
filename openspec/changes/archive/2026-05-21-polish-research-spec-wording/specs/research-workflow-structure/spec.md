## MODIFIED Requirements

### Requirement: Prompt interpretation review checks prompt fidelity against governing specs

The prompt interpretation review workflow SHALL ask a reviewing agent to compare a generated or updated prompt against its governing OpenSpec spec.

The review SHALL answer whether the prompt is a faithful interpretation of the spec and whether the spec or prompt can be made clearer.

#### Scenario: Reviewer checks a generated prompt

- **WHEN** an agent generates a prompt from a governing spec
- **THEN** a reviewing agent compares the prompt against that spec
- **THEN** the reviewer identifies any mismatch, ambiguity, or improvement opportunity

### Requirement: Prompt interpretation review is sequential

The workflow SHALL allow later reviewing agents to see the current accepted change state, including earlier accepted deltas from previous reviewers.

The workflow SHALL NOT require isolated calibration branches or blind independent proposals.

#### Scenario: Later reviewer follows accepted deltas

- **WHEN** one agent generates a prompt and an earlier review produces an accepted OpenSpec delta
- **THEN** a later reviewing agent reviews the prompt against the updated current spec/change state
- **THEN** the later reviewing agent may propose another OpenSpec delta if it finds a further improvement
