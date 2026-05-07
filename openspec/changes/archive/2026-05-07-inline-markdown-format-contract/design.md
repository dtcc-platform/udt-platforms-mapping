# Design: inline Markdown formatting contract in web prompts

## Approach

Canonical web prompts that emit Markdown will list `openspec/specs/repo-prompt-markdown-format/spec.md` under `## Required Contracts`.

The resolver already inlines every required contract. By adding the Markdown format spec to the required contracts list, the resolved prompt gives the web model the shared formatting rules without each `act/*.md` file carrying a full duplicate `### Markdown and Formatting Rules` section.

## Contract Changes

`repo-web-prompt-template` will require Markdown-emitting web prompt templates to declare `repo-prompt-markdown-format` as a required contract.

`repo-prompt-markdown-format` will become more executable by specifying:

- portable Markdown viewers
- permitted Markdown syntax
- prohibited syntax and AI-specific artifacts
- whitespace rules
- output-contract precedence

Prompt-specific specs will require their corresponding live prompts to declare and use the Markdown contract.

## Prompt Changes

The three live web prompt templates will:

- add `openspec/specs/repo-prompt-markdown-format/spec.md` to `## Required Contracts`
- keep resolver instructions unchanged because they already inline required contracts
- replace duplicated Markdown rule blocks with a short instruction to follow the inlined Markdown contract

## Tradeoffs

Resolved prompts will include the full Markdown contract text, which is slightly longer.

The benefit is that formatting behavior is no longer manually copied across prompts and can be changed in one spec.
