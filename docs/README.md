# Public Pages

`docs/` contains static publication output generated with Pandoc.

Jekyll is not required. The committed HTML files can be opened directly in a browser or served by any static file host.

## Files

- `index.html` is the local/public entry page.
- `entity-discovery.html` is the published entity discovery table page.
- `assets/site.css` contains shared page and table styling.

## Update Workflow

Maintain the source Markdown manually, then regenerate HTML with Pandoc.

Example:

```bash
pandoc <source>.md \
  --standalone \
  --css assets/site.css \
  --metadata title="Entity Discovery Tables" \
  -o docs/entity-discovery.html
```

When publishing from this repository without a hosting service, open `docs/index.html` or `docs/entity-discovery.html` directly.
