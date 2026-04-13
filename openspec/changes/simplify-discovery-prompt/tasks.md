## 1. Edit the prompt file

- [ ] 1.1 Remove the `[SEARCH_SCOPE]` placeholder line and its guard instruction ("If you see the literal text `[SEARCH_SCOPE]`...") from `prompts/platform-discovery.md`
- [ ] 1.2 Replace with a hardcoded `**Search scope:**` line: global city-scale UDT platforms and foundational building blocks (commercial and open-source), covering all major geographies including non-English-speaking markets and government-led initiatives
- [ ] 1.3 Simplify the usage header to two steps: (1) paste from the cut-line, (2) save as `responses/global-platforms-discovery.md`
- [ ] 1.4 Update the docs reference in the usage header from `docs/methodology.md` to `docs/02-methodology.md`

## 2. Verify

- [ ] 2.1 Confirm `[SEARCH_SCOPE]` no longer appears anywhere in `prompts/platform-discovery.md`
- [ ] 2.2 Confirm the usage header has exactly two numbered steps with no placeholder replacement step
- [ ] 2.3 Confirm the save-as filename in the usage header is `responses/global-platforms-discovery.md`
