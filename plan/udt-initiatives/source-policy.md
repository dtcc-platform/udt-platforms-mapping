# Source Policy

## Purpose

This policy governs evidence selection for the `udt-initiatives` cycle.
It is used when identifying and characterizing initiatives, projects, programmes, and deployments related to Urban Digital Twins.

Unlike `udt-platforms`, this cycle is allowed to keep an initiative in scope even when the exact technical substrate is unclear, provided the initiative itself is supported by acceptable evidence.

## Ranked Source Types

Prefer higher-ranked sources.
Use lower-ranked sources when higher-ranked sources are unavailable or when they only help corroborate existing claims.

| Rank | Type | Typical Use |
| ---- | ---- | ----------- |
| 1 | Official initiative or programme pages | City programme pages, project homepages, official deployment pages |
| 2 | Institutional or government documentation | Agency pages, municipal documentation, public programme reports |
| 3 | Official project repositories | Project repos, documentation portals, public implementation artifacts |
| 4 | Peer-reviewed literature | Papers discussing the initiative, deployment, or case study |
| 5 | Technical reports | Government, institutional, or consortium reports |
| 6 | Official organizational communications | Press releases, partner announcements, project blog posts |
| 7 | Reputable secondary sources | Established journalism, curated summaries, analyst overviews |

## Priority Rules

- Use higher-ranked sources to support initiative existence, scope, participants, and deployment claims.
- Prefer official initiative or institutional pages for:
  - initiative name
  - link
  - public description
  - deployment or programme framing
- Use repositories and literature to support technical context where available.
- If the initiative is well-supported but the underlying technical artifacts are unclear, keep the initiative in scope and use `?` in the `Uses` field.
- Do not invent a platform, framework, or module just to avoid `?`.

## Not Acceptable As Canonical Evidence

Do not use these as canonical evidence in `udt-initiatives` outputs:

- anonymous forum posts
- AI-generated summaries
- unattributed or undated pages with unclear provenance
- generic marketing pages that mention a city or project with no concrete project context

## Contradictions

If sources conflict:

- prefer the higher-ranked source
- if an official programme page and a lower-ranked communication disagree, the official programme page controls the canonical judgment
- if deployment details remain unclear after higher-ranked review, keep the initiative only if its existence is still supported and record `Uses` as `?`

## Practical Reminder

This cycle maps real-world efforts, not just reusable software.
An initiative can be canonical even when its technical stack is only partially visible.
