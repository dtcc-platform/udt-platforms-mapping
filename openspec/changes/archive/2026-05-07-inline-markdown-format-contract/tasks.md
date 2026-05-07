## 1. Specs

- [x] 1.1 Update `repo-web-prompt-template` to require `repo-prompt-markdown-format` as an inlined required contract for Markdown-emitting web prompts.
- [x] 1.2 Update `repo-prompt-markdown-format` with model-facing formatting rules suitable for inlining.
- [x] 1.3 Update `act-discover-platforms-prompt` to require the Markdown format contract.
- [x] 1.4 Update `act-discover-initiatives-prompt` to require the Markdown format contract.
- [x] 1.5 Update `act-compare-platforms-prompt` to require the Markdown format contract.

## 2. Prompt Templates

- [x] 2.1 Add `repo-prompt-markdown-format` to `act/discover-platforms.md` required contracts.
- [x] 2.2 Add `repo-prompt-markdown-format` to `act/discover-initiatives.md` required contracts.
- [x] 2.3 Add `repo-prompt-markdown-format` to `act/compare-platforms.md` required contracts.
- [x] 2.4 Remove duplicated Markdown rule blocks from those prompt templates.
- [x] 2.5 Add concise prompt-body instructions to follow the inlined Markdown format contract.

## 3. Validation

- [x] 3.1 Run `openspec validate inline-markdown-format-contract --strict`.
- [x] 3.2 Run `openspec validate --all --strict`.
