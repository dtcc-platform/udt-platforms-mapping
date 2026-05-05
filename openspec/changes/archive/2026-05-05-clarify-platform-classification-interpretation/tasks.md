## 1. Platform Definition Contract

- [x] 1.1 Add interpretation rules to `plan/platform-definition.md`.
- [x] 1.2 Define tie-break guidance for artifacts that resemble multiple `Type` values.
- [x] 1.3 Define how to handle weak, ambiguous, or insufficient evidence.
- [x] 1.4 Keep initiative/project discovery separate from platform discovery.

## 2. Discover Platforms Prompt

- [x] 2.1 Update `act/discover-platforms.md` to apply the interpretation rules before assigning `Type`.
- [x] 2.2 Make the prompt preserve uncertainty when evidence is weak or ambiguous.
- [x] 2.3 Keep the existing output format and save-location instructions unchanged.

## 3. Validation

- [x] 3.1 Run `openspec validate clarify-platform-classification-interpretation --strict`.
- [x] 3.2 Run `openspec validate --all --strict`.
