# Source Policy

## Acceptable Source Types

Sources are ranked by reliability. Prefer higher-ranked sources and only use lower-ranked ones when higher-ranked sources are unavailable or insufficient.

| Rank | Type                                   | Examples                                                                                        |
| ---- | -------------------------------------- | ----------------------------------------------------------------------------------------------- |
| 1    | Official documentation                 | Platform docs sites, GitHub READMEs, official wikis                                             |
| 2    | Peer-reviewed publications             | Academic papers, conference proceedings (ISPRS, ACM, IEEE)                                      |
| 3    | Official project repositories          | GitHub/GitLab source code, release notes, changelogs                                            |
| 4    | Official organizational communications | Press releases, blog posts from the platform's own organization                                 |
| 5    | Technical reports                      | Government or institutional technical reports                                                   |
| 6    | Reputable secondary sources            | Established tech journalism, analyst reports — use only to corroborate, not as primary evidence |

**Not acceptable:** Wikipedia, anonymous forum posts, AI-generated summaries, undated web pages without clear authorship.

## Citation Format

All sources cited in logs and documents use the following format:

```
[Short label](URL) — Type, Date accessed YYYY-MM-DD
```

Example:

```
[Cesium official docs](https://cesium.com/docs/) — Official documentation, accessed 2026-03-01
```

For non-URL sources (papers, reports):

```
Author(s), "Title", Venue/Publisher, Year. DOI or stable URL if available.
```

## Paywalled Sources

If a source is paywalled:

- Note the citation with `[paywalled]` suffix
- Record what can be inferred from the abstract or freely available excerpt
- Do not guess or infer content beyond what is accessible

## Unreliable or Contradictory Sources

If a source contradicts a higher-ranked source, prefer the higher-ranked source and note the discrepancy in the search log. If the contradiction is significant, flag it in the `notes/` file for the platform.

## Source Storage

Raw source material (downloaded PDFs, license files, screenshots) is stored in `sources/<platform-name>/`. File names should be descriptive: `<platform>-license-2026.txt`, `<platform>-architecture-diagram.png`.
