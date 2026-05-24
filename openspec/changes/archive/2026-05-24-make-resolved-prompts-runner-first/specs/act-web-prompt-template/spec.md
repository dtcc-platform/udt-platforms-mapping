## MODIFIED Requirements

### Requirement: Canonical web prompts include resolver instructions

Canonical web prompt templates that conform to this contract SHALL include resolver instructions before the prompt body.

The resolver instructions SHALL tell the resolver to inline each required contract and run input under a heading naming the source file or spec.

The resolver instructions SHALL tell the resolver to append the prompt body and resolved context in runner-first order for saved resolved prompt artifacts.

The resolver instructions SHALL tell the resolver to output one copy-ready block with no wrapper text or narration.

When a resolved prompt artifact is saved for review or reuse, the resolver instructions SHALL tell the resolver to save it using the governed `act/<action>-resolved-<resolver-short>.md` convention.

Saved resolved web prompt artifacts SHALL start with the executable research query before provenance metadata or inlined contracts.

#### Scenario: Researcher resolves a web prompt

- **WHEN** a researcher resolves a conforming canonical web prompt
- **THEN** the result is one copy-ready prompt block
- **THEN** the executable research query appears before provenance metadata and inlined contracts
- **THEN** required contracts and inputs are inlined after the top-level query and provenance metadata

#### Scenario: Researcher saves a resolved web prompt

- **WHEN** a researcher resolves a web prompt for review or reuse
- **THEN** the resolved prompt is saved under `act/` using the governed resolved-prompt naming convention
- **THEN** the saved resolved prompt starts with the runnable query
