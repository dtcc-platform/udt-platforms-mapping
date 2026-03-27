## Why

Neither `responses/` nor `search_logs/` has a defined file naming convention, so saved files accumulate without a predictable structure — making it impossible to sort, filter, or locate outputs by platform, date, or prompt type. Defining a convention now, before the corpus grows, prevents retroactive cleanup.

## What Changes

- Define a naming convention for raw AI response files saved to `responses/`: `YYYY-MM-DD-<platform>-<prompt-type>.md`
- Confirm and document the naming convention for session log files in `search_logs/`: `YYYY-MM-DD-<platform>.md` (already implied in the README but never formally specified)
- Document both conventions in `docs/methodology.md` under a new **File Naming** section
- Update the three prompt templates to include the expected output filename in their usage instructions, so the researcher knows what to name the file before saving

## Capabilities

### New Capabilities

- `output-file-naming`: Defines the naming rules for files saved to `responses/` and `search_logs/`, including the format, allowed characters, and prompt-type token values

### Modified Capabilities

- `platform-discovery-prompt`: add naming instruction to the usage header (the filename the researcher should save the response as)
- `platform-comparison-prompt`: add naming instruction to the usage header
- `license-analysis-prompt`: add naming instruction to the usage header

## Impact

- `docs/methodology.md` — new **File Naming** section added
- `prompts/platform-discovery.md` — usage header updated with save-as filename instruction
- `prompts/platform-comparison.md` — usage header updated with save-as filename instruction
- `prompts/license-analysis.md` — usage header updated with save-as filename instruction
