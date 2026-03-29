## 1. Update Live Specs

- [x] 1.1 In `openspec/specs/platform-discovery-prompt/spec.md`, update "Discovery prompt response ends with a required summary table" — remove `Select` from the column list and remove all `Select`-column language from its scenarios
- [x] 1.2 In `openspec/specs/platform-discovery-prompt/spec.md`, update "Discovery prompt requests structured output aligned with inventory" — remove `x`-marked language from the "Discovery scores feed into comparison" scenario
- [x] 1.3 In `openspec/specs/platform-comparison-prompt/spec.md`, update "Comparison prompt uses a single selection table token" — replace `x`-marked rows language with direct row selection, add header row instruction

## 2. Update Prompts

- [x] 2.1 In `prompts/platform-discovery.md`, remove `Select` column from the summary table definition and remove the instruction "Leave the **Select** column empty — the researcher fills it in to mark platforms for a comparison session"
- [x] 2.2 In `prompts/platform-comparison.md`, remove step 2 ("Place `x` in the **Select** column") from the usage header
- [x] 2.3 In `prompts/platform-comparison.md`, update step 3 to read "Copy the rows you want to compare (including the header row) from the summary table"

## 3. Update Methodology

- [x] 3.1 In `docs/methodology.md`, remove step 6 ("Clear the `x` marks from the discovery response when done") from the Discovery to Comparison Workflow
- [x] 3.2 In `docs/methodology.md`, update step 2 to remove `x`-marking language — change to "Open the saved response and choose which platforms to compare"
