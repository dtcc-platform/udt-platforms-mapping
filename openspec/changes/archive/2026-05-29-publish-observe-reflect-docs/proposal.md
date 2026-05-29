## Why

The repository has saved observation and reflection Markdown artifacts that should be easy to browse from GitHub Pages or any static file host. A repeatable publication workflow is needed so `observe/` and `reflect/` artifacts can be converted to HTML and linked from a single public home page.

## What Changes

- Add a publication workflow that converts every Markdown file directly under `observe/` and `reflect/` into matching HTML files under `docs/`.
- Update the public `docs/index.html` home page so it groups generated links into `Observations` and `Reflections`.
- Add `scripts/publish.sh` as the repository command for running Pandoc publication.
- Keep source research artifacts in `observe/` and `reflect/`; `docs/` remains the static publication output.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `research-workflow-structure`: clarifies that `docs/` is static publication output for phase artifacts, that published observation and reflection pages are grouped under category folders `docs/observations/` and `docs/reflections/`, and that `scripts/` may contain operational automation without becoming a research phase folder.

## Impact

- Adds a `scripts/` directory with `publish.sh`.
- Updates `docs/index.html` and generated HTML pages under `docs/observations/` and `docs/reflections/`.
- Requires `pandoc` to be installed for publication.
