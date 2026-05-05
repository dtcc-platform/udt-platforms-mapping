# Rename Specs By Effect Scope

## Why

The active spec names mix phase-scoped names with repository-wide and workflow names. Phase specs such as `act-udt-platforms-prompt` and `reflect-udt-platforms-benchmarking` already communicate where they take effect, but repo-wide specs such as `repository-structure`, `prompt-markdown-format`, and `prompt-interpretation-review` do not share the same first-token convention.

Renaming repo-wide specs to `repo-*` makes the spec list easier to scan and makes the naming rule explicit: the first token indicates effect scope.

## What Changes

- Rename `repository-structure` to `repo-structure`.
- Rename `workflow-naming-conventions` to `repo-naming-conventions`.
- Rename `prompt-markdown-format` to `repo-prompt-markdown-format`.
- Rename `prompt-interpretation-review` to `repo-prompt-review`.
- Update README links and spec headings.

## Impact

- Active spec paths become more consistent.
- Existing phase/thread spec names remain unchanged.
- Archived OpenSpec history remains unchanged except for this rename change.
