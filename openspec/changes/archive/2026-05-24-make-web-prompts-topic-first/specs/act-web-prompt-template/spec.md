## MODIFIED Requirements

### Requirement: Canonical web prompts include resolver instructions

Canonical web prompt templates that conform to this contract SHALL include resolver instructions before the prompt body.

The resolver instructions SHALL tell the resolver to inline each required contract and run input under a heading naming the source file or spec.

The resolver instructions SHALL tell the resolver to append the prompt body and resolved context in runner-first order for saved resolved prompt artifacts.

The resolver instructions SHALL tell the resolver to output one copy-ready block with no wrapper text or narration.

When a resolved prompt artifact is saved for review or reuse, the resolver instructions SHALL tell the resolver to save it using the governed `act/<action>-resolved-<resolver-short>.md` convention.

Saved resolved web prompt artifacts SHALL start with a plain `Research topic:` line before headings, role text, provenance metadata, or inlined contracts.

The `Research topic:` line SHALL name the concrete research subject and action for the target web runner.

#### Scenario: Researcher resolves a web prompt

- **WHEN** a researcher resolves a conforming canonical web prompt
- **THEN** the result is one copy-ready prompt block
- **THEN** the first non-empty line is a plain `Research topic:` line
- **THEN** the executable research query appears before provenance metadata and inlined contracts
- **THEN** required contracts and inputs are inlined after the top-level query and provenance metadata

#### Scenario: Researcher saves a resolved web prompt

- **WHEN** a researcher resolves a web prompt for review or reuse
- **THEN** the resolved prompt is saved under `act/` using the governed resolved-prompt naming convention
- **THEN** the saved resolved prompt starts with a concrete research topic

### Requirement: Canonical web prompts include execution and save guidance

Canonical web prompt templates that conform to this contract SHALL include guidance for web model execution.

The prompt SHALL tell the researcher where to save the resulting web response.

The save location SHALL match the relevant observe output contract.

When a resolved prompt is provided to a web research tool as an attachment, the execution guidance SHALL include a launcher message telling the runner to read the attached file as the complete research prompt.

#### Scenario: Researcher runs a web prompt

- **WHEN** a researcher runs a conforming canonical web prompt
- **THEN** they know where to save the response

#### Scenario: Researcher uploads a resolved prompt file

- **WHEN** a researcher uploads a saved resolved prompt to a web research tool
- **THEN** the researcher uses a launcher message telling the tool to read the attached file as the complete prompt
- **THEN** the web research tool has an explicit chat query even when the prompt is supplied as an attachment
