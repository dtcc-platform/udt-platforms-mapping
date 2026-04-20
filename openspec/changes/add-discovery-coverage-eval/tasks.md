## 1. Create tests/ directory structure

- [ ] 1.1 Create `tests/reports/.gitkeep` so the reports directory is tracked in version control

## 2. Create tests/discovery-fixtures.md

- [ ] 2.1 Create `tests/discovery-fixtures.md` with a file header explaining its purpose and how to add entries
- [ ] 2.2 Add first gap category: `## Gap: No digital-twin framing — urban resilience & climate risk` with explanatory prose
- [ ] 2.3 Add GeoDatalytics as the first fixture entry (Name, Link, Expected Layer: domain-module, Why tricky)

## 3. Create tests/eval-discovery.md

- [ ] 3.1 Create `tests/eval-discovery.md` as a Claude Code CLI prompt
- [ ] 3.2 Prompt instructs: read `tests/discovery-fixtures.md`, extract expected platforms and gap categories
- [ ] 3.3 Prompt instructs: glob `responses/global-platforms-discovery-*.md`, extract model name from YAML metadata
- [ ] 3.4 Prompt instructs: for each expected platform, check case-insensitive name match in each response's summary table
- [ ] 3.5 Prompt instructs: note Layer mismatch when found platform has a different Layer than expected
- [ ] 3.6 Prompt instructs: write report to `tests/reports/YYYY-MM-DD-coverage.md`, append `-2` suffix if file already exists

## 4. Verify

- [ ] 4.1 Run the eval prompt against the three existing discovery responses and confirm a report is written to `tests/reports/`
- [ ] 4.2 Confirm GeoDatalytics shows as `✗ missing` for all three models in the report
- [ ] 4.3 Confirm the summary table lists correct found/missing counts per model
