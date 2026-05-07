## 1. Cross Spec

- [x] 1.1 Add `repo-web-prompt-template` baseline spec.
- [x] 1.2 Define required contracts and required run inputs sections.
- [x] 1.3 Define resolver instructions for copy-ready web prompts.
- [x] 1.4 Define explicit output-contract rendering, including metadata blocks.
- [x] 1.5 Define paste/save guidance.
- [x] 1.6 Reuse `repo-prompt-markdown-format` for shared Markdown rules.

## 2. Prompt Specs

- [x] 2.1 Update `act-discover-platforms-prompt` to conform to `repo-web-prompt-template`.
- [x] 2.2 Update `act-discover-initiatives-prompt` to conform to `repo-web-prompt-template`.
- [x] 2.3 Update `act-compare-platforms-prompt` to conform to `repo-web-prompt-template`.
- [x] 2.4 Do not update benchmark or report prompt specs.

## 3. Prompt Files

- [x] 3.1 Update `act/discover-platforms.md` to satisfy the shared web prompt template and render its metadata block.
- [x] 3.2 Update `act/discover-initiatives.md` to satisfy the shared web prompt template and render its metadata block.
- [x] 3.3 Update `act/compare-platforms.md` to satisfy the shared web prompt template and render its metadata block.
- [x] 3.4 Leave benchmark and report prompt files unchanged.

## 4. Validation

- [x] 4.1 Run `openspec validate add-web-prompt-template-contract --strict`.
- [x] 4.2 Run `openspec validate --all --strict`.
