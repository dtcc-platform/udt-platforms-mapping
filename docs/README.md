# Public Pages

`docs/` contains static publication output generated with Pandoc.

Jekyll is not required. The committed HTML files can be opened directly in a browser or served by any static file host.

## Files

- `index.html` is the local/public entry page.
- `observations/` contains published HTML pages generated from direct Markdown artifacts in `observe/`.
- `reflections/` contains published HTML pages generated from direct Markdown artifacts in `reflect/`.
- `assets/site.css` contains shared page and table styling.

## Update Workflow

Maintain the source Markdown in the research phase folders, then regenerate public HTML with:

```bash
scripts/publish.sh
```

The publish command converts eligible direct Markdown files as follows:

- `observe/<name>.md` -> `docs/observations/<name>.html`
- `reflect/<name>.md` -> `docs/reflections/<name>.html`

Phase-local `README.md` files are not published as research artifact pages.

When publishing from this repository without a hosting service, open `docs/index.html` directly.
