## MODIFIED Requirements

### Requirement: plan/ holds research run inputs

`plan/` SHALL contain researcher-facing run inputs used by governed prompts.

`plan/` SHALL NOT be the canonical home for stable behavior definitions, source policies, scoring rubrics, output contracts, or prompt behavior contracts.

Stable behavior definitions, source policies, and scoring rubrics SHALL be governed in `openspec/specs/`.

`openspec/specs/plan-entity-definition/spec.md` SHALL be the canonical definition contract for UDT entities, including technical artifacts, initiatives, exclusions, and initiative-to-artifact substrate interpretation.

`plan/platform-comparison-set.md` SHALL contain the selected platform comparison set.
`plan/platform-discovery-benchmark.md` SHALL contain the platform discovery benchmark fixture.

Additional `plan/` files MAY contain run-specific scope notes, seed inputs, selected candidates, or temporary input material used by canonical prompts.

#### Scenario: Researcher starts from planning inputs

- **WHEN** a researcher opens `plan/`
- **THEN** they see run inputs as direct files
- **THEN** stable behavior definitions, policies, and rubrics are not treated as canonical plan artifacts
- **THEN** the researcher can identify `openspec/specs/plan-entity-definition/spec.md` as the canonical UDT entity definition contract
