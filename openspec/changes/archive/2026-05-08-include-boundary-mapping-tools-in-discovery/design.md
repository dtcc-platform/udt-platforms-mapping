# Design: boundary mapping tools in platform discovery

## Approach

This change touches two contracts.

`platform-definition` defines the classification boundary. It should explicitly state that map storytelling, communication, presentation, and lightweight web-map narrative tools are excluded when they are not UDT technical artifacts.

`act-discover-platforms-prompt` defines discovery behavior. It should instruct broad discovery runs to include relevant boundary candidates as `excluded` rows when they are likely to be confused with UDT artifacts or useful for explaining the study boundary.

## Why two specs

`platform-definition` can classify StoryMapJS once it is considered, but it does not control candidate recall.

`act-discover-platforms-prompt` controls the discovery behavior that decides whether boundary candidates should be surfaced in the output at all.

Together they produce the intended future behavior:

```text
StoryMapJS appears in discovery candidate set
-> platform-definition classifies it as excluded
-> observe output records the exclusion reason
```

## Expected Output Behavior

When StoryMapJS or a similar map-storytelling tool is included in a future platform discovery result, it should appear like:

```md
| StoryMapJS | [StoryMapJS](https://storymap.knightlab.com/) | excluded | storytelling map tool, not a technical UDT artifact |
```

The exact link label and reason may vary, but the classification should be `excluded`.
