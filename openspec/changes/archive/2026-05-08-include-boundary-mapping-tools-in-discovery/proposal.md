# Proposal: include boundary mapping tools in platform discovery

## Summary

Update platform discovery behavior so future discovery prompts include relevant boundary-adjacent mapping and storytelling tools as explicit `excluded` rows when they are plausible confusion cases.

StoryMapJS is the motivating example: it is a map-based storytelling tool, not an Urban Digital Twin platform, framework, or module. Future platform discovery runs should be able to surface it as `excluded` instead of silently omitting it.

## Motivation

The current specs correctly exclude non-UDT artifacts, but they do not clearly tell discovery runs to include useful negative examples. This can make omissions ambiguous:

- Was the artifact missed?
- Was it intentionally excluded?
- Was it outside the search boundary?

For tools that researchers may reasonably ask about, an explicit `excluded` row is more useful than silence. It documents the boundary of the study and makes the classification contract easier to inspect.

## Scope

In scope:

- clarify `platform-definition` so map storytelling, communication, and presentation tools are outside platform discovery unless they expose a distinct technical UDT artifact
- update `act-discover-platforms-prompt` so broad discovery includes relevant boundary candidates and records them as `excluded`
- use StoryMapJS as an example of this boundary class

Out of scope:

- changing allowed `Type` values
- changing observe output shape
- adding StoryMapJS to a benchmark fixture
- editing existing observed model outputs
