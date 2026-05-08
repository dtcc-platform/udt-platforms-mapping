## 1. Specs

- [x] 1.1 Update `platform-definition` to classify map storytelling, communication, and presentation tools as `excluded` unless they expose a distinct technical UDT artifact.
- [x] 1.2 Add a StoryMapJS-style scenario to `platform-definition`.
- [x] 1.3 Update `act-discover-platforms-prompt` to include relevant boundary candidates as explicit `excluded` rows during broad discovery.
- [x] 1.4 Add a scenario showing StoryMapJS or similar tools are surfaced as `excluded` rather than silently omitted.

## 2. Validation

- [x] 2.1 Run `openspec validate include-boundary-mapping-tools-in-discovery --strict`.
- [x] 2.2 Run `openspec validate --all --strict`.
