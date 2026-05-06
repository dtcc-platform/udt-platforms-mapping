## MODIFIED Requirements

### Requirement: plan/ holds research definitions and run inputs

`plan/` SHALL contain researcher-facing run inputs used by governed prompts.

`plan/` SHALL NOT be the canonical home for stable behavior definitions, source policies, scoring rubrics, output contracts, or prompt behavior contracts.

Stable behavior definitions, source policies, and scoring rubrics SHALL be governed in `openspec/specs/`.

`plan/platform-comparison-set.md` SHALL contain the selected platform comparison set.
`plan/platform-discovery-benchmark.md` SHALL contain the platform discovery benchmark fixture.

Additional `plan/` files MAY contain run-specific scope notes, seed inputs, selected candidates, or temporary input material used by canonical prompts.

#### Scenario: Researcher starts from planning inputs

- **WHEN** a researcher opens `plan/`
- **THEN** they see run inputs as direct files
- **THEN** stable behavior definitions, policies, and rubrics are not treated as canonical plan artifacts
- **THEN** no canonical planning input uses the old `udt-` thread-prefixed filename pattern
