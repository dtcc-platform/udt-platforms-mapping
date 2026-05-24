## MODIFIED Requirements

### Requirement: Canonical web prompts include resolver instructions

Canonical web prompt templates that conform to this contract SHALL include resolver instructions before the prompt body.

The resolver instructions SHALL tell the resolver to inline each required contract and run input under a heading naming the source file or spec.

The resolver instructions SHALL tell the resolver to append the prompt body after the resolved context.

The resolver instructions SHALL tell the resolver to output one copy-ready block with no wrapper text or narration.

When a resolved prompt artifact is saved for review or reuse, the resolver instructions SHALL tell the resolver to save it using the governed `act/<action>-resolved-<resolver-short>.md` convention.

#### Scenario: Researcher resolves a web prompt

- **WHEN** a researcher resolves a conforming canonical web prompt
- **THEN** the result is one copy-ready prompt block
- **THEN** required contracts and inputs are inlined before the prompt body

#### Scenario: Researcher saves a resolved web prompt

- **WHEN** a researcher resolves a web prompt for review or reuse
- **THEN** the resolved prompt is saved under `act/` using the governed resolved-prompt naming convention
