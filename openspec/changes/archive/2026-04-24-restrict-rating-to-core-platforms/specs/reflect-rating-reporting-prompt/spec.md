## MODIFIED Requirements

### Requirement: Rating reporting prompt generates CSV and HTML outputs

The prompt SHALL instruct the model to extract the Part 1 scoring table from qualifying rating responses using a layer-free schema:
- `Name`
- `Link`
- `Arch`
- `Open`
- `City`
- `Mature`
- `Integ`
- `Gov`
- `Viz`
- `DM`
- `Sim`
- `IoT`
- `Std`
- `Infra`

The generated CSV SHALL append `Model` and `Date` after those columns.

#### Scenario: Researcher completes rating reporting

- **WHEN** the model finishes the rating reporting prompt
- **THEN** it writes `ecosystem.csv` and `ecosystem-map.html` under `reflect/rating/reporting/` using the layer-free Part 1 schema
