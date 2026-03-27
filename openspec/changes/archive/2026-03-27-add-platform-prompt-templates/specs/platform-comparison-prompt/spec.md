## ADDED Requirements

### Requirement: Platform comparison prompt file exists
The repository SHALL contain a file at `prompts/platform-comparison.md` that provides a self-contained prompt template for AI-assisted side-by-side comparison of two or more UDT platforms.

#### Scenario: File is present and non-empty
- **WHEN** a researcher navigates to `prompts/platform-comparison.md`
- **THEN** the file exists and contains a complete, copy-pasteable prompt

### Requirement: Comparison prompt uses parameterized platform name tokens
The prompt template SHALL include `[PLATFORM_A]` and `[PLATFORM_B]` placeholder tokens (and optionally more) that the researcher replaces with the names of the platforms to compare.

#### Scenario: Researcher customizes platforms to compare
- **WHEN** a researcher replaces `[PLATFORM_A]` with "DTCC" and `[PLATFORM_B]` with "Cesium"
- **THEN** the model produces a comparison specifically for those two platforms

### Requirement: Comparison prompt covers the six research dimensions
The prompt template SHALL instruct the model to compare platforms across all six dimensions used in this research: technical architecture, openness and licensing, city-scale capability, platform maturity, integration posture, and governance model.

#### Scenario: Response covers all dimensions
- **WHEN** an AI responds to the comparison prompt
- **THEN** the response addresses each of the six dimensions for every platform being compared

### Requirement: Comparison prompt requests a structured table output
The prompt template SHALL instruct the model to include a summary comparison table with one row per platform and one column per dimension, in addition to any prose analysis.

#### Scenario: Researcher extracts summary data
- **WHEN** an AI responds to the comparison prompt
- **THEN** the response includes a Markdown table suitable for direct inclusion in research notes or docs

### Requirement: Comparison prompt instructs use of primary sources
The prompt template SHALL instruct the model to base its comparison on primary sources (official documentation, repositories, published papers) and to cite sources for each claim.

#### Scenario: Response includes source citations
- **WHEN** an AI responds to the comparison prompt
- **THEN** each substantive claim is accompanied by a source reference or URL
