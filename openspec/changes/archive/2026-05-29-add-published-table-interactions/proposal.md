## Why

Published observation and reflection pages can contain large Pandoc-generated tables that are hard to inspect as static HTML. Adding shared table sorting and filtering makes those pages easier to browse without changing the source Markdown artifacts.

## What Changes

- Add client-side table filtering for published documentation pages.
- Add client-side column sorting for published documentation tables.
- Load the shared JavaScript from generated publication pages through the Pandoc workflow.
- Keep the enhancement dependency-free and shared through `docs/assets/`.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `research-workflow-structure`: published documentation pages generated from research artifacts support shared table interactions.

## Impact

- Adds `docs/assets/site.js`.
- Updates `scripts/publish.sh` to include the shared JavaScript in generated pages.
- Updates `docs/assets/site.css` for interaction controls and sortable headers.
- Regenerates published pages under `docs/`.
