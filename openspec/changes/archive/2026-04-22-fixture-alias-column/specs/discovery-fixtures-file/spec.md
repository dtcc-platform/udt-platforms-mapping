## MODIFIED Requirements

### Requirement: tests/discovery-fixtures.md exists and groups expected platforms by gap category

The repository SHALL contain a file at `tests/discovery-fixtures.md`. This file is the canonical recall benchmark for discovery sessions — it lists platforms that are expected to appear in discovery responses but are at risk of being missed due to specific discovery failure modes.

The file SHALL group expected platforms into named gap categories. Each gap category SHALL have:
- A `##` heading naming the gap (e.g., `## Gap: No digital-twin framing — urban resilience & climate risk`)
- One or two sentences explaining what makes platforms in this category easy to miss
- A pipe table with columns: `Name`, `Link`, `Expected Layer`, `Why tricky`, `Aliases`

The `Expected Layer` column SHALL contain one of: `core-platform`, `backbone`, `domain-module`.

The `Aliases` column SHALL contain a comma-separated list of known variant names for the platform, or be empty if no aliases are known. See the `fixture-alias-column` spec for full alias rules.

The file SHALL NOT define scoring rubrics, discovery instructions, or Layer criteria — those belong in `docs/01-discovery-scope.md`.

The file SHALL be maintained by researchers: new entries are added when a known platform is found to be missing from a discovery response; new gap categories are added when a new class of discovery failure is identified; aliases are added when a model uses a variant name that caused a false negative.

#### Scenario: Researcher adds a newly discovered missed platform

- **WHEN** a researcher notices that a known in-scope platform did not appear in any model's discovery response
- **THEN** they add a row to the appropriate gap category in `tests/discovery-fixtures.md`, or create a new gap category if none fits

#### Scenario: Eval prompt reads the fixture

- **WHEN** the eval prompt runs
- **THEN** it reads `tests/discovery-fixtures.md` and extracts all expected platforms with their gap category, expected Layer, and Aliases

#### Scenario: Researcher consults the fixture to understand coverage gaps

- **WHEN** a researcher reads `tests/discovery-fixtures.md`
- **THEN** they can see, by gap category, which platforms are known to be systematically missed and why
