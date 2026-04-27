## ADDED Requirements

### Requirement: UDT initiatives source policy file exists

The repository SHALL contain a file at `plan/udt-initiatives/source-policy.md` that governs acceptable evidence and source-priority rules for the `udt-initiatives` cycle.

#### Scenario: Researcher opens the initiatives planning inputs
- **WHEN** a researcher inspects `plan/udt-initiatives/`
- **THEN** they find a `source-policy.md` file alongside the cycle’s other canonical inputs

### Requirement: UDT initiatives source policy defines ranked evidence for initiative mapping

`plan/udt-initiatives/source-policy.md` SHALL define a ranked evidence model suited to initiatives, projects, and deployments.

It SHALL prioritize official initiative or programme pages, institutional or government documentation, official project repositories when present, peer-reviewed literature, technical reports, official organizational communications, and reputable secondary sources.

#### Scenario: Researcher evaluates a city initiative page
- **WHEN** the researcher needs evidence for a named initiative or deployment
- **THEN** the policy makes official project and institutional pages first-class evidence for that cycle

### Requirement: UDT initiatives source policy allows unknown technical substrate without inventing one

`plan/udt-initiatives/source-policy.md` SHALL allow the cycle to record an initiative even when the underlying technical artifacts are unclear, provided the initiative itself is supported by acceptable evidence.

#### Scenario: Initiative is documented but the stack is unclear
- **WHEN** an initiative is clearly documented but its `Uses` field cannot be resolved confidently
- **THEN** the policy permits the initiative to remain in-scope while recording `Uses` as `?`

### Requirement: UDT initiatives source policy defines contradiction handling

`plan/udt-initiatives/source-policy.md` SHALL define how contradictions between initiative claims are handled, including preferring higher-ranked sources and recording ambiguity when deployment details cannot be confidently resolved.

#### Scenario: A press release and programme page disagree
- **WHEN** deployment scope or participants differ between a lower-ranked communication and an official programme page
- **THEN** the policy requires the official programme source to control the canonical initiative mapping judgment
