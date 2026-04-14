## MODIFIED Requirements

### Requirement: Prompt extracts Part 1 scoring table rows from comparison responses

For comparison responses, the prompt SHALL instruct the model to locate the Part 1 scoring table and extract every data row (excluding the header row).

Each extracted row SHALL be output as a CSV row with `Phase` set to `comparison`.

The `Relevance` column SHALL be extracted from the Part 1 table and included in each output row.

#### Scenario: Response contains a Part 1 table

- **WHEN** a qualifying comparison response file contains a Part 1 scoring table with platform rows
- **THEN** the model extracts all data rows from that table with Phase=`comparison`, including the `Relevance` value

#### Scenario: Part 1 table is missing from a qualifying comparison file

- **WHEN** a qualifying comparison response file does not contain a Part 1 scoring table
- **THEN** the model skips that file and notes the omission in its preamble output

#### Scenario: Comparison Relevance differs from discovery Relevance

- **WHEN** a platform appears in both a discovery row and a comparison row in the inventory
- **THEN** the two rows may carry different Relevance values, reflecting the first-pass survey vs. deep-research assessment
