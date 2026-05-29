## 1. Publication Script

- [x] 1.1 Create `scripts/publish.sh` as the canonical publication command.
- [x] 1.2 Convert eligible direct `observe/*.md` and `reflect/*.md` files to matching `docs/observations/*.html` and `docs/reflections/*.html` files with Pandoc.
- [x] 1.3 Generate `docs/index.md` and `docs/index.html` with `Observations` and `Reflections` sections.
- [x] 1.4 Fail clearly when `pandoc` is missing.

## 2. Documentation Output

- [x] 2.1 Run the publication script to refresh `docs/` output.
- [x] 2.2 Update `docs/README.md` with the publication command and source-to-output mapping.

## 3. Validation

- [x] 3.1 Validate the OpenSpec change with `openspec validate publish-observe-reflect-docs --strict`.
- [x] 3.2 Verify generated `docs/index.html` links include observation and reflection groups.
