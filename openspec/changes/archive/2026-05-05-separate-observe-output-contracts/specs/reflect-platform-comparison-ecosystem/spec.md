## MODIFIED Requirements

### Requirement: Platform comparison ecosystem contains structured comparison outputs

The repository SHALL contain `reflect/platform-comparison-ecosystem.csv` and `reflect/platform-comparison-ecosystem-map.html` as structured platform comparison reflection outputs.

The CSV output SHALL use exactly this header:

`Name,Link,Arch,Open,City,Mature,Integ,Gov,Viz,DM,Sim,IoT,Std,Infra,Model,Date`

CSV rows SHALL be extracted from qualifying `observe/platform-comparison-*.md` files whose YAML metadata contains `prompt: platform-comparison`.

CSV rows SHALL be ordered by `Date`, then `Model`, then `Name`, then `Link`.

The HTML output SHALL be self-contained, visualize the same row set as the CSV, provide model filtering, provide a readable comparison table, and include at least one visual summary of score dimensions.

#### Scenario: Researcher opens reflect/

- **WHEN** a researcher opens `reflect/`
- **THEN** platform comparison ecosystem outputs are available as direct files
- **THEN** the CSV and HTML outputs follow the governed comparison export contract
