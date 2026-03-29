## Why

Part 3 of the comparison output is currently specified as four loose bullet-point questions, leaving the AI free to structure its answer however it likes. This produces inconsistent output — sometimes prose paragraphs, sometimes lists, sometimes mixed — making it harder to scan across sessions or compare responses from different agents.

## What Changes

- Replace the four bullet-point questions in the Part 3 instruction with four enforced `####` subheadings, each followed by a bullet list
- Subheadings: `#### Landscape Gaps`, `#### DTCC's Position`, `#### Comparable Platforms`, `#### Complementary Platforms`
- Clarify in the prompt that Part 3 subheadings use `####` so they do not visually conflict with `###` platform profile headings in Part 2

## Capabilities

### New Capabilities

_(none)_

### Modified Capabilities

- `platform-comparison-prompt`: The Part 3 output requirement changes — unstructured bullet questions replaced with four enforced subheadings, each containing a list.

## Impact

- `prompts/platform-comparison.md` — Part 3 instruction in the Output Format section
- `openspec/specs/platform-comparison-prompt/spec.md` — scenario for Part 3 updated to reflect enforced subheading structure
