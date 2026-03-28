## ADDED Requirements

### Requirement: Discovery prompt response ends with a required summary table
The prompt template SHALL instruct the model to append a summary table after all per-platform sections. The table is required, not optional, and SHALL use the following columns: **Name**, **Organization**, **License**, **Type**, **Maturity**, **Inclusion Criterion**, **Select**.

The **Select** column SHALL be left empty in the model's response. The researcher fills it in manually by placing `x` in rows they want to use as comparison targets.

#### Scenario: Researcher saves a discovery response and wants to start a comparison
- **WHEN** a researcher opens a saved discovery response
- **THEN** the file ends with a summary table containing all discovered platforms and an empty Select column ready to be marked

#### Scenario: Researcher marks platforms for comparison
- **WHEN** a researcher places `x` in the Select column for two or more rows
- **THEN** those marked rows can be copied and pasted directly into the comparison prompt as the scope input
