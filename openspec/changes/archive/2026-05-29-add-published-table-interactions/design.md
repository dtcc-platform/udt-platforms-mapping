## Context

Published HTML pages are generated from direct Markdown files in `observe/` and `reflect/` by `scripts/publish.sh`. The pages already share `docs/assets/site.css`; they do not currently share JavaScript behavior.

## Goals / Non-Goals

**Goals:**

- Enhance Pandoc-generated tables on published artifact pages with filtering and sorting.
- Keep the enhancement in shared assets so regenerated pages retain the behavior.
- Avoid external dependencies.
- Preserve readable static tables when JavaScript is unavailable.

**Non-Goals:**

- Change source Markdown artifacts.
- Add server-side search, pagination, or persistent state.
- Support complex typed sorting beyond pragmatic text and numeric comparisons.

## Decisions

- Add `docs/assets/site.js` and load it from publication pages with a small Pandoc `--include-after-body` HTML include.
- Enhance tables after `DOMContentLoaded` by inserting a filter input before each table and making header cells button-like sort controls.
- Treat sorting as progressive enhancement: original table order remains the initial state, and no table content is rewritten before user interaction.
- Keep the index page on shared CSS only because it is navigation-oriented and does not need table interaction behavior.

## Risks / Trade-offs

- Very large tables may still be slower than a dedicated table library. Mitigation: keep the implementation simple and dependency-free for current static research tables.
- Pandoc output can vary by Markdown table shape. Mitigation: only enhance tables with header cells and body rows; leave other tables untouched.
