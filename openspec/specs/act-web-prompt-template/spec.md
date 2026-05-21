# Spec: act-web-prompt-template

## Purpose

Defines the shared structure for canonical web prompt templates.

## Requirements

### Requirement: Canonical web prompts declare contracts and run inputs separately

Canonical web prompt templates that conform to this contract SHALL distinguish required behavior/output contracts from required run inputs.

The prompt SHALL conform to `act-prompt-manifest`.

The prompt SHALL use a `## Required Contracts` section when it depends on OpenSpec behavior or output contracts.

The prompt SHALL use a `## Required Run Inputs` section when it depends on `plan/` files or other run-specific input artifacts.

#### Scenario: Researcher opens a canonical web prompt

- **WHEN** a researcher opens a conforming canonical web prompt
- **THEN** required OpenSpec contracts are distinguishable from run inputs
- **THEN** the prompt follows the repository act prompt manifest contract

### Requirement: Canonical web prompts include resolver instructions

Canonical web prompt templates that conform to this contract SHALL include resolver instructions before the prompt body.

The resolver instructions SHALL tell the resolver to inline each required contract and run input under a heading naming the source file or spec.

The resolver instructions SHALL tell the resolver to append the prompt body after the resolved context.

The resolver instructions SHALL tell the resolver to output one copy-ready block with no wrapper text or narration.

#### Scenario: Researcher resolves a web prompt

- **WHEN** a researcher resolves a conforming canonical web prompt
- **THEN** the result is one copy-ready prompt block
- **THEN** required contracts and inputs are inlined before the prompt body

### Requirement: Canonical web prompts render output contracts explicitly

Canonical web prompt templates that conform to this contract SHALL render the relevant observe output contract into executable model instructions.

When an observe output contract requires a metadata block, the prompt SHALL explicitly include that metadata block in the output format.

The prompt SHALL preserve the output contract's required tables, columns, section structure, and allowed values.

#### Scenario: Model follows a web prompt

- **WHEN** a model follows a conforming canonical web prompt
- **THEN** the model sees the required output metadata, tables, sections, and allowed values

### Requirement: Canonical web prompts include execution and save guidance

Canonical web prompt templates that conform to this contract SHALL include guidance for web model execution.

The prompt SHALL tell the researcher where to save the resulting web response.

The save location SHALL match the relevant observe output contract.

#### Scenario: Researcher runs a web prompt

- **WHEN** a researcher runs a conforming canonical web prompt
- **THEN** they know where to save the response

### Requirement: Canonical web prompts reuse shared Markdown formatting

Canonical web prompt templates that conform to this contract and ask models to emit Markdown SHALL require `repo-prompt-markdown-format` as an inlined required contract.

The prompt SHALL list `openspec/specs/repo-prompt-markdown-format/spec.md` under `## Required Contracts`.

The web prompt template contract SHALL NOT require each prompt template to duplicate the full shared Markdown formatting rules in the prompt body.

#### Scenario: Prompt emits Markdown

- **WHEN** a conforming canonical web prompt asks a model to emit Markdown
- **THEN** it lists `repo-prompt-markdown-format` as a required contract
- **THEN** the resolver inlines the shared Markdown formatting contract before the prompt body
- **THEN** the prompt body can reference the inlined Markdown formatting contract instead of duplicating it
