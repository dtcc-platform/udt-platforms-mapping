## Why

The current discovery prompt produces non-conforming responses in practice:

1. **Citation format not enforced strongly enough** — ChatGPT overrides the inline-link instruction and falls back to `【†source】` bracket citations. The prohibition exists but isn't forceful enough to override the model's default behaviour.
2. **Summary table at the end** — The table is appended after all per-platform sections, requiring researchers to scroll past dozens of sections to reach the overview. Moving it to the top makes the response immediately useful as a comparison starting point.
3. **No default scope** — If a researcher forgets to replace `[SEARCH_SCOPE]`, the model receives a literal placeholder token and either errors or produces a generic result. Defining a default scope makes the prompt more robust.

## What Changes

- Strengthen the citation format prohibition in `prompts/platform-discovery.md` — make it an override instruction that explicitly supersedes the model's default citation mode
- Move the summary table to the top of the output (before per-platform sections) in the prompt and spec
- Add a default scope: if `[SEARCH_SCOPE]` is not replaced, the model SHALL treat the scope as "global city-scale Urban Digital Twin platforms and foundational building blocks"

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `platform-discovery-prompt`: three requirement changes:
  - "Discovery prompt enforces agent-agnostic output structure" — strengthen citation override instruction
  - "Discovery prompt response ends with a required summary table" → table moves to the beginning
  - "Discovery prompt uses a parameterized search scope token" — add default scope fallback

## Impact

- `prompts/platform-discovery.md` — citation rule, output format order, scope token instruction
- `openspec/specs/platform-discovery-prompt/spec.md` — three modified requirements
