# Proposal: make-web-canonical-for-act-prompts

## Why

The current act-prompt workflow is CLI-centered, but the intended execution environment for the research prompts is the web interface.

That mismatch creates friction:

- the canonical contract says to run act prompts in an AI CLI
- the user intends to run the research work in web chat interfaces
- `udt-initiatives` does not yet have a governed act prompt, so the three threads are inconsistent

If web is the real canonical interface, the repository should say so explicitly and govern prompts around that mode instead of keeping CLI as the default path.

## What Changes

- make web the canonical execution mode for `act/` research prompts
- update:
  - `act/udt-platforms/prompt.md`
  - `act/udt-platform-comparison/prompt.md`
- add a new governed prompt:
  - `act/udt-initiatives/prompt.md`
- add a baseline capability for the `udt-initiatives` act prompt
- update folder-layout and prompt-status expectations so the three act prompts are treated consistently
- use a web-oriented save convention for act prompt outputs

## Impact

- the canonical research prompts become copy/paste prompts for web interfaces
- act-prompt instructions become simpler and better aligned with actual use
- all three research threads gain a governed act-prompt surface
- the repository stops implying that CLI is the default runtime for research execution
