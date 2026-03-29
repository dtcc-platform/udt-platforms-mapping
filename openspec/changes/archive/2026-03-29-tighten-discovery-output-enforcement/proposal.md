## Why

The current discovery prompt describes the desired Markdown shape, but real outputs still drift in predictable ways: AI-specific citation syntax appears, secondary sources get used, non-canonical inclusion labels show up, and extra trailing prose is added outside the required structure. Tightening the prompt and spec now will make saved discovery responses reliably reusable in the comparison workflow without manual cleanup.

## What Changes

- Strengthen `prompts/platform-discovery.md` so the output format is an exact contract, not loose guidance
- Require canonical inclusion-criterion values only: `Explicit UDT`, `City-Scale Capabilities`, `Adjacent Architecture or Governance`
- Forbid extra content outside the required metadata block, summary table, and platform sections
- Require factual sentences in platform detail sections to use inline Markdown links to primary sources, and require `?` instead of a secondary-source fallback
- Update the discovery prompt spec to reflect the stricter output contract and source-formatting requirements

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `platform-discovery-prompt`: tighten output-shape and source-formatting requirements so discovery responses are deterministic and easier to validate

## Impact

- `prompts/platform-discovery.md` — stricter formatting, citation, source, and allowed-value instructions
- `openspec/specs/platform-discovery-prompt/spec.md` — modified requirements covering exact structure, canonical labels, no-extra-content rule, and primary-source citation expectations
