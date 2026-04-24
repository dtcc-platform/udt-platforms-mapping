# Rating Platform Selection

This file holds the platforms selected for the **current** rating cycle run.
It is a required input of `act/rating/prompt.md` — the AI CLI reads it in CLI mode and inlines it into the resolved prompt in Web mode.

Unlike `scope.md`, `rubrics.md`, and `source-policy.md` — which are slow-moving **definitions** reused across cycle runs — this file is **per-run data** and is expected to change between rating cycles.
Add a row to include a platform in the current comparison; remove a row to drop it.
The git history of this file is the authoritative record of which platforms were compared in each cycle.

Rating in this repository is intentionally restricted to **core platforms**. Inclusion in this table already means the researcher selected that row as a canonical `core-platform` from discovery, so `Layer` does not need to be repeated here.

**The DTCC row MUST be present.** The rating prompt's Part 3 landscape observations orient around DTCC, so removing the DTCC row breaks Part 3 output.
If DTCC is missing, the rating prompt will surface a scope error and refuse to produce output.

Aliases do not belong here. Rating compares the exact canonical platforms the researcher selected; it does not do fuzzy name matching across noisy outputs. Alias handling belongs in discovery benchmarking, where matching variant names across responses is part of the task.

| Name | Link |
| ---- | ---- |
| DTCC Platform | [platform.dtcc.chalmers.se](https://platform.dtcc.chalmers.se/) |
| Virtual Singapore | [nrf.gov.sg/programmes/virtual-singapore](https://www.nrf.gov.sg/programmes/virtual-singapore) |
| ArcGIS Urban | [esri.com/arcgis/products/arcgis-urban](https://www.esri.com/en-us/arcgis/products/arcgis-urban/overview) |
