# Proposal: inline Markdown formatting contract in web prompts

## Summary

Make `repo-prompt-markdown-format` an explicit required contract for canonical web prompts that emit Markdown.

This removes duplicated Markdown rule blocks from live prompt templates and makes the resolved web prompt carry the shared formatting contract through normal contract inlining.

## Motivation

The current prompt templates conform to `repo-prompt-markdown-format`, but they do so by copying Markdown rules into each `act/*.md` file. That makes the shared spec a governance check rather than a contract that is actually present in the resolved prompt.

Researchers should be able to understand the pattern simply:

- prompt templates list all required contracts
- the resolver inlines those contracts
- the web model receives the same shared Markdown rules through the resolved prompt

## Scope

In scope:

- update `repo-web-prompt-template` so Markdown-emitting web prompts require `repo-prompt-markdown-format`
- update `repo-prompt-markdown-format` so it contains model-facing formatting rules suitable for inlining
- update platform discovery, initiative discovery, and platform comparison prompt specs
- update `act/discover-platforms.md`, `act/discover-initiatives.md`, and `act/compare-platforms.md`

Out of scope:

- benchmark prompts
- report prompts
- changing observe output contracts
- adding a standalone prompt resolver command
