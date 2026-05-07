# Proposal: make act prompts contract manifests

## Summary

Refactor governed `act/` prompt files into contract manifests.

Each governed `act/*.md` file should explain which specs and run inputs affect the prompt, with short purpose comments, while avoiding duplicated behavior. The only behavior allowed directly in the manifest is resolver or execution glue, such as how to inline contracts, where to save results, or how to invoke a CLI-capable model.

## Motivation

The current prompt files repeat behavior that already belongs in specs:

- research scope
- evidence handling
- output shape
- Markdown formatting
- filesystem scanning behavior
- report/export rules

This makes the repository harder to reason about because a reviewer has to compare the prompt implementation against the specs and decide which wording is authoritative.

The desired model is simpler:

- specs define behavior and output contracts
- `act/` files declare the relevant contracts and inputs
- prompt resolution inlines the contracts
- the prompt body gives only a minimal task invocation

## Scope

In scope:

- add a repo-wide `repo-act-prompt-manifest` spec
- update existing governed act prompt specs to require manifest-style prompt files
- apply the manifest rule to all current governed prompt files under `act/`
- preserve short comments explaining each required contract's purpose
- allow resolver/execution instructions in the manifest

Out of scope:

- changing the semantics of platform discovery, initiative discovery, comparison, benchmark, or report workflows
- changing observe or reflect output contracts
- changing untracked research case-study files
- adding a dedicated resolver command

## Expected Result

Researchers see `act/` as the action menu and manifest layer:

```text
act/discover-platforms.md
  lists required specs and explains why each matters
  tells the resolver to inline them
  gives a short task invocation
```

The resolved prompt, not the manifest file alone, contains the executable behavior.
