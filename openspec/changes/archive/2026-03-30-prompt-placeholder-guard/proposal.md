## Why

Prompts that require user-supplied data (e.g. a platform table) contain placeholders like `[PASTE_SELECTED_PLATFORMS_HERE]`. When these prompts are used via `@file` references without filling in the placeholder, the model silently produces a stub or incomplete response rather than asking for the missing input. A consistent guard instruction before each placeholder prevents this.

## What Changes

- Add a standard guard instruction block immediately before each unfilled placeholder in `prompts/platform-comparison.md`
- Add a standard guard instruction block immediately before each unfilled placeholder in `prompts/license-analysis.md`
- Define a canonical wording for the guard so it is consistent across all current and future prompts

## Capabilities

### New Capabilities

- `prompt-placeholder-guard`: A standard guard instruction block that is placed immediately before any required user-data placeholder in a prompt file, instructing the model to stop and ask for the missing data rather than proceeding

### Modified Capabilities

- `platform-comparison-prompt`: Guard block added before `[PASTE_SELECTED_PLATFORMS_HERE]`
- `license-analysis-prompt`: Guard block added before `[PASTE_SELECTED_PLATFORM_HERE]`

## Impact

- `prompts/platform-comparison.md` — one guard block inserted
- `prompts/license-analysis.md` — one guard block inserted
- No API, dependency, or schema changes
