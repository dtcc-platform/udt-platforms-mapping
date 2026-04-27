# Source Policy

## Purpose

This policy governs evidence selection for the `udt-platforms` cycle.
It is used when identifying, classifying, and characterizing technical artifacts such as platforms, frameworks, and modules.

The goal is not to prove absolute truth. The goal is to make source priority explicit, reduce dependence on promotional claims, and make contradictions reviewable.

## Ranked Source Types

Prefer higher-ranked sources.
Use lower-ranked sources only when higher-ranked sources are unavailable, incomplete, or only useful for corroboration.

| Rank | Type | Typical Use |
| ---- | ---- | ----------- |
| 1 | Official technical documentation | Product docs, developer docs, official manuals, official architecture docs |
| 2 | Official repositories and release records | GitHub or GitLab repos, README files, changelogs, release notes, license files |
| 3 | Standards and specifications | OGC specs, formal data-model specs, protocol specs, official standards documentation |
| 4 | Peer-reviewed literature | Journal papers, conference papers, systematic reviews |
| 5 | Official organizational communications | Vendor or foundation blog posts, press releases, product pages |
| 6 | Technical reports | Government, institutional, or research-lab reports |
| 7 | Reputable secondary sources | Established technical journalism, analyst writeups, curated ecosystem summaries |

## Priority Rules

- Use ranked sources to support final factual claims in canonical outputs.
- Prefer primary technical sources for:
  - official name
  - link
  - license
  - artifact type
  - evidence for `Type` classification
- Use peer-reviewed literature and technical reports to support broader framing, taxonomy, and relevance.
- Use secondary or promotional sources mainly to discover candidates or corroborate claims already supported by higher-ranked evidence.
- If higher-ranked evidence cannot support a claim, write `unknown` or `?` rather than guessing.
- Prefer omission over weakly supported inclusion.

## Not Acceptable As Canonical Evidence

Do not use these as canonical evidence in `udt-platforms` outputs:

- anonymous forum posts
- AI-generated summaries
- unattributed or undated pages with unclear provenance
- copy-pasted catalog listings with no clear owner or source trail

## Contradictions

If sources conflict:

- prefer the higher-ranked source
- if the contradiction materially affects inclusion or `Type` classification, note the discrepancy in working notes or reflection artifacts
- if the contradiction cannot be resolved confidently, use the most conservative supported classification or exclude the artifact

## Practical Reminder

Secondary sources may help you find artifacts.
Primary and higher-ranked sources should support what becomes canonical.
