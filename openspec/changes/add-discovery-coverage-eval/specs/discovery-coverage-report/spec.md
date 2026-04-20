## ADDED Requirements

### Requirement: Coverage report is structured in two parts: per-gap-category table and summary

The coverage report saved to `tests/reports/YYYY-MM-DD-coverage.md` SHALL contain:

1. A header block with: report date, fixture file path, number of response files tested
2. One section per gap category from the fixture, each containing a pipe table with columns: `Platform`, `Expected Layer`, and one column per model (using the model name from the response YAML metadata). Each cell SHALL contain `✓ found`, `✗ missing`, or `✓ found (Layer: <actual>)` when the Layer in the response differs from the expected Layer
3. A summary section with a pipe table: `Model`, `Found`, `Missing`, `Wrong layer` — one row per model

The report SHALL be a valid Markdown file readable in any standard viewer.

#### Scenario: Researcher reads the per-gap-category section

- **WHEN** a researcher opens a coverage report
- **THEN** they can see, for each gap category and each model, which expected platforms were found and which were missing — enabling targeted prompt improvement per gap type

#### Scenario: All models miss the same platform

- **WHEN** a platform appears as `✗ missing` in every model column
- **THEN** the summary row for each model reflects one additional missing count — making systematic gaps immediately visible

#### Scenario: A model finds a platform but assigns the wrong Layer

- **WHEN** a model's response includes a platform from the fixture but with a different Layer than expected
- **THEN** the report cell shows `✓ found (Layer: <actual>)` and the summary counts it as found but also increments the wrong-layer count

### Requirement: Report filename includes the date and does not overwrite previous reports

The report SHALL be saved as `tests/reports/YYYY-MM-DD-coverage.md` using the date the eval was run. If a report for that date already exists, the eval prompt SHALL append a suffix (e.g., `-2`) rather than overwriting.

#### Scenario: Researcher runs eval twice on the same day

- **WHEN** a researcher runs the eval prompt twice on the same calendar date
- **THEN** the second run produces `YYYY-MM-DD-coverage-2.md` and the first report is preserved
