## MODIFIED Requirements

### Requirement: Discovery prompt requests structured output aligned with inventory
The prompt template SHALL instruct the model to return one `##`-level Markdown section per platform, each containing a fixed bullet list with exactly the following labelled fields: **Organization**, **Link**, **License**, **Type**, **Maturity**, **City-scale capability**, **Integration posture**, **Inclusion criterion**, and **Notes**. This structure SHALL appear before any optional summary content.

The prompt template SHALL include a concrete example of the per-platform section so agents can reproduce the exact shape without interpreting an abstract description.

#### Scenario: Response is used to populate inventory
- **WHEN** an AI responds to the discovery prompt
- **THEN** the response contains one `##` heading per platform followed by exactly the nine labelled bullet fields, making each field directly transferable to a platform-inventory.md row

#### Scenario: Response is opened for manual review
- **WHEN** a researcher opens a saved discovery response
- **THEN** each platform is scannable as a self-contained section with consistent field labels, without needing to cross-reference a table and a separate paragraph block

#### Scenario: Two responses from different agents cover the same platform
- **WHEN** a researcher compares a ChatGPT response and a Claude response for the same platform
- **THEN** both use the same section heading and bullet field structure, making the comparison straightforward
