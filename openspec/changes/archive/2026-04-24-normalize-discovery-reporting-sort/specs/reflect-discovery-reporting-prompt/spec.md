## MODIFIED Requirements

### Requirement: Discovery reporting output is ordered by URL part of Link

The consolidated Markdown table SHALL be ordered only after all qualifying rows from all discovery responses have been aggregated into one combined row set.

The ordering rule SHALL use a normalized URL sort key extracted from each Markdown link cell:

- extract the URL target from the `Link` cell
- lowercase the URL target
- extract the host/domain portion
- remove a leading `www.` from the host if present

Rows SHALL be sorted first by that normalized host/domain key, then by the full URL target, then by `Name`, then by `Layer`, then by `Reason`.

#### Scenario: Two rows appear in different source files

- **WHEN** two platform rows come from different discovery responses
- **THEN** their order in the final Markdown table follows the normalized URL ordering rule rather than response-file order

#### Scenario: Related host variants are grouped together

- **WHEN** the combined row set contains links for `dtcc.chalmers.se`, `www.dtcc.chalmers.se`, and `platform.dtcc.chalmers.se`
- **THEN** the rows are grouped under the shared normalized host ordering rather than split by raw URL-string sorting

#### Scenario: Sorting happens after full aggregation

- **WHEN** qualifying rows are extracted from multiple discovery response files
- **THEN** the implementation gathers all qualifying rows first and sorts the final combined row set once before writing the Markdown table
