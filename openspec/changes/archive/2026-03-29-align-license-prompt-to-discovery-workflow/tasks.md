## 1. Update Live Spec

- [x] 1.1 In `openspec/specs/license-analysis-prompt/spec.md`, remove the "License analysis prompt uses a parameterized platform token" requirement
- [x] 1.2 In `openspec/specs/license-analysis-prompt/spec.md`, add the "License analysis prompt uses a discovery table row token" requirement
- [x] 1.3 In `openspec/specs/license-analysis-prompt/spec.md`, add the "License analysis prompt usage header follows the discovery-to-prompt pattern" requirement

## 2. Update the Prompt

- [x] 2.1 In `prompts/license-analysis.md`, replace the usage header instructions with the row-paste pattern (open response, copy header + platform row, replace token, paste prompt)
- [x] 2.2 In `prompts/license-analysis.md`, replace the `[PLATFORM_NAME]` and `[LICENSE_URL_OR_TEXT]` tokens with a single `[PASTE_SELECTED_PLATFORM_HERE]` token
- [x] 2.3 In `prompts/license-analysis.md`, update the prompt body preamble to instruct the model to derive the platform name from the Name column, use the Link column to locate the license, and treat the License column as a seed signal

## 3. Update Methodology

- [x] 3.1 In `docs/methodology.md`, add a note after the Discovery to Comparison Workflow that license analysis is an optional parallel path — copy the platform row and paste it into `prompts/license-analysis.md`
